# Motion

Sources: [Motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive), [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations)

System components already animate, and adjust that motion for accessibility settings and input (Liquid Glass reacts more strongly to touch than to a trackpad). The rules below apply to motion you add yourself.

## When to animate

- **Animate to explain a change, confirm an action or show status; never just to decorate.** Excess motion distracts and can make people feel unwell. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Best-practices)
- **Never let motion be the only carrier of information;** pair it with a state change people can read, plus haptics or sound where useful. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Best-practices)
- **Skip custom motion on frequent interactions** in apps; the system's subtle feedback is enough and repeated animation costs attention every time. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)
- **Prefer an animated SF Symbol over a custom animation** for small feedback (see `sf-symbols.md`). [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)

## How to animate

- **Keep feedback brief and precise,** tied to the moment of the action. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)
- **Follow the gesture and physical expectation:** a view pulled down from the top is dismissed upward, not sideways. Track the finger directly; spring to rest. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)
- **Make every animation interruptible;** people must be able to act before it ends, especially for animations they see repeatedly. SwiftUI springs (`.spring`, `.smooth`, `.snappy`) retarget mid-flight; avoid blocking input with `allowsHitTesting(false)` during transitions. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Providing-feedback)
- **Games:** hold a steady 30–60 fps with good defaults per device, and offer performance/battery modes. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#Leveraging-platform-capabilities)

## Reduce Motion

When Reduce Motion is on, cut automatic and repeating animation, zooms, scaling and peripheral movement. Concretely: [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)

| Instead of | Use |
|---|---|
| Slide or push along x, y or z | Cross-fade |
| Bouncy spring | Tighter spring, no overshoot |
| Animating depth / z-layer changes | Instant change or fade |
| Animating into or out of blur | Fade |
| Autoplaying loops, parallax, background motion | Static frame, play on request |
| Free-running motion during a gesture | Motion locked to the finger |

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

DetailCard(item)
    .transition(reduceMotion ? .opacity : .move(edge: .bottom).combined(with: .opacity))
    .animation(reduceMotion ? .easeInOut(duration: 0.2) : .bouncy, value: selection)
```

UIKit: `UIAccessibility.isReduceMotionEnabled` and `reduceMotionStatusDidChangeNotification`. Also respect Dim Flashing Lights in video, avoid fast blinking content, and don't autoplay video or audio without controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility#Cognitive)

## visionOS comfort

- **Keep motion out of peripheral vision;** if something must move there, match its brightness to the surroundings. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#visionOS)
- **Large moving objects: raise translucency or lower contrast,** and keep windows people drag fairly small. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#visionOS)
- **Relocate with fade-out, move, fade-in** when the path itself means nothing. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#visionOS)
- **Don't rotate the virtual world,** even under the person's control; change direction instantly during a quick fade. Give a stationary frame of reference. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#visionOS)
- **Avoid sustained oscillation, especially around 0.2 Hz;** keep amplitude low and the object translucent. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#visionOS)

## watchOS
Layout and appearance animations in WatchKit always ease in and out and can't be changed; prefer SwiftUI animation. [HIG](https://developer.apple.com/design/human-interface-guidelines/motion#watchOS)
