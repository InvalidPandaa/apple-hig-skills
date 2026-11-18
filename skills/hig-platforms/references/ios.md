# iOS (iPhone)

Sources: [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button), [Camera Control](https://developer.apple.com/design/human-interface-guidelines/camera-control), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo), [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)

## What people expect
- A medium display held in one or both hands, a foot or two away, rotated as needed. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)
- Sessions from a one-minute check to an hour of reading or play; constant switching between apps.
- **Few onscreen controls, secondary actions one step away.** Put primary content first and reveal the rest with menus, swipe actions, and context menus. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios#Best-practices)
- **Controls in thumb reach.** The middle and bottom of the screen are easiest; support swipe-to-go-back and swipe actions on list rows.
- **Use device data instead of asking**, with permission: Apple Pay, Face ID, location, contacts.

## Navigation and structure
- **`TabView` with `Tab` for top-level sections, `NavigationStack` inside each.** The tab bar floats on Liquid Glass at the bottom (iOS 26+); keep it visible across sections and don't use it for actions. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iOS)
- **Search as a trailing tab:** `Tab(role: .search)`. Use the standard tab style for an explore-first landing page, the button appearance when people want to type immediately. [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-a-tab)
- **Otherwise place search in a bottom toolbar when there's room,** at the top only when bottom content must stay clear (Wallet). [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-in-a-toolbar)
- **Minimize the tab bar on scroll when an accessory matters:** `.tabBarMinimizeBehavior(.onScrollDown)` with `.tabViewBottomAccessory { }` (iOS 26+), like Music's MiniPlayer.
- **Avoid a More tab;** keep the tab count small, or move to a sidebar-adaptable design on larger widths. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Toolbar: only the essential items in the main area, the rest in a menu;** large titles that collapse on scroll. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#iOS)
- **Split views only in regular width** (large iPhones in landscape, iPhone Duo inner display); collapse to a stack in compact. [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#iOS)
- **Build every screen to resize.** iPhone Mirroring and iPhone Duo (two displays, many poses) give iPhone apps many sizes; read size classes and container geometry, not the device model. See `iphone-duo.md`. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)

## Inputs
- **Standard gestures mean the same thing everywhere:** tap activates, swipe reveals or dismisses, touch and hold shows more, pinch zooms. Never repurpose them for an app-only action, and never invent a gesture for a standard one. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Best-practices)
- **Reserved system gestures:** three-finger swipe (undo/redo), three-finger pinch (copy/paste), shake (undo). Don't redefine them; name the undo target in the alert ("Undo Address Change"). [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Platform-considerations)
- **Custom gestures only for frequent specialized tasks** (games, drawing), discoverable, distinct, and always backed by a visible control like a Back button. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Custom-gestures)
- **Show when a gesture can't work** (locked object, unavailable control) so the app doesn't look frozen.
- **Simultaneous gestures only where they help,** typically a game with a joystick plus buttons. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Platform-considerations)
- **Hardware keyboards and game controllers attach to iPhone too;** respect standard shortcuts (`.keyboardShortcut`).

### Action button
- **Offer App Shortcuts for your essential tasks, not "Open App"** (the system already provides that). [HIG](https://developer.apple.com/design/human-interface-guidelines/action-button#Best-practices)
- **Label each action with a verb-first, present-tense, title-case phrase of at most three words** ("Start Egg Timer"); no articles.
- **Run the action without leaving context** when possible: a Live Activity or custom snippet instead of launching the app. [HIG](https://developer.apple.com/design/human-interface-guidelines/action-button#iOS)
- **Don't write your own Action button tutorial;** the system explains setup.

### Camera Control (iPhone 16 and later)
- **Expose sliders and pickers through `AVCaptureControl`; the system's zoom and exposure controls are optional extras.** [HIG](https://developer.apple.com/design/human-interface-guidelines/camera-control#Anatomy)
- **SF Symbols only, short names, units on slider values (EV, %), prominent values for the common stops.** [HIG](https://developer.apple.com/design/human-interface-guidelines/camera-control#Best-practices)
- **Keep viewfinder UI out of the overlay area next to the button,** in both orientations; don't duplicate overlay controls onscreen while it shows.
- **Controls are fixed at setup;** enable or disable them per mode instead of adding or removing. Order common ones toward the middle.
- **Add a locked camera capture extension** so the button launches your camera from the Lock Screen and anywhere else.

## System integrations people expect
- Widgets, Home Screen quick actions, Spotlight, Shortcuts and App Shortcuts, the share sheet (`ShareLink`), Live Activities, Siri. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)
- Picture in Picture for video and calls; pause attention-requiring activity on switch-away, resume where people left off, finish user-started downloads in the background, notify only for important completions. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- Audio: pause indefinitely for primary interruptions (calls, other music), duck or pause briefly for short ones (navigation prompts).
- Orientation, Dark Mode, Dynamic Type: adapt without an in-app override.

## Checklist (any design → iPhone)
- [ ] Tab bar for top-level sections, search as a tab or bottom toolbar, no hamburger menu.
- [ ] Primary actions reachable with a thumb; swipe back works on every pushed screen.
- [ ] No custom bars or glass; system `TabView`, `.toolbar`, sheets.
- [ ] Layout from size classes and safe areas; tested on iPhone Duo outer and inner displays.
- [ ] Undo available for destructive edits (toolbar or gesture) and system gestures untouched.
- [ ] App Shortcuts for Action button, Spotlight, and Siri; widgets for glanceable data.
- [ ] Camera apps: Camera Control controls and locked capture extension.
