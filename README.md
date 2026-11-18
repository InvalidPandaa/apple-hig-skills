# apple-hig-skills

Agent skills for building native Apple-platform apps that follow Apple's current
[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/):
SwiftUI, UIKit and AppKit on iPhone, iPad, Mac, Apple Watch, Apple TV, Apple Vision Pro and
iPhone Duo, including Liquid Glass (OS 26 and later) and the 2026 updates.

Coding agents already know a lot of HIG basics. In our baseline tests (see `evals/`) they mostly got
these things wrong:

- **Conflicting requirements.** They silently built requirements that contradict the guidelines,
  such as an in-app Light/Dark theme picker.
- **No sources.** They quoted "the HIG" from memory without links, and they didn't know the 2025–2026
  changes (search as a tab, sheet button rules, menu icons, iPhone Duo).
- **Hand-built chrome.** They drew custom bars, glass and controls where system components exist.
- **Unranked reviews.** Their reviews were long, unranked lists.

These skills target exactly those gaps. They don't copy Apple's text. They contain original
summaries with links, plus a small tool that fetches the live guidelines when an agent needs the
exact current rule.

## Skills

| Skill | Purpose |
|---|---|
| `apple-hig` | Entry point: design workflow, the 2026 design principles, common brief conflicts, live lookup tool |
| `hig-platforms` | iOS, iPadOS, macOS, watchOS, tvOS, visionOS, iPhone Duo, games: idioms, inputs, porting checklists |
| `hig-components` | Choosing and configuring system components, with the SwiftUI API for each |
| `hig-liquid-glass` | The Liquid Glass design language, its SwiftUI APIs, and migrating older screens |
| `hig-foundations` | Color, typography, layout, SF Symbols, icons, Dark Mode, motion, writing, branding |
| `hig-patterns` | UX flows: onboarding, permissions, loading, feedback, undo, search, settings, modality, AI |
| `hig-accessibility` | VoiceOver, Dynamic Type, contrast, motion, inclusion, right-to-left |
| `hig-review` | Auditing code or screenshots, with severity levels and linked findings |

Claude Code also gets three commands and a subagent:

| | |
|---|---|
| `/apple-hig:design <feature>` | Design spec (structure, components, states, accessibility, sources) before code |
| `/apple-hig:review [target]` | Ranked HIG review of files, a screenshot or the current changes |
| `/apple-hig:lookup <topic>` | Fetch and summarize the current guideline on a topic |
| `hig-reviewer` agent | Independent read-only review after a screen is built |

## Install

**Claude Code** (plugin with skills, commands and agent):

```sh
/plugin marketplace add <github-owner>/apple-hig-skills
/plugin install apple-hig@apple-hig-skills
```

For a local checkout, use `/plugin marketplace add /path/to/apple-hig-skills`.

**Other agents** (Codex, Gemini CLI, Cursor, Copilot and any tool that reads
[Agent Skills](https://agentskills.io)). Install the skills only:

```sh
npx skills add <github-owner>/apple-hig-skills
```

Or copy or symlink the folders in `skills/` into your agent's skills directory, for example
`~/.agents/skills/` or `~/.claude/skills/`. Keep `apple-hig` installed next to the others, because
they use its lookup tool at `../apple-hig/scripts/hig.py`.

## Live lookup

```sh
python3 skills/apple-hig/scripts/hig.py search "search field"
python3 skills/apple-hig/scripts/hig.py fetch search-fields --section "iOS"
python3 skills/apple-hig/scripts/hig.py fetch "/documentation/swiftui/view/glasseffect(_:in:)"
python3 skills/apple-hig/scripts/hig.py index      # refresh the page index after WWDC
```

It uses only the Python standard library and needs network access to developer.apple.com.

## Development

```sh
python3 -I skills/apple-hig/scripts/hig.py selftest   # renderer self-test (offline)
python3 -I scripts/validate.py                        # frontmatter, links, slugs, sizes
python3 -I scripts/validate.py --online               # + HIG anchors, API links, copied-text check
claude plugin validate .
claude plugin eval . --allow-tools "Bash(python3:*)" WebFetch   # with/without-plugin comparison
```

After each WWDC, run `hig.py index` and read the HIG's
[What's new](https://developer.apple.com/design/whats-new/) page. Then update the skills that
cover the changed pages and rerun the online validation.

## License and notice

MIT for the original text and code in this repository. This project is not affiliated with Apple.
See [NOTICE.md](NOTICE.md) for details on trademarks and Apple's content.
