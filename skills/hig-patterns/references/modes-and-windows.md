# Modality, full screen, multitasking, audio, video, live TV, workouts

Sources: [Modality](https://developer.apple.com/design/human-interface-guidelines/modality), [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio), [Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video), [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps), [Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts)

## Modality

### Choosing a presentation

| Need | Use (SwiftUI) |
|---|---|
| Critical info that needs a decision | `.alert` (one at a time, ever) |
| Choose among actions related to what was just tapped, incl. destructive | `.confirmationDialog` |
| Short, scoped task (compose, add item, edit details) | `.sheet`, with `.presentationDetents` if partial height helps |
| Immersive or multistep task (photo editing, camera, video) | `.fullScreenCover` (iOS); a separate window on iPadOS/macOS/visionOS |
| Supplementary controls while the main view stays usable | Nonmodal: inspector, popover, panel (Mac), split view; nonmodal sheet on iOS |
| Self-contained document task on Mac | New window rather than a sheet |

### Rules
- **Use a modal only when focusing or deciding is the point;** it pulls people out of context and demands a dismissal. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Keep modal tasks short and linear.** No app-within-an-app: if subviews are needed, one path through them and nothing that looks like the dismiss button. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Title the modal with its task** so people remember why they're there. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Make the exit obvious and platform-standard:** a top toolbar button or swipe-down on iOS, iPadOS, watchOS; a button in the content on macOS and tvOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Guard only real loss.** If dismissing (button or swipe) would drop user-created content, explain and offer Save / Discard / Keep Editing. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Never stack modals.** Close the first before showing the next; reopen the first afterward if needed. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices), [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices)
- **Give Done a companion:** Cancel (discard) or Back (previous step), never Cancel, Done, and Back together. Sheet button placement guidance was updated in March 2026; fetch `sheets` before laying out sheet toolbars. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices)
- **SwiftUI roles (iOS 26+):** `Button(role: .close)` for leaving without losing anything, `Button(role: .cancel)` for abandoning changes, `Button(role: .confirm)` for committing. The label-less `Button(role:action:)` init (iOS 26+) supplies the standard symbol, e.g. an x for cancel.

```swift
NavigationStack {
    EditorForm(draft: $draft)
        .navigationTitle("New Event")
        .toolbar {
            ToolbarItem(placement: .cancellationAction) { Button(role: .cancel) { attemptDismiss() } }
            ToolbarItem(placement: .confirmationAction) { Button(role: .confirm) { save() } }
        }
}
.interactiveDismissDisabled(draft.hasChanges)   // swipe can't silently drop edits
.confirmationDialog("Discard this event?", isPresented: $askDiscard) {
    Button("Discard Changes", role: .destructive) { dismiss() }
}
```

## Going full screen

- **Offer full screen for games, media, slideshows, and deep focused work.** [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#Best-practices)
- **Adapt the layout to the extra space, but never resize the window yourself;** keep the same items, adjust proportions subtly. [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#Best-practices)
- **Keep essential controls reachable** (playback controls always visible or one tap away). [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#Best-practices)
- **Hide bars for content-first views, and bring them back with a familiar tap, swipe down, or pointer at the top edge** (`.toolbarVisibility(.hidden, for:)`, `.persistentSystemOverlays(.hidden)`). Keep controls that navigation depends on. [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#Best-practices)
- **Leave the Dock reachable in iPadOS and macOS, except in games.** [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#Best-practices)
- **Pause on switch-away and resume where people left off; let people decide when to exit.** [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#Best-practices)
- **iOS games with accidental exits: defer the Home indicator gesture to two swipes** (`.defersSystemGestures(on: .bottom)`), otherwise keep the default single swipe. [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#iOS-iPadOS)
- **macOS: use the system full-screen mode** (handles the camera housing); entry via the window button, View menu, or Control-Command-F, no custom window-mode menu; games don't change display mode. [HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen#macOS)
- Not applicable to tvOS, visionOS, watchOS.

## Multitasking and backgrounding

- **Assume interruption at any moment;** save and restore context continuously. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- **Pause what needs attention (games, media playback) when people leave,** and resume seamlessly. Watch `@Environment(\.scenePhase)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- **Finish user-started work in the background** (downloads, exports). iOS 26+: `BGContinuedProcessingTaskRequest` lets a foreground-started task keep running, with system-shown progress the person can cancel. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- **Notify only for important completions** the person is waiting on. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- **iPadOS: expect free-form resizable windows and full-screen apps;** the app gets no signal about the arrangement, so layout must adapt to any size. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#iPadOS)
- **visionOS: don't pause a window's video when people look away, don't restyle window edges, and expect audio ducking** when not the Now Playing app. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#visionOS)

## Playing audio

- **Pick the audio session category by intent:** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#Best-practices)

| Category | For | Silent switch | Mixes | Background |
|---|---|---|---|---|
| `.soloAmbient` (default) | Game with its own soundtrack | Silences | No | No |
| `.ambient` | Sound effects, people's own music may play | Silences | Yes | No |
| `.playback` | Podcasts, audiobooks, music, language lessons | Ignores | Optional | Yes |
| `.record` | Voice recorder | Ignores | No | Yes |
| `.playAndRecord` | Calls, voice messages | Ignores | Optional | Yes |

- **Never change system volume;** mix your own levels below it, and use `MPVolumeView` for an in-app volume and route control. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#Best-practices)
- **Allow rerouting (AirPlay, Bluetooth); pause immediately when headphones disconnect.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio)
- **Silent mode silences nonessential sound** (effects, keyboard clicks, game music); only explicitly started media plays. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio)
- **Respond to remote controls only when you're the audio context;** never repurpose them, and ignore ones you don't support. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#Best-practices)
- **Signal others to resume after temporary audio** (`.notifyOthersOnDeactivation`). [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#Best-practices)
- **Interruptions:** pause primary audio indefinitely, duck or pause briefly for short ones (navigation prompts); after a resumable interruption, media apps check `shouldResume` before restarting, games just resume. Never reopen a mic automatically after the iPad Smart Folio closes. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#Handling-interruptions), [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- **Never convey essential information with sound alone.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#visionOS)
- **visionOS: prefer playing sound; give custom elements custom sounds, use Spatial Audio, vary repeated sounds.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#visionOS)
- **watchOS: 64 kbps HE-AAC; consider the system Now Playing view.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-audio#watchOS)

## Playing video

- **Use the system player** (`VideoPlayer`, `AVPlayerViewController`); a custom player must behave like it, since near-identical but different controls frustrate. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Best-practices)
- **Keep the original aspect ratio, with no baked-in letterbox or pillarbox bars.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Best-practices)
- **Space plays and pauses everywhere a keyboard is attached.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Best-practices)
- **Avoid mixed audio when people switch between full screen and PiP** (handle secondary-audio hints). [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Best-practices)
- **From the TV app: black screen, then content immediately;** no splash or intro, resume automatically without asking, switch to the requested profile, resume long clips from the last position. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Integrating-with-the-TV-app)
- **Loading over 2 s: black screen with a centered spinner only, then start as soon as enough is buffered.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Loading-content)
- **On exit, show the detail view of what was playing with Resume.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#Exiting-playback)
- **tvOS: small, translucent overlays only; interactive overlays pause playback (wait at least 0.5 s) and dismiss clearly.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#tvOS)
- **visionOS: never auto-start fully immersive playback;** start in a small resizable window with surroundings visible, keep virtual content off the controls, supply 160 px wide thumbnails for scrubbing. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#visionOS)
- **watchOS: clips up to about 30 s, H.264, no scaling, a poster image that shows the content and doesn't look like a control.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video#watchOS)

## Live-viewing apps

- **Put live content first and one tap (or zero) from launch.** A Watch Now button disappears and goes full screen on tap. [HIG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#Best-practices)
- **Mark live items clearly** (a "Live" row, badge, progress through the program). [HIG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#Best-practices)
- **Playback is always the primary action;** secondary actions (Start Over, Record, Favorite) keep the same order everywhere. [HIG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#Best-practices)
- **Give instant feedback on channel changes;** stop audio when people leave the live tab. [HIG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#Best-practices)
- **EPG: open on now, browse without leaving playback (PiP), categories that match the content footer.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#EPG-experience)
- **Cloud DVR: record from the info panel, choose episode vs series, offer automatic storage cleanup.** [HIG](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps#Cloud-DVR)

## Workouts

- **watchOS: run a workout session** (`HKWorkoutSession`) so the app stays up between wrist raises, showing the metrics people care about and lap or interval controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
- **Strip everything else during a workout;** no catalog browsing mid-session. [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
- **Make an active session look distinct** (live-updating metrics page). [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
- **Large, easy pause/resume/stop controls with clear start and stop feedback** (`.start`/`.stop` haptics). [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
- **Explain missing sensor data in Workout-app-style language** (water and heart rate during swims). [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
- **End with a summary (optionally Activity rings); drop or ask about sessions only seconds long.** [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
- **Large, high-contrast text for reading in motion; Activity rings only for their documented meaning.** [HIG](https://developer.apple.com/design/human-interface-guidelines/workouts#Best-practices)
