#!/usr/bin/env python3
"""Look up Apple's Human Interface Guidelines (and Apple developer docs) live.

Usage:
  python3 hig.py search <query>              find HIG pages by title/slug (offline, uses index.json)
  python3 hig.py fetch <slug|path|url> [--images] [--section <heading>]
                                             print a HIG page or API doc page as Markdown
                                             (--images adds image descriptions)
  python3 hig.py index                       rebuild index.json from the live HIG table of contents
  python3 hig.py selftest                    offline check of the Markdown renderer

Examples:
  python3 hig.py search "tab bar"
  python3 hig.py fetch tab-bars --section "Best practices"
  python3 hig.py fetch /documentation/swiftui/view/glasseffect(_:in:)

Only the Python standard library is used. Content is fetched from developer.apple.com
at call time and is © Apple Inc.; it is printed, never stored.
"""
import difflib
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://developer.apple.com"
DATA = BASE + "/tutorials/data"
HIG = "/design/human-interface-guidelines"
INDEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.json")


def to_path(target):
    """Accept a slug, a site path or a full URL; return a lowercase site path."""
    t = target.strip()
    if t.startswith("http"):
        t = urllib.parse.urlparse(t).path
    t = t.split("#")[0].rstrip("/")
    if not t.startswith("/"):
        t = HIG + "/" + t
    return t.lower()


def get_json(path):
    url = DATA + urllib.parse.quote(path, safe="/():_-.~,") + ".json"
    req = urllib.request.Request(url, headers={"User-Agent": "hig-lookup/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        hint = " (try: hig.py search <words>)" if e.code == 404 else ""
        sys.exit(f"error: {e.code} for {path}{hint}")
    except urllib.error.URLError as e:
        sys.exit(f"error: cannot reach developer.apple.com: {e.reason}")


# ---------------------------------------------------------------- rendering

class Renderer:
    def __init__(self, refs, images=False):
        self.refs = refs
        self.images = images

    def ref_link(self, ident, title=None):
        r = self.refs.get(ident, {})
        title = title or r.get("title") or ident.rsplit("/", 1)[-1]
        url = r.get("url", "")
        if url.startswith("/"):
            url = BASE + url
        return f"[{title}]({url})" if url else title

    def inline(self, nodes):
        out = []
        for n in nodes or []:
            t = n.get("type")
            if t == "text":
                out.append(n["text"])
            elif t == "codeVoice":
                out.append(f"`{n['code']}`")
            elif t == "strong":
                out.append(f"**{self.inline(n.get('inlineContent'))}**")
            elif t == "emphasis":
                out.append(f"*{self.inline(n.get('inlineContent'))}*")
            elif t in ("small", "superscript", "subscript", "newTerm"):
                out.append(self.inline(n.get("inlineContent")))
            elif t == "reference":
                title = self.inline(n.get("overridingTitleInlineContent")) or n.get("overridingTitle")
                out.append(self.ref_link(n["identifier"], title))
            elif t == "link":
                out.append(f"[{n.get('title', n.get('destination'))}]({n.get('destination')})")
            elif t == "image" and self.images:
                alt = self.refs.get(n.get("identifier"), {}).get("alt")
                if alt:
                    out.append(f"[image: {alt}]")
            elif "inlineContent" in n:
                out.append(self.inline(n["inlineContent"]))
        return "".join(out)

    def cell(self, blocks):
        return " ".join(self.blocks(blocks).split()).replace("|", "\\|")

    def blocks(self, nodes, indent=""):
        out = []
        for n in nodes or []:
            t = n.get("type")
            if t == "heading":
                out.append(f"\n{'#' * (n.get('level', 2) + 1)} {n['text']}\n")
            elif t == "paragraph":
                text = self.inline(n.get("inlineContent"))
                if text.strip():
                    out.append(indent + text + "\n")
            elif t in ("unorderedList", "orderedList"):
                for i, item in enumerate(n.get("items", []), 1):
                    mark = f"{i}." if t == "orderedList" else "-"
                    body = self.blocks(item.get("content"), indent + "  ").strip()
                    out.append(f"{indent}{mark} {body}")
                out.append("")
            elif t == "aside":
                body = self.blocks(n.get("content")).strip().replace("\n", "\n> ")
                out.append(f"> **{n.get('name') or n.get('style', 'Note').title()}:** {body}\n")
            elif t == "table":
                rows = [[self.cell(c) for c in row] for row in n.get("rows", [])]
                if rows:
                    width = max(len(r) for r in rows)
                    rows = [r + [""] * (width - len(r)) for r in rows]
                    out.append("| " + " | ".join(rows[0]) + " |")
                    out.append("|" + "---|" * width)
                    out.extend("| " + " | ".join(r) + " |" for r in rows[1:])
                    out.append("")
            elif t == "tabNavigator":
                for tab in n.get("tabs", []):
                    out.append(f"\n**[{tab.get('title')}]**\n")
                    out.append(self.blocks(tab.get("content"), indent))
            elif t == "row":
                for col in n.get("columns", []):
                    out.append(self.blocks(col.get("content"), indent))
            elif t == "codeListing":
                out.append(f"```{n.get('syntax') or ''}\n" + "\n".join(n.get("code", [])) + "\n```\n")
            elif t == "links":
                out.extend(f"- {self.ref_link(i)}" for i in n.get("items", []))
                out.append("")
            elif t in ("image", "video"):
                if not self.images:
                    continue
                alt = self.refs.get(n.get("identifier"), {}).get("alt")
                if alt:
                    out.append(f"{indent}[{t}: {alt}]\n")
            elif t == "termList":
                for item in n.get("items", []):
                    term = self.inline(item.get("term", {}).get("inlineContent"))
                    out.append(f"- **{term}**: {self.blocks(item.get('definition', {}).get('content')).strip()}")
                out.append("")
            elif "content" in n and isinstance(n["content"], list):
                out.append(self.blocks(n["content"], indent))
            elif "inlineContent" in n:
                out.append(indent + self.inline(n["inlineContent"]) + "\n")
        return "\n".join(out)


def render(doc, images=False):
    r = Renderer(doc.get("references", {}), images)
    md = []
    title = doc.get("metadata", {}).get("title", "")
    md.append(f"# {title}\n")
    abstract = r.inline(doc.get("abstract"))
    if abstract:
        md.append(abstract + "\n")
    for sec in doc.get("primaryContentSections", []):
        kind = sec.get("kind")
        if kind == "declarations":
            for d in sec.get("declarations", []):
                code = "".join(tok.get("text", "") for tok in d.get("tokens", []))
                md.append(f"```swift\n{code}\n```\n")
        elif kind == "parameters":
            md.append("## Parameters\n")
            for p in sec.get("parameters", []):
                md.append(f"- `{p['name']}`: {r.blocks(p.get('content')).strip()}")
            md.append("")
        else:
            md.append(r.blocks(sec.get("content")))
    avail = doc.get("metadata", {}).get("platforms")
    if avail:
        md.append("Availability: " + ", ".join(
            f"{p.get('name')} {p.get('introducedAt', '')}{' (beta)' if p.get('beta') else ''}".strip()
            for p in avail))
    body = "\n".join(md)
    for sec in doc.get("topicSections", []):
        items = [f"- {r.ref_link(i)}" for i in sec.get("identifiers", [])]
        items = [i for i in items if i not in body]  # skip links the page already listed
        if items:
            md.append(f"\n## {sec.get('title', 'Topics')}\n")
            md.extend(items)
    text = "\n".join(md)
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text.strip() + "\n"


def only_section(md, heading):
    """Keep the part of the Markdown under the heading that matches `heading`."""
    lines, keep, level = md.splitlines(), [], None
    for line in lines:
        if line.startswith("#"):
            lvl = len(line) - len(line.lstrip("#"))
            if level is not None and lvl <= level:
                break
            if level is None and heading.lower() in line.lower():
                level = lvl
        if level is not None:
            keep.append(line)
    if not keep:
        heads = [l for l in lines if l.startswith("## ")]
        sys.exit(f"error: no section matching '{heading}'. Sections:\n" + "\n".join(heads))
    return "\n".join(keep) + "\n"


# ---------------------------------------------------------------- index + search

def build_index():
    entries, seen = [], set()

    # depth 1 = area (Foundations, Components, ...); under Components, depth 2 = group.
    def walk(path, area, group, depth):
        if path in seen or depth > 3:
            return
        seen.add(path)
        doc = get_json(path)
        title = doc.get("metadata", {}).get("title", "")
        if depth == 1:
            area = title
        if depth >= 1:
            entries.append({"slug": path.rsplit("/", 1)[-1], "title": title, "area": area, "group": group})
        if depth == 2 and area == "Components":
            group = title
        for sec in doc.get("topicSections", []):
            for ident in sec.get("identifiers", []):
                child = doc["references"].get(ident, {}).get("url", "").lower()
                if child.startswith(HIG + "/"):
                    walk(child, area, group, depth + 1)

    walk(HIG, "", "", 0)
    with open(INDEX, "w") as f:
        json.dump(entries, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {len(entries)} entries to {os.path.normpath(INDEX)}")


# Common terms that HIG page titles do not contain.
ALIASES = {
    "materials": "liquid glass blur vibrancy translucency",
    "toolbars": "navigation bar nav bar liquid glass",
    "typography": "dynamic type font text style sf pro",
    "playing-haptics": "haptic vibration feedback",
    "modality": "modal sheet full screen cover",
    "sheets": "modal bottom sheet detent",
    "alerts": "dialog confirmation",
    "action-sheets": "confirmation dialog",
    "dark-mode": "dark appearance",
    "color": "semantic colors tint accent",
    "layout": "safe area margins size class spacing grid",
    "app-icons": "icon composer",
    "sf-symbols": "symbol image glyph",
    "accessibility": "a11y contrast reduce motion",
    "right-to-left": "rtl localization arabic hebrew",
    "searching": "search tab",
    "settings": "preferences",
    "lists-and-tables": "list table form",
    "context-menus": "long press",
    "generative-ai": "llm apple intelligence ai",
    "designing-for-iphone-duo": "foldable dual display",
}


def search(query):
    with open(INDEX) as f:
        entries = json.load(f)
    q = query.lower()
    words = q.replace("-", " ").split()

    def score(e):
        hay = f"{e['title']} {e['slug']} {e['group']} {e['area']} {ALIASES.get(e['slug'], '')}".lower().replace("-", " ")
        s = sum(2 for w in words if w in hay)
        s += difflib.SequenceMatcher(None, q, e["title"].lower()).ratio()
        return s

    ranked = sorted(entries, key=score, reverse=True)[:8]
    for e in ranked:
        where = e["area"] + (f" › {e['group']}" if e["group"] else "")
        print(f"{e['slug']:<34} {e['title']}  ({where})")


# ---------------------------------------------------------------- self-test

def selftest():
    doc = {
        "metadata": {"title": "Tab bars"},
        "abstract": [{"type": "text", "text": "A tab bar lets people navigate."}],
        "references": {"doc://x/sidebars": {"title": "Sidebars", "url": "/design/human-interface-guidelines/sidebars"},
                       "img1": {"alt": "A tab bar"}},
        "primaryContentSections": [{"kind": "content", "content": [
            {"type": "heading", "level": 2, "text": "Best practices"},
            {"type": "paragraph", "inlineContent": [
                {"type": "strong", "inlineContent": [{"type": "text", "text": "Use tabs"}]},
                {"type": "text", "text": " not "},
                {"type": "reference", "identifier": "doc://x/sidebars", "isActive": True},
                {"type": "codeVoice", "code": "TabView"}]},
            {"type": "unorderedList", "items": [{"content": [{"type": "paragraph", "inlineContent": [{"type": "text", "text": "one"}]}]}]},
            {"type": "table", "header": "row", "rows": [
                [[{"type": "paragraph", "inlineContent": [{"type": "text", "text": "A"}]}], [{"type": "paragraph", "inlineContent": [{"type": "text", "text": "B|C"}]}]],
                [[{"type": "paragraph", "inlineContent": [{"type": "text", "text": "1"}]}]]]},
            {"type": "tabNavigator", "tabs": [{"title": "iOS", "content": [{"type": "paragraph", "inlineContent": [{"type": "text", "text": "ios text"}]}]}]},
            {"type": "aside", "style": "tip", "name": "Tip", "content": [{"type": "paragraph", "inlineContent": [{"type": "text", "text": "be brief"}]}]},
            {"type": "image", "identifier": "img1"},
            {"type": "heading", "level": 2, "text": "Platform considerations"},
            {"type": "paragraph", "inlineContent": [{"type": "text", "text": "later"}]}]}],
    }
    assert "[image:" not in render(doc)
    md = render(doc, images=True)
    assert md.startswith("# Tab bars\n"), md
    assert "### Best practices" in md
    assert "**Use tabs** not [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)`TabView`" in md
    assert "- one" in md
    assert "| A | B\\|C |" in md and "| 1 |  |" in md, md
    assert "**[iOS]**" in md and "ios text" in md
    assert "> **Tip:** be brief" in md
    assert "[image: A tab bar]" in md
    sec = only_section(md, "best practices")
    assert "Use tabs" in sec and "later" not in sec
    assert to_path("Tab-Bars") == HIG + "/tab-bars"
    assert to_path("https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best") == HIG + "/tab-bars"
    assert to_path("/documentation/SwiftUI/View") == "/documentation/swiftui/view"
    print("selftest ok")


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help", "help"):
        print(__doc__)
        return
    cmd, args = argv[1], argv[2:]
    if cmd == "fetch" and args:
        section = None
        images = "--images" in args
        args = [a for a in args if a != "--images"]
        if "--section" in args:
            i = args.index("--section")
            section = " ".join(args[i + 1:])
            args = args[:i]
        md = render(get_json(to_path(" ".join(args))), images)
        print(only_section(md, section) if section else md, end="")
    elif cmd == "search" and args:
        search(" ".join(args))
    elif cmd == "index":
        build_index()
    elif cmd == "selftest":
        selftest()
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv)
