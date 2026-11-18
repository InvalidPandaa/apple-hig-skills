# Presentation components

Sources: [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls), [Panels](https://developer.apple.com/design/human-interface-guidelines/panels), [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers), [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views), [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Windows](https://developer.apple.com/design/human-interface-guidelines/windows), [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)

Glass styling of sheets, popovers and bars is covered by the `hig-liquid-glass` skill; this file only covers when and how to present.

## Choosing between components in this group

Ask in order: did the person start this? Is it a choice, a task, or a warning? How much room and how long?

| Situation | Component | SwiftUI |
|---|---|---|
| Something unexpected happened, or an uncommon destructive action can't be undone; the person must decide now | Alert | `.alert(_:isPresented:actions:message:)` |
| The person just triggered an action and must pick between 2+ outcomes of it (Delete Draft / Save Draft), or confirm a destructive choice | Confirmation dialog (action sheet) | `.confirmationDialog(_:isPresented:titleVisibility:actions:message:)` |
| Short, scoped task tied to the current context (fill a form, pick a file, compose), then back to the parent | Sheet | `.sheet(item:)` + `.presentationDetents` |
| A few controls or facts tied to one button or region, regular width only | Popover | `.popover(isPresented:attachmentAnchor:arrowEdge:)` |
| Immersive media, camera, or a long multistep edit on iPhone/iPad | Full-screen modal | `.fullScreenCover(isPresented:)` |
| Self-contained task people want next to other content (compose, a document, a detail) on iPad, Mac, Vision Pro | New window | `WindowGroup(for:)` + `openWindow` |
| Mac: controls that adjust the selection while people keep working (inspector, Fonts, find/replace) | Panel or inspector | `UtilityWindow` (macOS 15+), `.inspector(isPresented:)` |
| Pure information, nothing to decide | No modal: inline status or indicator | Label, banner row, toolbar status |
| Common destructive action that can be undone (delete a mail, a file) | No confirmation: just do it and offer Undo | `UndoManager` |

Tie-breakers:
- **Alert vs. confirmation dialog:** the alert is for news the person didn't ask for; the dialog clarifies an action they chose. If there is more than "do it / cancel", it is a dialog.
- **Confirmation dialog vs. menu:** a dialog appears *because of* an action; a menu appears because the person asked to see options. Choices offered up front belong in a `Menu`.
- **Sheet vs. full-screen cover:** sheets keep the parent visible and are swipe-dismissible; use full screen only when the parent context would distract.
- **Sheet vs. window (iPad/Mac/visionOS):** if people would want to look at the parent while doing the task, or keep several open, use a window.
- **Popover vs. sheet:** popovers don't fit compact width; SwiftUI turns them into sheets there. Never put a warning in a popover.
- **Sheet vs. panel (Mac):** if people enter input repeatedly and watch the result each time, use a panel.

## Alerts

Use for: critical problems, confirming an uncommon, irreversible action, a purchase the person started. Not for: information only (use inline status), choices about an action the person chose (confirmation dialog). Errors go in alerts, never in notifications.

- **Don't confirm common, undoable deletions.** Delete immediately and provide Undo; reserve the alert for rare actions that can't be reversed. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Best-practices)
- **Never show an alert at launch.** Show cached data plus a quiet offline label instead of a "No connection" alert. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Best-practices)
- **Title states what happened and why; never "Error" or an error code.** Keep it to two lines; add a message only when it adds something. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Content)
- **Name buttons after their result ("Erase", "Convert"); "OK" only for purely informational alerts, and always "Cancel" for cancel.** Max three buttons. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons)
- **Apply the destructive style only when the destructive outcome is not what the person deliberately asked for.** When they chose "Empty Trash", the confirm button stays default style so Return works. `Button(role: .destructive)` [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons)
- **Never make Cancel the default button.** To force reading, give the alert no default button; a single-button alert uses "Done", not "Cancel". `Button(role: .cancel)` [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons)
- **Add a text field only when the input resolves the situation** (e.g. a password). Put `TextField`/`SecureField` in the `actions` closure. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Content)
- **macOS: use the caution symbol rarely; offer a suppression checkbox for repeating alerts.** `.dialogIcon(_:)`, `.dialogSuppressionToggle(isSuppressed:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#macOS)

SwiftUI: `.alert(_:isPresented:actions:message:)`, `.alert(_:isPresented:presenting:actions:)`. UIKit `UIAlertController(.alert)`, AppKit `NSAlert`.
Platforms: macOS and visionOS alerts can carry an icon and accessory view (visionOS accessory ≤ 154 pt tall, 16 pt corner radius); visionOS anchors the alert to its window.

## Action sheets (confirmation dialogs)

Use for: choices that follow an action the person started, including "discard changes?" when dismissing a sheet. Not for: unexpected problems (alert), options people open on purpose (menu, pull-down button).

- **Put destructive choices first and mark them destructive; Cancel goes last.** SwiftUI adds Cancel automatically. `Button(role: .destructive)` [HIG](https://developer.apple.com/design/human-interface-guidelines/action-sheets#Best-practices)
- **Keep the title to one line and skip the message unless needed.** `titleVisibility: .visible` only when the context doesn't already explain the choice. [HIG](https://developer.apple.com/design/human-interface-guidelines/action-sheets#Best-practices)
- **Never let it scroll.** Too many buttons means it should be a list, menu, or sheet. [HIG](https://developer.apple.com/design/human-interface-guidelines/action-sheets#iOS-iPadOS)
- **Attach the modifier to the control that triggers it.** In regular width iOS shows the dialog as a popover pointing at that control, dismissed by tapping outside (per the `confirmationDialog` docs). [HIG](https://developer.apple.com/design/human-interface-guidelines/action-sheets#iOS-iPadOS)
- **watchOS: at most four buttons including Cancel.** [HIG](https://developer.apple.com/design/human-interface-guidelines/action-sheets#watchOS)

SwiftUI: `.confirmationDialog(...)`. UIKit `UIAlertController(preferredStyle: .actionSheet)` (needs a `popoverPresentationController` source on iPad).
Platforms: not supported in visionOS (use an alert or menu there).

## Sheets

Use for: a scoped task related to the current view. Not for: long or complex flows (full-screen cover, or a window on iPad/Mac), navigation through the app, warnings (alert), supplementary controls on Mac (panel/inspector).

- **Single-view sheet: Cancel leading and Done trailing in the sheet's top toolbar (March 2026).** `ToolbarItem(placement: .cancellationAction)` / `.confirmationAction`; with iOS 26+ use `Button(role: .cancel)` / `Button(role: .confirm)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#iOS-iPadOS)
- **Multistep sheet (March 2026): step 1 shows Cancel + disabled Done; later steps replace Cancel with Back; Done enables only on the final step.** Never show Cancel, Back and Done at once. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#iOS-iPadOS)
- **Never show Done alone.** Pair it with Cancel (discard) or Back (previous step) so finishing isn't the only exit. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices)
- **For a sheet with nothing to discard, use a Close button.** `Button(role: .close)` (iOS 26+) signals dismissal without losing progress, unlike `.cancel`. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Anatomy)
- **Keep swipe-to-dismiss; when there are unsaved changes, intercept it and offer a confirmation dialog.** `.interactiveDismissDisabled(hasChanges)` plus a dialog with Discard/Save (UIKit: `presentationControllerDidAttemptToDismiss`). [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#iOS-iPadOS)
- **One sheet at a time.** Close the first before presenting a second; never stack sheets on sheets. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices)
- **iPhone: consider the medium detent for progressive disclosure; show a grabber whenever the sheet resizes.** `.presentationDetents([.medium, .large])`, `.presentationDragIndicator(.visible)`; compose-style sheets stay full height. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#iOS-iPadOS)
- **iPad: prefer form or page sizing; Mac: open at a sensible size and let other app windows stay usable.** `.presentationSizing(.form)` / `.page`. [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#macOS)

SwiftUI: `.sheet(item:onDismiss:content:)` (prefer `item:` over `isPresented:` when the sheet shows a model), `.presentationDetents`, `.presentationSizing`. UIKit `UISheetPresentationController`, AppKit `presentAsSheet(_:)`.
Platforms: always modal on macOS, tvOS, visionOS, watchOS; iOS/iPadOS can be nonmodal (Notes formatting). visionOS: center in view, don't slide from the window bottom, don't cover the whole window. watchOS: full-screen; use only when you need a custom title or layout.

```swift
.sheet(item: $draft) { draft in
    NavigationStack {
        DraftForm(draft: draft)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) { Button("Cancel", role: .cancel) { dismiss() } }
                ToolbarItem(placement: .confirmationAction) { Button("Done", role: .confirm) { save() }.disabled(!isValid) }
            }
    }
    .interactiveDismissDisabled(hasChanges)
}
```

## Popovers

Use for: a few related controls or details anchored to a control, in regular width. Not for: warnings (alert), compact width (sheet), large content (sheet or window).

- **Don't use popovers in compact size classes.** SwiftUI adapts a popover to a sheet there; don't override that with `.presentationCompactAdaptation(.popover)` on iPhone. [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#iOS-iPadOS)
- **One popover at a time, never a popover from a popover, and nothing on top of it except an alert.** [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#Best-practices)
- **Save work when a nonmodal popover closes by tapping outside.** Discard only on an explicit Cancel. [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#Best-practices)
- **Point the arrow straight at the source and don't cover it.** `attachmentAnchor:` / `arrowEdge:`. [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#Best-practices)
- **Add Close/Cancel/Done only when it clarifies saving; keep it open while multiple selections are possible.** [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#Best-practices)
- **Animate size changes so it doesn't look like a new popover.** [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#Best-practices)
- **macOS: consider making it detachable into a panel that looks nearly the same.** [HIG](https://developer.apple.com/design/human-interface-guidelines/popovers#macOS)

SwiftUI: `.popover(isPresented:attachmentAnchor:arrowEdge:content:)`, `.popover(item:)`. UIKit `UIPopoverPresentationController`, AppKit `NSPopover`.
Platforms: not available in tvOS or watchOS.

## Full-screen modal (iOS, iPadOS)

Not a separate HIG page; the sheets and modality pages recommend it for video, photos, camera, and multistep editing. Always provide a visible dismiss button (no swipe-down by default) and confirm before discarding work. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
SwiftUI: `.fullScreenCover(isPresented:onDismiss:content:)` (iOS, iPadOS, tvOS, watchOS, visionOS; not macOS: use a window or full-screen mode there).

## Windows

Use for: primary navigation (primary window) and self-contained tasks (auxiliary window) on iPadOS, macOS, visionOS. Not for: iOS, tvOS, watchOS (no app windows there).

- **Don't open new windows by default; offer "Open in New Window" in a context menu or the File menu.** Open one automatically only when side-by-side is the point (Mail compose). `openWindow(value:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#Best-practices)
- **Never build custom window frames or controls.** Imperfect copies of system chrome make the app feel broken. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#Best-practices)
- **Say "window" in UI text, never "scene".** [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#Best-practices)
- **iPadOS (2025): layouts must work at any window size, and leading toolbar items must move inward when window controls appear.** [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS)
- **iPadOS: consider a pinch gesture to open an item in its own window.** [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS)
- **macOS: keep critical info and actions out of a bottom bar; use an inspector for more detail.** [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#macOS)
- **macOS: custom windows must still show main/key/inactive states.** System components do this for free. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#macOS-window-states)
- **visionOS: keep the glass background, set min/max sizes, start with a shape that fits the content (default 1280×720 pt), and use a volume for deep 3D content.** `.windowStyle(.volumetric)`, `.windowResizability(_:)`, `.defaultSize(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-windows)

SwiftUI: `WindowGroup`, `Window`, `WindowGroup(for:)`, `@Environment(\.openWindow)`. UIKit `UIWindowScene`, AppKit `NSWindow`.

## Panels (macOS)

Use for: inspectors and controls that act on the current selection while the main window stays usable. Not for: fixed-content Info windows (regular window), iOS/visionOS (use a sheet, nonmodal sheet, or split view).

- **Fill panels with direct controls (sliders, steppers), not typing or item selection.** [HIG](https://developer.apple.com/design/human-interface-guidelines/panels#Best-practices)
- **Give it a short noun title; menus say "Show Inspector", not "Show Inspector Panel".** [HIG](https://developer.apple.com/design/human-interface-guidelines/panels#Best-practices)
- **Hide panels when the app is inactive, bring them all back when it activates; keep them out of the Window menu's document list; no minimize button.** `UtilityWindow` handles most of this. [HIG](https://developer.apple.com/design/human-interface-guidelines/panels#Best-practices)
- **Default to standard panels; use a HUD only for media-centric apps, keep it small, and keep one style across modes.** `NSWindow.StyleMask.hudWindow` [HIG](https://developer.apple.com/design/human-interface-guidelines/panels#HUD-style-panels)

SwiftUI: `UtilityWindow` (macOS 15+), or `.inspector(isPresented:)` for a split-view inspector. AppKit `NSPanel`. Not available outside macOS.

## Scroll views

Use for: content larger than its container. Not for: page-by-page lists of peers without a paging behavior (add one).

- **Never nest scroll views with the same axis.** A horizontal carousel inside a vertical list is fine. [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Best-practices)
- **Hint at overflow by letting content peek at the edge.** [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Best-practices)
- **For paging use the system behavior, not a custom gesture.** `.scrollTargetBehavior(.paging)` or `.viewAligned`; pair with a page control and hide the same-axis indicator. [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#iOS-iPadOS)
- **Scroll automatically only as far as needed** to reveal a search hit, the insertion point, or a selection about to be acted on. `ScrollViewReader`, `.scrollPosition` [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Best-practices)
- **Use a scroll edge effect only under floating UI, one per view, and prefer the automatic style (iOS 26+, updated June 2026).** Test legibility thoroughly if you pick `.soft`; in split views keep pane effects the same height. `.scrollEdgeEffectStyle(.automatic, for: .top)`, `.scrollEdgeEffectHidden(_:for:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Scroll-edge-effects)
- **Set sensible min/max zoom.** [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Best-practices)
- **visionOS (March 2026): opt reading and browsing views into Look to Scroll, not control-dense lists; remove parallax and scroll-driven effects first, and apply it consistently across similar views.** `.scrollInputBehavior(.enabled, for: .look)` (visionOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#Look-to-Scroll)
- **watchOS: prefer vertical scrolling driven by the Digital Crown; page with a vertical `TabView`.** [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views#watchOS)

SwiftUI: `ScrollView`, `List`, `.scrollTargetBehavior`, `.scrollEdgeEffectStyle(_:for:)`. UIKit `UIScrollView`, AppKit `NSScrollView`.
Platforms: tvOS scrolls by focus, no indicators; macOS can use small/mini scroll bars in panels; visionOS indicator is thicker, so widen tight margins.

## Page controls

Use for: a flat, ordered set of peer pages (Weather locations, onboarding). Not for: hierarchy or random access (sidebar, split view, grid), more than about 10 pages (grid).

- **Center it near the bottom.** [HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls#Best-practices)
- **Use at most two indicator images (default plus one special page) and don't color them.** [HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls#Customizing-indicators)
- **Don't animate page transitions while people scrub; animate only on tap.** [HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls#iOS-iPadOS)
- **Use the prominent background only when it's the screen's main navigation; don't allow scrubbing with the minimal style.** `UIPageControl.backgroundStyle`; SwiftUI `.indexViewStyle(.page(backgroundDisplayMode:))` [HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls#iOS-iPadOS)
- **watchOS: use vertical pagination with the Digital Crown, ideally one screen per page.** [HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls#watchOS)

SwiftUI: `TabView` + `.tabViewStyle(.page)`. UIKit `UIPageControl`.
Platforms: not on macOS; visionOS shows it but it isn't interactive; tvOS only for full-screen pages.
