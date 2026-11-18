# Layout

Sources: [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)

## Visual hierarchy

- **Put the most important items at the top and leading edge;** standard components flip for right-to-left automatically, custom ones may not. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)
- **Align to make scanning easy and indent to show subordination.** People read aligned items as related and indented items as children. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)
- **Group with space, container shapes or separators,** and hide secondary content behind disclosure, menus or navigation (progressive disclosure). [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)
- **Separate controls from content with Liquid Glass and a scroll edge effect, not an opaque or semi-opaque bar fill.** (iOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)
- **Run full-screen background content under sidebars, toolbars and tab bars.** If a sidebar or inspector would cover the important part of an image, mirror it underneath with `.backgroundExtensionEffect()` (UIKit `UIBackgroundExtensionView`). (iOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)

```swift
NavigationSplitView {
    Sidebar()
} detail: {
    HeroImage().backgroundExtensionEffect()
}
```

## What a layout must survive

Size classes (all four combinations), screen sizes and aspect ratios, orientation, Dynamic Island and camera housings, external displays, Display Zoom, resizable windows on iPad and Mac, iPhone Mirroring, text size from xSmall to AX5, right-to-left and long translations. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)

- **Even an orientation-locked app must resize cleanly** across devices and window sizes. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)
- **Test the extremes first:** smallest and largest layouts, longest localization, largest text. Device Hub in Xcode previews resized iPad windows, iPhone Mirroring and iPhone Duo poses. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)
- **Scale background artwork to fill rather than changing its aspect ratio,** and draw extra beyond the usual frame, because windows can be very wide or very tall. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)

## Size classes

- **Branch on `horizontalSizeClass` / `verticalSizeClass` (UIKit trait changes via `UITraitChangeObservable`), not on `userInterfaceIdiom` or orientation.** Idiom and orientation tell you nothing about available space. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
- **Design for every combination,** e.g. an iPad window resized to regular height in landscape, or compact portrait widened to regular. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
- **Never remove functionality in a smaller size;** only change how much is visible at once (tab bar ↔ sidebar via `TabView` + `.tabViewStyle(.sidebarAdaptable)`, overflow menu ↔ inline buttons). [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
- **Keep the idiom's look while resizing:** an iPad app in a narrow window is still an iPad app, not an iPhone clone. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)

## Guides, margins, safe areas, readable width

- **Respect the safe area** so the Dynamic Island, camera housing, home indicator and bars never cover content or controls. SwiftUI respects it by default; `.ignoresSafeArea()` only for backgrounds. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas)
- **Use the system margins rather than hand-picked padding.** `List`, `Form`, `NavigationStack` content and toolbars already apply them; for scroll content use `.contentMargins(_:_:for:)` and `.safeAreaPadding(_:_:)` (iOS 17+) instead of fixed `.padding(16)`. UIKit: `layoutMarginsGuide`, `directionalLayoutMargins`. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas)
- **Limit line length for long text.** UIKit: pin text to `readableContentGuide`. SwiftUI has no direct equivalent: cap the column with `.frame(maxWidth:)` using a `@ScaledMetric` value and center it, so very wide iPad and Mac windows don't produce endless lines. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas)
- **Make room for larger text:** side-by-side views may need to stack, rows must grow, single-line rows may wrap. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)

### Device dimensions
The current Layout page carries no per-device point-size tables. Don't hard-code screen sizes, margin values or safe-area insets; read them at runtime (`GeometryReader`, `safeAreaInsets`) and get mockup dimensions from [Apple Design Resources](https://developer.apple.com/design/resources/). [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Dynamic-layouts)

## Multitasking and windows (iPad, Mac, visionOS)

- **Assume any window size at any time;** iPad apps can be full screen or freely resized windows with tiling controls, and apps are not told which configuration people chose. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#iPadOS)
- **Leave room for iPad window controls at the top leading corner** if you place custom content there (they are a reserved region). [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions)
- **Save and restore context continuously,** because multitasking can start without warning. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)

## iPhone Duo (iOS 27+)

- **Treat the outer display as compact width and the inner as regular width;** don't design per pose. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Device-poses)
- **Keep functionality and element state the same on both displays;** you may add one level of hierarchy on the inner display (Mail: list or message closed, both side by side open). [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)
- **Let system toolbars and tab bars move to the side;** they do so automatically on the wide, short outer display. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)
- **Avoid reserved regions in custom layouts:** the outer camera (always present), the inner camera (only when active) and the fold (when partly open). System alerts, menus, sheets and split views adapt already. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions)
- **Prefer even grid column counts and small adjustments over rearranging** when the device folds. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions)

```swift
// iOS 27.1+: keep a custom canvas clear of the hinge
GeometryReader { proxy in
    let folds = proxy.reservedRegions(kind: .division)
    CanvasView(avoiding: folds)
}
```
`kind:` is `.occlusion` (cameras, Dynamic Island, window controls) or `.division` (the fold). Only active regions are returned unless you pass `options: .includeInactive`; frames mirror for right-to-left by default. UIKit: `UIView.ReservedRegion`.

## Platform specifics

- **macOS:** keep key controls and information away from the window's bottom edge, which often ends up below the screen; no content behind the camera housing (`NSPrefersDisplaySafeAreaCompatibilityMode`). [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#macOS)
- **tvOS:** inset primary content 60 pt top and bottom, 80 pt left and right; leave room for focused items to grow; grids use 40 pt horizontal and at least 100 pt vertical spacing (two columns 860 pt wide down to nine at 160 pt); keep partially visible offscreen items the same width on both sides. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#tvOS)
- **visionOS:** support window resizing (min/max sizes only to prevent breakage, not to block resizing); keep content centered when large; 3D content inline only for meaningful moments and inset from edges; supplemental content in a new window (`defaultWindowPlacement(_:)`), not an ornament; button centers at least 60 pt apart. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS)
- **watchOS:** at most three glyph buttons or two text buttons in a row; consider autorotation for content shown to others (QR codes, images). [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#watchOS)
