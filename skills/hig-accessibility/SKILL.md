---
name: hig-accessibility
description: Use when building, reviewing, or fixing accessibility in a native Apple-platform app - VoiceOver labels, icon-only or toggle buttons, custom controls, grouping, Dynamic Type at accessibility sizes, contrast, hit targets, Reduce Motion, color-only status, captions, Voice Control, Switch Control, Full Keyboard Access, Assistive Access, Accessibility Nutrition Labels, accessibility testing, inclusive language, or right-to-left layout.
---
# Accessibility (VoiceOver, Dynamic Type, assistive tech)

Every element must tell assistive technologies what it is, what state it is in, and what it does, and
the layout must survive the largest text size and every display setting the person turned on.

## Quick decisions

| Need / situation | Do this (API) | HIG |
|---|---|---|
| Icon-only button | `Button("Share", systemImage: "square.and.arrow.up")` + `.labelStyle(.iconOnly)`, or `.accessibilityLabel` | [voiceover#Descriptions](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions) |
| Custom slider, rating, knob | `.accessibilityRepresentation { Slider(...) }` or `.accessibilityValue` + `.accessibilityAdjustableAction` | [voiceover#Descriptions](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions) |
| Custom on/off control | Prefer `Toggle` + custom `ToggleStyle`; else `.accessibilityAddTraits(.isToggle)` (iOS 17+) + value | [voiceover#Descriptions](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions) |
| Card / cell with image, title, meta | `.accessibilityElement(children: .combine)`; row buttons become `.accessibilityAction(named:)` | [voiceover#Navigation](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation) |
| Section titles in a scroll view | `.accessibilityAddTraits(.isHeader)` or `.accessibilityHeading(.h2)` | [voiceover#Navigation](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation) |
| Decorative image | `Image(decorative:)` or `.accessibilityHidden(true)` | [voiceover#Descriptions](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions) |
| Row of items breaks at large text | `dynamicTypeSize.isAccessibilitySize` -> `AnyLayout(VStackLayout())`, or `ViewThatFits` | [typography#Supporting-Dynamic-Type](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type) |
| Fixed padding / icon size next to text | `@ScaledMetric(relativeTo: .body)` | [typography#Supporting-Dynamic-Type](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type) |
| Custom bar whose labels must not grow | `.accessibilityShowsLargeContentViewer()` | [typography#Conveying-hierarchy](https://developer.apple.com/design/human-interface-guidelines/typography#Conveying-hierarchy) |
| Content changed without navigation | `AccessibilityNotification.Announcement("...").post()` (iOS 17+) | [voiceover#Navigation](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation) |
| Custom animation or parallax | `@Environment(\.accessibilityReduceMotion)` -> fade or no animation | [accessibility#Cognitive](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive) |
| Custom blur / glass / gradient overlay | `@Environment(\.accessibilityReduceTransparency)` -> opaque fill | [color#Best-practices](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices) |
| Status shown by color | Add symbol or text; check `accessibilityDifferentiateWithoutColor` | [color#Inclusive-color](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color) |
| Swipe / drag / pinch gesture | Also a visible button or menu item, plus an accessibility action | [accessibility#Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility) |
| App used in Assistive Access | `AssistiveAccess { }` scene + `UISupportsAssistiveAccess` (iOS 26+) | [accessibility#Cognitive](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive) |
| App Store submission | Fill in Accessibility Nutrition Labels per device, only for features that pass | [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) |

## Rules

### Semantics for VoiceOver, Voice Control, and Switch Control
- **Label every control that has no visible text, with the action or object, not the icon.** "Share", not "square.and.arrow.up" or "Share button"; the button trait already says "button". [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions)
- **Keep a toggled control's label stable and expose its state separately.** A favorite star stays "Favorite" with `.isSelected` or `.isToggle` plus a value; only swap the label when the action itself changes (Play/Pause). [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions)
- **Give custom controls the semantics of the standard control they imitate.** `accessibilityRepresentation` with a real `Slider`, `Toggle`, or `Picker` gets traits, value, and adjust gestures right in one step. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions)
- **Group what sighted people read as one thing.** A cell's image, title, and subtitle become one element via `.combine`; otherwise VoiceOver reads all images first and all captions after. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation)
- **Move secondary buttons inside a grouped row into custom actions.** One swipe per row with actions in the Actions rotor beats five stops per row; `swipeActions` already show up there. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation)
- **Mark headings and give each screen a unique title.** `navigationTitle` is the first thing announced; headings power rotor navigation in long content. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation)
- **Add custom rotors for long, typed content.** Unread messages, errors in a form, or links in an article: `accessibilityRotor`. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation)
- **Announce changes that happen off the focused element.** Upload finished, validation error, new results: post an announcement, or move focus with `@AccessibilityFocusState`. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Navigation)
- **Describe images by what they convey in context; hide purely decorative ones.** Don't repeat the adjacent caption in the label. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions)
- **Make charts navigable, not just labeled.** Give a one-line summary plus `accessibilityChartDescriptor` (Swift Charts does much of this automatically). [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions)
- **Make the visible text the start of the label so Voice Control can target it.** People say "Tap Send"; add spoken alternatives, most important first, with `accessibilityInputLabels(["Send", "Submit"])`. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)
- **Never let a gesture be the only path.** Swipe-to-dismiss needs a Close button; drag-to-reorder needs Move actions; pinch needs `accessibilityZoomAction`. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)
- **Make every control reachable and operable with Full Keyboard Access.** Custom controls need `.focusable()` and a key handler (`onKeyPress`, iOS 17+); don't override system shortcuts. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Speech)
- **Use the native accessibility APIs, never a home-made screen reader or voice mode.** The Nutrition Labels guidance tells you to support VoiceOver and Voice Control natively instead of rebuilding them. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)

### Dynamic Type and reflow
- **Test at AX5, not just xxxLarge, and reflow instead of truncating.** At AX5, Body is 53 pt: switch horizontal rows to stacks, drop columns, let text wrap (`lineLimit(nil)`). [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Show as much text at the largest accessibility size as at the largest standard size.** Truncation is acceptable only if a tap opens the full text. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Scale meaningful icons and spacing with text.** SF Symbols scale with the font; custom images and paddings need `@ScaledMetric`. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Keep primary content first when the layout stacks.** The title stays above the timestamp and badges at AX sizes. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Grow content, not chrome.** Tab titles and toolbar labels may stay fixed; give custom bars the Large Content Viewer so a long-press shows the item enlarged. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Conveying-hierarchy)
- **Make custom fonts scale and honor Bold Text.** `Font.custom(_:size:relativeTo:)`; check `legibilityWeight` for a heavier face. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Using-custom-fonts)
- **Target 200% enlargement (140% on watchOS).** macOS has no Dynamic Type, so reading-heavy Mac apps need their own text-size control (View > Make Text Bigger). [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)

### Color, contrast, and sensory settings
- **Meet 4.5:1 for text up to 17 pt, 3:1 for 18 pt and larger or bold, in light and dark.** Apple's thresholds are in points, so 18 pt regular already counts as large text. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)
- **Ship an Increase Contrast variant for every custom color.** Asset catalog "High Contrast" appearance; if defaults miss the minimum, this variant must reach it. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)
- **Never encode state in hue alone.** Pair red/green with a symbol, text, or shape, and let people recolor charts or game pieces where practical. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color)
- **Under Reduce Motion, swap slides, zooms, depth, and blur transitions for fades.** Tighten springs, keep gesture-tracked motion, stop auto-repeating animation. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)
- **Never make motion the only carrier of meaning.** Pair it with text, haptics, or sound. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Best-practices)
- **Give custom translucent surfaces an opaque fallback under Reduce Transparency.** System materials and Liquid Glass adapt on their own; hand-rolled blur does not. [HIG](https://developer.apple.com/design/human-interface-guidelines/color#Best-practices)

### Hearing, media, and cognition
- **Offer captions, subtitles, audio descriptions, and transcripts as fits the media.** `AVPlayerViewController` exposes track selection; a custom player must expose it too. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Hearing)
- **Pair audio cues with haptics and visual cues.** A success chime gets a haptic; off-screen game sounds get an onscreen pointer. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Hearing)
- **Don't autoplay without controls; honor Dim Flashing Lights and Auto-Play Animated Images.** `accessibilityDimFlashingLights`, `accessibilityPlayAnimatedImages` (iOS 17+). [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)
- **Replace auto-dismissing UI with an explicit dismiss.** VoiceOver and Switch Control users need time to reach a toast's Undo. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)
- **For Assistive Access, keep core tasks, one step per screen, and confirm destructive actions twice.** Use the `AssistiveAccess` scene and `assistiveAccessNavigationIcon` (iOS 26+), or `UISupportsFullScreenInAssistiveAccess` for the existing UI. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)

### Hit targets per platform
- **Size targets per platform (default / minimum):** iOS and iPadOS 44x44 / 28x28 pt, macOS 28x28 / 20x20, watchOS 44x44 / 28x28, tvOS 66x66 / 56x56, visionOS 60x60 / 28x28. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)
- **Space targets apart: about 12 pt around bezeled controls, 24 pt around borderless ones.** Grow the tappable area with `.contentShape(Rectangle())` and padding, not by enlarging the glyph. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)
- **Don't port iOS density to visionOS.** 60 pt is the comfortable default for eye-and-pinch input; keep content in the field of view and avoid head-anchored UI (`accessibilityPrefersHeadAnchorAlternative`). [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#visionOS)
- **In visionOS, custom hand gestures get no input while VoiceOver runs.** Provide accessibility actions as the alternative path. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#visionOS)
- **On tvOS, show focus by scale and motion, never by color alone.** [HIG](https://developer.apple.com/design/human-interface-guidelines/color#tvOS)

### Basics (checklist, no explanation needed)
- Text styles (`.body`, `.headline`) not fixed sizes; system/semantic colors; no light weights at small sizes; min text 11 pt iOS, 10 pt macOS, 12 pt watchOS/visionOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Ensuring-legibility)
- Prefer standard components: they ship correct traits, values, focus, and Large Content Viewer. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)

### Testing and Nutrition Labels
- **Run Accessibility Inspector's audit on every screen, then inspect custom controls element by element.** Check label, value, traits, and frame; it also toggles display settings live. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- **Preview Dynamic Type variants and AX sizes in Xcode.** Canvas Variants > Dynamic Type Variants, or `.environment(\.dynamicTypeSize, .accessibility5)`; add `performAccessibilityAudit()` to UI tests (iOS 17+). [HIG](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)
- **Test VoiceOver, Voice Control, Switch Control, and Assistive Access on a device.** None run in Simulator; use VoiceOver with Screen Curtain and complete each main task. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)
- **Claim a Nutrition Label only if every common task works with that feature on that device.** Common tasks: core function, first launch, login, purchase, settings. Labels: VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, Audio Descriptions. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)

## Brief conflicts

Raise the conflict, propose the alternative, then follow the person's decision.

| Request | Why it conflicts | Compliant alternative |
|---|---|---|
| "Lock font sizes, the layout breaks at big text" | Layouts must adapt to all sizes ([typography#Supporting-Dynamic-Type](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)) | Stack at AX sizes; cap only chrome with `.dynamicTypeSize(...)` + Large Content Viewer |
| "Green/red dot for online/offline" | Color alone ([color#Inclusive-color](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color)) | Dot plus distinct symbol or text, label carries the state |
| "Toast with Undo that vanishes after 3 s" | Time-boxed UI ([accessibility#Cognitive](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)) | Persist until dismissed, or longer when VoiceOver/Switch Control is on; plus Edit > Undo |
| "Swipe-only delete / gesture-only navigation" | Needs alternatives ([accessibility#Mobility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility)) | Visible button or menu item + accessibility action |
| "Light gray brand text on white" | Below 4.5:1 ([accessibility#Vision](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision)) | Darker shade for text, brand gray for large or decorative areas, Increase Contrast variant |
| "Autoplaying hero video / looping parallax" | Playback control and motion ([accessibility#Cognitive](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)) | Poster frame + play control; static under Reduce Motion |
| "Tick every Nutrition Label so we look good" | Labels must be accurate ([accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)) | Test each common task per device; claim only what passes |
| "Gender: Male / Female (required)" | Inclusion ([inclusion#Gender-identity](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)) | Drop the field, or add nonbinary, self-identify, decline to state |

## Common mistakes
- Icon-only buttons with no label, so VoiceOver reads the symbol name or "button".
- Labels that include the type ("Close button") or change text to express state ("Unfavorited").
- Custom controls built from `onTapGesture` on a shape: no button trait, no value, invisible to Switch Control and Full Keyboard Access. Use `Button`, or a standard control in `accessibilityRepresentation`.
- `.accessibilityElement(children: .ignore)` without a replacement label, so the element goes silent.
- Cells left ungrouped (five swipes per row) or grouped with their buttons trapped inside.
- Dynamic Type "supported" because text styles are used, while `HStack`s truncate or overlap at AX3+, fixed `frame(height:)` clips text, and padding stays fixed.
- Contrast checked only in light mode, or only on the resting background, not over Liquid Glass or images.
- Reduce Motion handled by shortening durations instead of changing slide/zoom to fade.
- Assuming 44 pt everywhere: macOS controls are smaller, visionOS needs 60 pt, tvOS 66 pt.
- Claiming VoiceOver works after testing only with Accessibility Inspector in Simulator.

## References
- `references/swiftui-accessibility.md` - read when writing SwiftUI: labels, values, traits, grouping, actions, rotors, headings, adjustable controls, Dynamic Type reflow and `@ScaledMetric`, display-setting environment values, `accessibilityRepresentation`, focus, testing snippets.
- `references/inclusion-and-rtl.md` - read when writing copy or imagery, asking for personal data, localizing, or supporting Arabic and Hebrew: inclusive language, RTL mirroring rules, which icons flip, localization-friendly layout.

## Look it up live
Slugs: `accessibility`, `voiceover`, `typography`, `color`, `motion`, `inclusion`, `right-to-left`, `charts`, `playing-haptics`, `keyboards`.
```
python3 ../apple-hig/scripts/hig.py fetch accessibility --section "Mobility"
python3 ../apple-hig/scripts/hig.py fetch /documentation/swiftui/view-accessibility
```
