# watchOS

Sources: [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos), [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)

## What people expect
- A glance on a raised wrist, under a foot away, one hand operating, often while moving; interactions under a minute. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)
- Always On: the watch face still shows information with the wrist down.
- **People use complications, notifications, and Siri more than the app itself.** Design those first.
- **The app works on its own;** it must not need the iPhone app open.
- **Proactive, personal content:** what matters now or very soon, from on-device data. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos#Best-practices)

## Navigation and structure
- **Shallow hierarchy.** Single-screen tasks done in a tap or two; `NavigationStack` only a level or two deep.
- **Vertical pages driven by the Crown:** `TabView` + `.tabViewStyle(.verticalPage)`; page indicator appears next to the Crown. [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#watchOS)
- **List/detail shows one full-screen view at a time;** open on the most relevant detail (location, time, recent activity).
- **Place toolbar buttons at the top leading/trailing corners or in a bottom bar** (`.topBarLeading`, `.topBarTrailing`, `.bottomBar`); a related but non-primary action (New Message in Inbox) can sit as a scrolling button at the top of the list (`.primaryAction`). [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#watchOS)
- **At most three icon buttons or two short text buttons in a row;** full-width text buttons are usually better. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#watchOS)
- **Background color and materials carry meaning and place** (`.containerBackground(_:for:)`).
- **Autorotate only views people show to someone else** (an image, a QR code).

## Inputs
### Digital Crown
- **Anchor navigation to the Crown:** lists, vertical tabs, and scroll views all scroll with it; give each a touch equivalent. [HIG](https://developer.apple.com/design/human-interface-guidelines/digital-crown#Apple-Watch)
- **Apps never receive Crown presses;** the system owns them.
- **Where nothing needs scrolling, use the Crown to inspect data** (World Clock scrubs time); SwiftUI `.digitalCrownRotation(_:)`.
- **Always show visible feedback for rotation, matched to rotation speed.**
- **Keep the default detent haptics unless they fight your animation;** use linear detents for lists with very uneven row heights.

### Touch and double tap
- **Tap, swipe, drag;** the edge swipe is a system gesture, don't claim it. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Custom-gestures)
- **Double tap (watchOS 11+) scrolls lists and advances vertical tabs by default.** Assign a primary action with `.handGestureShortcut(.primaryAction)` only in non-scrolling views, on the most-used control (play/pause). [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Double-tap)
- In notifications, double tap runs the first nondestructive action; order actions accordingly.

### Action button (Apple Watch Ultra)
- **First press starts the person's chosen workout, dive, or waypoint** through your App Shortcut; label it verb-first in three words or fewer. [HIG](https://developer.apple.com/design/human-interface-guidelines/action-button#watchOS)
- **Later presses advance the activity** (next segment, next modality), usable without looking; at most one secondary function.
- **Don't stop a workout with the button;** put Stop in the UI.
- **Action + side button together pauses,** except in a dive app where pausing is unsafe.

## System integrations
- Complications on watch faces, Smart Stack widgets (relevance-driven), actionable notifications, Always On states, Live Activities in the Smart Stack, Siri and Shortcuts, workouts and sensor data (heart, blood oxygen, altimeter, GPS). [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)
- No game controllers and no physical keyboard; games use touch and the Crown. Minimum text 12 pt (default 16), buttons 44×44 pt default, 28×28 minimum. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Look-stunning-on-every-display)
- No multitasking model; but expect frequent short sessions, so restore state instantly.

## Porting checklist (iPhone → Apple Watch)
- [ ] Pick the two or three tasks people do in seconds; drop the rest.
- [ ] Complication and Smart Stack widget for the key number or status.
- [ ] Notifications that carry the info and the action, so the app needn't open.
- [ ] Tab bars → vertical page `TabView`; deep stacks → one level.
- [ ] Every scrolling surface works with the Crown and with touch.
- [ ] Double tap: primary action only in non-scrolling views.
- [ ] No text-heavy forms; dictation or presets instead.
- [ ] Runs independently of the iPhone.
