# Selection and input components

Sources: [Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells), [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes), [Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views), [Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells), [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers), [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls), [Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders), [Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers), [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields), [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)

Glass styling of controls and keyboard accessories is covered by the `hig-liquid-glass` skill.

## Choosing between components in this group

| Situation | Component | SwiftUI |
|---|---|---|
| On/off setting in a list or form row (iOS) | Switch | `Toggle` (default `.switch` in `Form`) |
| On/off state outside a list (iOS), e.g. a filter in a toolbar | Button that toggles | `Toggle` + `.toggleStyle(.button)` |
| On/off setting, or a hierarchy of settings (macOS) | Checkbox | `Toggle` + `.toggleStyle(.checkbox)` |
| 2–5 mutually exclusive options with labels (macOS) | Radio buttons | `Picker` + `.pickerStyle(.radioGroup)` |
| 2–5 closely related views or modes of one object | Segmented control | `Picker` + `.pickerStyle(.segmented)` |
| Short list of choices | Pull-down / pop-up menu | `Picker` + `.pickerStyle(.menu)` |
| Medium-to-long, predictable list | Picker | `Picker` (`.wheel`, `.navigationLink`, `.inline`) |
| Very large set, needs search or index | List or table | `List` + `.searchable` |
| Date or time | Date picker | `DatePicker` (`.compact`, `.graphical`, `.wheel`) |
| Continuous value between fixed bounds | Slider | `Slider` |
| Small whole-number increments | Stepper (+ text field for big jumps) | `Stepper` |
| Short free text (name, email) | Text field | `TextField`, `SecureField` |
| Long text | Text view | `TextEditor` |
| Free text plus suggested values (macOS) | Combo box | `NSComboBox`; `.textInputSuggestions` (macOS 15+) |
| Color | Color well | `ColorPicker` |
| Editable image by drop/paste (macOS) | Image well | `NSImageView` (`isEditable`) |
| PIN or code on Apple TV | Digit entry view | `TVDigitEntryViewController` |

## Toggles

Use for: two opposing states of a setting or view. Not for: choosing among items (pop-up button, picker), triggering an action (button).

- **iOS: use the switch only inside list rows; everywhere else use a button-style toggle that changes its background.** The row text is the label; a toggle button needs only an icon. `.toggleStyle(.button)` [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#iOS-iPadOS)
- **Keep the default switch color unless you swap in the app accent with enough contrast.** Don't hard-code `.tint(.blue)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#iOS-iPadOS)
- **Show state with more than color** (fill, checkmark, shape). [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#Best-practices)
- **macOS: switches, checkboxes and radio buttons go in the window body, never in a toolbar or status bar.** [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#macOS)
- **macOS: reserve switches for settings with weight (a group); use mini switches in grouped form rows; don't swap existing checkboxes for switches.** `.controlSize(.mini)` [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#Switches)
- **macOS: use checkboxes for dependent settings, indent children, and show the mixed state on the parent.** `Toggle(sources:isOn:)` gives mixed state. [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#Checkboxes)
- **macOS: radio buttons for 2–5 exclusive options; above that, a pop-up button; a single on/off is a checkbox, not one radio button.** [HIG](https://developer.apple.com/design/human-interface-guidelines/toggles#Radio-buttons)

SwiftUI: `Toggle`, `.toggleStyle(.switch | .checkbox | .button)`. UIKit `UISwitch`, `UIButton.changesSelectionAsPrimaryAction`; AppKit `NSSwitch`, `NSButton` checkbox/radio.

## Segmented controls

Use for: closely related choices or subviews that affect one object or view. Not for: switching app sections (tab bar), main-window view switching on Mac (tab view), filtering on tvOS (split view).

- **Don't mix action segments and selection segments in one control.** Momentary action groups (Reply / Reply All / Forward) are a separate kind. [HIG](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#Best-practices)
- **About 5 segments max on iPhone, 5–7 in wide layouts; keep widths equal.** [HIG](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#Best-practices)
- **Use all text or all images, never a mix; noun labels in title case.** [HIG](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#Content)
- **macOS: add a tooltip per segment, and labels under icon segments when meaning is unclear.** `.help(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#macOS)
- **tvOS: keep other focusable views away; segments select on focus.** [HIG](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#tvOS)

SwiftUI: `Picker` + `.pickerStyle(.segmented)`. UIKit `UISegmentedControl` (`isMomentary`), AppKit `NSSegmentedControl` (supports multi-select).
Platforms: not on watchOS; visionOS shows your label text as a tooltip for icon segments.

## Pickers

Use for: medium-to-long lists of predictable values; dates and times. Not for: very short lists (pull-down button / `.menu`), huge lists (searchable list or table).

- **Show the picker in context (below the field, or in a popover); never navigate away just to pick.** [HIG](https://developer.apple.com/design/human-interface-guidelines/pickers#Best-practices)
- **Order values predictably (alphabetical, numeric) so hidden values can be guessed.** [HIG](https://developer.apple.com/design/human-interface-guidelines/pickers#Best-practices)
- **Coarsen minute granularity when the task allows** (e.g. 15-minute steps; interval must divide 60). UIKit `UIDatePicker.minuteInterval`. [HIG](https://developer.apple.com/design/human-interface-guidelines/pickers#Best-practices)
- **iOS: use the compact date picker when space is tight.** Countdown mode isn't available in compact or inline. `.datePickerStyle(.compact)` [HIG](https://developer.apple.com/design/human-interface-guidelines/pickers#iOS-iPadOS)
- **macOS: textual style for precise entry in tight space, graphical for browsing days or ranges.** `.datePickerStyle(.field | .graphical)` [HIG](https://developer.apple.com/design/human-interface-guidelines/pickers#macOS)
- **watchOS: Digital Crown drives wheels; long lists use the navigation-link style.** `.pickerStyle(.navigationLink)` [HIG](https://developer.apple.com/design/human-interface-guidelines/pickers#watchOS)

SwiftUI: `Picker`, `DatePicker`, `MultiDatePicker`. UIKit `UIPickerView`, `UIDatePicker`; AppKit `NSDatePicker`, `NSPopUpButton`.
Platforms: tvOS pickers come through SwiftUI only; values and order follow the device locale.

## Sliders

Use for: a value in a continuous, bounded range. Not for: audio volume on iOS (system volume view), exact values alone (pair with a field).

- **Minimum on the leading side (or bottom), maximum on the trailing side (or top).** RTL is handled by the system. [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#Best-practices)
- **iOS: never build a volume slider; use the system volume view.** `MPVolumeView` / `AVRoutePickerView` [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#iOS-iPadOS)
- **For wide ranges add a text field and stepper for exact entry.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#Best-practices)
- **Use min/max icons that show meaning** (small/large image). `Slider(value:in:label:minimumValueLabel:maximumValueLabel:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#Best-practices)
- **Add tick marks (labeled at least at the ends) where specific values matter.** `Slider(... ticks:)` with `SliderTick` (iOS 26+, macOS 26+). [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#macOS)
- **macOS: give live feedback while dragging; use circular sliders for values that wrap (rotation).** [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#macOS)
- **visionOS: prefer horizontal.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sliders#visionOS)

SwiftUI: `Slider`. UIKit `UISlider`, AppKit `NSSlider`.
Platforms: not on tvOS; watchOS shows discrete steps with − / + buttons (custom glyphs allowed).

## Steppers

Use for: small increments of a visible value. Not for: wide ranges alone (add a text field).

- **Always show the value next to the stepper**; the control has none. Put it in the label: `Stepper("Copies: \(n)", value: $n, in: 1...99)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/steppers#Best-practices)
- **Pair with a text field when big jumps are likely; on Mac consider Shift-click for 10× steps.** [HIG](https://developer.apple.com/design/human-interface-guidelines/steppers#macOS)

SwiftUI: `Stepper`. UIKit `UIStepper`, AppKit `NSStepper`. Not on watchOS or tvOS.

## Text fields

Use for: short, specific input. Not for: long text (text view, `TextEditor`); tvOS/watchOS input that could be a choice (buttons, list).

- **Keep a visible label in addition to placeholder text,** since the placeholder vanishes on typing. `LabeledContent`, `Form` rows, or `TextField("Email", text: $email, prompt: Text("name@example.com"))` [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#Best-practices)
- **Always use a secure field for passwords and other secrets.** `SecureField` [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#Best-practices)
- **Validate at the right moment:** email on leaving the field; user name/password rules before leaving. [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#Best-practices)
- **Use a number formatter for numeric input; never assume a locale's format.** `TextField(value:format:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#Best-practices)
- **Match field width to expected input; stack fields vertically with consistent widths; keep Tab order logical.** `@FocusState` for focus flow. [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#Best-practices)
- **Set the matching keyboard and content type.** `.keyboardType(.emailAddress)`, `.textContentType(.emailAddress)` [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#Best-practices)
- **iOS: offer a Clear button at the trailing end; leading image shows purpose, trailing end extra features.** UIKit `clearButtonMode`. [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#iOS-iPadOS)
- **macOS: show an expansion tooltip for truncated text; use a combo box when input pairs with a list.** [HIG](https://developer.apple.com/design/human-interface-guidelines/text-fields#macOS)

SwiftUI: `TextField`, `SecureField`, `.textFieldStyle`. UIKit `UITextField`, AppKit `NSTextField`.

## Virtual keyboards

Use for: choosing the right system keyboard; rarely, a custom input view or keyboard extension. Not for: macOS (none).

- **Pick the keyboard and semantic content type for every field** (number pad, decimal pad, email, URL, phone, one-time code). `.keyboardType(_:)`, `.textContentType(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#Best-practices)
- **Set the Return key to the action** (Search, Send, Next, Done). `.submitLabel(.search)` + `.onSubmit` [HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#Best-practices)
- **iOS (2025): put task-specific controls above the keyboard in a standard toolbar so they adopt Liquid Glass automatically, and respect the keyboard layout guide.** `ToolbarItemGroup(placement: .keyboard)`; UIKit `inputAccessoryView`, `UIKeyboardLayoutGuide`. [HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#iOS-iPadOS)
- **A custom input view must be clearly better than the system keyboard and play the click sound.** `UIDevice.current.playInputClick()` [HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#Custom-input-views)
- **Custom keyboard extensions: provide an obvious keyboard switch, don't duplicate Globe/Dictation keys, and teach usage in the app, not in the keyboard.** In-app-only needs belong in a custom input view. [HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards#Custom-keyboards)

Platforms: visionOS keyboard floats in its own window (no layout work); watchOS can't change the keyboard type but honors `textContentType`; tvOS shows a linear keyboard for the Siri Remote.

## Color wells

Use for: letting people pick a color for text, shapes or other content. Prefer the system color picker so saved colors carry across apps. `ColorPicker` (`supportsOpacity:`); UIKit `UIColorWell`, AppKit `NSColorWell`. Not on tvOS or watchOS. On Mac, color wells support drag and drop between wells. [HIG](https://developer.apple.com/design/human-interface-guidelines/color-wells#Best-practices)

## Combo boxes (macOS only)

Text field plus a list of likely values; custom entries are not added to the list. Prefill a meaningful default from the list, introduce it with a title-case label ending in a colon, and keep list items no wider than the field. AppKit `NSComboBox`; no SwiftUI equivalent (`TextField` + `.textInputSuggestions`, macOS 15+, is the nearest). [HIG](https://developer.apple.com/design/human-interface-guidelines/combo-boxes#Best-practices)

## Image wells (macOS only)

Editable image view (drop, copy, paste, delete). Restore the default image when a required image is cleared, and wire up the standard Edit menu items and shortcuts. AppKit `NSImageView` with `isEditable = true`. [HIG](https://developer.apple.com/design/human-interface-guidelines/image-wells#Best-practices)

## Digit entry views (tvOS only)

Full-screen PIN/code entry. Use secure digits for anything sensitive and a title plus prompt that say why the code is needed. TVUIKit `TVDigitEntryViewController`. [HIG](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views#Best-practices)
