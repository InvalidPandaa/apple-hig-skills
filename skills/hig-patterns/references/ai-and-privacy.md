# Generative AI, machine learning, privacy and permissions

Sources: [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai), [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning), [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy), [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)

## Generative AI

The Generative AI page was added in June 2025 and revised on June 8, 2026 with guidance on refining results, feedback during generation, and choosing a model type. (2026)

### Before building
- **Use AI only where it adds clear value** (saves time, improves communication, helps creativity), not as decoration. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Best-practices)
- **Keep the app useful when AI is unavailable or declined.** Prefer a non-AI path; Foundation Models needs a compatible device with Apple Intelligence on. Check `SystemLanguageModel.default.availability` (iOS 26+) and hide or explain the feature by reason. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Best-practices), [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Models-and-datasets)
- **Pick the model for privacy as well as capability.** On-device first (private, fast, offline); with a server model, send the minimum, say what leaves the device, and state whether it's stored or used for training. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Privacy)
- **Keep the model swappable behind the UI** so later models don't force a redesign. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Continuous-improvement)

```swift
switch SystemLanguageModel.default.availability {
case .available:
    Button("Summarize", systemImage: "text.append") { summarize() }
case .unavailable(.appleIntelligenceNotEnabled):
    Text("Turn on Apple Intelligence in Settings to get summaries.")
case .unavailable(.modelNotReady):
    ProgressView("Preparing summaries")      // transient: model downloading
case .unavailable:
    EmptyView()                              // device not eligible: manual path only
}
```

### Transparency and control
- **Label AI features and AI-made content;** never let people think a human wrote it. Follow local disclosure laws. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Transparency)
- **State capabilities and limits up front,** with curated example prompts for open-ended inputs and an explanation when results are poor. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Transparency)
- **Keep people in charge:** they can dismiss new content and revert or retry any transformation. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Best-practices)
- **Don't infer personal or cultural traits when generating people;** ask, and test with a diverse group for stereotypes. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Best-practices)

### Inputs
- **Seed the input with varied example requests.** [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Inputs)
- **Limit hallucination risk by scope:** don't ask the model for facts it can't verify, say outputs may contain errors, and keep AI out of places where an error could harm someone. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Inputs)
- **No automated destructive or hard-to-undo actions** (deleting photos, purchases); ask for confirmation before significant actions on someone's behalf. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Inputs)

### Outputs (2026 refinements)
- **Put Edit, Undo, Retry, or Adjust right next to the generated content, and visibly acknowledge when a refinement took effect.** (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **During generation, say what's actually happening** ("Checking your calendar for open evenings"), not "Processing…"; on failure, say what went wrong in plain words with a next step. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **Design for latency:** a loading state, streaming partial output (`LanguageModelSession.streamResponse(to:options:)`, iOS 26+), or background generation while people keep working. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **When a request is blocked, coach toward a better one** with example requests, instead of a dead end. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **Consider several meaningfully different results to pick from.** [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **Test misuse, vague, sensitive, and out-of-scope prompts; guard against reproducing copyrighted work** (curated prompts, protected base models). [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)

### Feedback on outputs
- **Offer voluntary, unobtrusive feedback** (thumbs up/down next to the result, optional detail for complex issues), and act on it quickly. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Continuous-improvement)

## Machine learning patterns

Classify each ML feature first; the stricter the classification, the higher the bar for accuracy. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#The-role-of-machine-learning-in-your-app)

| Axis | Higher bar when |
|---|---|
| Critical vs complementary | The app fails without it |
| Private vs public data | Data is sensitive (health, finance) |
| Proactive vs reactive | Results appear unasked |
| Visible vs invisible | Invisible: hard to judge or give feedback on |
| Dynamic vs static | Dynamic: needs calibration and feedback loops |

- **Explicit feedback: ask rarely, always voluntary, and label options by consequence** ("Suggest less pop music", not "Dislike"); apply it instantly and persist it. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Explicit-feedback)
- **Implicit feedback: secure it, tell people how it flows between apps, and let them limit it;** prioritize recent signals, combine several, and keep room for exploration. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Implicit-feedback)
- **Withhold suggestions based on private or sensitive topics;** devices get shared. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Implicit-feedback)
- **Calibration only if the feature can't work without it:** once, early, quick, with a visible goal and progress, cancellable at any time without judgment, editable later. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Calibration)
- **Plan for mistakes in proportion to their cost;** be strictest with proactive features. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Mistakes)
- **Corrections: use the same familiar controls the automation used, apply immediately, persist, and prefer guided alternatives to freeform edits.** Don't rely on corrections to excuse weak results. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Corrections)
- **Multiple options: a few diverse ones, most likely first and preselected, differences called out.** [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Multiple-options)
- **Confidence: show it only once you know it tracks quality;** translate it into plain concepts or actions ("Good time to buy"), and suppress low-confidence proactive results. Raw percentages only where people expect statistics (weather, polls). [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Confidence)
- **Attribution: factual and neutral** ("Because you read nonfiction", not "Because you love…"), neither vague nor creepily specific. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Attribution)
- **Limitations: set expectations, show how to get good results, explain bad ones** (Memoji: "doesn't work well in the dark"), suggest alternatives instead of empty results, and announce when a limit is lifted. [HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning#Limitations)

## Privacy and permission requests

### When to ask

| Situation | Timing |
|---|---|
| App is meaningless without it (navigation needs location; AR game needs surroundings) | At launch or in onboarding, with an explanation |
| One feature needs it | When people first use that feature |
| One-off location need | `LocationButton`, no standing permission |
| Photos for import | `PhotosPicker`: runs out of process, needs no library permission |
| A few contacts | `ContactAccessButton` (iOS 18+) instead of full contacts access |
| Notifications | After an action that makes alerts useful |
| App tracking (ATT) | Before collecting any tracking data, with the system alert |

- **Ask only for data you need, as narrowly as possible, and only once interest is shown.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Best-practices)
- **Avoid launch-time requests unless the need is obvious.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission)
- **Purpose strings (`NSCameraUsageDescription`, `NSLocationWhenInUseUsageDescription`, `NSUserTrackingUsageDescription` …): one complete, active, specific sentence in sentence case with a period.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission)

| Good | Bad |
|---|---|
| "The app uses your location to show stores near you." | "Location is needed for a better experience." (vague, passive) |
| "The app scans receipts you photograph to fill in expenses." | "Turn on camera access." (no reason) |

- **Pre-alert screen only if context can't explain the request:** exactly one button ("Continue" or "Next", never "Allow"), no close, cancel, or skip, unless a legal consent requires it. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Pre-alert-screens-windows-or-views)
- **Tracking: no incentives, no fake request screens, no image of the alert, no arrows or annotations behind it.** Consent screens required by local law are allowed. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Tracking-requests)
- **When access is denied, keep the rest of the app working** and show a `ContentUnavailableView` that explains what's missing with a button to the app's page in Settings (`UIApplication.openSettingsURLString`). People change choices in Settings > Privacy. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission)
- **Respect Hide My Email and Mail Privacy Protection.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Best-practices)
- **Process on device where possible.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Best-practices)
- **For AI features, ask before using personal data or usage data,** use the minimum, offer opt-out, get explicit permission for training use; stricter rules apply to kids' apps. [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Privacy)

### Location button
- **Use `LocationButton` for "share my location now" moments** (find a store, tag a post). The first tap shows a one-time explainer alert; later taps grant one-time access directly. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Location-button)
- **Customize only title variant, filled or outlined glyph, colors, and corner radius;** the text must fit at all Dynamic Type sizes and languages, and a button the system judges illegible won't get location. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Location-button)

### Protecting data
- **Passkeys over passwords; two-factor if passwords remain; Face ID / Touch ID / Optic ID to reopen signed-in apps** (Local Authentication). [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Protecting-data)
- **Secrets in the keychain, never in plain files, and no homemade auth schemes.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Protecting-data)
- **macOS: sandbox (required on the Mac App Store), Developer ID outside it, and don't assume a single signed-in user.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#macOS)
- **visionOS: ARKit data needs a Full Space and permission; gaze isn't exposed (hover effects are system-drawn); camera features from iOS ports become import options.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#visionOS)
- **App Store privacy details must match what the app collects.** [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)
