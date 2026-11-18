# Feedback, status, haptics, notifications, undo

Sources: [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Loading](https://developer.apple.com/design/human-interface-guidelines/loading), [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators), [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics), [Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications), [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo), [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)

## Matching feedback to stakes

| What happened | Channel | Example |
|---|---|---|
| Ongoing status | Passive, next to the thing it describes | "Updated just now" under a toolbar title, unread badge |
| Routine success | Nothing, or the visible result itself | Row disappears after delete |
| Significant success | Brief confirmation | Payment complete |
| Failure or impossible command | Inline explanation with a next step | "Add a destination to get directions" |
| Unexpected, irreversible data loss | Interrupt: alert or confirmation dialog | Erasing a whole library |

- **Give feedback through more than one channel** (color plus text, sound plus haptic) so it survives silent mode, VoiceOver, and people looking away. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **Put status inside the interface near what it describes,** not in alerts. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **Keep alerts for critical, ideally actionable information;** frequent alerts stop being read. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **Don't warn when removing data is the whole point of the action.** Moving a file to the Trash doesn't ask. Warn only for loss that is both irreversible and surprising. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **Confirm completion only for important tasks;** people assume success and need to hear about failure. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **When a command can't run, say why.** [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)

## Loading and progress

- **Show something immediately.** A blank screen reads as a bug; render the real layout with placeholder content and swap in data as it arrives. [HIG](https://developer.apple.com/design/human-interface-guidelines/loading#Best-practices)
- **Keep the rest of the app usable while content loads in the background.** [HIG](https://developer.apple.com/design/human-interface-guidelines/loading#Best-practices)
- **For unavoidable long waits, give people something worth looking at** (tips, hints) sized to the expected wait. [HIG](https://developer.apple.com/design/human-interface-guidelines/loading#Best-practices)
- **Download large assets after install or at quiet times** with Background Assets instead of at first launch. [HIG](https://developer.apple.com/design/human-interface-guidelines/loading#Best-practices)
- **Prefer determinate progress** (`ProgressView(value:total:)`), keep it moving at an even, honest pace, and switch indeterminate to determinate once the duration is known. Never switch between spinner and bar. [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Label progress with specifics, not "Loading" or "Authenticating".** [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Offer Cancel when stopping is harmless; add Pause when cancelling would lose work,** and confirm a cancel that discards progress. [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **Refresh automatically;** pull-to-refresh (`.refreshable`) is an extra, not the only way data updates. [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Refresh-content-controls)
- **macOS: a small unlabeled spinner fits background work and tight spaces.** [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#macOS)
- **watchOS: avoid loading indicators;** show content right away, and for longer work promise a notification. A spinner still beats a blank screen for a second or two. [HIG](https://developer.apple.com/design/human-interface-guidelines/loading#watchOS)
- **Games may use a custom loading view** that matches the game's style. [HIG](https://developer.apple.com/design/human-interface-guidelines/loading#Showing-progress)

### Placeholder vs spinner

| Situation | Use |
|---|---|
| Layout is known, data isn't yet (lists, cards, profiles) | Real views with sample data + `.redacted(reason: .placeholder)` |
| Known duration or byte count (download, export) | `ProgressView(value:total:)` with a specific label |
| Unknown duration, nothing meaningful to lay out | `ProgressView()` spinner, centered, short |
| Small inline background task (Mac field, button) | Small spinner, no label |
| Content partially loaded | Show what's there; spinner only on the missing part |

## Empty and unavailable states

No dedicated HIG page exists; the rules follow from the feedback guidance on explaining why something can't happen and the ML guidance to suggest alternatives instead of showing nothing. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices), [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Limitations)

- **Use `ContentUnavailableView` for empty lists, no search results, missing permissions, and offline states.** Include what's missing, why, and the next action (create, retry, open Settings).
- **Use `ContentUnavailableView.search` inside a `.searchable` hierarchy;** it inserts the query into the message.
- **Don't show an empty state while still loading.** Loading → placeholders; loaded and empty → empty state; failed → error state with Retry.

```swift
List(items ?? Item.samples) { ItemRow(item: $0) }
    .redacted(reason: items == nil ? .placeholder : [])
    .overlay {
        if items?.isEmpty == true {
            ContentUnavailableView {
                Label("No Trips", systemImage: "airplane")
            } description: { Text("Trips you plan appear here.") }
              actions: { Button("Plan a Trip") { showNewTrip = true } }
        }
    }
```

## Haptics

- **Use system patterns only for their documented meaning.** Success means success; don't reuse it for "level failed". [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)
- **Keep one haptic per cause, consistently, and in sync with the matching animation or sound.** [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)
- **Use haptics sparingly and keep them short in non-game apps;** long or constant buzzing dilutes meaning (especially on Apple Pencil Pro). [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)
- **Never depend on haptics alone,** and avoid vibration while the camera, gyroscope, or microphone is in use. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)
- **Standard controls (toggles, sliders, pickers) already play haptics;** don't add another on top. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#iOS)
- **Make custom haptics mutable** (games, Core Haptics); for standard feedback the systemwide setting already applies. [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)

| Meaning | SwiftUI `.sensoryFeedback(_:trigger:)` |
|---|---|
| Outcome of a task | `.success`, `.warning`, `.error` |
| Value changing in a picker-like control | `.selection` |
| Physical contact, snap into place | `.impact(weight:intensity:)` |
| Value crossed a threshold up/down | `.increase`, `.decrease` |
| Activity started/stopped (timer) | `.start`, `.stop` |
| Mac trackpad: aligned / pressure level | `.alignment`, `.levelChange` |

## Notifications

- **Request notification permission in context,** after people do something that makes alerts useful (follow a team, start a delivery), not at launch. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications), [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission)
- **Set an honest interruption level** (`UNNotificationInterruptionLevel`): [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Integrating-with-Focus)

| Level | Use for | Breaks Focus / summary | Overrides silent switch |
|---|---|---|---|
| `.passive` | Browse-later info | No | No |
| `.active` (default) | Nice to know now | No | No |
| `.timeSensitive` | Affects the person now or within an hour | Yes | No |
| `.critical` | Health and safety; needs an entitlement | Yes | Yes |

- **Never send marketing as Time Sensitive.** [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Sending-marketing-notifications)
- **Marketing needs its own explicit opt-in screen and an in-app setting to change it.** [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Sending-marketing-notifications)
- **Messaging and calls use communication notifications** (SiriKit `INSendMessageIntent`) so Focus can filter by sender. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Integrating-with-Focus)
- **Notify when an important task the person started finishes in the background;** skip routine completions. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)

## Undo and redo

- **Prefer undo to confirmation for anything reversible.** It lets people explore safely. [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)
- **Name the action** so the result is predictable: menu "Undo Typing", shake alert "Undo Name" (the system adds "Undo "/"Redo "; you supply one or two words via `setActionName`). [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Best-practices)
- **Show what undo changed,** scrolling to or highlighting off-screen content. [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Best-practices)
- **Don't cap undo depth;** people expect to go back to the last open or save. Group related tweaks (one slider drag = one undo) and consider a "revert all". [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Best-practices)
- **Use the system triggers:** Edit menu top items with Command-Z / Shift-Command-Z on Mac; shake and three-finger swipe on iPhone/iPad (never redefine them). Toolbar undo/redo buttons, with system symbols, only when the app needs them visible (drawing, editing). [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Platform-considerations)
- **Not available on tvOS or watchOS.** [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Platform-considerations)
- **Make drag and drop undoable;** confirm first only when a drop can't be undone. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Best-practices)

SwiftData gives undo for free with `.modelContainer(for: Item.self, isUndoEnabled: true)`. Manual registration:

```swift
@Environment(\.undoManager) private var undoManager
func delete(_ item: Item) {
    guard let i = store.items.firstIndex(of: item) else { return }
    store.items.remove(at: i)
    undoManager?.registerUndo(withTarget: store) { store in
        store.items.insert(item, at: i)   // register the inverse here to support redo
    }
    undoManager?.setActionName("Delete \(item.title)")
}
```
