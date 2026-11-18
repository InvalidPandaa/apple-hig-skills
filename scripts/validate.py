#!/usr/bin/env python3
"""Check the skill set for structural problems.

  python3 -I scripts/validate.py            offline checks
  python3 -I scripts/validate.py --online   also check HIG anchors, API links, and copied HIG text

Offline: SKILL.md frontmatter (name = folder, description starts with "Use when", length),
size limits, relative links, HIG slugs known to index.json, plugin manifests parse.
Online: every linked HIG heading anchor exists, every /documentation link resolves, and no run of
8+ consecutive words is copied from a linked HIG page.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "skills", "apple-hig", "scripts"))
import hig  # noqa: E402

LINK = re.compile(r"\]\(([^)\s]+)\)")
HIG_URL = re.compile(r"https://developer\.apple\.com/design/human-interface-guidelines/([a-z0-9-]+)(?:#([A-Za-z0-9-]+))?")
DOC_PREFIX = "](https://developer.apple.com/documentation/"
SHINGLE = 8

errors, warnings = [], []


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields


def md_files():
    for base in ("skills", "commands", "agents"):
        for dirpath, _, files in os.walk(os.path.join(ROOT, base)):
            for f in files:
                if f.endswith(".md"):
                    yield os.path.join(dirpath, f)


def check_offline():
    for manifest in ("plugin.json", "marketplace.json"):
        try:
            json.load(open(os.path.join(ROOT, ".claude-plugin", manifest)))
        except Exception as e:
            errors.append(f".claude-plugin/{manifest}: {e}")

    index = {e["slug"] for e in json.load(open(os.path.join(ROOT, "skills", "apple-hig", "index.json")))}
    skills_dir = os.path.join(ROOT, "skills")
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            errors.append(f"skills/{name}: missing SKILL.md")
            continue
        fm = frontmatter(open(path).read()) or {}
        desc = fm.get("description", "")
        if fm.get("name") != name:
            errors.append(f"skills/{name}: frontmatter name {fm.get('name')!r} != folder name")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"skills/{name}: invalid skill name")
        if not desc.startswith("Use when"):
            errors.append(f"skills/{name}: description must start with 'Use when'")
        if len(desc) > 1024:
            errors.append(f"skills/{name}: description is {len(desc)} chars (max 1024)")

    for path in md_files():
        rel = os.path.relpath(path, ROOT)
        text = open(path).read()
        lines = text.count("\n")
        limit = 200 if path.endswith("SKILL.md") else 250
        if "/references/" in path and lines > limit or path.endswith("SKILL.md") and lines > limit:
            warnings.append(f"{rel}: {lines} lines (limit {limit})")
        if not path.endswith("SKILL.md") and "/skills/" not in path and frontmatter(text) is None:
            errors.append(f"{rel}: missing frontmatter")
        for target in LINK.findall(text):
            if target.startswith(("http", "#", "mailto:")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target.split("#")[0]))):
                errors.append(f"{rel}: broken relative link {target}")
        for slug, _ in HIG_URL.findall(text):
            if slug not in index:
                errors.append(f"{rel}: unknown HIG slug '{slug}'")


def doc_links(text):
    """Markdown link targets under /documentation, allowing balanced parentheses in the path."""
    out, i = [], text.find(DOC_PREFIX)
    while i != -1:
        j, depth = i + 2, 0
        while j < len(text) and not text[j].isspace():
            if text[j] == "(":
                depth += 1
            elif text[j] == ")":
                if depth == 0:
                    break
                depth -= 1
            j += 1
        out.append(text[i + 2:j].split("#")[0].replace("https://developer.apple.com", ""))
        i = text.find(DOC_PREFIX, j)
    return out


def words(text):
    text = re.sub(r"https?://\S+", " ", text)  # URLs are not prose
    return re.findall(r"[a-z0-9’']+", text.lower())


def check_online():
    pages, docs, anchors_used = {}, set(), {}
    for path in md_files():
        rel = os.path.relpath(path, ROOT)
        text = open(path).read()
        for slug, anchor in HIG_URL.findall(text):
            anchors_used.setdefault(slug, set())
            if anchor:
                anchors_used[slug].add((anchor, rel))
            pages.setdefault(slug, set()).add(rel)
        docs.update((d, rel) for d in doc_links(text))

    shingles = {}
    for slug in sorted(pages):
        try:
            doc = hig.get_json(hig.to_path(slug))
        except SystemExit as e:
            errors.append(f"HIG page {slug}: {e}")
            continue
        found = set()

        def collect(n):
            if isinstance(n, dict):
                if n.get("type") == "heading" and n.get("anchor"):
                    found.add(n["anchor"])
                for v in n.values():
                    collect(v)
            elif isinstance(n, list):
                for x in n:
                    collect(x)
        collect(doc.get("primaryContentSections", []))
        for anchor, rel in anchors_used[slug]:
            if anchor not in found:
                errors.append(f"{rel}: anchor #{anchor} not on page {slug}")
        w = words(hig.render(doc))
        for i in range(len(w) - SHINGLE + 1):
            shingles[" ".join(w[i:i + SHINGLE])] = slug

    for d, rel in sorted(docs):
        try:
            hig.get_json(hig.to_path(d))
        except SystemExit:
            errors.append(f"{rel}: API link does not resolve: {d}")

    for path in md_files():
        rel = os.path.relpath(path, ROOT)
        text = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", open(path).read())  # ignore link text
        text = re.sub(r"```.*?```", " ", text, flags=re.S)             # ignore code
        w = words(text)
        hits = {}
        for i in range(len(w) - SHINGLE + 1):
            s = " ".join(w[i:i + SHINGLE])
            if s in shingles:
                hits.setdefault(shingles[s], []).append(s)
        for slug, found in hits.items():
            warnings.append(f"{rel}: {len(found)} run(s) of {SHINGLE}+ words copied from '{slug}', e.g. \"{found[0]}\"")


def selftest():
    t = "[a](https://developer.apple.com/documentation/swiftui/texteditor/init(text:selection:)) and [b](https://developer.apple.com/documentation/swiftui/view#x)."
    assert doc_links(t) == ["/documentation/swiftui/texteditor/init(text:selection:)", "/documentation/swiftui/view"], doc_links(t)


def main():
    selftest()
    check_offline()
    if "--online" in sys.argv:
        check_online()
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
