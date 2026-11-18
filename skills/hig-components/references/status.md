# Status components

Sources: [Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings), [Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges), [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators)

## Choosing between components in this group

| Situation | Component | API |
|---|---|---|
| Task with a measurable amount of work (download, export) | Determinate progress bar or circle | `ProgressView(value:total:)` |
| Task of unknown length (connecting, syncing) | Indeterminate spinner | `ProgressView()` |
| Person wants to reload a list now | Refresh control | `.refreshable { }` |
| A current value within a range that is not "work done" (temperature, battery, speed) | Gauge | `Gauge(value:in:)` |
| Same, in a Lock Screen widget or complication | Accessory gauge | `.gaugeStyle(.accessoryCircular)` / `.accessoryLinearCapacity` |
| macOS capacity meter (disk space) | Level indicator | `NSLevelIndicator` (`.continuousCapacity`, `.discreteCapacity`) |
| macOS star ranking | Rating indicator | `NSLevelIndicator.Style.rating` |
| A person's Move / Exercise / Stand progress | Activity rings | `HKActivityRingView` |

## Progress indicators

Use for: showing an operation is alive while content loads or work runs. Not for: values that aren't progress (gauge), decorative loading screens with no real work behind them.

- **Prefer determinate progress whenever you can measure the work.** People decide whether to wait, come back, or cancel based on it. `ProgressView(value:)`; Foundation `Progress` [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Advance at an honest, even pace.** Racing to 90% then stalling feels like a hang or a trick. [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Switch an indeterminate bar to determinate once the length is known, but never swap a spinner for a bar.** The shapes differ, so the change jars. [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Never leave an indicator frozen; if work stalls, say what's wrong and what to do.** [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Skip vague captions like "Loading…"; describe the specific work only when it helps** ("Importing 120 photos"). [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Offer Cancel when stopping is safe; add Pause when canceling loses progress, and confirm such a cancel with an alert.** [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Keep the indicator in the same place every time.** [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **iOS refresh control: still refresh automatically; give it a title only for useful info (last update time), never instructions.** `.refreshable`; UIKit `UIRefreshControl` [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Refresh-content-controls)

SwiftUI: `ProgressView`, `.progressViewStyle(.linear | .circular)`. UIKit `UIProgressView`, `UIActivityIndicatorView`; AppKit `NSProgressIndicator`.
Platforms: macOS also has an indeterminate bar; on Mac use an unlabeled spinner for background work or inside a field/next to a button. watchOS draws white by default; set a tint to change it.

## Gauges

Use for: a value within a known range, with optional context about the range. Not for: task progress (progress indicator).

- **Label the current value and both ends of the range concisely;** VoiceOver reads them even when the style hides some. `Gauge(value:in:) { label } currentValueLabel: { } minimumValueLabel: { } maximumValueLabel: { }` [HIG](https://developer.apple.com/design/human-interface-guidelines/gauges#Best-practices)
- **Use a gradient fill when it explains the scale** (cold blue to hot red). `.tint(Gradient(colors:))` [HIG](https://developer.apple.com/design/human-interface-guidelines/gauges#Best-practices)
- **Pick capacity style (fill to the value) for amounts, standard style (marker at the value) for positions;** use the accessory variants in widgets and complications. [HIG](https://developer.apple.com/design/human-interface-guidelines/gauges#Anatomy)
- **macOS level indicators: continuous for large ranges, discrete only when segments stay readable; change fill color at meaningful thresholds (tiered).** [HIG](https://developer.apple.com/design/human-interface-guidelines/gauges#macOS)

SwiftUI: `Gauge`, `.gaugeStyle(...)`. AppKit `NSLevelIndicator`. Not on tvOS.

## Activity rings

Use for: Move, Exercise and Stand progress of one person, in health and fitness apps (workout metrics, workout summary). Not for: any other data, multiple people, decoration, branding, app icons, notifications.

- **Never recolor, restyle or reuse the rings for other metrics, and never show Activity data in your own ring-like view.** [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings#Best-practices)
- **Always on black, ideally inside a circle made by corner radius (not a mask), with an outer margin at least the gap between rings.** No gradients, shadows, or opacity changes; adapt the surrounding UI, not the rings. [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings#Best-practices)
- **Make it obvious whose rings they are** (label, photo, avatar). [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings#Best-practices)
- **Use the official ring colors for related labels and values; fetch the RGB values from the page.** [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings#Best-practices)
- **Separate any other rings from Activity rings with padding, lines, labels, color, or scale.** [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings#Best-practices)
- **Don't send notifications that repeat the Activity app's progress updates, and never put the rings in a notification.** [HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings#Best-practices)

API: HealthKitUI `HKActivityRingView` (wrap with `UIViewRepresentable` in SwiftUI); watchOS `WKInterfaceActivityRing`.
Platforms: iOS shows only the Move ring when no Apple Watch is paired, so history can mix one-ring and three-ring days. Not on macOS, tvOS, visionOS.

## Rating indicators (macOS only)

Row of whole stars (no partial symbols), fixed spacing. Let people change a rating inline in the list rather than on an edit screen; replace the star only with a symbol whose meaning is obvious. AppKit `NSLevelIndicator.Style.rating`; on other platforms build ratings from `Image(systemName: "star.fill")` buttons with an accessibility value. [HIG](https://developer.apple.com/design/human-interface-guidelines/rating-indicators#Best-practices)
