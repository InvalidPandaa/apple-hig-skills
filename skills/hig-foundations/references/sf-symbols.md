# SF Symbols

Sources: [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), [Icons](https://developer.apple.com/design/human-interface-guidelines/icons), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type), [Motion](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback), [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)

Symbols and features ship per OS year: a symbol or effect added in SF Symbols 7 does not exist on iOS 18. Check each name's availability in the SF Symbols app against the deployment target, and provide a fallback when needed. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)

**License:** symbols, and anything confusingly similar, may not be used in app icons, logos or other trademark use. Symbols that depict Apple products can be displayed but not modified. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)

## Size, weight and scale

- **Size a symbol through the font of the text it sits with,** so it gets the same point size, weight and Dynamic Type scaling: `Label("Inbox", systemImage: "tray")` or `Image(systemName:)` inside text-styled content. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Weights-and-scales)
- **Change emphasis with `.imageScale(.small/.medium/.large)`, not with `.resizable().frame()`.** Scales are relative to SF's cap height and keep weight matching intact. UIKit `UIImage.SymbolConfiguration(textStyle:scale:)`, AppKit `NSImage.SymbolConfiguration`. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Weights-and-scales)
- **Match symbol weight to adjacent text** unless one of them is meant to stand out; nine weights mirror SF's nine. [HIG](https://developer.apple.com/design/human-interface-guidelines/icons#Best-practices)
- **Prefer the enclosed variant (circle, square) for legibility at very small sizes.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Design-variants)

## Rendering modes (`.symbolRenderingMode(_:)`)

| Mode | What it does | Use for |
|---|---|---|
| `.monochrome` | One color on all layers | Default UI, toolbars, text-like use |
| `.hierarchical` | One color, opacity per layer level | Depth with the accent color |
| `.palette` | One color per layer (`.foregroundStyle(a, b, c)`); two colors on a three-level symbol share the second | Matching a specific color scheme |
| `.multicolor` | The symbol's intrinsic colors (green leaf, red `trash.slash`) | Meaning carried by real-world color |

- **Use system or dynamic colors in any mode** so symbols adapt to Dark Mode, vibrancy and accessibility settings. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Rendering-modes)
- **Check legibility of the chosen mode at the actual size and background;** automatic gives the preferred mode but not always the most legible one. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Rendering-modes)
- **Gradient (SF Symbols 7):** `.symbolColorRenderingMode(.gradient)` (iOS 26+) draws a linear gradient from one source color in any mode; it reads best at larger sizes. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Gradients)

## Variable color

- **Use variable color for a value that changes (volume, signal, capacity), never to suggest depth;** depth is Hierarchical's job. `Image(systemName: "speaker.wave.3", variableValue: level)` with `level` in 0...1. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Variable-color)
- **iOS 26+:** `.symbolVariableValueMode(.draw)` renders the value by drawing the path instead of coloring layers (`.color` is the classic behavior). Verify the symbol has draw data.

## Variants (`.symbolVariant(_:)`)

- **Outline** is the default and suits toolbars, lists and symbols next to text. **Fill** adds emphasis: iOS tab bars, swipe actions, accent-colored selection. **Slash** shows unavailable; **enclosed** shapes help small sizes. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Design-variants)
- **Don't force variants inside system containers.** Tab bars pick fill and toolbars outline themselves; pass the base name (`"house"`, not `"house.fill"`). [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Design-variants)
- **Language and script variants switch automatically** with the device language (Arabic, Hebrew, CJK, Devanagari, Thai and more), and directional symbols flip for right-to-left. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Design-variants)
- **Depict people with the nongendered `person` and `figure` symbols.** [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)

## Animations

Each effect has one meaning; pick it by what you need to say. API: `.symbolEffect(_:options:value:)` for one-shot effects triggered by a value change, `.symbolEffect(_:options:isActive:)` for ongoing ones, `.contentTransition(.symbolEffect(.replace))` when the symbol name changes, `.symbolEffectsRemoved()` to switch all off in a subtree. Effects are in the Symbols framework (`SymbolEffect`).

| Effect | Means | Typical use | Since |
|---|---|---|---|
| Appear / Disappear | Comes into / leaves view | Showing an optional badge | iOS 17 |
| Bounce | "This happened" or "act here", plays once | Item added, download finished | iOS 17 |
| Scale | Stays bigger or smaller until reset | Highlight the chosen item | iOS 17 |
| Pulse | Opacity throb, annotated layers only | Ongoing activity, waiting | iOS 17 |
| Variable color | Layers light up cumulatively or one by one | Connecting, playing, broadcasting | iOS 17 |
| Replace (down-up, up-up, off-up) | One symbol becomes another | Play ↔ pause; up-up for forward progress; off-up to stress the next action | iOS 17 |
| Magic Replace | Smart morph between related shapes (slash draws on, badge appears) | Mute toggle; default replace, falls back to down-up for unrelated symbols | iOS 18 |
| Wiggle | Directional nudge | Call to action people might miss, arrows | iOS 18 |
| Breathe | Opacity and size swell | Live status, recording in progress | iOS 18 |
| Rotate | Spins, whole or by layer (fan blades) | Work in progress | iOS 18 |
| Draw On / Draw Off (`.drawOn`, `.drawOff`) | Drawn along its path, whole, by layer or individually | Progress, reinforcing a direction | iOS 26 |

Rules:
- **Animate only when the motion says something** the static symbol can't; don't stack several effects in one view. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations)
- **Stop indefinite effects when the condition ends** (pulse, breathe, rotate, variable color tied to a real state, via `isActive:`). A forever-pulsing icon reads as "still working". [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations)
- **Match the app's tone;** a banking app and a game don't wiggle alike. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations)
- **Under Reduce Motion, keep meaning without movement:** prefer replace or an opacity change over bounce and wiggle for essential feedback. See `motion.md`.

```swift
Image(systemName: "bell")
    .symbolEffect(.bounce, value: unreadCount)          // once per change

Image(systemName: isMuted ? "speaker.slash" : "speaker.wave.2")
    .contentTransition(.symbolEffect(.replace))          // Magic Replace when shapes relate

Image(systemName: "waveform")
    .symbolEffect(.variableColor.iterative, isActive: isRecording)
```

## Custom symbols

- **Start from an exported template of the closest system symbol** and keep its detail level, optical weight, alignment and perspective; simple, recognizable, inclusive, directly tied to its meaning. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- **Annotate layers** (color or primary/secondary/tertiary level) in the SF Symbols app to support rendering modes, and set z-order for variable color. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- **Draw whole shapes plus erase layers instead of cutouts** so animations by layer behave; test every animation preset. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- **Build badges and enclosures from the app's component library,** not into the base symbol. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- **Use negative side margins** (named like `left-margin-Regular-M`) to align badged symbols optically. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- **Give every custom symbol an accessibility label;** system symbols have default labels, custom ones don't. [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- **Never draw Apple products or modify symbols flagged as Apple features.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Custom-symbols)
- Add custom symbols to the asset catalog and load with `Image("name")`; they gain the same weight, scale and effect support.
