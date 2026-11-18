---
name: hig-review
description: Use when reviewing, auditing or critiquing a native Apple-platform screen, SwiftUI/UIKit/AppKit view code, a screenshot, a mockup or a pull request for conformance with Apple's Human Interface Guidelines, or when asked "does this follow the HIG", "is this Apple-like", "what's wrong with this screen", or to check your own UI work before handing it over.
---

# HIG Review

A review is useful when the person can act on it in order: the worst problems first, each one tied to a rule they can check and a fix they can paste.

## Process

1. **Establish the context.** Platform(s), minimum OS (26+ means Liquid Glass), and the screen's job. If the input doesn't say, infer it from the code (`.topBarTrailing` means iOS, `NSWindow` means macOS) and state your assumption in the report header.
2. **Walk the checklist below** from top to bottom. Read the code or image for each area; don't stop at the first few findings.
3. **Verify every rule you cite that is not a basic.** Fetch the section with `python3 ../apple-hig/scripts/hig.py fetch <slug> --section "<Heading>"` and use the page and heading you actually read for the link. Leave out anything you couldn't back with a page.
4. **Rank the findings** by severity, then write the report in the format below.

## Severity

| Level | Meaning | Examples |
|---|---|---|
| Blocker | Some people can't use it, or core platform behavior is broken | No accessible label on an icon-only button, fixed font sizes, text contrast below 4.5:1, lost back navigation, information conveyed only by color |
| Major | Clearly not how the platform works; people notice | Hand-built bars instead of the system toolbar/tab bar, alert with Yes/No, iPhone layout on Mac, glass in the content layer, tab bar hidden on push |
| Minor | Polish and consistency | Spacing off the system margins, mixed icon styles in a menu group, title-case slips, animation too long |

## Report format

Use exactly this structure:

```markdown
## HIG review: <screen name>
Context: <platform(s), minimum OS, assumptions>
Summary: <n> blocker, <n> major, <n> minor. <one sentence on the biggest theme>

### Blocker
1. **<Problem in a few words>** (`File.swift:42` or the screenshot region)
   Rule: <the guideline in your own words>. [<Page> › <Section>](https://developer.apple.com/design/human-interface-guidelines/<slug>#<Section>)
   Fix: <concrete change; a short SwiftUI snippet when it helps>

### Major
...

### Minor
...

### Brief conflicts
<requirements in the brief that contradict the HIG, with the compliant alternative; omit the section if none>
```

After the report, give corrected code if the person asked for it or the input was code. Merge findings that share one cause (for example "custom header replaces the navigation bar" covers missing back swipe, missing glass and small targets) into one finding and list the effects in its Rule line.

## Checklist

**Structure and navigation**
- System navigation bar, tab bar, sidebar, toolbar kept visible and used, not rebuilt. ([toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [tab-bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- Tab bar for navigation only, not actions; stays visible on push. Search placement fits the app (tab, toolbar or inline).
- Presentation matches the task: alert vs. confirmation dialog vs. sheet vs. popover vs. full-screen vs. window. One sheet at a time; Done paired with Cancel.
- Platform idioms: Mac has menu bar commands, keyboard shortcuts, Settings scene, multiple windows; iPad adapts to sidebar and multitasking; watchOS is glanceable.

**Components and controls**
- `Button`, `Toggle`, `Picker`, `Menu` etc. instead of tap gestures on images or shapes.
- Destructive actions marked with `role: .destructive`, kept apart from frequent actions, reversible with undo where possible.
- Button and alert labels are specific verbs; no Yes/No, no "Submit"/"OK" where a verb fits.
- Toolbar items grouped by meaning; primary action prominent; icons from SF Symbols.

**Liquid Glass (OS 26+)**
- Glass only in the functional layer (bars, floating controls), never on content or stacked on glass; no custom blur imitations.
- No forced opaque bar backgrounds (`toolbarBackground`) left over from older designs; scroll edge effects not blocked.
- Tint used sparingly, with the app accent rather than hard-coded colors. See `hig-liquid-glass`.

**Foundations**
- Text styles (`.body`, `.headline`, ...) or scaled custom fonts; no fixed point sizes.
- Semantic colors (`.primary`, `.secondary`, system backgrounds); works in Dark Mode and Increase Contrast.
- System margins and spacing; content respects safe areas; layout adapts to size classes.
- SF Symbols at matching weight and scale; one style per group.
- Writing: concise, consistent capitalization, helpful errors.

**Behavior**
- Permissions asked in context with a reason; no forced account before value; no rating prompt at launch.
- Loading, empty and error states exist (`ContentUnavailableView` for empty).
- Animations short and purposeful; respect Reduce Motion.

**Accessibility** (see `hig-accessibility`)
- Every interactive element has a meaningful label; toggled state announced; decorative images hidden.
- Related elements grouped; headings marked; reading order sensible.
- Layout reflows at accessibility text sizes; targets at least 44×44 pt on iOS (platform-specific elsewhere).
- Color is never the only signal; contrast at least 4.5:1 for text.

## Common mistakes

- Unranked lists of twenty equal-weight bullets. Rank and merge.
- Citing "the HIG says" without a link, or linking a page that doesn't contain the rule.
- Reviewing only what's visible in code and ignoring states (empty, loading, error, AX sizes, Dark Mode).
- Reporting a requirement conflict as a code bug. Put it under Brief conflicts, because the decision belongs to the person.
