# iPadOS

Sources: [Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados), [Windows](https://developer.apple.com/design/human-interface-guidelines/windows), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar), [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices), [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards), [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection), [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble), [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)

## What people expect
- A large display held, propped on a stand, or flat on a desk, up to about three feet away; quick tasks or hours of work, play, and creation. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)
- Several apps onscreen at once, several windows of one app, drag and drop between them.
- Touch, keyboard, trackpad or mouse, and Apple Pencil, often combined.
- **Elevate content and cut modality.** Use the space for content, avoid full-screen modal hops, keep controls reachable but out of the way. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados#Best-practices)
- **Size and density depend on distance and input;** a trackpad user tolerates more density than someone holding the device.

## Navigation and structure
- **Tab bar near the top that can turn into a sidebar:** `TabView` + `.tabViewStyle(.sidebarAdaptable)`; `.tabBarOnly` when a sidebar never makes sense; `NavigationSplitView` for sidebar-only apps. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iPadOS)
- **Let people customize tabs** (`TabViewCustomization`), with a default of five or fewer so compact and regular widths stay consistent.
- **Toolbar and tab bar can share the top row** to keep the full width for content. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#iPadOS)
- **Split views with two or three columns** that still navigate logically at narrow, intermediate, and wide widths. [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#iPadOS)
- **Sidebar: edge swipe to hide, not hidden by default, two levels max, customizable contents, icons follow the accent color.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)

## Windows and multitasking
- **People choose full screen or windowed in Settings; you get no signal which.** Every size must work. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#iPadOS)
- **Windowed: window controls appear at the toolbar's leading edge;** shift leading toolbar items inward when they appear. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS)
- **Support multiple windows** (`WindowGroup`, `openWindow`); offer "Open in New Window" in context menus and the File menu, and consider a pinch-out to open an item as a window (Notes).
- **Don't open new windows by default** unless it helps (Mail's compose).
- **Picture in Picture** for video and calls floats over both modes.

## Menu bar (iPadOS 26+)
- **Hidden until people move the pointer to the top or swipe down;** centered; same menu order and items as the Mac. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#iPadOS)
- **Define it with the same SwiftUI `.commands` you use on Mac** (UIKit: `UIMenuBuilder`).
- **App menu > Settings opens your page in the system Settings app;** put your in-app preferences as a separate item below it.
- **List each tab as a View menu item with a shortcut** in tab-based apps.
- **Use submenus more than on Mac;** rows are taller for touch.
- **Everything in the menu bar must also exist in the UI,** because it is usually hidden; dynamic (modifier) items need another path.

## Inputs

### Touch
- Standard gestures plus three-finger undo/redo and copy/paste; four-finger swipe switches apps and is reserved. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Platform-considerations)
- **Multi-item drags:** let people add items to an in-progress drag and accept multiple drops. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Platform-considerations)

### Pointer (trackpad, mouse)
- **The pointer adds to touch, it doesn't replace it;** distinguish pointer from finger only when it adds value (click-to-seek on a scrubber). [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#iPadOS)
- **Use the system content effects:** highlight for controls grouped in a glass container, lift for standalone glass controls or small opaque elements, hover (custom scale/tint/shadow) for large elements. SwiftUI: `.hoverEffect(.highlight)`, `.hoverEffect(.lift)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Standard-pointers-and-effects)
- **Hit regions: about 12 pt padding around bezeled elements, 24 pt around unbezeled ones;** make adjacent bar-button regions contiguous so the highlight doesn't flicker.
- **Don't scale rows on hover** (they can't grow without overlapping); use tint. Shadow without scale looks wrong. [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Customizing-pointers)
- **Let the pointer reveal minimized or faded controls** (Safari toolbar, video controls).
- **Band selection** for multi-select in custom views; standard collection views get it free.
- **No instructional text on the pointer, no decorative pointer effects;** pointer accessories (small arrows, plus) only when they clarify. [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Pointer-accessories)

### Keyboard and focus
- **Support Full Keyboard Access; don't build your own keyboard navigation for buttons, switches, or segmented controls.** [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#Best-practices)
- **Focus covers content: text fields, sidebars, lists, collections.** Tab moves between focus groups in reading order; arrows move within a group. Group custom stacks so focus order makes sense (UIKit `focusGroupIdentifier`, SwiftUI `.focusable`, `@FocusState`). [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#iPadOS)
- **Focus ring for text and search fields, row highlight in lists.** Don't move focus on your own. [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#Best-practices)
- **Standard shortcuts, shown in the menu bar and in the hold-Command overlay.**

### Apple Pencil and Scribble
- **Mark on first contact; no mode switch or tool button required.** [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Best-practices)
- **All controls respond to Pencil too;** people shouldn't have to switch to a finger.
- **Map pressure, tilt, azimuth, and barrel roll to continuous stroke properties;** keep it simple.
- **Place controls so neither a left nor right hand covers them,** or let people move them.
- **Hover: preview the mark (size, color) at a mid-range value; never trigger actions on hover;** limit previews to Pencil, not the pointer. [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Hover)
- **Double tap follows the person's system setting** (eraser, previous tool, color picker); a custom mode must be opt-in and visible; never use it to change content destructively. SwiftUI: `.onPencilDoubleTap`. [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Double-tap)
- **Squeeze (Pencil Pro): one discrete, undoable action; show resulting UI near the tip.** People may map squeeze to a shortcut instead. SwiftUI: `.onPencilSqueeze`. [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Squeeze)
- **Barrel roll changes the mark only,** never navigation or UI. [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Barrel-roll)
- **Scribble works in standard text fields automatically;** in custom fields don't require a tap first, hide placeholders and autocompletion while writing, keep the field still and unscrolled, give it room (grow it before writing starts, not during). [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Scribble)
- **PencilKit in compact width lacks undo/redo in the tool picker;** add toolbar buttons. Keep markup colors fixed over PDFs and photos. [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Custom-drawing)

## System integrations
- Multitasking and windows, widgets, drag and drop, menu bar, Picture in Picture; everything in `ios.md` too.
- Smooth path to Mac (Catalyst or a shared SwiftUI target); see `macos.md`.

## Porting checklist (iPhone → iPad)
- [ ] Bottom tab bar → top tab bar that adapts to a sidebar (`.sidebarAdaptable`), or `NavigationSplitView`.
- [ ] Show list and detail together; three columns where the hierarchy is deep.
- [ ] Replace full-screen modals for small tasks with sheets sized to content, popovers, or inline editing.
- [ ] Test narrow, intermediate, and full widths; resizing must never lose state.
- [ ] Leading toolbar items clear of window controls.
- [ ] Multiple windows and "Open in New Window".
- [ ] `.commands` menu bar with standard shortcuts; tabs listed in View.
- [ ] Hover effects on custom controls; contiguous hit regions.
- [ ] Keyboard focus through sidebar, lists, and fields; Full Keyboard Access test.
- [ ] Drag and drop in and out of the app, multi-item.
- [ ] Pencil: if the app draws or annotates, Pencil marks immediately; Scribble works in all text input.
