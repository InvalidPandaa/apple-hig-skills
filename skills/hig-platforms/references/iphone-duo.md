# iPhone Duo

Sources: [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games); developer docs: [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo), [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion), [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview).

New in September 2026. Most models know nothing about this device; follow this file, and verify with `hig.py` when in doubt. It is still an iPhone: everything in `ios.md` applies.

## The device
- **Two displays, one hinge.** The outer display is used closed; it is wider and shorter than other iPhone displays, so it gets a compact-width layout. The inner display is used open; it gets a regular-width layout.
- **Two front cameras.** The outer camera sits in a corner and is always visible; it lines up with the side controls. The inner camera is under the display and only shows (and takes space) while it is in use.
- **Poses.** People hold it partly folded like a book, lay it flat, fold it like a small laptop, or stand it on an edge. Each pose and rotation can move your app between displays and change its size.
- **Split View multitasking** on the inner display adds more sizes.
- Preview poses with Device Hub in Xcode. Build with the latest Xcode: apps built with Xcode 26 or earlier don't extend under the status bar and camera.

## What people expect
- **The same app on both displays.** Same features, same state, same information hierarchy as they open and close it. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)
- **One more level of hierarchy when open, if the content suits it.** Mail closed shows the list or a message; open, it shows both side by side.
- **Nothing lost when the pose changes.** Controls may overflow into a menu and content may resize, but every control and piece of content stays reachable.

## Layout rules
- **Don't design a layout per pose.** Compact width for the outer display plus regular width for the inner one covers every pose; let the existing layout grow into extra space. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Device-poses)
- **Build to resize.** Layout margins, safe area insets, size classes; no fixed widths, no assumptions tied to one display. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Dynamic-layouts)
- **Measure the scene or container, never the screen.** In UIKit, don't use `userInterfaceIdiom` or `UIInterfaceOrientation` for layout; track size class traits. In SwiftUI, read `horizontalSizeClass` / `verticalSizeClass` and container geometry.
- **Prefer system containers.** `NavigationSplitView`, `TabView`, `NavigationStack`, sheets, alerts, and context menus already avoid the fold and cameras. Split views collapse to one pane on the outer display and balance column widths and margins around the fold on the inner one. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Split-views)
- **Make small adjustments when the device folds.** Move only what must move to stay visible and tappable; dramatic rearrangement makes controls hard to track. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions)
- **Use an even column count in grids.** Content then splits cleanly at the fold.

## Reserved regions (iOS 27.1+)
Areas content should avoid or adapt around. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions)

| Region | Kind | When active |
|---|---|---|
| Outer front camera (grows into the Dynamic Island for Live Activities) | `.occlusion` | Always |
| Inner front camera (UI shifts aside when it turns on) | `.occlusion` | Only while the camera is in use |
| Fold | `.division` | Only when partly open; inactive when flat |

- **Check regions only in custom views that place their own content.** Floating controls, custom overlays, explicit frames, custom `Layout`. System containers already handle them.
- **Scrolling containers don't split around the fold.** Lists, scroll views, and grids let a row cross the fold; if that hurts readability, read the division and arrange content yourself.
- **Query inside the view that positions the content.** Frames are in that view's local coordinates, start at its top-leading corner, and already include the region's margins.
- **Reserve space for inactive regions to avoid jumps.** Pass `options: .includeInactive` and check `isActive`.
- **Frames are mirrored for right-to-left by default.** Pass `layoutDirectionBehavior: .fixed` only if your placement doesn't flip with layout direction.

```swift
GeometryReader { proxy in
    if let fold = proxy.reservedRegions(kind: .division).first {
        let sideBySide = fold.frame.height > fold.frame.width   // book fold
        // place each pane fully on one side of fold.frame
    } else {
        SinglePane()
    }
}
```

## Arrangement views (iOS 27.1+)
A container holding a primary and a secondary view that rearranges them for size, orientation, and the fold. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Arrangement-views)

- **Split** (`.arrangementViewStyle(.split)`): two separate areas; side by side when wider than tall (primary leading), stacked when taller than wide (primary on top). Closed in landscape, only the primary shows. Replaces an `HStack`/`VStack` you switch by hand.
- **Overlay** (`.arrangementViewStyle(.overlay)`): primary layered above secondary on a flat display; when partly folded, they move to opposite sides (secondary leading or top, primary trailing or bottom). Good for a clear foreground/background pair, like player controls over video. Replaces a `ZStack`.
- **Limit axes when needed:** `.split.axes(.vertical)` or `.split.axes(.horizontal)`; the overlay style has `axes(_:)` too, and the secondary view can be collapsed.
- **Keep navigation outside.** Put `NavigationSplitView` or `TabView` around an arrangement view, never inside it; don't nest an arrangement view in a scroll view, list, grid, or split view, which can make part of it unreachable.

```swift
ArrangementView {
    PlayerControls()
} secondary: {
    VideoPlayer(player: player)
}
.arrangementViewStyle(.overlay)
```

## Vertical bars
On iPhone Duo, toolbars, navigation bars, tab bars, the status bar, and the Dynamic Island move to a vertical strip on the side. They go vertical on the outer display and on the inner display in landscape; the inner display in portrait keeps normal horizontal bars. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Vertical-controls)

- The strip follows the hardware: it keeps the same position relative to the outer camera and **does not flip in right-to-left languages**.
- With two apps in Split View, each app puts its strip on its outer edge.
- Contexts: inspectors keep horizontal bars; in a multi-column split view, sidebar and content columns are horizontal while the detail column is vertical; sheets on the outer display are vertical; sheets on the inner display are horizontal when centered or leading, vertical when trailing (`presentationPlacement(_:)`, iOS 27+).

Rules:
- **Get bars from the navigation container.** Attach `.toolbar` to content inside `NavigationStack` / `NavigationSplitView`; custom bar views (or UIKit `UIToolbar`/`UINavigationBar`/`UITabBar` you add yourself) never go vertical.
- **Lay content out for asymmetry.** Respect safe areas so neither your own strip nor the neighbor app's strip covers content.
- **Order the strip from the top: Back or Close, then the prominent action (Done), then the remaining groups.** Use `.topBarPinnedTrailing` (iOS 27+) for Done-like items and `.cancellationAction` for a custom Back/Close; the system adds space between items that came from the top and bottom bars.
- **Group with `ToolbarItemGroup`, never with manual spacers or fixed padding.** Groups get spacing and adapt as space shrinks.
- **Rank items for overflow.** Items overflow bottom to top by default; set `.visibilityPriority(.high)` (iOS 27+) on frequent actions (Compose, New Note) and on badged items, whole groups first.
- **Give every item a title and a symbol.** Use `Label` or `Button("Title", systemImage:)`; the vertical strip shows the symbol, the overflow menu shows both. Text-only items and custom-view items never go vertical, so keep text buttons rare.
- **Control axis per item when needed.** `.axisBehavior(.horizontalOnly)` or `.verticalPreferred` (iOS 27.1+), for example a toggle that only makes sense horizontally.
- **Choose what compresses first.** Navigation-focused screens keep the tab bar and overflow toolbar items (default, `.prefersTabBar`); task-focused screens keep toolbar items and minimize the tab bar: `.toolbarVerticalCompressionBehavior(.prefersToolbarItems)` (iOS 27.1+).
- **Use the system overflow menu.** Move your own "More" items into `ToolbarOverflowMenu { }` (iOS 27+); reserve the ellipsis symbol for overflow; every other menu needs its own symbol.
- **Keep controls near the content they act on.** Controls for a leading pane (the message list in Mail) stay above that pane, not in the trailing strip.
- **Keep relative positions stable across poses.** Not every pose is vertical, so preserve the order people learned.
- **Don't override default placement.** Opt out with `.toolbarVerticalBehavior(.disabled)` (iOS 27.1+) only for views better served by horizontal bars, like full-screen video controls or a calculator-style non-scrolling layout; set it once, don't toggle it per state. To hide bars, use `toolbarVisibility(_:for:)` instead.
- **Go full width only for non-scrolling, immersive views** that don't collide with the Dynamic Island or status bar (Calculator). A hero image can span the full width under the strip with `.backgroundExtensionEffect()` while scrolling content stays inset.
- **Custom views can read `@Environment(\.toolbarVerticalEdge)`** (iOS 27.1+, an optional `HorizontalEdge`) to know which side the strip is on.

```swift
.toolbar {
    ToolbarItem(placement: .topBarPinnedTrailing) { Button("Done", systemImage: "checkmark") { save() } }
    ToolbarItemGroup {
        Button("Compose", systemImage: "square.and.pencil") { compose() }
    }
    .visibilityPriority(.high)
    ToolbarOverflowMenu { Button("Export", systemImage: "square.and.arrow.up") { export() } }
}
```

## Games and camera
- **Make games playable in every pose.** Locking to portrait or landscape is fine, but fill the screen as the pose changes, keep text and control sizes steady, and prefer changing aspect ratio over letterboxing; if bars are unavoidable, fill them with art. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)
- **Camera apps:** the app can move between displays and the active camera can end up facing the other way; choose cameras by facing direction (AVKit "Choosing a camera by the direction it faces").

## Porting checklist (existing iPhone app → iPhone Duo)
- [ ] Rebuild with the current Xcode; run every screen on both displays, open, closed, partly folded, and rotated.
- [ ] Replace fixed widths, screen-size math, and idiom checks with size classes and container geometry.
- [ ] Use `NavigationSplitView` where iPad already shows list + detail; verify one pane closed, two open.
- [ ] Find custom overlays, floating buttons, and explicit-frame layouts; move them off the fold and cameras with `reservedRegions(kind:)` or an `ArrangementView`.
- [ ] Even column counts in grids; check list rows crossing the fold.
- [ ] Move every bar into `.toolbar` on a navigation container; no hand-built bars.
- [ ] Every toolbar item has title + symbol; Back/Close first, Done pinned trailing; groups via `ToolbarItemGroup`.
- [ ] Set `visibilityPriority` for frequent and badged items; move a custom overflow menu into `ToolbarOverflowMenu`.
- [ ] Pick `toolbarVerticalCompressionBehavior` for task-focused screens.
- [ ] Check sheet bar orientation and `presentationPlacement`.
- [ ] Games: full screen in every pose, no unexplained letterboxing.
