# macOS

Sources: [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar), [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards), [Windows](https://developer.apple.com/design/human-interface-guidelines/windows), [Settings](https://developer.apple.com/design/human-interface-guidelines/settings), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo), [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst)

## What people expect
- Stationary use at a desk, large (often several) displays, sessions from minutes to hours, many apps open at once.
- Keyboard and pointer first. On a Mac with a touch display (2026) people reach forward for brief, deliberate touches, not sustained work.
- More content in fewer levels, little modality, resizable and full-screen windows, a complete menu bar, shortcuts for everything frequent, precise selection, personalization (toolbar customization, window configuration). [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos#Best-practices)

## Menu bar and commands
- **Keep the standard menus in order:** app menu, File, Edit, Format, View, app-specific menus, Window, Help. Rename or drop File only if you handle no files; drop Format without rich text. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Anatomy)
- **List every command in the menu bar, including rare ones and everything in the toolbar or context menus.** That is where people look first, where shortcuts live, and how Full Keyboard Access reaches them. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-specific-menus)
- **Disable, don't hide, unavailable items.** [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Best-practices)
- **Use the system's icons for common menu actions** (Copy, Share, Delete) and keep icon use consistent. (2025–2026 guidance) [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Best-practices)
- **App menu:** About first in its own group (short name, no version), then Settings…, app-level config items, Services, Hide/Hide Others/Show All, Quit. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-menu)
- **File menu:** "New *Item*" named for what you create; Open… with an ellipsis; Open Recent without paths, newest first; autosave; prefer Duplicate over Save As/Export unless you truly export another format. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu)
- **Edit menu:** Undo/Redo at the top naming the action ("Undo Paste"), Cut, Copy, Paste, Paste and Match Style, Delete (not "Erase"/"Clear"), Select All, Find submenu. Find for files or objects can live in File instead. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu)
- **View menu, even if it only holds Enter Full Screen.** Show/Hide items reflect current state ("Hide Sidebar" when visible). No window navigation here. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#View-menu)
- **Window menu, even with one window.** Minimize and Zoom must be reachable from the keyboard; list open windows alphabetically; Zoom never toggles full screen. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Window-menu)
- **App-specific menus mirror your hierarchy** (Mailbox, Message) and go from general to specific; prefer one-word titles.
- **Dynamic (Option-revealed) items: single modifier, menu bar only, never the only path.** [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Dynamic-menu-items)
- **Menu bar extra (`MenuBarExtra`):** symbol icon (menu bar is 24 pt tall), opens a menu rather than a popover, people opt in via a setting, never assume it is visible; also offer a Dock menu. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Menu-bar-extras)

```swift
.commands {
    CommandGroup(after: .newItem) {
        Button("New Folder") { model.newFolder() }
            .keyboardShortcut("n", modifiers: [.command, .shift])
    }
    CommandMenu("Message") {
        Button("Reply") { reply?() }.keyboardShortcut("r").disabled(reply == nil)
    }
    SidebarCommands(); ToolbarCommands()
}
```
Route commands to the key window with `@FocusedValue` / `.focusedSceneValue(_:)`; a disabled state then follows the active window.

## Keyboard shortcuts
- **Keep the standard set:** ⌘N, ⌘O, ⌘S, ⇧⌘S, ⌘W, ⌘P, ⌘Z, ⇧⌘Z, ⌘X/C/V, ⌘A, ⌘F, ⌘G, ⌘, (Settings), ⌘? (Help), ⌘M, ⌘Q, ⌥⌘T (toolbar), ⌃⌘F (full screen). Repurpose one only when its action can't exist in your app (⌘I as Get Info without text styling). [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#Standard-keyboard-shortcuts)
- **Custom shortcuts only for frequent app-specific commands.** Command as the main modifier, Shift as a secondary, Option sparingly, avoid Control (system uses it). [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#Custom-keyboard-shortcuts)
- **Display modifiers in the order Control, Option, Shift, Command;** write ⌘? not ⇧⌘/; don't build an unrelated shortcut by adding a modifier to a known one (⇧⌘Z must stay redo).
- **Prefer letters with extra modifiers;** symbols vary across keyboard layouts. The system localizes and mirrors shortcuts for you.
- **Test with Full Keyboard Access on.** [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#Best-practices)

## Settings scene
- **Use the `Settings` scene; the system adds the app-menu item and ⌘,.** Open it from code with `SettingsLink` or `@Environment(\.openSettings)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#macOS)
- **No settings button in the toolbar.** Document-level options go in the File menu.
- **Panes in a noncustomizable toolbar** (a `TabView` inside `Settings`) that always shows the selected pane; window title names the pane ("App Name Settings" with a single pane); reopen the last pane; minimize and zoom dimmed.
- **Don't duplicate system settings** (appearance, accessibility, scrolling). [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)

## Windows
- **Let people resize, move, hide, and full-screen every window; set sensible min sizes** (`.windowResizability`, `.defaultSize`). [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos#Best-practices)
- **Use `WindowGroup` for primary windows, `Window` for a single auxiliary one, `UtilityWindow` (macOS 15+) for panels; `DocumentGroup` for documents.**
- **Open new windows deliberately.** Compose-style tasks may open one by default; otherwise offer "Open in New Window" in a context menu or File menu via `openWindow`. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#Best-practices)
- **Never draw custom frames or traffic lights.** If you build custom window chrome anyway, it must track main, key, and inactive states (gray controls, no vibrancy when inactive). [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#macOS-window-states)
- **Keep critical controls out of the bottom of windows and sidebars;** people push windows below the screen edge. A bottom bar shows only small status info (item counts). [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#macOS-window-anatomy)
- **Keep content clear of the camera housing** along the top edge. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#macOS)
- **Keep playback running when people move to another window;** they expect it to continue while they work elsewhere. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#visionOS)

## Toolbars, sidebars, inspectors
- **Toolbar holds frequent commands only, all duplicated in menus;** make it customizable with `.toolbar(id:)`; trailing edge for inspector toggles, search, and the primary action. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#macOS)
- **Group related toolbar items** and separate groups with `ToolbarSpacer` (macOS 26+) instead of fixed padding.
- **Sidebar in `NavigationSplitView`;** at most two levels (add a content column if deeper), let it collapse when the window narrows, Show/Hide Sidebar in View menu (`SidebarCommands()`), don't hide it by default. [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#macOS)
- **Sidebar icons use the accent color, which people can change system-wide;** fixed colors only where they carry meaning (2026). [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **Inspector on the trailing side, not a popover:** `.inspector(isPresented:) { }` with a toolbar toggle and a View-menu command with a shortcut. [HIG](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst#Layout)
- **Split view panes:** thin dividers, min/max sizes that keep the divider visible, several ways to restore a hidden pane. [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#macOS)

## Pointer and hover
- **Use standard pointer styles** via `.pointerStyle(_:)` (macOS 15+): `.link`, `.horizontalText`, `.grabIdle`/`.grabActive`, `.columnResize`, `.frameResize(position:directions:)`, `.zoomIn`. [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Pointers)
- **Don't redefine system trackpad gestures** (Mission Control, swipe between full-screen apps, Notification Center); keep "swipe between pages" consistent. [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Best-practices)
- **Modifier + drag behaves the same with pointer and touch** (Option-drag duplicates).
- **Context menus on every object** (`.contextMenu`), since Mac users expect them everywhere. [HIG](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst#Menus)

## Undo
- **Make every destructive or editing action undoable** (delete especially) and register it with `@Environment(\.undoManager)`; text views get undo for free. [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#macOS)
- **Undo/Redo top of the Edit menu, ⌘Z and ⇧⌘Z, with an action name** (`setActionName("Delete Note")`).

## Drag and drop
- **Support it in and out of your app:** `.draggable(_:)` and `.dropDestination(for:action:isTargeted:)` with `Transferable` types.
- **Drags to Finder produce a file your app can reopen** (Calendar writes `.ics`) or a clipping. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#macOS)
- **Allow dragging from an inactive window without activating it, and without breaking its background selection.**
- **Select and drag in one motion; show a count badge for multi-item drags; use copy, link, disappearing-item, and not-allowed pointers.**

## Touch on Mac (2026)
- **Keep layout and control sizes identical; touch is secondary.** People switch inputs constantly. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#macOS)
- **Enlarge hit targets, not controls.** Standard controls already do this; for custom ones, extend `.contentShape` beyond the visible bounds.
- **Offer expandable variants for small or dense controls**, shown on tap, kept briefly after lift. System sliders, steppers, and dials do it automatically.
- **Touch is never the only path; give touch equivalents** for hover menus and modifier-drags.
- **Hidden-on-hover controls:** add touch only for essential ones; reveal them when people tap their area, hide after use or a few seconds, keep the current selection, and put them in a context menu (touch and hold opens it). [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Touch-support-for-hidden-controls)
- **Sidebar:** tapping a header or row reveals its hidden controls without triggering them; they stay until touch leaves the sidebar. **Tabbed window:** a tap anywhere shows the selected tab's close button.
- **Gesture mapping:** select = tap, open = double tap, scroll = one finger, context menu = touch and hold, drag = touch and hold then drag. Custom gestures must work on both trackpad and touch display.

## Mac Catalyst specifics
- **Start with the iPad idiom (UI scaled to 77%), move to the Mac idiom when ready** for crisper text and art; then audit layout, use text styles, consider a separate asset catalog. [HIG](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst#Choose-an-idiom)
- **Menus via `UIMenuBuilder`, shortcuts via `UIKeyCommand`.**

## Porting checklist (iPhone/iPad → Mac)
- [ ] Tab bar → sidebar (`NavigationSplitView` or `.sidebarAdaptable`); each former tab also in the View menu with ⌘1…⌘n. [HIG](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst#Navigation)
- [ ] Bottom and side buttons → window toolbar; top-down flow; inspector instead of popovers for properties.
- [ ] One column → multiple columns; reflow on window resize.
- [ ] Full menu bar audited against the HIG tables; every toolbar/context action present with a shortcut.
- [ ] Undo for every edit and delete; Find (⌘F) wherever there's a searchable list.
- [ ] `Settings` scene replaces an in-app settings screen; no system-setting duplicates.
- [ ] Multiple windows; state restoration; "Open in New Window".
- [ ] Next/Previous buttons wherever iPad relies on swiping between pages.
- [ ] Hover states and pointer styles; context menus on all objects.
- [ ] Drag and drop with Finder and other apps.
- [ ] Touch display check: same layout, larger hit areas, hidden controls reachable.
- [ ] macOS app icon.
