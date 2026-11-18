#!/usr/bin/env python3
"""Report HIG pages that changed since the skills were last synced.

  python3 -I scripts/check_updates.py

Compares the live HIG with skills/apple-hig/index.json (latest Change log date and content hash
per page) and prints a Markdown report: changed, new and removed pages, what the Change log says,
and which skill files link each page.

Exit codes: 0 no changes, 2 changes found, 1 error.
After updating the skills, run `python3 skills/apple-hig/scripts/hig.py index` to record the new
state as synced.
"""
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "skills", "apple-hig", "scripts"))
import hig  # noqa: E402


def diff(stored, live):
    """(changed, added, removed). changed = [(stored_entry, live_entry)]."""
    s = {e["slug"]: e for e in stored}
    l = {e["slug"]: e for e in live}
    changed = [(s[k], l[k]) for k in l if k in s and
               (l[k]["updated"] > s[k].get("updated", "") or l[k]["hash"] != s[k].get("hash"))]
    added = [l[k] for k in l if k not in s]
    removed = [s[k] for k in s if k not in l]
    return changed, added, removed


def linking_files(slug):
    pattern = re.compile(r"human-interface-guidelines/" + re.escape(slug) + r"(?![a-z0-9-])")
    hits = []
    for dirpath, _, files in os.walk(os.path.join(ROOT, "skills")):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(dirpath, f)
                if pattern.search(open(path).read()):
                    hits.append(os.path.relpath(path, ROOT))
    return sorted(hits)


def page(e):
    return f"[{e['title']}](https://developer.apple.com/design/human-interface-guidelines/{e['slug']})"


def report(changed, added, removed, checked):
    out = [f"# HIG changes since last sync\n",
           f"Checked {checked} pages on {datetime.date.today().isoformat()} against "
           "`skills/apple-hig/index.json`.\n"]
    if changed:
        out.append(f"## Changed pages ({len(changed)})\n")
        for old, new in sorted(changed, key=lambda p: p[1]["updated"], reverse=True):
            out.append(f"### {page(new)}\n")
            log = [(d, c) for d, c in new["_log"] if d > old.get("updated", "")]
            out.extend(f"- {d}: {c}" for d, c in log)
            if not log:
                out.append("- Content changed without a new Change log entry.")
            files = linking_files(new["slug"])
            out.append("\nSkill files that link this page: " +
                       (", ".join(f"`{f}`" for f in files) if files else "none yet") + "\n")
    if added:
        out.append(f"## New pages ({len(added)})\n")
        out.extend(f"- {page(e)} ({e['area']}{' › ' + e['group'] if e['group'] else ''})" for e in added)
        out.append("")
    if removed:
        out.append(f"## Removed pages ({len(removed)})\n")
        for e in removed:
            files = linking_files(e["slug"])
            out.append(f"- `{e['slug']}` ({e['title']})" + (": linked from " + ", ".join(f"`{f}`" for f in files) if files else ""))
        out.append("")
    out.append("## Next steps\n")
    out.append("1. Read the changed pages (`python3 skills/apple-hig/scripts/hig.py fetch <slug>`) and update the listed skill files in your own words.")
    out.append("2. Run `python3 -I scripts/validate.py --online`.")
    out.append("3. Run `python3 skills/apple-hig/scripts/hig.py index` to record the new state as synced.")
    out.append("4. Bump the version in `.claude-plugin/plugin.json` and `gemini-extension.json`, then commit.")
    return "\n".join(out) + "\n"


def selftest():
    stored = [{"slug": "a", "updated": "2026-01-01", "hash": "x"}, {"slug": "b", "updated": "", "hash": "y"},
              {"slug": "c", "updated": "2026-01-01", "hash": "z"}, {"slug": "gone", "updated": "", "hash": "q"}]
    live = [{"slug": "a", "updated": "2026-03-01", "hash": "x2"}, {"slug": "b", "updated": "", "hash": "y2"},
            {"slug": "c", "updated": "2026-01-01", "hash": "z"}, {"slug": "new", "updated": "", "hash": "n"}]
    changed, added, removed = diff(stored, live)
    assert [n["slug"] for _, n in changed] == ["a", "b"], changed
    assert [e["slug"] for e in added] == ["new"] and [e["slug"] for e in removed] == ["gone"]
    assert linking_files("sheets") and "skills/hig-components/references/presentation.md" in linking_files("sheets")
    assert not linking_files("sheets-that-do-not-exist")


def main():
    selftest()
    live = hig.collect_index()
    changed, added, removed = diff(hig.load_index(), live)
    if not (changed or added or removed):
        print(f"No changes since last sync ({len(live)} pages checked).")
        return 0
    print(report(changed, added, removed, len(live)), end="")
    return 2


if __name__ == "__main__":
    sys.exit(main())
