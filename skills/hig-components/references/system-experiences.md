# System experiences

Sources: [App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts), [Complications](https://developer.apple.com/design/human-interface-guidelines/complications), [Controls](https://developer.apple.com/design/human-interface-guidelines/controls), [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities), [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications), [Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets), [Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars), [Top Shelf](https://developer.apple.com/design/human-interface-guidelines/top-shelf), [Watch faces](https://developer.apple.com/design/human-interface-guidelines/watch-faces), [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets)

These surfaces live outside your app's windows. Clear and tinted (Liquid Glass) widget appearances are explained by the `hig-liquid-glass` skill; this file covers content and behavior.

## Choosing between components in this group

| Situation | Component | API |
|---|---|---|
| Glanceable info that changes over the day; Home Screen, desktop, Smart Stack | Widget | WidgetKit `Widget`, `TimelineProvider` |
| Live, frequently changing event with a start and end (≤ 8 h): delivery, ride, game, timer | Live Activity | ActivityKit `Activity`, `ActivityConfiguration` |
| One-tap action or on/off from Control Center, Lock Screen, Action button | Control | WidgetKit `ControlWidgetButton`, `ControlWidgetToggle` |
| Data on the watch face; Lock Screen accessory | Complication / accessory widget | `.accessoryCircular`, `.accessoryRectangular`, `.accessoryInline`, `.accessoryCorner` |
| Run app actions from Siri, Spotlight, Shortcuts, Action button, Pencil squeeze | App Shortcut (or app schemas for Apple Intelligence) | App Intents `AppShortcutsProvider` |
| Show the result of, or confirm, an intent run from Siri/Spotlight/Shortcuts | Snippet | App Intents `SnippetIntent` |
| Timely, high-value info while the app isn't frontmost | Notification | UserNotifications |
| Featured content on the Apple TV Home Screen | Top Shelf | TVServices `TVTopShelfContentProvider` |
| Preconfigured watch face featuring your complications | Shareable watch face | ClockKit `CLKWatchFaceLibrary` |
| Hide device status during full-screen media | Status bar visibility | `.statusBarHidden(_:)` |

Real-time updates belong in a Live Activity, not a widget; errors belong in an alert, not a notification; repeating the same update as both a push and a Live Activity alert is wrong.

## Widgets

Use for: a focused slice of your app's content, refreshed periodically. Not for: real-time data (Live Activity), a launcher that only repeats the app icon, app-like dense UI.

- **Show content that changes and relates to the app's core purpose; never just the icon.** [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Best-practices)
- **Offer only the sizes that add something; don't stretch small-widget content into large.** [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Best-practices)
- **Deep-link every tap target to the matching screen; keep interactions few, large, and simple.** Inline accessory widgets have one target. `Button(intent:)`, `Toggle(isOn:intent:)`, `.widgetURL` [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Adding-interactivity)
- **Let the system update dates and times, and show "updated at" text if people check more often than you can refresh.** `Text(date, style: .timer)`, `Text(.now, style: .relative)` [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Updating-widget-content)
- **Use 16 pt standard margins (11 pt for tight groupings), ≥ 11 pt text, and real text, never rasterized.** `ContainerRelativeShape` for inner corners. [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Choosing-margins-and-padding)
- **Design for every rendering mode: full color, accented (tinted/clear Home Screen, Apple Watch) and vibrant (Lock Screen, StandBy at night).** Split views into accent and primary groups with `.widgetAccentable()`; keep full-color images for media via `.widgetAccentedRenderingMode(.fullColor)`; read `@Environment(\.widgetRenderingMode)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Rendering-modes)
- **Never convey meaning by color alone;** widgets may be monochrome, tinted, or inverted on watch faces. [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Using-color)
- **Mark the background removable so the widget works in StandBy and CarPlay (small size, scaled up, background removed).** `.containerBackground(for: .widget)`, `.containerBackgroundRemovable(true)` [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#StandBy-and-CarPlay)
- **Gallery: realistic preview, placeholder made of shapes, one description per widget starting with a verb, sizes grouped.** `.description(_:)`, `placeholder(in:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/widgets#Previews-and-placeholders)

Platforms: Lock Screen widgets follow complication rules and must stay legible on the Always-On display. watchOS Smart Stack: background color can carry meaning; supply relevance (RelevanceKit). visionOS (2025): widgets are physical objects; design simplified (distance) and default (near) detail levels with `@Environment(\.levelOfDetail)` (visionOS 26+), choose `.supportedMountingStyles(_:)` (elevated, recessed) and `.widgetTexture(_:)` (paper, glass). Apple HomeView (October 2026): small system widgets on the Home Screen and the shared Modular face, which can show one member's data to the whole household. Not on tvOS.

## Live Activities

Use for: tracking a task or event with a defined start and end, typically under 8 hours. Not for: ads, open-ended status (widget), information already sent as notifications.

- **Support all four presentations: compact, minimal, expanded, Lock Screen.** Start from the iPhone design, then tailor StandBy, CarPlay, and watchOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Presentation)
- **Compact leading and trailing views must read as one piece of info, sit snug against the TrueDepth camera, and link to the same screen.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Compact-presentation)
- **Adapt compact and minimal views to a 28 pt circle when the Dynamic Island is width-limited (landscape, iPhone Duo, several activities); if no trailing view fits, leave it empty (iOS 27+, October 2026).** `@Environment(\.isDynamicIslandLimitedInWidth)` [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Creating-Live-Activity-layouts)
- **Minimal view shows live data, not just a logo; logos go without a container, never the full app icon.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Minimal-presentation)
- **Lock Screen: 14 pt margins, its own layout (not a notification copy), legible in Dark Mode and Always-On; check the generated dismiss button color.** `.activitySystemActionForegroundColor(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Lock-Screen-presentation)
- **Medium-or-heavier text; at most one interactive element, only for direct actions like pause/resume.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Offering-interactivity)
- **Update only when content changes, alert only for updates people must not miss, and never duplicate with push notifications.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Starting-updating-and-ending-a-Live-Activity)
- **End it the moment the event ends; set a dismissal time of 15–30 minutes for a summary (it otherwise lingers up to 4 hours).** Give people an in-app way to stop it. `activity.end(_:dismissalPolicy: .after(_:))` [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Starting-updating-and-ending-a-Live-Activity)
- **Prefer one Live Activity that rotates through several events over many separate ones.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Starting-updating-and-ending-a-Live-Activity)
- **Hide sensitive data; it's visible on the Lock Screen.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities#Best-practices)

Animations max 2 s. Platforms: shown in the Mac menu bar (click opens iPhone Mirroring), Apple Watch Smart Stack (custom layout via `.supplementalActivityFamilies([.small])`, also used by CarPlay), CarPlay Dashboard where interactive elements are disabled, so skip buttons if people use it while driving. Not on tvOS or visionOS.

## Controls

Use for: a button or toggle in Control Center, on the Lock Screen, or on the Action button (iOS 18+). Not for: anything needing the app's UI.

- **Pick a symbol that explains the action on its own, with separate on/off symbols for toggles** (`door.garage.open` / `door.garage.closed`). Lock Screen shows only the symbol. [HIG](https://developer.apple.com/design/human-interface-guidelines/controls#Best-practices)
- **Animate state changes; animate continuously while a timed action runs.** SF Symbols `symbolEffect`. [HIG](https://developer.apple.com/design/human-interface-guidelines/controls#Best-practices)
- **Prompt for configuration when added, if the control needs a target** (which light). `.promptsForUserConfiguration()` [HIG](https://developer.apple.com/design/human-interface-guidelines/controls#Best-practices)
- **Give the Action button a verb hint and a placeholder for variable titles.** `.controlWidgetActionHint(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/controls#Best-practices)
- **Redact title/value when locked, and require unlock for security actions (doors, car).** `IntentAuthenticationPolicy` [HIG](https://developer.apple.com/design/human-interface-guidelines/controls#Best-practices)
- **Locked-device camera controls reuse the app's camera UI; everything beyond capture needs unlock.** `LockedCameraCapture` [HIG](https://developer.apple.com/design/human-interface-guidelines/controls#Camera-experiences-on-a-locked-device)

Platforms: the HIG lists iOS, iPadOS, macOS; WidgetKit's control APIs also list macOS 26 and watchOS 26.

## Notifications

Use for: timely, high-value info people can grasp at a glance. Not for: errors (alert), instructions to do something in the app, marketing.

- **Never send repeats for the same thing, and don't notify while the app is frontmost; update the UI or badge quietly instead.** `userNotificationCenter(_:willPresent:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/notifications#Best-practices)
- **Keep private data out, and provide a generic body for hidden previews** ("New comment"). `hiddenPreviewsBodyPlaceholder` [HIG](https://developer.apple.com/design/human-interface-guidelines/notifications#Content)
- **Don't put your app name or icon in the text; use a specific title or let the system show the app name.** [HIG](https://developer.apple.com/design/human-interface-guidelines/notifications#Content)
- **Up to four actions that save opening the app, each with a short title-case label and an SF Symbol; no "Open app" action; prefer nondestructive.** `UNNotificationAction(icon:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/notifications#Notification-actions)
- **Badges count unread notifications only; clear them promptly and never fake a badge in your UI.** `UNUserNotificationCenter.setBadgeCount(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/notifications#Badging)
- **watchOS: always ship a static long look, ideally a dynamic one too; order actions with the most common nondestructive first because double tap runs it.** [HIG](https://developer.apple.com/design/human-interface-guidelines/notifications#Double-tap)

## App Shortcuts

Use for: your most common tasks, available from install with no setup; up to 10 per app. Not for: generic domains covered by app schemas (adopt those for Apple Intelligence and Siri, 2026).

- **Check app schemas first; use App Shortcuts for features schemas don't cover (June 2026).** [HIG](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts#Best-practices)
- **Short spoken phrases containing the app name, at most one parameter with predictable values; ask for missing info in a follow-up.** `AppShortcutPhrase` [HIG](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts#Editorial-guidelines)
- **Put all critical info in the full dialog text for audio-only devices.** `IntentDialog(full:supporting:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts#Responding-to-App-Shortcuts)
- **Teach shortcuts in context with occasional tips; order them by importance.** `SiriTipView`, `ShortcutsLink` [HIG](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts#iOS-iPadOS)
- **Write "App Shortcuts" and "Shortcuts" in title case, plural; a person's "shortcut" in lowercase.** [HIG](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts#Editorial-guidelines)

Platforms: macOS has no App Shortcuts, but your App Intents appear in Shortcuts on Mac; not on tvOS.

## Snippets (new June 2026)

Compact custom view shown after an intent runs from Siri, Spotlight or Shortcuts: a *confirmation* snippet (system Cancel + primary button) and/or a *result* snippet (system Done).

- **Keep custom views ≤ 400 pt tall at every text size; deep-link for more detail.** [HIG](https://developer.apple.com/design/human-interface-guidelines/snippets#Best-practices)
- **Label the primary button with the action ("Order"), not OK/Proceed; the default is Continue.** `ConfirmationActionName` [HIG](https://developer.apple.com/design/human-interface-guidelines/snippets#Best-practices)
- **Make the view self-explanatory without the spoken dialog, and check contrast on the system background in light and dark.** [HIG](https://developer.apple.com/design/human-interface-guidelines/snippets#Best-practices)

API: `SnippetIntent` (iOS 26+, macOS 26+), `.result(view:)`. Not on tvOS, visionOS, watchOS.

## Complications (watchOS)

- **Show live, essential data; support every family you can, with several complications per family and a distinct deep link each.** Fall back to an app image where no data fits. [HIG](https://developer.apple.com/design/human-interface-guidelines/complications#Best-practices)
- **Look right in tinted mode (don't rely on color; supply tinted image variants) and use lines ≥ 2 pt.** `WidgetRenderingMode`, `.widgetAccentable()` [HIG](https://developer.apple.com/design/human-interface-guidelines/complications#Visual-design)
- **Choose gauge style by data: closed for percent-of-whole, open or segmented for arbitrary ranges.** [HIG](https://developer.apple.com/design/human-interface-guidelines/complications#Visual-design)
- **Plan timeline entries carefully (update budget is limited) and provide placeholders; mind Always On privacy.** [HIG](https://developer.apple.com/design/human-interface-guidelines/complications#Best-practices)

API: WidgetKit accessory families (watchOS 9+); ClockKit only for older watchOS. Rectangular complications can appear in the Smart Stack. Sizes: fetch the page's tables.

## Watch faces

Share preconfigured faces featuring your complications; provide a preview image for each, offer variants for older devices, and on incompatibility offer an alternative face instead of an error. ClockKit `CLKWatchFaceLibrary`. watchOS only. [HIG](https://developer.apple.com/design/human-interface-guidelines/watch-faces#Best-practices)

## Top Shelf (tvOS)

Feature new or personalized content with Play / More Info, not ads, prices, or already-watched items; prefer dynamic layouts (carousel actions/details, sectioned row with enough items to fill the width, 3–8 inset banners with text baked in and in the accessibility label); always ship a 2320×720 pt static fallback that doesn't look focusable. `TVTopShelfContentProvider`. [HIG](https://developer.apple.com/design/human-interface-guidelines/top-shelf#Best-practices)

## Status bars (iOS, iPadOS)

Keep it legible over content with a scroll edge effect, not a custom blur; hide it only temporarily for full-screen media and restore it with a simple tap; never hide it permanently. `.scrollEdgeEffectStyle(_:for:)` (iOS 26+), `.statusBarHidden(_:)`; UIKit `preferredStatusBarStyle`. [HIG](https://developer.apple.com/design/human-interface-guidelines/status-bars#Best-practices)
