---
name: hig-components
description: Use when choosing or configuring a native Apple UI component in SwiftUI, UIKit or AppKit (tab bar vs. sidebar, sheet vs. popover vs. alert vs. confirmation dialog, toolbar items, menus, context menus, lists, tables, pickers, segmented controls, toggles, text fields, search, progress, widgets, Live Activities, controls, notifications), or when code builds a custom control, bar or dialog that the system already provides.
---

# HIG Components

Pick the system component whose job matches the situation, then configure it the way the HIG describes. People already know how system components behave. A custom imitation has to rebuild states, accessibility, keyboard, pointer and Liquid Glass behavior, and usually misses some of them.

## Quick decisions

**Navigation model**

| Situation | Component | SwiftUI |
|---|---|---|
| A few top-level sections on iPhone | Tab bar | `TabView { Tab(...) }` |
| More sections, or iPad/Mac/visionOS | Tab bar that adapts to a sidebar | `.tabViewStyle(.sidebarAdaptable)`, `TabSection` |
| Mac app with deep content, sidebar that never becomes tabs | Split view with sidebar | `NavigationSplitView` + `List(selection:)` |
| Drill down through a hierarchy | Navigation stack | `NavigationStack` + `NavigationLink(value:)` |
| App-wide search with discovery | Search tab | `Tab(role: .search)` |
| Search within one view | Search field | `.searchable(text:placement:)` |

**Presentation.** Ask: did the person start this, and is it news, a choice, or a task?

| Situation | Component | SwiftUI |
|---|---|---|
| Unexpected problem, or a rare destructive action that can't be undone | Alert | `.alert` |
| The person chose an action and must pick its outcome | Confirmation dialog | `.confirmationDialog` |
| Short task tied to the current context | Sheet | `.sheet` + `.presentationDetents` |
| A few controls tied to a button, regular width | Popover | `.popover` |
| Immersive media, camera, long multistep edit (iPhone/iPad) | Full-screen cover | `.fullScreenCover` |
| A task people keep open beside other content (iPad, Mac, visionOS) | Window | `WindowGroup(for:)` + `openWindow` |
| A common destructive action that can be undone | No dialog: act and offer Undo | `UndoManager` |

**Actions and choices**

| Situation | Component | SwiftUI |
|---|---|---|
| Actions on the current view | Toolbar | `.toolbar { ToolbarItem(placement:) }` |
| Commands for one item | Context menu | `.contextMenu`, `.contextMenu(forSelectionType:)` |
| Several commands behind one button | Pull-down button | `Menu` |
| Choose one value and show it | Pop-up button / menu picker | `Picker` + `.pickerStyle(.menu)` |
| 2–5 modes or views of one thing | Segmented control | `Picker` + `.pickerStyle(.segmented)` |
| On/off in a list row (iOS) | Switch | `Toggle` |
| On/off outside a list (iOS) | Toggle button | `.toggleStyle(.button)` |
| Share or export | Share sheet | `ShareLink` |
| Every command (Mac, iPad keyboard) | Menu bar | `.commands { CommandMenu / CommandGroup }` |

**Status**: measurable work → `ProgressView(value:total:)`; unknown length → `ProgressView()`; pull to reload → `.refreshable`; a value in a range that isn't "work done" → `Gauge`; nothing to show → `ContentUnavailableView`.

## Rules that cut across components

- **Use the system bar, not a drawn one.** Keep the navigation bar, tab bar and toolbar, and put actions in `.toolbar`. Hidden bars plus a custom header lose back-swipe, Liquid Glass, scroll edge effects and accessibility. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- **Tab bars navigate, toolbars act.** Never put an action in a tab. Keep the tab bar visible on pushed screens, and don't disable or hide tabs. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Don't build your own overflow menu (iOS 27+).** The system adds one. Steer it with `.visibilityPriority(_:)` and `ToolbarOverflowMenu`. See references/menus-and-actions.md.
- **Make sheet buttons follow the pattern (2026).** Cancel goes on the leading side and Done on the trailing side. A multistep sheet replaces Cancel with Back after step one. Never show Cancel, Back and Done together, and never Done alone. Use `.cancellationAction`, `.confirmationAction` and `Button(role: .close)` when there's nothing to discard. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices)
- **One sheet at a time.** Close the first sheet before showing another.
- **Mark destructive actions with `role: .destructive`** and keep them away from frequent actions. Don't confirm a common deletion that Undo can reverse.
- **Every hidden command has a visible twin.** Anything in a context menu, Dock menu or toolbar also exists in the main UI or the menu bar. Context menus hide unavailable items; the menu bar dims them. [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)
- **Menu icons: all or none within a group,** using the standard symbols for standard actions (2025–2026). [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Icons)
- **Switches belong in list rows on iOS.** Anywhere else use a toggle button. On the Mac, use checkboxes, and never put switches in toolbars.
- **A custom control must match the system.** If no component fits, make it a `Button`, `Toggle` or a view with full accessibility traits, a pressed state, a 44×44 pt target (iOS), keyboard focus and pointer hover, never an `Image` with `.onTapGesture`.

## Brief conflicts

| Request | Why it conflicts | Propose instead |
|---|---|---|
| "Put a + action in the tab bar" | Tabs navigate; actions go in a toolbar. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices) | Toolbar button or a primary action in the view |
| "Floating action button like Android" | Not an Apple idiom; it competes with bars and Liquid Glass controls | Toolbar item (`.primaryAction`, bottom toolbar on iPhone) |
| "Confirm every delete" | Confirmations are for actions that can't be undone or that people didn't expect. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts) | Delete right away and offer Undo; confirm only permanent deletion |
| "Hide the tab bar on detail screens" | The tab bar should stay visible during navigation. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices) | Keep it; hide only for a modal or immersive view |
| "Use our custom dropdown/picker component" | Loses system behavior on each platform | `Picker`/`Menu` with the app tint |
| "Settings as a tab on the Mac" | Mac settings live in the app menu (⌘,) | `Settings` scene |

## Common mistakes

- An alert for something the person just chose to do, where a confirmation dialog fits. Or a confirmation dialog for unexpected news, where an alert fits.
- A `Picker` with `.segmented` for actions instead of modes.
- `TabView` on macOS expected to give a tab bar: with the automatic style it draws a bordered pane switcher. Use a sidebar for app sections.
- A popover in compact width (SwiftUI turns it into a sheet), or a warning shown in a popover.
- Real-time updates in a widget instead of a Live Activity; errors sent as notifications.

## References

Read the file for the group you're working in. Each starts with a table for choosing within the group, then has an entry per component (use for / not for, rules, SwiftUI API, platforms).

- [references/presentation.md](references/presentation.md): alerts, confirmation dialogs, sheets, popovers, windows, panels, scroll views, page controls
- [references/menus-and-actions.md](references/menus-and-actions.md): buttons, toolbars, menus, context and edit menus, share, menu bar, ornaments, quick actions
- [references/navigation-and-search.md](references/navigation-and-search.md): tab bars, sidebars, search fields and tabs, token fields, path controls
- [references/layout-and-organization.md](references/layout-and-organization.md): lists, tables, collections, split views, outline and column views, disclosure, labels, boxes, tab views
- [references/selection-and-input.md](references/selection-and-input.md): toggles, pickers, segmented controls, sliders, steppers, text fields, keyboards, color and image wells
- [references/status.md](references/status.md): progress indicators, gauges, rating indicators, activity rings
- [references/content.md](references/content.md): charts, image views, text views, web views
- [references/system-experiences.md](references/system-experiences.md): widgets, Live Activities, controls, complications, App Shortcuts, snippets, notifications, Top Shelf

Glass styling of any of these is in `hig-liquid-glass`; platform differences are summarized in `hig-platforms`.

## Look it up live

```sh
python3 ../apple-hig/scripts/hig.py fetch <component-slug>   # e.g. sheets, toolbars, tab-bars, menus
python3 ../apple-hig/scripts/hig.py search "<component>"
```
