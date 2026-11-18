# Migrating an iOS 17/18-style screen to Liquid Glass

Sources: [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Color](https://developer.apple.com/design/human-interface-guidelines/color), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views), [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons); developer docs [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass), [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views).

Most of a migration is deletion. Rebuild with the current SDK first, look at what the system already
gives you, and only then decide what custom glass is still needed. When you explain changes,
give one line per change: what changed, why, and the HIG link (template at the end).

## 1. Find and replace (SwiftUI)

| Old pattern | Replace with | Why |
|---|---|---|
| `.toolbarBackground(Color.x, for: .navigationBar)` + `.toolbarBackground(.visible, …)` | Nothing (delete both) | A custom bar fill covers the glass and the scroll edge effect. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices) |
| A `Color.black.opacity(…)` or `.ultraThinMaterial` panel floating over content | Toolbar items, or `.glass` buttons / `.glassEffect` in one `GlassEffectContainer` | Controls are told apart from content by glass, not by fills. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy) |
| Same panel, but it's really part of the content (a card in a list) | Keep the standard material or semantic background | Glass doesn't belong in the content layer. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Standard-materials) |
| `.buttonStyle(.plain)` + `.background(...)` + `.clipShape(Circle())` | `.buttonStyle(.glass)` + `.buttonBorderShape(.circle)` | System press state, hit shape, accessibility adaptation. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Style) |
| `.buttonStyle(.plain)` + `.glassEffect()` | `.buttonStyle(.glass)` (or `.glassEffect(.regular.interactive())` on non-button views) | The same reasons, and no lost press feedback. |
| `.tint(.blue)`, `Color.blue` selection fill | Accent color from the asset catalog, applied implicitly | Respects brand, increased contrast, and the macOS accent setting. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color) |
| `.cornerRadius(16)` on views near rounded containers | `.clipShape(.rect(corners: .concentric(minimum: 16)))` or `ConcentricRectangle` | Corners nest with the sheet, window, and device. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices) |
| `ToolbarItem(placement: .navigationBarTrailing) { HStack { A; B; Done } }` | Separate items: `ToolbarItemGroup` for related symbols, `ToolbarSpacer(.fixed)`, `Button(role: .confirm)` | Groups get one capsule each and Done becomes prominent. Don't mix text and symbols in a group. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Item-groupings) |
| `Button("Back")` / `Button("Close")` text | System back button; `Button(role: .close)` / `.cancel` | Standard symbols. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Navigation) |
| A custom mini-player view stacked above the `TabView` | `.tabViewBottomAccessory { }` + `.tabBarMinimizeBehavior(.onScrollDown)` | The system positions it and moves it inline. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iOS) |
| A search field in a custom header in a tab app | `Tab(role: .search)` + `.searchable` | The search tab sits apart at the trailing end. [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-a-tab) |
| A custom bar view (`safeAreaInset`) over a scroll view | `safeAreaBar(...)` | Extends the scroll edge effect under it. [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Scroll-edge-effects) |
| A hero image that stops at the sidebar edge | `.backgroundExtensionEffect()` on the image | Content appears to continue under the floating sidebar. [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices) |
| `.presentationBackground(.thinMaterial)` / colored sheet fill | Delete | Sheets manage their own glass and turn opaque at full height. |
| Toolbar item hidden with `.opacity(0)` or `if` inside the item | `.hidden(_:)` on the `ToolbarContent` (iOS 26.4+) | No empty glass capsule. |
| `Text("SECTION").textCase(.uppercase)` headers | Title-style capitalization | List headers no longer render uppercase. |
| `UIDesignRequiresCompatibility = YES` | Delete | Ignored when building for 27. |

## 2. UIKit and AppKit equivalents

| Old pattern | Replace with |
|---|---|
| `UINavigationBarAppearance` / `UITabBarAppearance` with background colors or images | Delete the background configuration and keep the defaults |
| `UIVisualEffectView(effect: UIBlurEffect(...))` behind floating controls | `UIVisualEffectView(effect: UIGlassEffect())`, several inside `UIGlassContainerEffect` |
| Custom `UIButton` with blur background | `UIButton.Configuration.glass()` / `.prominentGlass()` / `.clearGlass()` |
| `UIBarButtonItem` styled bold for Done | `style = .prominent` |
| A custom overlay bar over a `UIScrollView` | Add `UIScrollEdgeElementContainerInteraction` to the bar |
| `layer.cornerRadius` on nested containers | `cornerConfiguration` with `UICornerConfiguration` |
| Mini player added above `UITabBar` | `tabBarController.bottomAccessory = UITabAccessory(contentView:)`, plus `tabBarMinimizeBehavior = .onScrollDown` |
| An extra space hack between bar items | `UIBarButtonItem.fixedSpace(_:)`; `hidesSharedBackground = true` to split one item out |
| AppKit `NSVisualEffectView` under the toolbar or sidebar | Delete it. For custom floating glass, use `NSGlassEffectView` (in `NSGlassEffectContainerView`) |
| AppKit custom bezel buttons floating over content | `NSButton.BezelStyle.glass`; toolbar primary item `NSToolbarItem.Style.prominent` |

## 3. Worked example: an editor screen over a photo

This is the common case of a full-bleed photo with a tool picker and slider panel in opaque black
rounded rectangles, and a toolbar forced black with Cancel / Undo / Redo / Done in one `HStack`.

**Toolbar.** Delete both `toolbarBackground` lines. Use semantic placements: Cancel leading,
Undo and Redo as a symbol group, then a fixed spacer, then Done as the confirm role (the snippet is in
`swiftui-api.md`, under Toolbars). Undo and Redo get accessibility labels from the `Button(_:systemImage:)` title.

**Tool picker.** It floats over media and is a mode control, so put it in the functional layer with clear glass.
Show the selection with one tinted item (the accent), not a blue fill on every state.

```swift
GlassEffectContainer(spacing: 12) {
    HStack(spacing: 12) {
        ForEach(Tool.allCases) { t in
            Button(t.title, systemImage: t.icon) { withAnimation { tool = t } }
                .labelStyle(.iconOnly)
                .buttonBorderShape(.circle)
                .buttonStyle(.glass(t == tool ? .regular.tint(.accentColor) : .clear))
                .accessibilityAddTraits(t == tool ? .isSelected : [])
        }
    }
}
```

**Slider panel.** Sliders already take on glass while they're dragged. If the labels are legible
over the photo without a panel, drop the panel. If not, use **regular** glass, because the panel holds text,
with a concentric shape, inside the same container as the tool picker.

```swift
ToolSliders(tool: tool)
    .padding()
    .glassEffect(.regular, in: .rect(corners: .concentric(minimum: 20), isUniform: true))
```

**Bright photos.** Clear glass over a bright image needs a dark dimming layer (about 35%) under the
controls. Check `accessibilityReduceTransparency` and make that layer opaque, or switch the
picker to `.regular`, when it is on.

**Keep:** `PhotoCanvas().ignoresSafeArea()`. Full-bleed media under the bars is what the design
wants.

**Alternative to raise with the person:** if the tools are plain actions, not a mode picker,
a `ToolbarItemGroup(placement: .bottomBar)` gives system glass, grouping, and edge effects without
custom code.

## 4. Review grep

Run this over the project and decide on every hit:

```
grep -rnE 'toolbarBackground|Appearance\(\)|UIBlurEffect|NSVisualEffectView|ultraThinMaterial|thinMaterial|Color\.black\.opacity|\.cornerRadius\(|navigationBar(Leading|Trailing)|\.tint\(\.(blue|red|green|orange|purple)|buttonStyle\(\.plain\)|glassEffect|presentationBackground|textCase\(\.uppercase\)|UIDesignRequiresCompatibility' --include='*.swift' --include='*.plist' .
```

- Every `glassEffect` hit should be on a floating, functional control. It needs a container if siblings
  exist, it comes last in the modifier chain, and it never sits inside a toolbar item or on top of other glass.
- Every material hit should be in the content layer, never behind bars.

## 5. Explaining the changes

Give one row per change and keep it short:

| Change | Reason | Source |
|---|---|---|
| Removed the black navigation bar background | Custom bar fills block the glass and the scroll edge effect | [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices) |
| Done uses `role: .confirm` on the trailing side | One prominent primary action, trailing | [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Actions) |
| Tool picker uses clear glass in a container | Floating control over media; container enables morphing | [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) |

Then list what you didn't change and why (for example, "kept the full-bleed canvas"), and any
brief conflict you raised, along with the person's decision.
