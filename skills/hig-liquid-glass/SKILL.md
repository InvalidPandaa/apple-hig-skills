---
name: hig-liquid-glass
description: Use when building, restyling, or reviewing a native iOS, iPadOS, macOS, watchOS, or tvOS 26+ screen for Apple's Liquid Glass design, or when an app "still looks like iOS 17/18". Triggers include toolbarBackground, custom blurs, opaque floating panels, hand-made glass circles, glassEffect, .glass or .glassProminent buttons, tinting, floating tab bars, tab bar accessories, toolbar grouping, scroll edge effects, sidebars, sheets, concentric corners, Icon Composer app icons, and Reduce Transparency or Increase Contrast problems.
---
# Liquid Glass

Liquid Glass is the functional layer: navigation and controls float on it, content sits underneath and never wears it. Standard components adopt it on their own when built with the 26+ SDK, so most of the work is deleting custom chrome. Add glass yourself only to the few custom controls that really float above content.

## Quick decisions

| Situation | Do this (API) | Source |
|---|---|---|
| Bars look flat, opaque, or branded | Delete `toolbarBackground(...)` and bar appearance backgrounds; the system draws the glass | [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices) |
| Custom control floats over content (map button, editor tool strip) | Prefer a toolbar item. Otherwise use `Button` + `.buttonStyle(.glass)`, and wrap several in `GlassEffectContainer` | [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) |
| Floating control over photos, video, or maps | `.buttonStyle(.glass(.clear))` / `.glassEffect(.clear)`, plus a dimming layer if the media is bright | [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) |
| Card, row, or panel inside the content | Standard material (`.regularMaterial`) or a semantic background, never glass | [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Standard-materials) |
| Primary action (Done, Save, Send) | `Button(role: .confirm)` in the toolbar or `.buttonStyle(.glassProminent)`: one per view, trailing | [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Actions) |
| Split toolbar items into groups | `ToolbarItemGroup` + `ToolbarSpacer(.fixed)` | [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Item-groupings) |
| Content scrolls under bars | Keep the automatic scroll edge effect. Register custom bars with `safeAreaBar(...)` | [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Scroll-edge-effects) |
| Hero image should reach under the sidebar or inspector | `.backgroundExtensionEffect()` on that one background view | [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices) |
| Mini player or app-wide status above the tab bar | `.tabViewBottomAccessory { }` + `.tabBarMinimizeBehavior(.onScrollDown)` | [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iOS) |
| Search in a tab-based app | `Tab(role: .search) { }` (trailing, set apart) | [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-a-tab) |
| Custom shape nested in a rounded container | `ConcentricRectangle()` / `.rect(corners: .concentric)` | [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices) |
| App icon | Layered Icon Composer file with unmasked square layers and no baked-in effects | [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Icon-formats) |

## Rules

### Layers: where glass goes
- **Keep glass out of the content layer.** Lists, cards, cells, and app backgrounds use standard materials or semantic colors. Sliders and toggles in content are the one exception: their knob turns to glass only while it's being touched. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)
- **Let system components supply the glass.** Bars, sheets, popovers, menus, and standard controls get it for free. Limit custom `glassEffect` to the few most important floating controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)
- **Never stack glass on glass.** Don't put glass buttons in a toolbar, a sheet, or another glass panel. Toolbar items already share the bar's glass, and overlapping glass muddles the hierarchy. [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- **Put neighboring custom glass views in one `GlassEffectContainer`.** It renders them together so they can blend and morph, and it is cheaper than separate effects. [Applying Liquid Glass](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views)
- **Run full-bleed content under every bar.** Use no opaque or semi-opaque strip behind controls. The scroll edge effect lifts the controls instead. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)

### Variants and color
- **Default to the regular variant.** It blurs and adjusts luminosity, so use it wherever there's text or the backdrop could hurt legibility. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)
- **Use clear glass only over rich media.** Add a dark dimming layer of about 35% under it if the media is bright. Skip the layer if the media is dark or AVKit controls already dim it. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass)
- **Color the glass of one or two key controls, not their labels.** Use `.glassProminent` or `Glass.tint(_:)` for a primary action or a status. Never tint a row of controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)
- **Tint with the app accent color, never a literal.** Set AccentColor in the asset catalog and leave `.tint` alone. `.tint(.blue)` breaks brand changes, increased-contrast variants, and the macOS accent setting. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#App-accent-colors)
- **Keep bar labels monochrome over colorful content.** By default, labels flip between dark and light to follow the content beneath. A brand-colored label over brand-colored content disappears. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices)
- **Ship light, dark, and increased-contrast variants of every custom color, even in a single-appearance app.** Small glass elements switch between light and dark to follow the content. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Check the resting state.** At the top of a scroll view, the content under controls must not share their colors. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)

### Shape
- **Make custom corners concentric with their container.** Use `ConcentricRectangle`, `.rect(corners: .concentric(minimum: 12))`, and `containerShape(_:)` on custom containers. A hard-coded radius fights sheet, window, and device corners. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices)
- **Don't hard-code control sizes or paddings.** Controls are rounder and larger in 26 and adjust themselves when you rebuild. [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)

### Scroll edge effects
- **Prefer the automatic style.** It turns more opaque for crowded top toolbars, text outside glass, and pinned headers. If you pick `.soft`, test legibility on varied content. [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Scroll-edge-effects)
- **Use the effect only where floating UI sits over a scroll view, and only one per view.** It isn't decoration or a dimmer. In split-view panes, keep the effect heights equal. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Scroll-edge-effects)

### Tab bars
- **Tabs navigate and never act.** A "+" or "Compose" tab belongs in a toolbar or a prominent button instead. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Let the bar float and stay visible.** Minimize it on scroll with `.tabBarMinimizeBehavior(.onScrollDown)` instead of hiding it, and never disable or hide individual tabs. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iOS)
- **Use the bottom accessory for app-wide, persistent state such as a mini player.** Don't use it for actions on the current screen. Read `tabViewBottomAccessoryPlacement` to show a compact layout inline, and use `tabViewBottomAccessory(isEnabled:content:)` (26.1+) to show it conditionally. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iOS)
- **Mark search with `Tab(role: .search)`.** Pick the standard tab style for a discovery landing page, or the button appearance for quick lookups. `.tabViewSearchActivation(.searchTabSelection)` focuses the field as soon as the tab is selected. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-a-tab)
- **Give `TabRole.prominent` to at most one destination tab.** It moves the tab to its own trailing spot, and without it the search tab may take that spot. (iOS 27+) [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **On iPad, use `.tabViewStyle(.sidebarAdaptable)`.** Use `NavigationSplitView` only when you want a sidebar and nothing else. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iPadOS)

### Toolbars
- **Group items by function, in at most three groups.** A `ToolbarItemGroup` shares one glass capsule, and `ToolbarSpacer(.fixed)` splits groups apart. Keep Done, Close, and Save in their own group. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Item-groupings)
- **Use SF Symbols without borders, and never mix text and symbol items in one group.** Use text only where no symbol reads well (Edit), and give every icon an accessibility label. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Actions)
- **Mark one prominent primary action and place it trailing.** In SwiftUI use `Button(role: .confirm)` or `.glassProminent`, in UIKit `UIBarButtonItem.Style.prominent`, and in AppKit `NSToolbarItem.Style.prominent`. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Actions)
- **Use the standard Back and Close symbols, never the words.** In SwiftUI use `Button(role: .close)` (26+) when dismissing loses nothing, and `.cancel` when it discards edits. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Navigation)
- **Hide the toolbar item, not its content.** Use `ToolbarContent.hidden(_:)` (iOS 26.4+). Hiding only the content leaves an empty capsule. [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- **Let the system manage overflow.** In iOS 27, rank items with `visibilityPriority(_:)`, send secondary actions to `ToolbarOverflowMenu`, and pin with `.topBarPinnedTrailing`. Never build a manual overflow. (iOS 27+) [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices)

### Sidebars, split views, sheets, menus
- **Extend content beneath the floating sidebar.** Do it with horizontal scrolling or with `.backgroundExtensionEffect()` on one background view (it clips that view). In UIKit use `UIBackgroundExtensionView`, in AppKit `NSBackgroundExtensionView`. [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **Let sidebar icons follow the accent color.** A fixed color is only for an icon whose meaning depends on it. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **Remove custom sheet and popover backgrounds.** Half sheets inset themselves and turn more opaque at full height, so a `presentationBackground` color or a blur view fights that. [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- **Put Cancel on the leading side of a sheet and Done on the trailing side.** In later steps of a multistep sheet, Back replaces Cancel. Never show all three. (Mar 2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#iOS-iPadOS)
- **Anchor action sheets and popovers to the control that opens them** so they grow out of it. [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- **Give menu items icons only where they speed up scanning, and give a whole group icons or none.** (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Icons)

### Buttons and motion
- **Use `.buttonStyle(.glass)` for floating secondary buttons and `.glassProminent` for the single primary.** Never use `.plain` + `.glassEffect()`, which loses the press state, the hit shape, and the system's adaptation. [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons#Style)
- **Make tappable custom glass `.interactive()`.** That gives it the system's touch and pointer response. [Applying Liquid Glass](https://developer.apple.com/documentation/swiftui/applying-liquid-glass-to-custom-views)
- **Morph glass that appears or disappears near other glass instead of fading it.** Use `glassEffectID(_:in:)` with `withAnimation`, `.glassEffectTransition(.materialize)` for distant shapes, and `glassEffectUnion` to fuse shapes at rest. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Best-practices)
- **Add no custom bounce or scale to glass controls.** The system already animates them, with stronger motion for touch and subtler motion for a trackpad. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)

### Accessibility
- **Test with Reduce Transparency, Increase Contrast, Reduce Motion, and the Liquid Glass look setting.** System glass adapts to them, but your dimming layers, tints, and custom animations don't. Read `accessibilityReduceTransparency`, `colorSchemeContrast`, and `accessibilityReduceMotion`. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass), [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)
- **Check contrast on both glass appearances.** Text on glass must meet 4.5:1 over both light and dark content. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)

### App icons
- **Build the icon in layers in Icon Composer.** Use a background plus foreground layers: square, unmasked, vector, with crisp edges. Bake in no highlights, shadows, or blur. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)
- **Prefer the Icon Composer format over a bitmap.** The system splits a bitmap into two layers and skips glass on text and thin lines. (Oct 2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Icon-formats)
- **Keep the same features in the default, dark, clear, and tinted variants.** Don't add or remove elements between them. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Appearances)

### Platforms
- **iOS 27 ignores `UIDesignRequiresCompatibility`.** When you build with the 27 SDKs the opt-out is gone, so adopt the design instead of postponing it. (iOS 27+) [Docs](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility)
- **macOS:** toolbar items have no bezel, and glass sits in the toolbar and sidebar. For custom glass, use `NSGlassEffectView` and `NSButton.BezelStyle.glass`. On touch displays, keep density and enlarge on touch. (Oct 2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos#Best-practices)
- **watchOS, tvOS, visionOS:** watch toolbar buttons get glass automatically, and tvOS controls turn to glass on focus. visionOS uses its own window glass (`glassBackgroundEffect`), because `glassEffect` isn't available there. [HIG](https://developer.apple.com/design/human-interface-guidelines/materials#tvOS)

## Brief conflicts
When a request contradicts these rules, say so, link the rule, propose the alternative, then follow the person's decision.

| Request | Conflict | Compliant alternative |
|---|---|---|
| "Paint the nav bar or tab bar our brand color" | [Bar backgrounds interfere with glass](https://developer.apple.com/design/human-interface-guidelines/toolbars#Best-practices) | Brand through the accent color on the prominent action, colored content, and the icon |
| "Glass cards for the feed or settings rows" | [No glass in the content layer](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) | Grouped backgrounds or standard materials; glass only on floating controls |
| "Make every button colorful and glassy" | [Color sparingly; one or two prominent buttons](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color) | One `.glassProminent`, the rest `.glass` with monochrome labels |
| "Keep the iOS 18 look via `UIDesignRequiresCompatibility`" | [Ignored when building for 27](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility) | Adopt now, and keep identity in content and icon |
| "Hide the tab bar on scroll" or "hide tabs that are empty" | [Tab bar stays visible; tabs stay enabled](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices) | `.tabBarMinimizeBehavior(.onScrollDown)`; an empty state that explains why |
| "Add a + tab" | [Tabs navigate, not act](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices) | A toolbar button, prominent if it's the primary action |
| "Solid dark panel behind the tools" | [Differentiate controls with glass, not fills](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy) | A bottom toolbar, or glass in a `GlassEffectContainer` |
| "Glossy icon with a photo and the app name" | [Simple layers; system adds effects; avoid text](https://developer.apple.com/design/human-interface-guidelines/app-icons#Design) | A layered illustration in Icon Composer |

## Common mistakes
- Building glass circles from `.buttonStyle(.plain)` + `.glassEffect()` + `.clipShape(Circle())` instead of `.buttonStyle(.glass)` with `.buttonBorderShape(.circle)`, or a bottom toolbar.
- Hard-coding `.tint(.blue)` or `Color.blue` selection fills instead of relying on the accent color.
- Leaving `toolbarBackground(Color.black, for: .navigationBar)` and `.visible` in place, which kills the glass and the scroll edge effect.
- Packing three buttons into one `ToolbarItem { HStack { … } }`. That yields mixed text and symbols in one capsule and no prominent Done. Use separate items or groups instead.
- Putting `glassEffect` before `padding`, `frame`, or `font`. It captures the view as it is at that point, so apply it last.
- Scattering many separate glass views without a container, which costs performance and prevents morphing.
- Putting clear glass with text over plain backgrounds, or using clear glass without a dimming layer over bright photos.
- Writing deprecated `navigationBarLeading` / `navigationBarTrailing` placements. Use `.cancellationAction`, `.confirmationAction`, `.primaryAction`, or `.topBarTrailing` instead.
- Writing uppercase section headers. Lists now use title-style capitalization.
- Skipping iOS 27 entirely: `ToolbarOverflowMenu`, `visibilityPriority`, `TabRole.prominent`, `toolbarMinimizationBehavior`.

## Migration checklist (iOS 17/18-style screen)
1. Build with the current SDK, delete `UIDesignRequiresCompatibility`, and look before you change anything.
2. Delete bar backgrounds: `toolbarBackground`, `UINavigationBarAppearance`/`UITabBarAppearance` fills, custom bar blurs.
3. Make content full-bleed (`ignoresSafeArea` on media only) and let it scroll under the bars.
4. Replace opaque or `Color.black.opacity` floating panels with toolbar items, or with `.glass` buttons in one `GlassEffectContainer` (`.clear` over media).
5. Rebuild the toolbar: semantic placements, symbols, groups plus `ToolbarSpacer`, one `role: .confirm` action.
6. Replace hard-coded `cornerRadius` near containers with concentric shapes, and remove custom sheet and popover backgrounds.
7. Swap literal colors for the accent color and semantic colors. Supply dark and increased-contrast variants.
8. Test Reduce Transparency, Increase Contrast, Reduce Motion, light and dark mode, and bright and dark content under every bar.

## References
- `references/swiftui-api.md`: read before writing code. It lists every verified Liquid Glass API with availability (26.x and 27) and its UIKit/AppKit equivalent.
- `references/migration.md`: read when updating an existing screen. It has find-and-replace patterns, a worked editor-screen conversion, and a review grep list.

## Look it up live
Most relevant slugs: `materials`, `color`, `toolbars`, `tab-bars`, `search-fields`, `scroll-views`, `sidebars`, `split-views`, `sheets`, `buttons`, `menus`, `motion`, `layout`, `app-icons`, `accessibility`.
```
python3 ../apple-hig/scripts/hig.py fetch materials --section "Liquid Glass"
python3 ../apple-hig/scripts/hig.py fetch /documentation/swiftui/view/glasseffect(_:in:)
python3 ../apple-hig/scripts/hig.py fetch /documentation/technologyoverviews/adopting-liquid-glass
```
