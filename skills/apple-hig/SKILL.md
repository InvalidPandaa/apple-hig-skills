---
name: apple-hig
description: Use when designing, building, or reviewing the UI or UX of a native app for iPhone, iPad, Mac, Apple Watch, Apple TV, Apple Vision Pro or iPhone Duo in SwiftUI, UIKit or AppKit; when a task says "native", "Apple-like", "feels like an Apple app", "follow the HIG" or "Human Interface Guidelines"; or when you need the current wording of an Apple design guideline.
---

# Apple Human Interface Guidelines

Native Apple UI is good when it does what people already expect from the system. Start from system components and behavior, apply the guidelines to this particular app, flag requirements that work against them, and check rules against the live guidelines instead of memory.

## Workflow for a screen or feature

1. **Platform and OS.** Which devices, which minimum OS. iOS/iPadOS/macOS 26 and later use Liquid Glass; 27 is current (2026). Read the platform file in `hig-platforms` for every platform you target.
2. **Check the brief against the HIG.** Before building, compare each requirement with the guidelines (see "Brief conflicts" below and in each skill). For every conflict, tell the person what conflicts, link the rule, and propose the compliant alternative. If they still want it, build it their way. If you can't ask (unattended run), build what was asked and put the conflict and the alternative at the top of your summary.
3. **Structure and navigation.** Choose the app's navigation model (tab bar, sidebar, split view, single window, hierarchy) and the presentation of each flow (push, sheet, popover, alert, new window). Use `hig-components`.
4. **Components.** Use the system component that fits. Build a custom control only when no system component fits, and then copy the system's behavior: states, accessibility, sizes, keyboard and pointer support.
5. **Foundations.** Semantic colors, text styles, SF Symbols, system margins, writing. Use `hig-foundations`. For bars, controls floating over content and anything glass, use `hig-liquid-glass`.
6. **Behavior and flows.** Onboarding, permissions, loading, empty states, errors, undo, search, settings. Use `hig-patterns`.
7. **Accessibility.** VoiceOver semantics, Dynamic Type reflow, contrast, motion. Use `hig-accessibility`.
8. **Review your own result** with the `hig-review` checklist before you hand it over.

## Design principles (2026)

Apple reintroduced explicit design principles in June 2026. Use them to settle trade-offs. [HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)

| Principle | What it asks of a design |
|---|---|
| Purpose | Know what the product is for; put the few features that matter first and make them excellent; don't rebuild what exists without a reason. |
| Agency | Get people to their content fast, let them move freely instead of locking them into flows, make guided flows skippable, make mistakes cheap to reverse. |
| Responsibility | Say plainly what the app does and why, explain every permission request, collect only the data you need, guard against misuse. |
| Familiarity | Reuse concepts people know from the world and from the system, keep elements consistent, show clearly what is happening. |
| Flexibility | Design for the full range of people and abilities from the start, keep context stable across devices, support many input methods, give every platform the same care. |
| Simplicity | Include what's needed (not the same as minimal), use the fewest clear words, make the hierarchy obvious. |
| Craft | Details show how much you care; finish the work. |

## Brief conflicts that come up everywhere

| Request | Conflict | Propose instead |
|---|---|---|
| In-app Light/Dark/System theme picker | The HIG advises against app-specific appearance settings; people expect the systemwide choice to apply. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices) | Follow the system appearance. Exception: media apps that are always dark. |
| App copies of systemwide options (text size slider, reduce motion, biometrics opt-in) | Settings should not duplicate systemwide options. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices) | Respect the system setting; offer only app-specific choices. A switch to mute the app's own haptics is fine: the HIG asks for haptics to be optional. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices) |
| Hide the navigation bar and draw a custom header | You lose back navigation, swipe-back, Liquid Glass, scroll edge effects and accessibility. | Keep the system bar; put actions in `.toolbar`. |
| Brand color on all text and backgrounds | Weakens hierarchy and often fails contrast. | Use the brand color as the app tint/accent and keep text in semantic colors. |
| Same iPhone layout on iPad/Mac | Each platform has its own idioms. | Share structure and data, adapt navigation and chrome (`hig-platforms`). |

## Verify instead of recalling

Look up the live page before you rely on a rule that is version-specific (2025 and later), a specific number, a rule you are about to cite in a review, or anything you're unsure of. The tool prints Apple's current page as Markdown (standard-library Python, network required):

```sh
python3 scripts/hig.py search "tab bar"                    # find the slug
python3 scripts/hig.py fetch tab-bars                      # whole page
python3 scripts/hig.py fetch sheets --section "Best practices"
python3 scripts/hig.py fetch tab-bars --section "Change log"   # what changed recently
python3 scripts/hig.py fetch "/documentation/swiftui/view/glasseffect(_:in:)"   # check an API
```

If `fetch` starts with a note that the page changed after the skills were last synced, the skill summaries on that topic may be out of date: follow the live page where they disagree.

Paths are relative to this skill's folder. From another skill in this set, use `../apple-hig/scripts/hig.py`. Without Python, read `https://developer.apple.com/design/human-interface-guidelines/<slug>` directly. `index.json` lists all ~170 page slugs by area (Getting started, Foundations, Patterns, Components, Inputs, Technologies). Technologies pages (Apple Pay, CarPlay, HealthKit, Sign in with Apple, Siri, widgets and more) have no summary in this set: fetch them when the feature comes up.

When you cite the HIG, link the page and section (`.../sheets#Best-practices`). Don't cite rules from memory without a link.

## Skill map

| Skill | Use it for |
|---|---|
| `hig-platforms` | iOS, iPadOS, macOS, watchOS, tvOS, visionOS, iPhone Duo, games: idioms, inputs, porting checklists |
| `hig-components` | Choosing and configuring bars, lists, menus, sheets, alerts, controls, widgets |
| `hig-liquid-glass` | The current design language: glass, bars, scroll edge effects, migrating older screens |
| `hig-foundations` | Color, typography, layout, SF Symbols, icons, Dark Mode, motion, writing, branding |
| `hig-patterns` | Flows: onboarding, permissions, loading, feedback, undo, search, settings, modality, AI features |
| `hig-accessibility` | VoiceOver, Dynamic Type, contrast, motion, inclusion, right-to-left |
| `hig-review` | Auditing code or screenshots against the HIG, with a fixed findings format |
| `hig-design` | A design spec (structure, components, states, accessibility, sources) before code |
| `hig-lookup` | Answering "what does the HIG say about X" from the live pages |

## Common mistakes

- Building what the brief says when it contradicts the HIG, without saying anything.
- Rebuilding system chrome (bars, back buttons, alerts, tab bars) by hand.
- Hard-coding colors, font sizes and spacing that the system provides semantically.
- Treating every Apple platform like a big iPhone.
- Citing "the HIG says" without a link, or relying on pre-2025 memory for bars, materials and search.
