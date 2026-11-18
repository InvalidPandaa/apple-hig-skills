---
name: hig-foundations
description: Use when choosing or reviewing colors, a brand or accent color, fonts and text sizes, spacing and layout, SF Symbols, interface icons, app icons, Dark Mode, animation, UI copy, capitalization, error messages, branding or image assets in a native Apple-platform app (SwiftUI, UIKit, AppKit), or when a brief asks for an in-app theme picker, a custom font, a logo-heavy screen, a hard-coded tint or a splash-style launch screen.
---

# HIG Foundations

Let the system carry color, type, spacing, symbols and motion so they adapt to appearance, text size, contrast and window size on their own; put your brand into content, accent and voice, never into replacements for those system behaviors.

## Quick decisions

| Need / situation | Do this (API) | Link |
|---|---|---|
| Brand color in the UI | `AccentColor` asset with light, dark and high-contrast variants; inherits app-wide, `.tint(_:)` only for local overrides | [color](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color) |
| Any custom color | Color Set in the asset catalog with 4 variants (light, dark, each with Increased Contrast) | [color](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices) |
| Text | Text styles `.font(.body)` etc.; emphasis via `.bold()` | [typography](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts) |
| Brand font | `Font.custom(_:size:relativeTo:)` for headlines; system font for body and captions | [branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices) |
| Spacing or icon size that should grow with text | `@ScaledMetric` | [typography](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type) |
| Row crowds at large text | Stack vertically when `dynamicTypeSize.isAccessibilitySize` (`AnyLayout`, `ViewThatFits`) | [typography](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type) |
| Layout differs on iPad / Mac / resized windows | Branch on `horizontalSizeClass`, never on idiom or orientation | [layout](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes) |
| Hardware or hinge covers custom content | Safe area first; `GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:)` (iOS 27.1+) | [iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions) |
| Hero image under sidebar/inspector | `.backgroundExtensionEffect()` (iOS 26+) | [layout](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy) |
| An icon for a common action | The standard SF Symbol name (see references/icons-and-app-icons.md) | [icons](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons) |
| Show a level (volume, signal) | `Image(systemName:variableValue:)`; never variable color for depth | [sf-symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Variable-color) |
| Feedback that something happened | `.symbolEffect(.bounce, value:)`, `.contentTransition(.symbolEffect(.replace))` | [sf-symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations) |
| App icon | Layered Icon Composer file (`.icon`), unmasked square layers | [app-icons](https://developer.apple.com/design/human-interface-guidelines/app-icons#Icon-formats) |
| Custom animation | Short, interruptible; check `accessibilityReduceMotion` and swap movement for a fade | [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive) |
| Button / menu / segment label | Verb (or noun for segments), title-style capitalization, no end punctuation | [alerts](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons) |
| Glass, materials, scroll edge effects | Out of scope here: use `hig-liquid-glass` | [materials](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) |

## Rules

### Color
- **Basics, no explanation needed:** semantic colors (`.primary`, `.secondary`, system backgrounds), never hard-coded RGB of system colors, never color as the only signal, 4.5:1 minimum text contrast.
- **Ship dark variants even if the app is light-only.** Liquid Glass adapts between light and dark over content, so every custom color needs both, plus an Increased Contrast version of each. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Use the app accent, not `.tint(.blue)`.** Hard-coding a system color as tint bypasses the AccentColor asset and its variants; on macOS the person's accent setting replaces yours anyway unless it is Multicolor. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#App-accent-colors)
- **Put accent color on the background of the one primary action, not on symbols or labels, and not on several controls.** That is what prominent system buttons do (`.buttonStyle(.glassProminent)` on iOS 26+, `.borderedProminent` before). [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)
- **Aim for 7:1 with custom foreground/background pairs, especially small text.** 4.5:1 is the floor, not the target, for colors you define. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)
- **Never reuse a semantic color for another role** (separator as text, secondary label as fill), and never give the interactive accent to static text. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#System-colors)
- **Keep the resting state of a screen legible:** colorful content may scroll under bars, but the top of the scroll position must not put similar colors under controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Liquid-Glass-color)

### Typography
- **Basics:** text styles everywhere, no fixed sizes, avoid Ultralight/Thin/Light, iOS default 17 pt and minimum 11 pt (macOS 13/10).
- **Get emphasis from `.bold()` on a text style, not a hand-picked weight.** Each style has a defined emphasized weight (Body → Semibold, Title 1 → Bold, macOS Headline → Heavy). (2025) [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Specifications)
- **Don't set `.tracking`/`.kerning` or line spacing on the system font.** SF adjusts tracking per point size and the text style sets leading; use `Font.leading(.tight/.loose)` if you must, never tight for 3+ lines. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts)
- **Make custom fonts honor Bold Text as well as Dynamic Type.** Scale with `relativeTo:` and switch to a heavier face when `legibilityWeight == .bold`. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-custom-fonts)
- **Use `Font.Design` (`.serif` for New York, `.rounded`, `.monospaced`) instead of bundling Apple fonts.** Don't embed SF or NY in the bundle. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-system-fonts)
- **Decide what grows.** Content text must scale; chrome like tab titles need not. Keep the same amount of useful text visible at AX sizes and keep primary items at the top. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Conveying-hierarchy)
- **macOS has no Dynamic Type.** Use its fixed text styles and the `NSFont` control/menu variants to match system controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#macOS)

### Layout
- **Basics:** respect safe areas and system margins, leading-to-trailing reading order, group with space before lines.
- **Decide layout from size classes, never from device model or orientation.** iPad windows, iPhone Mirroring and iPhone Duo produce every combination. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
- **Keep features identical across sizes; only how many are visible changes** (tab bar → sidebar, overflow menu → inline). [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
- **Separate controls from content with a scroll edge effect, not a solid bar background,** and extend full-bleed backgrounds under bars and sidebars. (iOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Visual-hierarchy)
- **On iPhone Duo, use size classes, margins and safe areas, no fixed widths, and an even column count in grids.** (iOS 27+) [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Dynamic-layouts)
- **Don't hard-code device dimensions.** The Layout page no longer lists per-device sizes; read safe areas and margins at runtime and use Apple Design Resources for mockups. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas)
- **macOS: keep critical controls off the window bottom; tvOS: inset 60 pt top/bottom, 80 pt sides; visionOS: button centers 60 pt apart.** [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Platform-considerations)

### SF Symbols, icons, app icons
- **Size symbols with the adjacent text's font and weight; adjust emphasis with `.imageScale`, not a frame.** A `.resizable()` frame scales strokes instead of matching the text weight. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Weights-and-scales)
- **Let the container pick outline vs. fill.** Tab bars fill, toolbars outline; don't hand-supply selected-state icons for system bars. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Design-variants)
- **Never put an SF Symbol (or a look-alike) in an app icon or logo.** The license forbids it. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- **Supply the app icon as layered Icon Composer art with square, unmasked layers and no baked-in shadows or highlights.** A flat PNG gets auto-segmented and text or thin lines get no glass. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Icon-formats)
- **Keep icon features identical across default, dark, clear and tinted appearances;** alternate icons need their own variants. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Appearances)

### Dark Mode and motion
- **Never add an in-app Light/Dark/System setting.** Respect the system choice; Auto can switch while the app runs. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices)
- **Use system backgrounds so sheets and popovers turn "elevated" in Dark Mode.** A custom background hides that depth cue. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Platform-considerations)
- **Animate only to explain or confirm, keep it brief, never block input on it, and skip it on frequent interactions.** [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)
- **Under Reduce Motion, replace slides, zooms and bounces with fades or tighter springs** and stop repeating effects. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)

### Writing and branding
- **Pick title-style or sentence-style per element type and never mix within it.** Buttons, menu items, segments and fragment titles: title-style; alert messages, notification bodies, full-sentence titles: sentence-style with punctuation. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Write errors next to the problem, saying how to fix it; no "we", no "Oops", no blame.** "Unable to Load Photos" beats "We're having issues". [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Say "tap" on touch devices and "click" only on Mac; when alert text must mention a button, use "choose" and its exact title.** [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Content)
- **Move brand color into the content layer and keep logos out of the chrome and the launch screen.** (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)

## Brief conflicts

When a request below appears, say that it conflicts with the HIG, link the rule, offer the alternative, then do what the person decides.

| Request | Why it conflicts | Compliant alternative |
|---|---|---|
| In-app Light/Dark/System picker | People must set two places and think the app is broken ([dark-mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices), [settings](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)) | Follow the system; dark-only only for immersive media viewing (`.preferredColorScheme(.dark)` on that scene) |
| "Use our brand blue on all buttons and icons" | Color on many controls dilutes emphasis and fights glass ([branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)) | Brand color as `AccentColor` for the primary action, selection and badges; more color in content |
| Brand font at fixed sizes everywhere | Breaks Dynamic Type and Bold Text ([typography](https://developer.apple.com/design/human-interface-guidelines/typography#Using-custom-fonts)) | Custom font scaled `relativeTo:` for headlines, system font for body |
| Logo in the nav bar on every screen, branded splash on launch | Branding must defer to content; launch screen is not a brand surface ([branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices), [launching](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens)) | Launch screen matching the first screen; brand moment inside onboarding |
| Light-only design, "no need for dark colors" | Glass bars still adapt to dark ([color](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)) | Define dark and high-contrast variants anyway |
| App name, a photo or a screenshot in the app icon | Not localizable, unreadable small, poor with layers ([app-icons](https://developer.apple.com/design/human-interface-guidelines/app-icons#Design)) | One simple illustrated idea; at most a single-letter mnemonic |
| Thin/Light weight body text for an "elegant" look | Hard to read ([typography](https://developer.apple.com/design/human-interface-guidelines/typography#Ensuring-legibility)) | Regular to Bold; express elegance with size, a display font for titles, or New York |
| Playful copy ("Oops! We messed up", "Let's do it!") | Unclear, insincere in errors ([writing](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)) | Plain verbs and fix-it messages; keep personality for success and empty states |
| Separate iPad layout keyed on `userInterfaceIdiom` | Ignores resized windows ([layout](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)) | Size-class-driven adaptive layout |

## Common mistakes
- `.tint(.blue)` or `Color(red:green:blue:)` for brand color instead of an AccentColor asset with variants.
- Custom color sets with only "Any" and "Dark", no Increased Contrast variants.
- `Image(systemName:).resizable().frame(width: 24, height: 24)` next to text, so weight and baseline no longer match.
- Old symbol names (`doc.on.doc`) where the standard is now `document.on.document`; verify availability for the deployment target.
- `.font(.system(size: 17))` or `Font.custom("X", size: 17)` without `relativeTo:`; padding in fixed points that clips at AX sizes.
- `.tracking()` added to SF for "polish", copied from a Figma mockup.
- Mixed capitalization: "Add to cart" button next to "Save Draft"; periods on button titles.
- App icon exported with rounded corners or drop shadows already applied.
- Custom animations that ignore `accessibilityReduceMotion`, or a symbol pulsing forever with nothing in progress.

## References
- `references/color.md`: accent and brand color setup, contrast, variants, color management, platform color notes.
- `references/typography.md`: text-style tables, emphasized weights, custom-font scaling code, macOS/watchOS/visionOS differences.
- `references/layout.md`: size classes, margins, readable width, multitasking, iPhone Duo, platform spacing numbers.
- `references/sf-symbols.md`: rendering modes, variants, every animation and when to use it, custom symbols.
- `references/icons-and-app-icons.md`: interface icon rules, standard action symbol names, Icon Composer and app icon specs.
- `references/dark-mode.md`: appearance testing matrix, elevated backgrounds, images, macOS desktop tinting.
- `references/motion.md`: purposeful motion, Reduce Motion substitutions, visionOS comfort.
- `references/writing.md`: voice, labels, capitalization by element, errors, empty states, inclusive wording.
- `references/branding-and-images.md`: brand expression limits, scale factors and formats, tvOS layered images.

## Look it up live
Slugs: `color`, `typography`, `layout`, `sf-symbols`, `icons`, `app-icons`, `dark-mode`, `motion`, `writing`, `branding`, `images`, `inclusion`, `accessibility`, `designing-for-iphone-duo`.
```
python3 ../apple-hig/scripts/hig.py fetch typography --section "Supporting Dynamic Type"
python3 ../apple-hig/scripts/hig.py fetch /documentation/swiftui/font/custom(_:size:relativeto:)
```
