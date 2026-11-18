# tvOS

Sources: [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos), [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection), [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls), [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)

## What people expect
- A very large screen seen from 8 feet or more, sometimes while walking around the room; long, immersive sessions, often with Picture in Picture alongside. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)
- **Cinematic presentation:** edge-to-edge artwork, subtle fluid motion, rich audio, legible from across the room. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos#Best-practices)
- **A shared device:** rare, easy sign-in, shared sign-in handling, automatic profile switching when the viewer changes.
- Sizes for this distance: text default 29 pt, minimum 23 pt; buttons 66×66 pt default, 56×56 minimum. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Look-stunning-on-every-display)

## Navigation and structure
- **Tab bar at the top** (fixed 68 pt tall, 46 pt from the top); it scrolls away with single-view tabs and stays pinned over split views; focus returns to it when people press Back/Menu. Avoid so many tabs that it fades and scrolls. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#tvOS)
- **Live-viewing apps order tabs:** live, recorded (cloud DVR), other.
- **Split views for filtering:** categories on the left third, results on the right two-thirds (or half and half), one title for the whole view. [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#tvOS)
- **Safe area: inset content 60 pt top and bottom, 80 pt left and right** for overscan. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#tvOS)
- **Grids with consistent spacing that leaves room for focused growth;** extra space for row titles; partially visible offscreen items equally wide on both sides.

## Focus
- **Every interactive element must be reachable by focus**, unlike iPad and Mac where only content needs it. [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#Best-practices)
- **Use the system focus effects** (lift, parallax); SwiftUI `.buttonStyle(.card)` for posters, `.focusable()` for custom views, `@FocusState` and `.defaultFocus` for initial focus, `.focusSection()` to guide directional movement between areas.
- **Design all five states:** unfocused, focused, highlighted (pressed), selected, unavailable. Supply art at the focused (larger) size, and space items so a focused one never covers its neighbors. [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#tvOS)
- **Don't move focus on your own,** except to a neighbor when the focused item disappears.
- **No pointer in menus and UI;** free-moving cursors only inside gameplay, and then highly visible.
- **Full-screen content shows no focus;** gestures there act on the content (scrubbing, panning), not on focus.

## Siri Remote
- **Swipe moves focus (or acts as a d-pad in games); press activates.** Swipes on the edge scroll fast. [HIG](https://developer.apple.com/design/human-interface-guidelines/remotes#Gestures)
- **Treat press as intent, tap as weak.** Resting a thumb, picking up, or passing the remote taps by accident; ignore taps during live video. Positional taps (up/down/left/right areas) only when discoverable. [HIG](https://developer.apple.com/design/human-interface-guidelines/remotes#Best-practices)
- **Back opens the parent in the app's hierarchy** (at the top level, the Home Screen), not simply the last screen. SwiftUI: `.onExitCommand`.
- **In gameplay, Back opens a pause menu;** Back again resumes. Leaving to the main menu takes a different action.
- **Play/Pause plays, pauses, resumes media** (`.onPlayPauseCommand`); in games it's the secondary button or skips the intro.
- **Press and hold Back always goes Home;** don't fight it.
- **EPG buttons on compatible remotes:** guide/browse opens your guide, page up/down pages it; during playback page up/down changes channel. [HIG](https://developer.apple.com/design/human-interface-guidelines/remotes#Compatible-remotes)
- **Custom remote gestures only in gameplay.**

## Other inputs
- Game controllers, keyboards, voice (Siri), and apps on people's other devices. Controller UI navigation: A activates, B goes back, shoulders switch sections, Menu pauses. [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Physical-controllers)
- A game may require a controller on tvOS (App Store badge), but must detect its absence and ask people to connect one.

## System integrations
- TV app integration, Top Shelf content, SharePlay, TV provider accounts (single sign-on), user profiles. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)
- Picture in Picture while browsing. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#tvOS)

## Porting checklist (iPhone/iPad → Apple TV)
- [ ] Replace touch layouts with focusable grids and shelves; verify every control is reachable by swiping.
- [ ] Bottom tab bar → top tab bar; detail screens as full-screen focusable layouts.
- [ ] Scale type and targets for 10-foot viewing; no dense lists or small text.
- [ ] Apply the 60/80 pt safe area; art edge to edge behind it.
- [ ] Focused-state art and spacing; system card/lift styles.
- [ ] Back, Play/Pause, and swipe behave as the tables above; no reliance on taps.
- [ ] Keep text entry minimal; make sign-in easy, infrequent, and shared across profiles.
- [ ] Top Shelf, TV app, and profile switching where relevant.
- [ ] No pointer, no hover-only UI, no touch gestures.
