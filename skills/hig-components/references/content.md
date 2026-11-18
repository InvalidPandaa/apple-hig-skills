# Content components

Sources: [Charts](https://developer.apple.com/design/human-interface-guidelines/charts), [Image views](https://developer.apple.com/design/human-interface-guidelines/image-views), [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views), [Web views](https://developer.apple.com/design/human-interface-guidelines/web-views)

## Choosing between components in this group

| Situation | Component | API |
|---|---|---|
| Show a trend, comparison, or distribution in data | Chart | `Chart` (Swift Charts); `Chart3D` (iOS/macOS/visionOS 26+) |
| Show a photo or picture that people only look at | Image view | `Image`, `AsyncImage` |
| Show an interface icon | SF Symbol, not an image view | `Image(systemName:)`, `Label` |
| An image people can tap or click | Button with an image label, not an image view | `Button { } label: { Image(...) }` |
| A few words of read-only text | Label (see layout-and-organization.md) | `Text`, `Label` |
| One line of editable text | Text field (see selection-and-input.md) | `TextField` |
| Long, styled, or editable multiline text | Text view | `TextEditor`, `Text` |
| Briefly show a web page or HTML inside the app | Web view | `WebView` + `WebPage` (WebKit, iOS/macOS/visionOS 26+) |
| Let people browse the web | Hand off to Safari, don't build a browser | `openURL`, `SFSafariViewController` |

## Charts

Use for: highlighting a few key facts in a dataset so people can decide something. Not for: one number (show it as text), data people must read exactly row by row (use a list or table).

- **Pick the mark for the question.** Bars compare categories or totals per period, lines show change over time, points show relationships and outliers; a line with point marks shows the trend and the individual values. `BarMark`, `LineMark`, `PointMark` [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Marks)
- **Decide fixed vs. dynamic axis range by meaning, and don't force zero everywhere.** Fixed when the bounds mean something (battery 0–100%); bars usually start at zero, but a heart-rate chart from zero hides the differences that matter. `chartYScale(domain:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Axes)
- **Use familiar tick steps (0, 5, 10) and keep grid lines and axis labels light** so the data stays the most prominent thing, especially when people can scrub. [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Axes)
- **Put the takeaway in a title or subtitle above the chart.** People, and VoiceOver users in particular, should get the main message before reading any marks. [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Descriptive-content)
- **Never hide critical information behind interaction, and make the whole plot area the scrub target** when marks are too small to hit. `chartXSelection(value:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Best-practices)
- **Don't encode meaning in color alone.** Add different symbols or patterns per series and separators between stacked segments. `.symbol(by:)`, `.foregroundStyle(by:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Color)
- **Write accessibility labels for what the data means, not what it looks like.** Label each important mark (or group of marks), use real values instead of words like "rapidly", spell out "June 6" and "60 minutes", and hide the visible axis/tick labels from VoiceOver. Swift Charts adds Audio Graphs automatically; give it a title and summary with `accessibilityChartDescriptor(_:)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Enhancing-the-accessibility-of-a-chart)
- **Announce data changes in a way that doesn't depend on animation**, so VoiceOver users and people with animations off notice them (accessibility notifications). [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Best-practices)

Also: in compact width maximize plot width with short Y labels; align the chart's leading edge with surrounding views, moving the Y axis to the trailing side if needed (`chartYAxis { AxisMarks(position: .trailing) }`). [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#Best-practices)

SwiftUI: `Chart` with marks (Swift Charts), `Chart3D` (26+). No UIKit/AppKit equivalent; host Swift Charts.
Platforms: watchOS: show glanceable data and avoid complex chart interactions; put detail in the iPhone app. [HIG](https://developer.apple.com/design/human-interface-guidelines/charts#watchOS)

## Image views

Use for: displaying a single image or an animated image sequence. Not for: icons (SF Symbols), tappable images (button), editable images on Mac (image well).

- **Make a tappable image a `Button`, not an `Image` with `.onTapGesture`.** The button brings press states, focus, and accessibility traits for free. On macOS this is an image button. [HIG](https://developer.apple.com/design/human-interface-guidelines/image-views#Best-practices)
- **Use SF Symbols or template images for icons** so they pick up the accent color, vibrancy, and Dark Mode; reserve image views for content. [HIG](https://developer.apple.com/design/human-interface-guidelines/image-views#Best-practices)
- **Protect text you put over an image** with sufficient contrast: a scrim, background layer, or shadow behind the text. [HIG](https://developer.apple.com/design/human-interface-guidelines/image-views#Content)
- **Give all frames of an animated sequence the same size, prescaled to the view**, to avoid runtime scaling cost. [HIG](https://developer.apple.com/design/human-interface-guidelines/image-views#Content)
- **macOS: use an image well when people can paste, drag, or delete the image.** [HIG](https://developer.apple.com/design/human-interface-guidelines/image-views#macOS)

SwiftUI: `Image`, `AsyncImage`. UIKit `UIImageView`, AppKit `NSImageView` (editable: image well).
Platforms: tvOS uses layered images for depth; visionOS windows can show stereoscopic and spatial photos (RealityKit `ImagePresentationComponent` outside image views); watchOS: animate with SwiftUI rather than image sequences. [HIG](https://developer.apple.com/design/human-interface-guidelines/image-views#visionOS)

## Text views

Use for: long, multiline, styled, or editable text. Not for: a short string (`Text`/label), a single editable line (`TextField`), editable text on tvOS (text field).

- **Choose by length and editability:** label for a little read-only text, text field for a short entry, text view for everything longer or formatted. [HIG](https://developer.apple.com/design/human-interface-guidelines/text-views#Best-practices)
- **For rich-text editing use `TextEditor` bound to an `AttributedString` (26+)** instead of wrapping `UITextView`/`NSTextView` just to get bold and italics; `AttributedTextSelection` tracks the styled selection. [SwiftUI](https://developer.apple.com/documentation/swiftui/texteditor/init(text:selection:))
- **Let people select and copy useful read-only text** such as error messages, serial numbers, or IP addresses. `.textSelection(.enabled)` [HIG](https://developer.apple.com/design/human-interface-guidelines/text-views#Best-practices)
- **Match the keyboard to the content** (email, URL, number pad) when editing on iOS/iPadOS. `.keyboardType(_:)`, `.textContentType(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/text-views#iOS-iPadOS)
- **Support find in long documents** through the standard find navigator, which also fills the Mac Edit > Find menu. `.findNavigator(isPresented:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu)

Checklist: Dynamic Type text styles; test with Bold Text and larger sizes; system label color by default.

SwiftUI: `TextEditor`, `Text`. UIKit `UITextView`, AppKit `NSTextView`.
Platforms: tvOS: text views display only; editable text uses text fields. [HIG](https://developer.apple.com/design/human-interface-guidelines/text-views#tvOS)

## Web views

Use for: showing web content briefly without leaving the app (HTML mail, a help page, a sign-up form you host). Not for: general browsing (send people to Safari or use `SFSafariViewController`).

- **Don't rebuild Safari in a web view.** No address bar, tabs, or bookmarks; when people need to browse, hand off to Safari. [HIG](https://developer.apple.com/design/human-interface-guidelines/web-views#Best-practices)
- **Add back and forward controls when people may follow links to several pages**, because a web view doesn't show them by default. With `WebPage`, drive toolbar buttons from its `backForwardList`. [HIG](https://developer.apple.com/design/human-interface-guidelines/web-views#Best-practices)

SwiftUI: `WebView(page)` with `WebPage` (WebKit, iOS/iPadOS/macOS/visionOS 26+); `.webViewBackForwardNavigationGestures(_:)`. Before 26: wrap `WKWebView`.
Platforms: not available on tvOS or watchOS.
