# Liquid Glass API reference (SwiftUI first)

Sources: [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout); developer docs [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views), [SwiftUI updates](https://developer.apple.com/documentation/updates/swiftui).

Every symbol below was checked against developer.apple.com in November 2026. Availability is copied
from the doc page. "26" means iOS/iPadOS/Mac Catalyst/macOS/tvOS/watchOS 26.0 unless the row
narrows it. Platforms that a row doesn't list don't have the symbol. Verify anything else with
`python3 ../../apple-hig/scripts/hig.py fetch /documentation/swiftui/<lowercased path>`.

## Glass material

| SwiftUI | Availability | Notes |
|---|---|---|
| `glassEffect(_ glass: Glass = .regular, in shape: some Shape = DefaultGlassEffectShape())` | 26, **no visionOS** | Default is regular in a capsule. Apply it **after** appearance modifiers (padding, frame, font), because it captures the view at that point. |
| `Glass.regular` | 26 | Default. Blurs and adjusts luminosity. Use it for anything with text. |
| `Glass.clear` | 26 | Highly translucent. Only over media. Add a dimming layer such as `.background(.black.opacity(0.35))` when the media is bright. |
| `Glass.identity` | 26 | No effect. Useful to switch glass off conditionally without changing the view tree. |
| `Glass.tint(_ color: Color?)` | 26 | Colors the glass. Reserve it for one primary or status element. Pass `.accentColor` or a semantic color, never a literal. |
| `Glass.interactive(_ isEnabled: Bool = true)` | 26 | The touch and pointer response that `.glass` buttons have. Use it on tappable custom glass. |

UIKit: `UIGlassEffect` in a `UIVisualEffectView` (iOS/iPadOS/Catalyst/tvOS 26). AppKit: `NSGlassEffectView` with `NSGlassEffectView.Style.regular` / `.clear` (macOS 26).

```swift
Label("Flag", systemImage: "flag.fill")
    .padding()
    .glassEffect(.regular.tint(.accentColor).interactive(), in: .capsule)
```

## Buttons

| SwiftUI | Availability | Notes |
|---|---|---|
| `.buttonStyle(.glass)` | 26 | Secondary floating buttons. On tvOS it is glass whether or not focused. |
| `.buttonStyle(.glassProminent)` | 26 | The one primary action. Filled with the accent color, like `borderedProminent`. |
| `.buttonStyle(.glass(_ glass: Glass))` | 26 | Configurable, for example `.glass(.clear)` over photos. |
| `ButtonRole.confirm` | 26 + visionOS 26 | Marks the action that confirms an operation (Done, Save) in toolbars and sheets. Label-less `Button(role: .confirm) { }` lets the system supply the label. |
| `ButtonRole.close` | 26 + visionOS 26 | Dismisses without losing anything (a read-only sheet). Use `.cancel` when dismissing discards edits. |
| `.buttonBorderShape(.circle / .capsule / .roundedRectangle)` | iOS 15 / macOS 12 | Shape for glass buttons. Prefer this to `clipShape`. |
| `ControlSize.extraLarge` | iOS 17 / macOS 14 | The larger control size that the 26 design leans on for big touch targets. |

UIKit: `UIButton.Configuration.glass()`, `.prominentGlass()`, `.clearGlass()`, `.prominentClearGlass()` (iOS 26); bar items use `UIBarButtonItem.Style.prominent` (iOS 26).
AppKit: `NSButton.BezelStyle.glass` (macOS 26); toolbar items use `NSToolbarItem.Style.prominent` (macOS 26).

## Containers, unions, morphing

| SwiftUI | Availability | Notes |
|---|---|---|
| `GlassEffectContainer(spacing: CGFloat? = nil) { }` | 26 | Renders child glass together for performance, blending, and morphing. If spacing exceeds the stack spacing, shapes merge at rest. |
| `glassEffectID(_ id:, in namespace:)` | 26 | Identity used to morph shapes as views appear or disappear. Requires a container and an animation. |
| `glassEffectUnion(id:namespace:)` | 26 | Fuses views with the same id, shape, and variant into one glass shape even when they aren't adjacent. |
| `glassEffectTransition(_:)` with `GlassEffectTransition.matchedGeometry` / `.materialize` / `.identity` | 26 | `matchedGeometry` (the default inside the spacing) morphs. Use `materialize` for shapes farther apart. |

UIKit: `UIGlassContainerEffect` (iOS 26). AppKit: `NSGlassEffectContainerView` (macOS 26).

```swift
@Namespace private var ns
GlassEffectContainer(spacing: 24) {
    HStack(spacing: 24) {
        Button("Crop", systemImage: "crop") { }.glassEffectID("crop", in: ns)
        if showMore {
            Button("Filters", systemImage: "camera.filters") { }
                .glassEffectID("filters", in: ns)
        }
    }
    .buttonStyle(.glass)
}
// toggle with: withAnimation { showMore.toggle() }
```

## Concentric shapes

| SwiftUI | Availability | Notes |
|---|---|---|
| `ConcentricRectangle()` and per-corner init | 26 + visionOS 26 | Each corner computes its radius from the container. It may resolve to square when far from the container's corners. |
| `Edge.Corner.Style.concentric`, `.concentric(minimum:)`, `.fixed(_:)` | 26 + visionOS 26 | `minimum:` keeps a rounded corner on square-cornered devices and far from edges. |
| `.rect(corners: Edge.Corner.Style, isUniform: Bool = false)` | 26 + visionOS 26 | Shape shorthand, for example `.glassEffect(in: .rect(corners: .concentric(minimum: 12)))`. Use `isUniform: true` for symmetric corners. |
| `containerShape(_ shape: some RoundedRectangularShape)` | 26 + visionOS 26 | Declares the container for nested concentric shapes in custom views. |

UIKit: `UIView.cornerConfiguration` with `UICornerConfiguration` (iOS 26).

## Scroll edge effects, bars, background extension

| SwiftUI | Availability | Notes |
|---|---|---|
| `scrollEdgeEffectStyle(_ style: ScrollEdgeEffectStyle?, for edges: Edge.Set)` | 26 | Styles are `.automatic` (preferred), `.hard` (opaque line), and `.soft` (subtle blur). |
| `scrollEdgeEffectHidden(_:for:)` | 26 | Removes the effect on an edge. Use it only when nothing floats there. |
| `safeAreaBar(edge:alignment:spacing:content:)` | 26 + visionOS 26 | Like `safeAreaInset`, and also extends the scroll edge effect under your custom bar. |
| `backgroundExtensionEffect()` / `backgroundExtensionEffect(isEnabled:)` | 26 + visionOS 26 | Mirrors and blurs a view into the safe area under a sidebar or inspector. It clips the view. Use one instance. |
| `inspector(isPresented:content:)` | iOS 17 / macOS 14 | A trailing inspector column that floats in the glass layer with `NavigationSplitView`. |

UIKit: `UIScrollEdgeEffect` / `UIScrollEdgeEffect.Style`, `UIScrollEdgeElementContainerInteraction` for custom bars, `UIBackgroundExtensionView` (iOS 26).
AppKit: `NSScrollEdgeEffectStyle` (macOS 26.1), `NSBackgroundExtensionView` (macOS 26).

## Tab views

| SwiftUI | Availability | Notes |
|---|---|---|
| `tabBarMinimizeBehavior(_:)` with `.automatic` / `.never` / `.onScrollDown` / `.onScrollUp` | 26 + visionOS 26 | Shrinks the floating bar while scrolling. It takes effect on iPhone. |
| `tabViewBottomAccessory { }` | iOS/iPadOS/Catalyst 26 | Accessory above the bar, which moves inline when the bar is minimized. |
| `tabViewBottomAccessory(isEnabled:content:)` | iOS/iPadOS/Catalyst **26.1** | Shows or hides the accessory without rebuilding the tab view. |
| `@Environment(\.tabViewBottomAccessoryPlacement)` with `.expanded` / `.inline` | 26 + visionOS 26 | Swap to a compact accessory layout when inline. |
| `Tab(role: .search) { }` | iOS 18 / macOS 15 | Set apart at the trailing end in 26. Pair it with `.searchable` on the `TabView`. |
| `tabViewSearchActivation(.searchTabSelection)` | iOS/iPadOS/Catalyst/macOS 26 | Selecting the search tab focuses the field (the quick-search, button-like behavior). |
| `TabRole.prominent` | **27**, all platforms | Gives one tab separate trailing treatment. Without it, the search tab may get that treatment. |
| `.tabViewStyle(.sidebarAdaptable)` | iOS 18 / macOS 15 | iPad tab bar that converts to a sidebar. |

UIKit: `UITabBarController.MinimizeBehavior` / `tabBarMinimizeBehavior`, `bottomAccessory` with `UITabAccessory` (iOS 26), `UISearchTab` (iOS 18), `UITabBarController.Mode.tabSidebar`.

## Toolbars

| SwiftUI | Availability | Notes |
|---|---|---|
| `ToolbarItemGroup(placement:)` | long-standing | Items in a group share one glass background. |
| `ToolbarSpacer(_ sizing: SpacerSizing = .flexible, placement:)` with `.fixed` / `.flexible` | iOS/iPadOS/Catalyst/macOS 26 | `.fixed` splits groups, and `.flexible` pushes items apart. It works in customizable toolbars too. |
| `sharedBackgroundVisibility(.hidden)` on `ToolbarContent` | iOS/iPadOS/Catalyst/macOS 26 | Takes an item (status view, avatar) out of the shared capsule into its own group. |
| `hidden(_:)` on `ToolbarContent` | iOS 26.4, macOS 15 | Hides the whole item. Hiding only the content leaves an empty capsule. |
| `matchedTransitionSource(id:in:)` on `ToolbarContent` | iOS/iPadOS/Catalyst 26 | Use with `.navigationTransition(.zoom(sourceID:in:))` so a sheet grows out of its toolbar button. |
| `navigationSubtitle(_:)` | iOS 26, macOS 13 | Subtitle under the title. In UIKit, `UINavigationItem.subtitle` (iOS 26). |
| `ToolbarItemPlacement.largeSubtitle` | iOS/iPadOS/Catalyst 26 | Custom view under a large title. |
| `searchToolbarBehavior(.minimize)` | modifier 26 + visionOS 26; `.minimize` iOS/iPadOS/Catalyst/visionOS 26 | Renders toolbar search as a button that expands into the field. |
| `visibilityPriority(_:)` on `ToolbarContent` | **iOS 27**, macOS 26.1 | Ranks items so low-priority ones move to overflow first. |
| `ToolbarOverflowMenu { }` | **iOS/iPadOS/Catalyst/visionOS 27** | Secondary actions that always live in the overflow menu. |
| `ToolbarItemPlacement.topBarPinnedTrailing` | **iOS/iPadOS/Catalyst/visionOS 27** | Pinned trailing item. It moves to overflow only during search with no room left. |
| `toolbarMinimizationBehavior(_:for: .navigationBar)` | **27**, all platforms | Minimizes the navigation bar (and an integrated top tab bar) on scroll. Pair it with `toolbarMinimizationSafeAreaAdjustment(_:for:)`. |
| `toolbarVerticalEdge` (environment), `toolbarVerticalBehavior(_:)` | **27.1** | Bars placed on the vertical axis (for example iPhone Duo). Read the edge before positioning custom floating glass. |

UIKit: `UIBarButtonItem.fixedSpace(_:)`, `.hidesSharedBackground`, `.isHidden`, `.Style.prominent` (iOS 26). AppKit: `NSToolbarItem.Identifier.space`, `NSToolbarItem.isHidden`, `.Style.prominent`.

```swift
.toolbar {
    ToolbarItem(placement: .cancellationAction) { Button("Cancel", role: .cancel) { } }
    ToolbarItemGroup(placement: .primaryAction) {
        Button("Undo", systemImage: "arrow.uturn.backward") { }
        Button("Redo", systemImage: "arrow.uturn.forward") { }
    }
    ToolbarSpacer(.fixed, placement: .primaryAction)
    ToolbarItem(placement: .confirmationAction) { Button("Done", role: .confirm) { } }
}
```

## Presentations

| SwiftUI | Availability | Notes |
|---|---|---|
| `NavigationTransition.crossFade` | **iOS/iPadOS/Catalyst/tvOS/visionOS/watchOS 27** | A sheet fades in over content instead of sliding up. |
| `presentationBackground(_:)` | iOS 16.4 | **Remove** custom fills when adopting. Sheets supply their own glass and opacity changes. |
| `confirmationDialog(...)` attached to the source control | long-standing | In 26, action sheets grow out of their source, so attach the dialog to the button that triggers it. UIKit: set `sourceView` / `sourceItem`. |

## Accessibility and compatibility

| Symbol | Availability | Use |
|---|---|---|
| `accessibilityReduceTransparency` | iOS 13 | Make your own dimming layers or translucent fills opaque. System glass adapts by itself. |
| `colorSchemeContrast` | iOS 13 | Strengthen custom tints and borders when the value is `.increased`. |
| `accessibilityReduceMotion` | iOS 13 | Replace custom morph and scale animations with fades. |
| `UIDesignRequiresCompatibility` (Info.plist) | iOS/macOS/tvOS 26 | Temporary opt-out to the old look. **Ignored when building for iOS/iPadOS/Catalyst/macOS/tvOS 27 or later.** |
| `glassBackgroundEffect(displayMode:)` | visionOS 1 | visionOS window-style glass. `glassEffect` is not available on visionOS. |

## Not verified, so don't use
Don't use any API that isn't listed here (for example a guessed `.liquidGlass()` modifier,
`Glass.thick`, or `.toolbarGlass`) until `hig.py fetch` confirms it.
