# Branding and images

Sources: [Branding](https://developer.apple.com/design/human-interface-guidelines/branding), [Images](https://developer.apple.com/design/human-interface-guidelines/images), [Launching](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens), [Color](https://developer.apple.com/design/human-interface-guidelines/color#Color-management), [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion#People-and-settings)

## Branding

A brand shows through voice, accent color, typography in headings, content and the app icon, while structure and behavior stay standard.

- **Write in the brand's voice everywhere,** and keep it consistent (see `writing.md`). [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **Use the accent color sparingly:** primary actions and status (unread badges, the selected tab icon), not every control. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **Put brand color in the content layer** (headers, cards, artwork) where it scrolls under Liquid Glass and tints it dynamically. (Sep 2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **A brand font goes in headlines and subheads; body and captions stay in the system font,** and the brand font must support Dynamic Type and Bold Text. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **Brand standard components instead of inventing new ones;** if you restyle a control, keep its size, position and behavior. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **Use standard symbols for common actions and keep navigation and modality conventional,** even in a highly styled UI. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **No logo-only elements in the chrome and no logo on every screen;** spend that space on content. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **The launch screen is not a brand surface:** make it match the first screen, without text or logo (unless the logo is a fixed part of that first screen). A brand moment belongs at the start of onboarding. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens)
- **Keep Apple trademarks out of the app name and images.** [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)
- **Represent a range of people and familiar settings in imagery;** avoid stereotyped roles and unneeded displays of affluence. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#People-and-settings)

How to raise a branding conflict: name the request ("logo in every nav bar", "brand color on all buttons", "animated logo splash"), link the rule above, propose the compliant version (brand header in content, accent on the primary action, brand screen in onboarding), then follow the person's decision.

## Images

### Resolution

Points are abstract units; pixels per point is the scale factor. Provide bitmaps for every scale factor of the devices you support: [HIG](https://developer.apple.com/design/human-interface-guidelines/images#Resolution)

| Platform | Scale factors |
|---|---|
| iOS | @2x and @3x |
| iPadOS, watchOS | @2x |
| macOS, tvOS | @1x and @2x |
| visionOS | @2x or higher; prefer vectors |

- **Design at @1x and scale up;** place vector control points on whole values so edges stay on the pixel grid at 2x and 3x. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#Resolution)

### Formats

| Content | Format |
|---|---|
| Bitmap art | De-interlaced PNG (8-bit palette if 24-bit color isn't needed) |
| Photos | JPEG (optimized) or HEIC |
| Stereo / spatial photos | Stereo HEIC |
| Flat icons and art that must scale | PDF or SVG |

[HIG](https://developer.apple.com/design/human-interface-guidelines/images#Formats)

- **Embed a color profile in every image;** use Display P3 for wide-color art (16-bit PNG) and add sRGB variants if P3 colors collapse. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#Best-practices)
- **Test images on real devices;** pixelation and stretching don't show at design time. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#Best-practices)
- **Provide Dark Mode variants under the same asset name when an image fails in one appearance.** See `dark-mode.md`.

### tvOS layered images
- **Focusable artwork uses 2–5 layer images for parallax;** required for the app icon, encouraged for Top Shelf and other focusable images. Standard focus APIs apply the effect automatically. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#tvOS)
- **Foreground for main subjects and text, middle for secondary content and shadows, opaque background;** keep depth subtle and leave a safe zone, because focused layers scale and crop. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#tvOS)
- **Images loaded at runtime must be `.lcr` files** (built with `layerutil`), never embedded in the bundle. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#tvOS)
- **Preview with Xcode or Parallax Previewer, then on a real TV.** [HIG](https://developer.apple.com/design/human-interface-guidelines/images#tvOS)

### visionOS
- **Prefer vectors for 2D art;** if raster is required, go above @2x only as needed (cost rises fast beyond @6x) and enable high-quality filtering. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#visionOS)
- **Show spatial photos and spatial scenes in their own sheet or window, not inline;** put text over them only with the feathered glass background effect; spatial scenes take seconds to generate, so trigger them explicitly. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#visionOS)

### watchOS
- **Skip transparency in images that always sit on the same background,** except template images (complications, menu icons) where alpha defines the tinted area. [HIG](https://developer.apple.com/design/human-interface-guidelines/images#watchOS)
- **Use one autoscaling PDF designed for 40/42 mm at @2x;** the system scales it from 90% (38 mm) up to 119% (45/49 mm). [HIG](https://developer.apple.com/design/human-interface-guidelines/images#watchOS)
