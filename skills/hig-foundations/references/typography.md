# Typography

Sources: [Typography](https://developer.apple.com/design/human-interface-guidelines/typography), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision), [Branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)

## System typefaces

| Family | Where | Notes |
|---|---|---|
| SF Pro | System font on iOS, iPadOS, macOS, tvOS, visionOS | Widths incl. Condensed and Expanded (`Font.width(_:)`); Rounded variant |
| SF Compact | System font on watchOS | SF Compact Rounded in complications |
| SF Mono | Code, aligned columns | `Font.Design.monospaced` |
| New York | Serif, pairs with SF | `Font.Design.serif`; on macOS only via Mac Catalyst; on visionOS specify styles explicitly |
| SF Arabic, Armenian, Georgian, Hebrew | Script variants | Picked automatically by the system |

- **Access them through `Font.Design` (`.default`, `.serif`, `.rounded`, `.monospaced`), never by bundling the font files.** [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts)
- **The system fonts are variable with dynamic optical sizes;** don't choose "Text" vs. "Display" cuts in code. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts)
- **SF Symbols share SF's nine weights,** so a symbol in the same font as its label matches automatically. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts)

## Legibility and hierarchy

- **Sizes:** iOS/iPadOS default 17 pt, min 11; macOS 13/10; tvOS 29/23; visionOS 17/12; watchOS 16/12. Thin custom fonts need more than the minimum. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Ensuring-legibility)
- **Weights:** Regular, Medium, Semibold, Bold for UI; avoid Ultralight, Thin, Light, especially small. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Ensuring-legibility)
- **Build hierarchy from weight, size and color, and keep it intact at every text size.** [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Conveying-hierarchy)
- **Use as few typefaces as possible,** even in a heavily branded UI. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Conveying-hierarchy)
- **Larger text should enlarge what people came to read;** tab titles and transient numbers (a game's hit damage) can stay put. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Conveying-hierarchy)
- **Support enlarging text by at least 200 percent (140 percent on watchOS).** [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)

## Text styles and emphasis

Text styles bundle size, weight and leading per Dynamic Type size. Use them, then modify with symbolic traits:

- **Emphasis:** `.bold()` (SwiftUI) or `traitBold` (UIKit `UIFontDescriptor`). The result is the style's defined emphasized weight, not always Bold. (Dec 2025) [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications)
- **Leading:** `Font.leading(.loose)` for wide columns and long passages, `.tight` for height-constrained rows, but never tight for three or more lines. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts)
- **Tracking:** SF tracks itself per point size at runtime. The tracking tables on the HIG page are for design mockups only; don't port them into `.tracking()` calls. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Tracking-values)

### iOS/iPadOS at the default size (Large)

| Style | SwiftUI | Weight | Size / leading (pt) | Emphasized |
|---|---|---|---|---|
| Large Title | `.largeTitle` | Regular | 34 / 41 | Bold |
| Title 1 | `.title` | Regular | 28 / 34 | Bold |
| Title 2 | `.title2` | Regular | 22 / 28 | Bold |
| Title 3 | `.title3` | Regular | 20 / 25 | Semibold |
| Headline | `.headline` | Semibold | 17 / 22 | Semibold |
| Body | `.body` | Regular | 17 / 22 | Semibold |
| Callout | `.callout` | Regular | 16 / 21 | Semibold |
| Subhead | `.subheadline` | Regular | 15 / 20 | Semibold |
| Footnote | `.footnote` | Regular | 13 / 18 | Semibold |
| Caption 1 | `.caption` | Regular | 12 / 16 | Semibold |
| Caption 2 | `.caption2` | Regular | 11 / 13 | Semibold |

Note: Headline and bold Body look the same weight (Semibold); use size or color to separate them. Tables for xSmall–xxxLarge and AX1–AX5: `hig.py fetch typography --section "Specifications"`.

### macOS (fixed, no Dynamic Type)

Large Title 26, Title 1 22, Title 2 17, Title 3 15, Headline 13 Bold (emphasized Heavy), Body 13, Callout 12, Subheadline 11, Footnote 10, Caption 1 10, Caption 2 10 Medium. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications)

To match standard controls in AppKit, use the `NSFont` variants: `controlContentFont(ofSize:)`, `labelFont(ofSize:)`, `menuFont(ofSize:)`, `messageFont(ofSize:)`, `toolTipsFont(ofSize:)`, `userFont(ofSize:)`, `userFixedPitchFont(ofSize:)`, `systemFont(ofSize:)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#macOS)

### Other platforms
- **tvOS:** Title 1 76 pt down to Caption 2 23 pt, mostly Medium; Body 29. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications)
- **visionOS:** bolder Body and Title styles, plus `.extraLargeTitle` and `.extraLargeTitle2` for editorial layouts; prefer flat 2D text; text not on a background can go bold, avoid shadows; billboard labels attached to 3D objects so they face the viewer. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#visionOS)
- **watchOS:** SF Compact; default size depends on case size (Small for 38 mm, Large for 40–42 mm, xLarge for 44–49 mm). [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications)

## Dynamic Type

- **Test at the largest accessibility size** (Settings > Accessibility > Display & Text Size > Larger Text) and at xSmall. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Grow meaningful icons with the text.** SF Symbols in a text font do this; custom images need `@ScaledMetric` sizes. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Wrap instead of truncate;** show as much useful text at AX5 as at xxxLarge, and truncate in scroll views only if a detail view shows the rest. `lineLimit(nil)` / `numberOfLines = 0`. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **At accessibility sizes, stack inline items (icons, timestamps) under the text and cut column counts.** [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Let rows and containers grow in height;** no fixed row heights. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability)

```swift
struct MessageRow: View {
    @Environment(\.dynamicTypeSize) private var size
    @ScaledMetric(relativeTo: .body) private var avatar = 40.0
    let message: Message
    var body: some View {
        let layout = size.isAccessibilitySize
            ? AnyLayout(VStackLayout(alignment: .leading))
            : AnyLayout(HStackLayout(alignment: .top))
        layout {
            Avatar(message.sender).frame(width: avatar, height: avatar)
            Text(message.body).font(.body)
            Text(message.date, style: .time).font(.footnote).foregroundStyle(.secondary)
        }
    }
}
```

## Custom fonts

- **Keep a custom font legible at the platform minimums,** and prefer it for headlines and subheads with the system font for body and captions. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **Give it the same accessibility behavior the system font has: Dynamic Type and Bold Text.** [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-custom-fonts)

```swift
struct BrandTitle: View {
    @Environment(\.legibilityWeight) private var legibility   // .bold when Bold Text is on
    let text: String
    var body: some View {
        Text(text)
            .font(.custom(legibility == .bold ? "Brand-Bold" : "Brand-Medium",
                          size: 28, relativeTo: .title))
    }
}
```

UIKit: `UIFontMetrics(forTextStyle: .title1).scaledFont(for: base)` and `adjustsFontForContentSizeCategory = true`; check `UIAccessibility.isBoldTextEnabled`. Unity games: Apple's Unity plug-ins, or another in-game text size control.

## Checklist
- No `.system(size:)` or `.custom(_:size:)` without `relativeTo:` for running text.
- No `.tracking` / `.kerning` / `lineSpacing` on SF to imitate a mockup.
- Bold via `.bold()` on the style; no `.fontWeight(.black)` for emphasis.
- Layout checked at AX5: no clipped or overlapping text, primary items still at the top.
