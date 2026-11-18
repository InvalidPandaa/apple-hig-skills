---
name: hig-patterns
description: Use when designing, building, or reviewing app behavior on Apple platforms - first launch, onboarding, sign-in or sign-up, permission prompts, settings screens, rating prompts, loading and empty states, delete confirmations, undo, notifications, haptics, search, saving documents, sharing, sheets and full screen, audio or video playback, AI features - or when a brief asks for a theme picker, forced sign-up, prompts at launch, or a confirmation on every delete.
---
# Apple HIG: UX patterns and behavior

Get people to their content at once, ask for nothing until a feature needs it, and make actions reversible instead of guarded. Where the system already owns a choice (appearance, text size, biometrics, permissions), defer to it instead of rebuilding it.

## Quick decisions

| Situation | Do this (API) | Source |
|---|---|---|
| Feature needs camera, mic, photos, contacts, location | Request when the person first uses that feature, with a specific purpose string (`NS…UsageDescription`). Ask at launch only if the app can't work at all without it | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission) |
| Location for a single action (find a store, tag a post) | `LocationButton` (CoreLocationUI): one-time grant without repeated alerts | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy#Location-button) |
| Context alone doesn't explain a permission | Optional pre-alert view with exactly one button ("Continue"), no Cancel or close | [privacy](https://developer.apple.com/design/human-interface-guidelines/privacy#Pre-alert-screens-windows-or-views) |
| Does the app need an account? | Only if core functionality requires one. Let people browse and use the app first, then ask at the point of value (checkout, sync) | [managing-accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices) |
| Account is required | Explain why in the sign-in view, offer `SignInWithAppleButton` (AuthenticationServices) at least as large as the other options, otherwise prefer passkeys | [sign-in-with-apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple) |
| Delete of something that can come back (row, file, message) | Delete at once and register undo through `@Environment(\.undoManager)`. No confirmation | [feedback](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices) |
| Data loss that is irreversible *and* unexpected | `.confirmationDialog` with a `role: .destructive` button | [feedback](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices) |
| Content is loading | Render the layout right away with placeholders (`.redacted(reason: .placeholder)`); `ProgressView(value:)` when duration is known; a bare spinner only when there is nothing to show | [loading](https://developer.apple.com/design/human-interface-guidelines/loading#Best-practices) |
| Nothing to show (empty list, no results, offline) | `ContentUnavailableView` with a reason and a next step; `ContentUnavailableView.search` inside `.searchable` | [feedback](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices) |
| Teaching a feature | TipKit `.popoverTip` / `TipView` next to the feature; a separate onboarding flow only if it's a prerequisite | [onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices) |
| Asking for a rating | `@Environment(\.requestReview)` after a completed meaningful task, at a natural pause | [ratings-and-reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices) |
| Adding an in-app settings screen | Only general, rarely changed app options; task options go in the screen they affect; macOS uses the `Settings` scene (Command-Comma) | [settings](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices) |
| Short, scoped task | `.sheet` with a title that names the task; for immersive or multistep editing use `.fullScreenCover` | [modality](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices) |
| Sheet buttons (iOS 26+) | `Button(role: .close)` or `.cancel` to leave, `Button(role: .confirm)` to commit; `.interactiveDismissDisabled(hasUnsavedEdits)` plus a save/discard choice | [modality](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices) |
| Documents | Autosave (`DocumentGroup`); no mandatory Save step | [file-management](https://developer.apple.com/design/human-interface-guidelines/file-management#Saving-work) |
| Search matters in the app | `.searchable` in a primary spot: `Tab(role: .search)` in a tab app or the toolbar; `.searchSuggestions` | [searching](https://developer.apple.com/design/human-interface-guidelines/searching#Best-practices) |
| Generated (AI) content | Edit, Undo, Retry next to the result; progress text that says what's happening; non-AI fallback when `SystemLanguageModel.default.availability` isn't `.available` (iOS 26+) | [generative-ai](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs) |

## Rules

### First run
- **Make the launch screen a blank copy of the first screen.** No logo, no text, no ads; it only exists to make launch feel instant. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens)
- **Restore where people left off.** Scroll position, selection, open windows; use `@SceneStorage` and state restoration so relaunch isn't a reset. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Best-practices)
- **Prefer in-context tips over a tour.** If onboarding is unavoidable, keep it short, interactive, and skippable, never show it again after a skip, and keep it reachable from help or settings. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)
- **Ship good defaults and postpone setup.** Customization and nonessential questions wait until people reach the feature. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-requests)

### Permissions and privacy
- **Request the narrowest access, at the moment of need.** A purpose string is one active, specific sentence ending in a period ("The app uses your location to show stores near you."), never "for a better experience". [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission)
- **Never precede the tracking alert with incentives, fake alerts, or arrows pointing at Allow.** App Review rejects these. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Tracking-requests)
- **Keep secrets in the keychain and use system auth.** Passkeys, Sign in with Apple, Password AutoFill; no homemade schemes, no plain-text passwords. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#Protecting-data)

### Accounts
- **Delay sign-in; in commerce, allow guest checkout and offer account creation after the purchase.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)
- **With Sign in with Apple, don't ask for a password or for a personal email in place of the relay address.** Mark extra fields as required or optional. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Collecting-data)
- **If people can create an account in the app, they must be able to delete it in the app** (or via a direct, easy-to-find link), and revoke SIWA tokens. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Deleting-accounts)
- **Name the auth method ("Sign In with Face ID") and only methods the device has** (`LABiometryType`); no in-app "enable Face ID" switch. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)

### Settings
- **Don't rebuild systemwide settings in the app.** Appearance, text size, accessibility, scrolling, authentication: people set these once in Settings and expect every app to follow. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Detect instead of asking.** Dark Mode, connected controllers, locale: read them, don't make them settings. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Put view options (sort, filter, show/hide) in the view, not in settings.** [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Task-specific-options)
- **macOS: settings live in the App menu, never a toolbar button;** the window titles itself after the pane and reopens the last pane. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#macOS)

### Feedback, loading, empty states
- **Match the interruption to the stakes.** Status goes inline (toolbar subtitle, badge); alerts are for critical, actionable news only; don't confirm routine success. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **When something can't be done, say why and what to do next.** An empty or failed state always carries a reason and, if possible, an action. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)
- **Use determinate progress when you can, with specific text instead of "Loading…".** [HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#Best-practices)
- **watchOS: avoid indeterminate spinners;** show content instantly or promise a notification when done. [HIG](https://developer.apple.com/design/human-interface-guidelines/feedback#watchOS)

### Undo
- **Don't cap undo, label it ("Undo Delete Photo"), and show the result** by scrolling to or highlighting what changed. [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Best-practices)
- **Use the system entry points:** Edit menu with Command-Z / Shift-Command-Z on Mac, shake and three-finger swipe on iPhone and iPad; toolbar undo buttons only when the app truly needs them. [HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo#Platform-considerations)

### Modality
- **Present modally only for a clear benefit, keep it short, and never stack a second modal** (close the first, then present). Only one alert at a time. [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Always provide an obvious way out, and confirm only if closing would lose user-created content.** [HIG](https://developer.apple.com/design/human-interface-guidelines/modality#Best-practices)
- **Pair Done with Cancel (or Back), never all three.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sheets#Best-practices)

### Notifications and haptics
- **Pick the honest interruption level.** Time Sensitive only for things happening now or within the hour; never for marketing. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Best-practices)
- **Use haptics with their documented meaning, sparingly, and alongside visual feedback** (`.sensoryFeedback(.success, trigger:)`). [HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)

### AI features
- **Disclose AI and keep people in control:** label generated content, put Edit, Undo, Retry next to it, and acknowledge when a refinement took effect. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **Describe the actual work while generating** ("Comparing prices across your saved stores"), and on failure give a plain cause and a next step. (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Outputs)
- **Prefer on-device models; with a server model, say what leaves the device and whether it's kept or used for training.** (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Privacy)

### Basics (already known, just check)
- Secure fields for secrets, never prefilled passwords. Pickers over typing. Validate fields as people type. `ShareLink` in the toolbar. System video player (`VideoPlayer`, `AVPlayerViewController`). Respect the silent switch via the right `AVAudioSession` category. Pause games and media when people switch away.

## Brief conflicts

When a request below appears, say that it conflicts with the HIG (with the link), propose the alternative, then do what the person decides.

| Request | Why it conflicts | Propose instead |
|---|---|---|
| "Add a Light/Dark/System theme picker" | App-level appearance overrides make people set it twice and look broken when the system changes ([dark-mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices), [settings](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)) | Follow the system appearance. A content-only option inside a task (a reader's page color) is fine |
| "Add a text size slider" | Duplicates Dynamic Type ([settings](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)) | Support Dynamic Type fully; offer zoom inside a document or reading view if needed |
| "Add an Enable Face ID toggle" | Biometrics are turned on systemwide ([managing-accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)) | Offer biometric unlock automatically when the device supports it (`LAContext`), with the account's normal sign-in as fallback |
| "Add a haptics on/off switch" | System controls already follow the systemwide haptics setting; a copy implies it doesn't apply ([settings](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)) | Rely on the system setting for standard feedback; a mute option is right only for custom or gameplay haptics ([playing-haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Best-practices)) |
| "Force sign-up before anything" | People abandon apps that demand commitment first ([managing-accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)) | Browse or try without an account; sign in at the point of value; if required, explain why, then SIWA + passkeys |
| "Ask for all permissions on first launch" | Requests without visible need erode trust ([privacy](https://developer.apple.com/design/human-interface-guidelines/privacy#Requesting-permission)) | Ask per feature at first use; onboarding only for access the app can't run without |
| "Pre-permission screen with Allow / Not now" | Two choices or an "Allow"-like button is manipulative ([privacy](https://developer.apple.com/design/human-interface-guidelines/privacy#Pre-alert-screens-windows-or-views)) | One "Continue" button that opens the system alert |
| "Show a rating prompt after launch / onboarding" | No opinion formed yet; tends to draw negative reviews ([ratings-and-reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)) | `requestReview` after a finished task, weeks apart; the system caps it at 3 per 365 days |
| "Custom 'Do you love our app?' dialog" | The system prompt is the expected, nonintrusive path ([ratings-and-reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)) | The system prompt via `requestReview`, triggered by engagement |
| "Confirm every delete" | Warnings are for unexpected, irreversible loss, not the expected result of Delete ([feedback](https://developer.apple.com/design/human-interface-guidelines/feedback#Best-practices)) | Delete immediately with undo; a Recently Deleted area; confirm only permanent or bulk-irreversible actions |
| "Multi-page feature tour at first launch" | Long tours overwhelm and aren't retained ([onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)) | TipKit tips in context; if needed, a short, interactive, skippable flow |
| "Logo splash for 2-3 seconds / branded launch screen" | Launch screens aren't for branding ([launching](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens)) | Launch screen = first screen; a brief splash at the start of onboarding if branding is essential |
| "Send promos as push notifications" | Needs explicit opt-in and an in-app toggle; never Time Sensitive ([managing-notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Sending-marketing-notifications)) | Separate marketing opt-in screen + in-app notification settings |
| "Let the AI act for the user automatically" (delete, buy, send) | Destructive or hard-to-undo actions need confirmation ([generative-ai](https://developer.apple.com/design/human-interface-guidelines/generative-ai#Inputs)) | AI proposes, person confirms; keep undo |
| "Settings button in the Mac toolbar" | Settings belong in the App menu ([settings](https://developer.apple.com/design/human-interface-guidelines/settings#macOS)) | App menu item via the `Settings` scene, Command-Comma |

## Common mistakes
- Silently building a requested theme picker, haptics toggle, or Face ID switch without flagging the conflict.
- Confirmation alerts on routine deletes, and no undo at all; on a Mac port, no Edit menu Undo or Command-Z.
- Full-screen spinner on a blank view instead of the real layout with placeholders; "Loading…" or "Processing…" as the only text.
- Blank screen for empty or failed data instead of `ContentUnavailableView` with a next step.
- All permission prompts in a row at launch; vague purpose strings; a pre-alert screen with a "Not now" escape.
- A sheet that opens another sheet; Done without Cancel; swipe-to-dismiss that silently drops typed content.
- A success alert ("Saved!") after every action; `.timeSensitive` on routine notifications.
- Rating prompt on launch or mid-task; account wall before any value; no in-app account deletion.
- Generative feature with no Retry/Undo, no disclosure that AI made the content, and no fallback when Apple Intelligence is off.
- Help text that explains standard controls; tips repeated to people who already used the feature.

## References
- `references/first-run-and-accounts.md`: launch screens, onboarding, tips and tooltips, sign-in, Sign in with Apple, account deletion, rating prompts.
- `references/feedback-and-status.md`: feedback levels, loading and progress, empty states, haptics, notifications and interruption levels, undo and redo.
- `references/data-and-content.md`: forms and data entry, search and Spotlight, settings screens, drag and drop, documents and saving, sharing and collaboration, printing, charts.
- `references/modes-and-windows.md`: modality and sheets, full screen, multitasking and backgrounding, audio sessions, video playback, live TV apps, workouts.
- `references/ai-and-privacy.md`: generative AI (incl. 2026 guidance on refining results and feedback during generation), ML patterns, permission requests, tracking, location button.

## Look it up live
Slugs: `launching onboarding managing-accounts sign-in-with-apple offering-help ratings-and-reviews feedback loading progress-indicators playing-haptics managing-notifications undo-and-redo entering-data searching settings drag-and-drop file-management collaboration-and-sharing printing charting-data modality sheets going-full-screen multitasking playing-audio playing-video live-viewing-apps workouts generative-ai machine-learning privacy`

```
python3 ../apple-hig/scripts/hig.py fetch privacy --section "Requesting permission"
python3 ../apple-hig/scripts/hig.py fetch /documentation/swiftui/contentunavailableview
```
