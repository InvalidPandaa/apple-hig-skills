# Menus and actions components

Sources: [Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus), [Dock menus](https://developer.apple.com/design/human-interface-guidelines/dock-menus), [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus), [Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus), [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments), [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons), [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)

Glass appearance of buttons, toolbars, and ornaments (`.glass`, `.glassProminent`, scroll edge effects, tinting) is covered by the `hig-liquid-glass` skill; this file covers choosing and configuring the component.

## Choosing between components in this group

| Situation | Component | API |
|---|---|---|
| One immediate action | Button | `Button` + `.buttonStyle(_:)`, `role:` |
| Frequent actions, navigation, title, and search for the current view | Toolbar | `.toolbar { ToolbarItem(placement:) }` |
| Pick one of several mutually exclusive options and show the current one | Pop-up button | `Picker` + `.pickerStyle(.menu)` |
| Several commands that refine one button's purpose (Add ▸, Sort ▸) | Pull-down button | `Menu`, `Menu(primaryAction:)` |
| Commands for a specific item, on long press or secondary click | Context menu | `.contextMenu { }`, `.contextMenu(forSelectionType:menu:primaryAction:)` |
| Cut, Copy, Paste, Look Up on selected content | Edit menu (system) | built into text views; UIKit `UIEditMenuInteraction` |
| Share or export the current content | Activity view (share sheet) | `ShareLink` |
| Every command the app has (Mac, iPad) | Menu bar | `.commands { CommandMenu / CommandGroup }` |
| Mac: functions available while the app isn't frontmost | Menu bar extra | `MenuBarExtra` |
| Mac: actions from the Dock icon | Dock menu | `applicationDockMenu(_:)` |
| iPhone/iPad: actions from the Home Screen icon | Home Screen quick actions | `UIApplicationShortcutItem` |
| visionOS: persistent controls attached to a window, beyond toolbar/tab bar | Ornament | `.ornament(attachmentAnchor:contentAlignment:ornament:)` |

Tie-breakers:
- **Pop-up vs. pull-down:** a pop-up chooses a value and shows it; a pull-down runs commands. Actions, multi-select, or submenus mean pull-down.
- **Pull-down vs. separate buttons:** fewer than three items → plain buttons or toggles; never hide a view's primary actions in a pull-down.
- **Context menu vs. edit menu (iOS):** offer one or the other for an item, never both.
- **Toolbar vs. tab bar:** toolbars act on the current view; tab bars only switch sections.
- **Every hidden menu needs a visible twin:** context-menu, Dock-menu, and toolbar commands must also exist in the main UI or the menu bar.

## Menus (applies to every menu type)

- **Label items with a verb phrase in title case, without articles** ("View Settings", not "View the Settings"); add an ellipsis when the command needs more input. [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Labels)
- **Dim unavailable items in regular menus; keep a menu or submenu openable even if all its items are unavailable.** (Context menus hide instead; see below.) `.disabled(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Labels)
- **Use item icons sparingly and consistently: icons for all items in a group or none**, standard symbols for standard actions (Copy, Share, Delete), and no icon when none clearly fits. (2025–2026) `Label(_:systemImage:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Icons)
- **Put frequent items first and group related ones with separators**, keeping a whole related set together (Paste and Match Style next to Paste). `Divider()`, `Section` [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Organization)
- **One submenu level, about five items max**; use a submenu instead of indenting, and name it after the repeated term ("Sort By"). [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Submenus)
- **Toggled items: a changing label (Show Map / Hide Map) or a checkmark**; add a verb if a state label is ambiguous ("Turn HDR On"). `Toggle` inside `Menu` [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Toggled-items)
- **iOS/iPadOS: use the small (4 icons) or medium (3 icons with labels) top row only for tightly related actions** (Bold/Italic/Underline; Scan/Lock/Pin). `ControlGroup` in a `Menu`; UIKit `UIMenu.preferredElementSize` [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#iOS-iPadOS)
- **visionOS: show menus near the content they affect; over 3D content keep the subtle breakthrough effect.** `.presentationBreakthroughEffect(.subtle)` (visionOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#visionOS)

## Buttons

Use for: instantaneous actions. Not for: on/off state (toggle), picking a value (pop-up button, segmented control), navigation between app sections (tab bar).

- **One or two prominent buttons per view, and mark the preferred option by style, not size.** `.borderedProminent` or `.glassProminent` (26+) for the main action, `.bordered`/`.glass` for the rest. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Style)
- **Use system styles instead of `.buttonStyle(.plain)` plus custom chrome.** A custom button must still show a press state; build it as a `ButtonStyle` using `configuration.isPressed`, never as `.onTapGesture`. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Best-practices)
- **Assign roles.** The likeliest button gets the primary role so Return triggers it (`.keyboardShortcut(.defaultAction)`), but never a destructive one; use `role: .destructive` / `.cancel`, and in 26+ `role: .confirm` and `role: .close` for system Done/Close buttons. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Role)
- **Keep labels monochrome when the content behind them is colorful**; don't tint buttons the same hue as the content layer (see `hig-liquid-glass`). [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Style)
- **Text labels start with a verb in title case ("Add to Cart"); familiar actions use their standard symbols** (`square.and.arrow.up` for Share). [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Content)
- **iOS/iPadOS: show progress inside the button for actions that take a moment**, optionally with an "…ing" label. UIKit `UIButton.Configuration.showsActivityIndicator`; SwiftUI: swap the label for a `ProgressView`. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#iOS-iPadOS)
- **macOS: add a trailing ellipsis when a push button opens another window or view; square (gradient) buttons, help buttons, and image buttons belong in the window body, never the toolbar.** One help button per window, in a bottom corner. `HelpLink` [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#macOS)
- **visionOS: circle for icon-only, capsule for text, centers at least 60 pt apart, no custom hover effects**, and never white fill with black content (that means "toggled on"). [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#visionOS)

Checklist: hit region ≥ 44×44 pt (60×60 pt visionOS).
SwiftUI: `Button`, `.buttonStyle`, `.buttonBorderShape`, `.controlSize`. UIKit `UIButton.Configuration`, AppKit `NSButton` bezel styles.
Platforms: watchOS: full-width buttons for primary actions, corner actions via the toolbar. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#watchOS)

## Toolbars

Use for: the current view's title, navigation (back, sidebar, search), and its most important actions. Not for: switching app sections (tab bar).

- **Choose items deliberately and plan what overflows.** The system adds the overflow menu on iPad and Mac, so never build your own. iOS 27+: rank items with `.visibilityPriority(_:)`, send secondary actions straight to the system overflow with `ToolbarOverflowMenu`, pin a must-stay item with `.topBarPinnedTrailing`. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices)
- **Group items by function, about three groups at most**, using fixed spacers between groups and between adjacent text-labeled buttons. `ToolbarSpacer(.fixed)` (26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Item-groupings)
- **Follow the standard zones.** Leading: back, sidebar toggle, title, document menu (not customizable). Center: common controls (customizable, collapse first). Trailing: must-stay items, inspector toggles, search, More menu, and the primary action. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Item-groupings)
- **Exactly one prominent primary action (Done, Submit), on the trailing side.** `Button(role: .confirm)` or `ToolbarItem(placement: .confirmationAction)`; UIKit `UIBarButtonItem.Style.prominent` (26+). [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Actions)
- **Use borderless system symbols** (`ellipsis`, not `ellipsis.circle`); text only where no symbol fits, such as Edit. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Actions)
- **Use the standard Back and Close buttons, never a text "Back" or "Close".** `Button(role: .close)` (26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Navigation)
- **No custom toolbar backgrounds or tinted items**; let content color the bar, and use a scroll edge effect if separation is needed. `.scrollEdgeEffectStyle(_:for:)` (26+), see `hig-liquid-glass` [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices)
- **Titles: useful, under 15 characters, never the app name**; iOS uses a large title that shrinks on scroll. `.navigationTitle`, `.navigationSubtitle` (iOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Titles)

More: iPad and Mac apps with many tools should allow customization (`.toolbar(id:)` + `ToolbarItem(id:)`); on macOS every toolbar item must also be a menu bar command. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#macOS) iOS 27+ `toolbarMinimizationBehavior(_:for: .navigationBar)` minimizes the navigation bar on scroll. iOS 27.1+ may place bars on a vertical axis (iPhone Duo); opt out with `toolbarVerticalBehavior(.disabled)` only for layouts like full-screen players or calculators ([SwiftUI](https://developer.apple.com/documentation/swiftui/view/toolbarverticalbehavior(_:))).
SwiftUI: `.toolbar`, `ToolbarItem`, `ToolbarItemGroup`, `DefaultToolbarItem(kind:placement:)` (26+), `.sharedBackgroundVisibility(_:)` (26+). UIKit `UINavigationBar`/`UIToolbar`, AppKit `NSToolbar`.
Platforms: iPadOS: a toolbar can share the top row with the tab bar. visionOS: system toolbar sits below the window as an ornament; no vertical toolbars, no pull-down menus in it, and don't let the window shrink narrower than the toolbar. watchOS: `.topBarLeading`, `.topBarTrailing`, `.bottomBar`, and a scrolling `.primaryAction` button. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#visionOS)

## Context menus

Use for: the few commands most relevant to one item. Not for: advanced or rare commands, or the only path to a command.

- **Offer every context-menu command somewhere visible too** (toolbar, detail view, Mac menu bar). [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#Best-practices)
- **Keep it short (about three groups) and consistent**: if some rows of a kind have context menus, all of them do. [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#Best-practices)
- **Hide unavailable items instead of dimming them** (on macOS, Cut/Copy/Paste may appear dimmed). [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#Best-practices)
- **No keyboard shortcuts in context menus; one submenu level at most.** [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#Best-practices)
- **Put destructive items last and mark them** so they render red. `Button(role: .destructive)` [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#Best-practices)
- **Title the menu only when it clarifies scope** (e.g. "3 Messages" for a multi-selection). [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#Content)
- **iOS/iPadOS: show a preview of the actual item whose clipping matches its shape**; on iPad, a context menu on empty space can create new objects. `.contextMenu(menuItems:preview:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#iOS-iPadOS)

SwiftUI: `.contextMenu`, `.contextMenu(forSelectionType:menu:primaryAction:)` for `List`/`Table` selections. UIKit `UIContextMenuInteraction`, AppKit `NSView.menu`.
Platforms: visionOS: keep the menu shorter than the window; prefer a context menu over an extra panel. Not available on watchOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus#visionOS)

## Edit menus

Use for: system editing commands on selected text or objects. Not for: custom buttons that duplicate Copy/Paste.

- **Use the system edit menu and the system gestures to open it**; don't build a lookalike or add duplicate Copy/Paste controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/edit-menus#Best-practices)
- **Show only commands that apply** (no Copy without a selection, no Paste with an empty pasteboard), and place custom commands next to related system ones. [HIG](https://developer.apple.com/design/human-interface-guidelines/edit-menus#Best-practices)
- **Let people copy static content (captions, statuses), but not control labels.** `.textSelection(.enabled)` [HIG](https://developer.apple.com/design/human-interface-guidelines/edit-menus#Best-practices)
- **Back every edit command with undo and redo**, and keep Delete (no pasteboard) distinct from Cut. `UndoManager` [HIG](https://developer.apple.com/design/human-interface-guidelines/edit-menus#Best-practices)
- **iPadOS: test both forms**, the horizontal bar from touch and the vertical menu from pointer or keyboard; move the menu if it covers key content. [HIG](https://developer.apple.com/design/human-interface-guidelines/edit-menus#iOS-iPadOS)

API: automatic in `TextField`/`TextEditor`; UIKit `UIEditMenuInteraction`; macOS uses the Edit menu (see the menu bar). Not available on tvOS or watchOS.

## Activity views (share sheet)

Use for: system sharing and actions on the current content, opened from the Share button. Not for: a custom share UI.

- **Open the share sheet from the standard Share button**, not from other entry points. `ShareLink`, `square.and.arrow.up` [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-views#Best-practices)
- **Don't duplicate system actions like Print**; if yours differs, give it a specific title ("Print Transaction"). [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-views#Best-practices)
- **Exclude activities that make no sense in your app**; name custom actions with a short verb phrase, no company name, with a symbol. UIKit `excludedActivityTypes`, `UIActivity` [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-views#Best-practices)
- **Share/action extensions: few steps, no extra modals over the extension, long work continues in the background with status in the app**, and no notification just for success. [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-views#Share-and-action-extensions)

SwiftUI: `ShareLink`. UIKit `UIActivityViewController`.
Platforms: macOS has no activity view (`ShareLink` shows the sharing picker, and share/action extensions still work); the HIG lists no activity view for tvOS or watchOS.

## Pop-up buttons

Use for: a flat list of mutually exclusive options, when space is tight. Not for: actions, multi-select, or submenus (pull-down button); switching tabs (tab view, segmented control).

- **Show a sensible default selection and make the choices predictable** from a label or the button title. [HIG](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons#Best-practices)
- **Add a "Custom…" item for rare options** instead of cluttering the menu. [HIG](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons#Best-practices)
- **iPadOS: in a popover or modal, use a pop-up button for a small set of row options instead of drilling into a detail view.** [HIG](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons#iPadOS)

SwiftUI: `Picker` + `.pickerStyle(.menu)`. UIKit `UIButton` with `showsMenuAsPrimaryAction` + `changesSelectionAsPrimaryAction`, AppKit `NSPopUpButton`. Not available on tvOS or watchOS.

## Pull-down buttons

Use for: commands that refine one button's purpose (Add which item, Sort by what). Not for: a value choice (pop-up button), one or two items (plain buttons), all of a view's actions.

- **List at least three items, but not so many that scanning is slow.** [HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons#Best-practices)
- **Mark destructive items and confirm them** with an action sheet (iOS) or popover (iPad). `Button(role: .destructive)` + `.confirmationDialog` [HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons#Best-practices)
- **A More (`ellipsis`) button is fine for secondary items, but it hides them**; weigh space against discoverability. [HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons#iOS-iPadOS)
- **A button can show its menu on long press** while tapping still runs its main action. `Menu(primaryAction:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons#iOS-iPadOS)

SwiftUI: `Menu`. UIKit `UIButton.menu`, AppKit `NSPopUpButton` (pull-down mode). Not available on tvOS or watchOS.

## The menu bar

Use for: the complete, discoverable list of an app's commands on Mac and iPad. Not for: the only path to a feature on iPad, where the bar is often hidden.

- **Keep the standard menus and order:** App, File, Edit, Format, View, app-specific, Window, Help; SwiftUI provides them, so extend with `CommandMenu` and `CommandGroup(replacing:/before:/after:)` rather than rebuilding. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Anatomy)
- **Never hide menu bar items based on context; disable them.** [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Best-practices)
- **List every command in the menu bar, including toolbar and context-menu ones, with standard shortcuts.** `.keyboardShortcut` [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-specific-menus)
- **Always include a View menu (at least Enter Full Screen) and a Window menu (Minimize, Zoom), even with one window**; show/hide titles reflect the current state. `SidebarCommands()`, `ToolbarCommands()` [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#View-menu)
- **Standard names:** Settings… in the app menu (`Settings` scene), Delete not Erase/Clear, "Undo Typing" style targets, Duplicate over Save As, Open Recent lists names not paths. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
- **Option-key alternate items are shortcuts only**: never the sole path, one modifier, menu bar menus only. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Dynamic-menu-items)
- **iPadOS (2025): the menu bar is hidden until revealed, so every function needs a UI path too**; Settings opens your page in the Settings app, with in-app preferences as a separate item below; consider each tab as a View menu item with a shortcut. `.commands`; UIKit `UIMainMenuSystem` (26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#iPadOS)
- **Menu bar extras: open a menu, not a popover; let people choose to show it; don't depend on it being visible**; use a template symbol. `MenuBarExtra` + `.menuBarExtraStyle(.menu)` (`.window` only when a menu can't hold it) [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Menu-bar-extras)

Platforms: macOS and iPadOS only.

## Ornaments

visionOS only. Use for: frequently needed controls tied to a window (Now Playing). Not for: toolbars and tab bars, which become ornaments automatically.

- **Use the system toolbar and `TabView` first; build an ornament only for custom components.** [HIG](https://developer.apple.com/design/human-interface-guidelines/ornaments#Best-practices)
- **Keep it visible (hide only during immersive viewing), no wider than its window, and limit how many you add.** [HIG](https://developer.apple.com/design/human-interface-guidelines/ornaments#Best-practices)
- **Use borderless buttons on the ornament's glass**; the system adds the hover effect. [HIG](https://developer.apple.com/design/human-interface-guidelines/ornaments#Best-practices)

SwiftUI: `.ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`, e.g. `attachmentAnchor: .scene(.bottom)`.

## Home Screen quick actions

iOS/iPadOS only. Up to four high-value actions on the app icon, changed only in predictable ways (recent conversations, location). Short titles without the app name, optional subtitle, an SF Symbol (never emoji). API: `UIApplicationShortcutItem` (static in Info.plist, dynamic via `UIApplication.shortcutItems`). [HIG](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions#Best-practices)

## Dock menus

macOS only. Add a few high-value items (open windows, actions useful when the app isn't frontmost, like New Message) and make each available elsewhere too. AppKit `applicationDockMenu(_:)` on the app delegate. [HIG](https://developer.apple.com/design/human-interface-guidelines/dock-menus#Best-practices)
