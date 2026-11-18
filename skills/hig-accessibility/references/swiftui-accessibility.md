# SwiftUI accessibility cookbook

Sources: [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type), [Color](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color), [Motion](https://developer.apple.com/design/human-interface-guidelines/motion#Best-practices). API index: `/documentation/swiftui/view-accessibility`.

Standard controls already carry correct traits, values, adjust gestures, and focus. This file is for going custom.

## Labels, values, hints

| Property | Answers | Example |
|---|---|---|
| Label | What is it? | "Favorite", "Volume", "Kim Lee, 3 unread" |
| Value | What state or amount? | "On", "60 percent", "4 of 5 stars" |
| Hint | What happens if I activate it? (optional, people can turn hints off) | "Adds the song to your library." |
| Traits | What kind of thing? | `.isButton`, `.isHeader`, `.isSelected`, `.isToggle` |

- Label: short, capitalized, no type word ("button"), no period, localized. Hint: third-person verb,
  the result, not the gesture ("Opens the message", not "Double tap to open").
- Prefer a visible title and let SwiftUI derive the label. An icon-only button still gets its
  label from the title:

```swift
Button("Delete Draft", systemImage: "trash") { delete() }
    .labelStyle(.iconOnly)          // shows the icon, VoiceOver says "Delete Draft, button"

Image(systemName: "bolt.fill")
    .accessibilityLabel("Fast charging")   // meaningful standalone image

Image(decorative: "hero-wave")             // decorative: not an element at all
```

- Images with text inside need that text in the label. For Voice Control, keep the visible word first
  and add alternatives, most important first: `.accessibilityInputLabels(["Compose", "New message"])`.

## Toggled state

Keep the label constant, put state in traits or value. Change the label only when the action changes (Play/Pause).

```swift
// Best: a real Toggle with a custom look
Toggle("Favorite", isOn: $isFavorite)
    .toggleStyle(StarToggleStyle())

// When it must stay a Button
Button { isFavorite.toggle() } label: {
    Image(systemName: isFavorite ? "star.fill" : "star")
}
.accessibilityLabel("Favorite")
.accessibilityAddTraits(.isToggle)           // iOS 17+; announced as a toggle
.accessibilityValue(isFavorite ? "On" : "Off")
```

For a selected chip or segment in a custom picker, use `.accessibilityAddTraits(isChosen ? .isSelected : [])`.

## Custom controls: give them real semantics

`accessibilityRepresentation` replaces the accessibility tree of a custom view with a standard
control, so traits, value, and adjust gestures come for free.

```swift
RatingStars(value: $rating)                      // custom drawing, custom gesture
    .accessibilityRepresentation {
        Stepper("Rating", value: $rating, in: 1...5)
            .accessibilityValue("\(rating) of 5 stars")
    }

CircularDial(level: $level)
    .accessibilityRepresentation {
        Slider(value: $level, in: 0...100) { Text("Volume") }
    }
```

Without a representation, build an adjustable element by hand:

```swift
SegmentedMeter(level: level)
    .accessibilityElement()
    .accessibilityLabel("Brightness")
    .accessibilityValue("\(level) percent")
    .accessibilityAdjustableAction { direction in
        switch direction {
        case .increment: level = min(level + 10, 100)
        case .decrement: level = max(level - 10, 0)
        @unknown default: break
        }
    }
```

- Never build a control from `onTapGesture` on a shape (no button trait, skipped by keyboard and
  switch users). Use `Button` with a custom `ButtonStyle`.
- Gesture-driven canvases (drawing, rotation, piano keys): `.accessibilityDirectTouch(options:
  .requiresActivation)` (iOS 17+) passes touches through to the view while VoiceOver is on.
  Pinch-to-zoom also needs `.accessibilityZoomAction`; scrolling content `.accessibilityScrollAction`.

## Grouping, order, and custom actions

```swift
HStack {
    AsyncImage(url: avatarURL)
    VStack(alignment: .leading) {
        Text(name).font(.headline)
        Text(preview).font(.subheadline)
    }
    Text(time).font(.caption)
}
.accessibilityElement(children: .combine)        // one stop: "Kim Lee, See you at 6, 9:41 AM"
.accessibilityAction(named: "Reply") { reply() }
.accessibilityAction(named: "Archive") { archive() }
```

| Mode | Use when |
|---|---|
| `.combine` | The parts read naturally in order; SwiftUI joins child labels |
| `.ignore` + own `accessibilityLabel` | You need a different order or wording; you must supply the label |
| `.contain` | A container whose children stay separate but belong together (e.g. a card with its own heading) |

- Named actions save swipes per row; `swipeActions` already appear in the Actions rotor.
- Reorder without changing layout: `.accessibilitySortPriority(1)` (higher reads first).
- Link a label to its control when they are separate views: `accessibilityLabeledPair(role:id:in:)`.
- Extra details read on demand ("More content" rotor): `.accessibilityCustomContent("Rating", "4.5")`.
- For several unrelated actions, group them: `.accessibilityActions(category:_:)` (iOS 18+).

## Headings, titles, rotors

```swift
Text("Upcoming").font(.title2).accessibilityAddTraits(.isHeader)
Text("Chapter 2").accessibilityHeading(.h2)        // levels for long documents

ScrollView { ForEach(messages) { MessageRow($0) } }
    .accessibilityRotor("Unread") {
        ForEach(messages.filter(\.isUnread)) { m in
            AccessibilityRotorEntry(m.sender, id: m.id)
        }
    }
```

- Every screen gets a unique `navigationTitle`. Rotors fit unread items, form errors, links, search
  matches (`accessibilityRotor(_:textRanges:)` for text).

## Announcements and focus

```swift
@AccessibilityFocusState private var errorFocused: Bool

TextField("Email", text: $email)
if let error { Text(error).accessibilityFocused($errorFocused) }

func submit() {
    if !isValid { error = "Enter a valid email address."; errorFocused = true }
    else { AccessibilityNotification.Announcement("Account created").post() }   // iOS 17+
}
```

- Move focus for new primary content; announce when content changes but focus should stay.
- Set where VoiceOver lands first on a screen: `.accessibilityDefaultFocus($focus, .title)` (iOS 26+).
- Describe scroll position in long, paged content: `.accessibilityScrollStatus("March 2026")` (iOS 26+).
- Keyboard (Full Keyboard Access, iPad and Mac keyboards): custom controls need `.focusable()`, key
  handling via `.onKeyPress` (iOS 17+), and visible focus (don't blanket `.focusEffectDisabled()`).
  Use `@FocusState` for text-field flow and `.keyboardShortcut` for commands, without overriding
  system shortcuts.

## Dynamic Type and reflow

```swift
struct EventRow: View {
    @Environment(\.dynamicTypeSize) private var size
    @ScaledMetric(relativeTo: .body) private var iconSide = 28.0

    var body: some View {
        let layout = size.isAccessibilitySize
            ? AnyLayout(VStackLayout(alignment: .leading, spacing: 4))
            : AnyLayout(HStackLayout(spacing: 12))
        layout {
            Image(systemName: "calendar").frame(width: iconSide, height: iconSide)
            Text(event.title).font(.body)              // primary stays first
            Text(event.time).font(.caption).foregroundStyle(.secondary)
        }
    }
}
```

- `ViewThatFits { HStack {...}; VStack {...} }` picks the first layout that fits, without size checks.
- No fixed heights around text (use `minHeight`); allow wrapping (`.lineLimit(nil)`), no
  `.minimumScaleFactor` on body text; derive grid column count from `size`.
- Custom fonts: `.font(.custom("Brand", size: 17, relativeTo: .body))` scales; `.custom(_:fixedSize:)` does not.
- Cap only chrome: `.dynamicTypeSize(...DynamicTypeSize.accessibility2)` on a custom bar, plus `.accessibilityShowsLargeContentViewer()`.

## Display and motion settings

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion
@Environment(\.accessibilityReduceTransparency) private var reduceTransparency
@Environment(\.colorSchemeContrast) private var contrast             // .increased
@Environment(\.accessibilityDifferentiateWithoutColor) private var noColorOnly

panel
    .transition(reduceMotion ? .opacity : .move(edge: .bottom))
    .background(reduceTransparency ? AnyShapeStyle(.background) : AnyShapeStyle(.ultraThinMaterial))
    .overlay { if contrast == .increased { RoundedRectangle(cornerRadius: 12).stroke(.primary) } }
```

| Setting | Environment value | Respond by |
|---|---|---|
| Reduce Motion | `accessibilityReduceMotion` | Fades instead of slides, zooms, depth; no parallax or autoplay loops; tighter springs |
| Reduce Transparency | `accessibilityReduceTransparency` | Opaque fills behind custom blur, glass, gradient scrims |
| Increase Contrast | `colorSchemeContrast == .increased` | High Contrast color variants in the asset catalog, stronger borders |
| Differentiate Without Color | `accessibilityDifferentiateWithoutColor` | Add shapes, symbols, patterns; do this by default for critical state |
| Button Shapes | `accessibilityShowButtonShapes` | Underline or outline custom borderless buttons |
| Bold Text | `legibilityWeight == .bold` | Heavier custom font weight |
| Invert Colors | `.accessibilityIgnoresInvertColors()` on photos and video | Keep media un-inverted |
| Dim Flashing Lights | `accessibilityDimFlashingLights` (iOS 17+) | Avoid or warn about strobing content |
| Animated images | `accessibilityPlayAnimatedImages` (iOS 17+) | Don't autoplay GIF-style images |
| VoiceOver / Switch Control on | `accessibilityVoiceOverEnabled`, `accessibilitySwitchControlEnabled` | Extend or remove timeouts; never change content or features |
| Assistive Access | `accessibilityAssistiveAccessEnabled` (iOS 18+) | Small adjustments; for a full alternate UI use the scene below |

Reduce Motion changes the kind of motion, not its speed: a faster slide is still a slide.

## Assistive Access (iOS 26+)

```swift
@main struct NotesApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
        AssistiveAccess { SimpleNotesView() }   // requires UISupportsAssistiveAccess = YES
    }
}
// In SimpleNotesView: .assistiveAccessNavigationIcon(systemImage: "note.text")
```

Or keep the existing UI with `UISupportsFullScreenInAssistiveAccess = YES` and a fully adaptive layout.

## Hit targets

Small glyph, full target: `.frame(minWidth: 44, minHeight: 44).contentShape(Rectangle())` (visionOS 60,
tvOS 66, macOS 28). On macOS prefer standard `controlSize` over hand-sized hit areas.

## Testing

- **Accessibility Inspector** (Xcode > Open Developer Tool): run Audit on each screen (contrast,
  missing labels, small targets, clipped text), then step through elements to check label, value,
  traits, and order. Works with Simulator, devices, and Mac apps; its Settings pane toggles
  Dynamic Type, Increase Contrast, Reduce Motion, and more.
- **Xcode previews**: Canvas > Variants > Dynamic Type Variants shows all sizes at once; pin one with
  `.environment(\.dynamicTypeSize, .accessibility5)`. Also preview `.environment(\.layoutDirection,
  .rightToLeft)` and dark mode.
- **Environment Overrides** (debug bar while running) flip text size and display settings live.
- **UI tests**: `try app.performAccessibilityAudit()` (iOS 17+) fails the test on audit issues.
- **On device**: VoiceOver, Voice Control, Switch Control, and Assistive Access don't run in
  Simulator. Set the Accessibility Shortcut first, turn on Screen Curtain for VoiceOver, and finish
  every main task (first launch, login, purchase, core flow, settings) with each technology.
  Claim a Nutrition Label only after those tasks pass with that feature on that device.
