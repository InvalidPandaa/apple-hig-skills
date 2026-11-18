---
name: hig-lookup
description: Use when someone asks what Apple's Human Interface Guidelines currently say about a topic, component or platform ("what does the HIG say about sheets", "is there a rule for tab bar badges", "what changed in the HIG for iOS 27"), or when you need the exact current guideline before relying on it.
---

# HIG Lookup

Answer from the live guidelines, not from memory. The HIG changes every year and many rules changed in 2025–2026.

## Process

1. Find the matching pages: `python3 ../apple-hig/scripts/hig.py search "<words>"`. Try two or three wordings if the first misses. `../apple-hig/index.json` lists every page slug by area.
2. Fetch the one to three most relevant pages, or only the sections you need: `python3 ../apple-hig/scripts/hig.py fetch <slug> --section "<Heading>"`. For recent changes, fetch `--section "Change log"`. For an API, fetch `/documentation/swiftui/<symbol>`.
3. If the output starts with a note that the page changed after the skills were last synced, say so in your answer and go by the live page.
4. Without Python, read `https://developer.apple.com/design/human-interface-guidelines/<slug>` directly.

## Output

Answer in your own words:

- the rules that apply, each linked to its page and section (`.../sheets#Best-practices`)
- platform differences
- the SwiftUI API, where one exists
- anything the page's Change log marks as new

Summarize and link. Don't paste long passages of Apple's text.
