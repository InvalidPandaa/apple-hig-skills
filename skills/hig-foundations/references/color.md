# Color

Sources: [Color](https://developer.apple.com/design/human-interface-guidelines/color), [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision), [Branding](https://developer.apple.com/design/human-interface-guidelines/branding), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion#Languages)

## Bringing a brand color in

1. Create an `AccentColor` color set in the asset catalog (Xcode new projects already reference it as the global accent). Fill in four appearances: Any, Dark, and High Contrast for each.
2. Let controls inherit it. Do not write `.tint(.blue)` or `.tint(Color("Brand"))` on every view; use `.tint(_:)` only where a subtree truly needs a different accent (for example a destructive area).
3. Use it on few things: the primary action's background, selection, badges, the selected tab icon. Not on body text, not on every toolbar symbol. [Branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
4. If the brand needs more presence, put it in content (headers, artwork, cards) that scrolls under the glass bars, where the system picks it up. (2026) [Branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
5. Check contrast of the accent against the backgrounds it sits on in all four appearances. If the content is very colorful, prefer monochrome bars or an accent that clearly differs from the content. [Color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)

```swift
// Only where a local override is needed; the app accent comes from the AccentColor asset.
Section { DeleteAccountButton() }
    .tint(.red)

// Reading system state instead of asking the person
@Environment(\.colorSchemeContrast) private var contrast   // .increased when Increase Contrast is on
@Environment(\.accessibilityDifferentiateWithoutColor) private var noColorOnly
```

## Rules

- **Mean one thing per color.** If the brand color marks interactive items, don't also use it for static text. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Provide light, dark and increased-contrast variants for every custom color, even in a single-appearance app.** Glass elements adapt to light and dark regardless. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Test outdoors and in dim light, and on True Tone and P3 vs. sRGB displays.** Reading, photo, video and game apps can tune white-point adaptation with `UIWhitePointAdaptivityStyle`. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Recheck nearby colors when artwork or translucency changes** (Maps switches its scheme in satellite mode). [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Use `ColorPicker` when people choose colors.** It shares saved colors across apps. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Back every color-coded meaning with text, a shape or a symbol.** Red/green and blue/orange pairs are the common failures; respect Differentiate Without Color. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color)
- **Check what colors mean in each locale you ship** (white can mean mourning or purity; red danger or luck). [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Languages)
- **Never hard-code the published values of system colors.** They change between releases (they did in June 2025). Use `Color.red`, `Color(.systemBackground)`, `NSColor.labelColor`. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#System-colors)
- **Use dynamic colors only for their named role.** Separator is not a text color; secondary label is not a fill. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#System-colors)

### Color on Liquid Glass (summary; details in `hig-liquid-glass`)
- **Glass has no color of its own; tint it only for emphasis** such as a primary action or status. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)
- **Color the background of the emphasized control, not its symbol or label,** and do this for one control, not a row of them. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)
- **Small bars (toolbars, tab bars) switch their symbols between dark and light over content;** don't fight this with fixed symbol colors. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)

## Contrast

| Case | Minimum | Source |
|---|---|---|
| Text up to 17 pt | 4.5:1 | [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision) |
| Text 18 pt and up, or bold | 3:1 | [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision) |
| Custom foreground/background pairs, small text | aim for 7:1 | [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors) |

- Accessibility Inspector applies the WCAG AA values above; APCA is also accepted as a measure.
- If the default palette misses the minimum, the app must at least reach it when Increase Contrast is on. Check light and dark separately.

## Backgrounds (iOS, iPadOS)

| Set | Use | Levels |
|---|---|---|
| `systemBackground` family | Plain lists and views | primary (whole view), secondary (groups inside), tertiary (groups inside groups) |
| `systemGroupedBackground` family | Grouped lists / `Form` / inset grouped tables | same three levels |

Foreground: `label`, `secondaryLabel`, `tertiaryLabel`, `quaternaryLabel`, `placeholderText`, `separator` (lets content show through), `opaqueSeparator`, `link`. In SwiftUI prefer the `.primary`, `.secondary`, `.tertiary`, `.quaternary` foreground styles and the `.background` style; reach for `Color(.secondarySystemBackground)` only when a specific level is needed. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Platform-considerations)

In Dark Mode these backgrounds switch between base and elevated automatically for sheets, popovers and multitasking; custom backgrounds lose that. See `dark-mode.md`.

## macOS

- **Accent color applies only while the person's General > Accent color is Multicolor.** Any other choice replaces your accent in buttons, selection and sidebar icons. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#App-accent-colors)
- **Sidebar icons follow the accent by default; give an icon a fixed color only when the color carries meaning** (Mail's yellow VIP). Fixed colors are not overridden by the accent setting. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- Notable AppKit roles: `controlAccentColor`, `selectedContentBackgroundColor` vs. `unemphasizedSelectedContentBackgroundColor` (non-key window), `alternatingContentBackgroundColors`, `windowBackgroundColor`, `underPageBackgroundColor`, `keyboardFocusIndicatorColor`, `findHighlightColor`. Using the unemphasized variants for inactive windows is a common omission. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Platform-considerations)

## Other platforms

- **tvOS:** a small palette tied to the logo; never indicate focus by color alone (scale and motion do that). [HIG](https://developer.apple.com/design/human-interface-guidelines/color#tvOS)
- **visionOS:** color sparingly on glass; color reads better on large areas and bold text than on thin text; in full immersion avoid a bright object on black, especially if it flashes or moves. System colors use the dark values. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#visionOS)
- **watchOS:** background color only when it communicates something; no full-screen color on long-lived screens (workouts, now playing); complications may be shown tinted. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#watchOS)

## Color management

- **Embed a color profile in every image;** sRGB is the safe default. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Color-management)
- **For wide color, use Display P3 at 16 bits per channel, exported as PNG,** designed on a P3 display. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Color-management)
- **Add sRGB-specific variants in the asset catalog when two P3 colors collapse or gradients clip on sRGB.** [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Color-management)

## System color names (SwiftUI)

red, orange, yellow, green, mint, teal, cyan, blue, indigo, purple, pink, brown, plus `gray` (= UIKit `systemGray`; UIKit also has `systemGray2`–`systemGray6`). Each has light, dark and increased-contrast values; read current values from the live page, not from memory. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Specifications)
