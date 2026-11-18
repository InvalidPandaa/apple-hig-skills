---
description: Write a HIG-based design spec for a native Apple-platform screen or feature before any code is written
argument-hint: <screen or feature, platform(s)>
---

Design this for a native Apple app: $ARGUMENTS

Use the `apple-hig` skill and follow its workflow. Load `hig-platforms`, `hig-components`, `hig-patterns`, `hig-foundations`, `hig-liquid-glass` and `hig-accessibility` as each step needs them. Verify version-specific rules with `hig.py`.

Reply with this spec and no code:

1. **Context**: platform(s), minimum OS, the screen's job, your assumptions.
2. **Brief conflicts**: requirements that contradict the HIG, each with a link and a compliant alternative. Write "None" if there are none.
3. **Structure**: navigation model and how each flow is presented (push, sheet, popover, alert, window), with the SwiftUI container for each.
4. **Components**: every element on the screen → system component → SwiftUI API, with a note on configuration.
5. **States**: empty, loading, error, offline, first run, accessibility text sizes, Dark Mode.
6. **Accessibility**: labels for icon-only controls, grouping, headings, reflow at large text sizes.
7. **Platform differences**: what changes per platform, if more than one is targeted.
8. **Sources**: the HIG pages you relied on, as links.

End by asking whether to implement it.
