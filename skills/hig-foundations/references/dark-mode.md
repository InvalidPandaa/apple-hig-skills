# Dark Mode

Sources: [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), [Color](https://developer.apple.com/design/human-interface-guidelines/color), [Settings](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)

Dark Mode is a system setting on iOS, iPadOS, macOS and tvOS. visionOS and watchOS have no Dark Mode.

## The appearance-setting rule

- **Don't build an in-app Light / Dark / System picker.** People would need to change two settings, and an app that ignores the system choice looks broken. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices)
- **Don't ask for information the system already has;** read `colorScheme` instead of asking which mode people use. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Don't copy system-wide settings into your settings screen at all** (appearance, accessibility, text size). It implies the system setting doesn't apply. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Exception: a permanently dark UI is acceptable for immersive media viewing** (photo, video, some games) so the UI recedes. Apply it to that scene with `.preferredColorScheme(.dark)`, not as a toggle. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices)

When a brief asks for a theme picker: say it conflicts with the HIG (link above), propose following the system appearance, and offer a real content option instead if the need is about reading comfort (for example a reader-view background choice for long-form text). Then implement what the person decides.

## Colors

- **Dark colors are not inverted light colors;** backgrounds get dimmer and foregrounds brighter, and some colors stay. Use semantic colors and Color Set assets with Any/Dark (+ High Contrast) variants; no hard-coded values. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)
- **Minimum contrast 4.5:1, aim for 7:1 with custom pairs and small text,** in both appearances. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)
- **Use the label colors for text and system text views/fields** so vibrancy and contrast adjust for you. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Text)

### Base and elevated backgrounds (iOS, iPadOS)
In Dark Mode the system background colors have a dimmer base set and a brighter elevated set. Sheets, popovers, multitasking apps and side-by-side windows switch to elevated automatically, which is how people see layering in the dark. A hard-coded dark background stays flat and loses that cue, so use `systemBackground` / `systemGroupedBackground` (SwiftUI `.background` style or `Color(.systemBackground)`). [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Platform-considerations)

### macOS desktop tinting
With the Graphite accent, window backgrounds pick up color from the desktop picture. Give custom components with a visible background or bezel a little transparency **in their neutral state only**; colored states stay opaque so their color doesn't shift as the window moves. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#macOS)

## Images and icons

- **SF Symbols adapt on their own** when tinted with dynamic colors or vibrancy; prefer them. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Icons-and-images)
- **One asset if it works in both modes, otherwise light and dark versions under one name in the asset catalog.** [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Icons-and-images)
- **Dim content images with white backgrounds slightly in Dark Mode** so they don't glow. [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)

```swift
@Environment(\.colorScheme) private var scheme
ProductPhoto(item)
    .brightness(scheme == .dark ? -0.08 : 0)   // soften white product shots
```

## Test matrix

Run each key screen in:

| Appearance | Increase Contrast | Reduce Transparency |
|---|---|---|
| Light | off / on | off / on |
| Dark | off / on | off / on |

Dark with Increase Contrast and Reduce Transparency (each alone and together) is where dark text on dark backgrounds most often fails, and Increase Contrast can even lower contrast between two dark custom colors. Also switch appearance while the app is running (Auto switches during the day). [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices)

SwiftUI previews: `.preferredColorScheme(.dark)` in a preview, or the Xcode canvas variants for color scheme and Dynamic Type.
