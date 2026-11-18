# Icons and app icons

Sources: [Icons](https://developer.apple.com/design/human-interface-guidelines/icons), [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons), [Images](https://developer.apple.com/design/human-interface-guidelines/images#tvOS), [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Icons-and-images)

## Interface icons (glyphs)

- **Prefer an SF Symbol; draw a custom glyph only when none fits,** ideally as a custom symbol so it scales and weights like text. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **One simple, familiar metaphor per icon,** directly tied to the action or content. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Keep size, detail, stroke weight and perspective consistent across all icons,** custom and system mixed; adjust dimensions for visual weight. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Center asymmetric glyphs optically, building the offset into the asset's padding** (a download arrow is heavy at the bottom). [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Skip selected-state artwork for toolbars, tab bars and buttons;** the system renders selection. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Avoid text in glyphs; if a letter is the concept (Bold), localize it, and supply a flipped version of abstract text lines for right-to-left.** [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Ship custom glyphs as PDF or SVG vectors** (asset catalog, "Preserve Vector Data"); PNG glyphs need every scale factor. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Give each custom glyph an accessibility label.** [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Use gender-neutral figures; no replicas of Apple hardware** (use Apple Design Resources images or the product symbols instead). [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Add light and dark versions only when one asset fails in one mode** (a full moon needs an outline on white, a drop of oil a rim on black). [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Icons-and-images)

## Standard symbols for common actions

Use these so actions look the same as in system apps. Several names changed in recent SF Symbols releases; check availability for the deployment target. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons)

| Action | Symbol | Action | Symbol |
|---|---|---|---|
| Cut | `scissors` | Copy | `document.on.document` |
| Paste | `document.on.clipboard` | Done | `checkmark` |
| Cancel / Deselect | `xmark` | Delete | `trash` |
| Undo / Redo | `arrow.uturn.backward` / `arrow.uturn.forward` | Compose | `square.and.pencil` |
| Duplicate | `plus.square.on.square` | Rename | `pencil` |
| Move to | `folder` | Attach | `paperclip` |
| Add | `plus` | More | `ellipsis` |
| Select | `checkmark.circle` | Search | `magnifyingglass` |
| Find | `text.page.badge.magnifyingglass` | Filter | `line.3.horizontal.decrease` |
| Share | `square.and.arrow.up` | Print | `printer` |
| Account | `person.crop.circle` | Like / Dislike | `hand.thumbsup` / `hand.thumbsdown` |
| Bold / Italic / Underline | `bold` / `italic` / `underline` | Superscript / Subscript | `textformat.superscript` / `textformat.subscript` |
| Align left / center / justify / right | `text.alignleft` / `text.aligncenter` / `text.justify` / `text.alignright` | Alarm / Archive / Calendar | `alarm` / `archivebox` / `calendar` |
| Bring to Front / Send to Back | `square.3.layers.3d.top.filled` / `square.3.layers.3d.bottom.filled` | Bring Forward / Send Backward | `square.2.layers.3d.top.filled` / `square.2.layers.3d.bottom.filled` |

The page also lists Save, Close, Export, Find and Replace, Find Next/Previous, User and Profile; fetch the section live for those names.

## macOS document icons

- **Let the system composite the folded-corner shape:** supply a background fill, a center image and/or a short term; without them macOS builds one from the app icon and file extension. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Document-icons)
- **Keep the top-right corner of the fill empty** (the fold covers it) and simplify the small sizes; drop fine detail at 16×16 px. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Document-icons)
- **Sizes:** fills at 512, 256, 128, 32 and 16 px @1x, each also at @2x; center image at half the canvas (256 down to 16 px @1x, plus @2x) with about a 10% margin; the extension or term is uppercased and auto-scaled, so keep it short (`scene`, not `scn`). [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Document-icons)

## App icons

### Format and tooling (iOS, iPadOS, macOS, watchOS)

- **Deliver a layered Icon Composer file.** In Icon Composer you set the background (solid or gradient), place foreground layers, tune specular highlights, refraction and translucency, annotate default, dark and mono variants, preview across OS versions, and export to Xcode. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)
- **A flat bitmap still works, but the system then splits it into two layers itself** and gives glass only to large simple shapes, not to text or thin lines. Use layers to control which parts get glass. (Oct 2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Icon-formats)
- **tvOS and visionOS icons are image stacks in the asset catalog,** not Icon Composer files (tvOS 2–5 layers with parallax; visionOS a background plus one or two layers). [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)

### Layers
- **Hard, clean edges on foreground shapes;** feathered edges spoil system highlights and shadows. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)
- **Import foreground layers opaque and set transparency in Icon Composer** to judge it with the system effects; varied opacity adds depth. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)
- **Vector (SVG, PDF) for shapes with text converted to outlines; PNG for raster art and mesh gradients.** An imported background must be full-bleed and opaque. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design)
- **Provide square (tvOS: rectangular) unmasked layers;** pre-rounded corners or circles produce jagged edges and break highlights. Keep the subject centered, especially for the circular visionOS and watchOS masks. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Icon-shape)
- **Group layers in Icon Composer when an effect should apply to several at once;** groups expose extra glass settings. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Visual-effects)

### Design
- **One core idea in a few overlapping filled shapes on a simple background;** the canvas need not be full. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Design)
- **Same design on every platform you ship,** so people don't think they are different apps. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Design)
- **No text unless essential;** a single-letter mnemonic is acceptable, words like "Play", "New" or "for visionOS" are not. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Design)
- **Illustrate instead of photographing; no screenshots or copies of standard UI controls; no Apple hardware; avoid hairlines and sharp corners.** [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Design)
- **Don't bake in shadows, bevels, glows, blurs or highlights;** the system adds dynamic ones. If you must, test in Icon Composer, Device Hub or on device. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Visual-effects)

### Appearances
- **iOS, iPadOS, macOS appearances:** default, dark, clear (light/dark), tinted (light/dark). The system generates any you omit. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Appearances)
- **Keep the same features in every appearance;** don't swap elements between variants. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Appearances)
- **Derive the dark icon from the light one,** with complementary colors, no glaring brights; colored backgrounds give dark icons the most contrast. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Appearances)
- **Alternate icons (iOS, iPadOS, tvOS, visionOS-compatible) need their own dark, clear and tinted variants,** must stay recognizably your app, and go through App Review. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Appearances)

### Specs

| Platform | Canvas | Mask | Notes |
|---|---|---|---|
| iOS, iPadOS, macOS | 1024×1024 px square | Rounded rectangle | Layered, six appearances |
| tvOS | 800×480 px | Rounded rectangle | 2–5 parallax layers; keep a safe zone, foreground crops more; text on top layer |
| visionOS | 1024×1024 px | Circle | 3D layers; no "hole" shapes in the background |
| watchOS | 1088×1088 px | Circle | Don't use a black background |

Color spaces: sRGB, Gray Gamma 2.2, Display P3 (not visionOS). Smaller sizes are generated by the system. [HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons#Specifications)
