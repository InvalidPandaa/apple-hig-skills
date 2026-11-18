---
name: hig-design
description: Use when asked to design, plan or spec a native Apple-platform screen, feature or app flow before writing code, for example "design the settings screen", "how should this work on iPad and Mac", "plan the onboarding", or when a UI task is big enough that structure and components should be agreed before implementation.
---

# HIG Design Spec

Agree on the design before writing code. A spec that names the system component for every element and lists the brief's conflicts with the HIG is much cheaper to change than finished SwiftUI.

## Process

Follow the workflow in `../apple-hig/SKILL.md`. Read `hig-platforms`, `hig-components`, `hig-patterns`, `hig-foundations`, `hig-liquid-glass` and `hig-accessibility` (sibling folders) as each step needs them. Verify version-specific rules with `python3 ../apple-hig/scripts/hig.py fetch <slug> --section "<Heading>"`.

## Output

Reply with this spec and no code:

1. **Context**: platform(s), minimum OS, the screen's job, your assumptions.
2. **Brief conflicts**: requirements that contradict the HIG, each with a link and a compliant alternative. Write "None" if there are none.
3. **Structure**: navigation model and how each flow is presented (push, sheet, popover, alert, window), with the SwiftUI container for each.
4. **Components**: every element on the screen → system component → SwiftUI API, with a note on configuration.
5. **States**: empty, loading, error, offline, first run, accessibility text sizes, Dark Mode.
6. **Accessibility**: labels for icon-only controls, grouping, headings, reflow at large text sizes.
7. **Platform differences**: what changes per platform, if more than one is targeted.
8. **Sources**: the HIG pages you relied on, as links.

End by asking whether to implement it. If nobody can answer (unattended run), implement the spec as written and keep the Brief conflicts list at the top of your summary.
