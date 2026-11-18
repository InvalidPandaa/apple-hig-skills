# First run, accounts, help, and ratings

Sources: [Launching](https://developer.apple.com/design/human-interface-guidelines/launching), [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding), [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts), [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple), [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help), [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)

The order on first run is: launch screen (system, instant) → first screen or optional splash → optional short onboarding → the app. Sign-in, permissions, ratings, and purchases are not part of this sequence unless the app cannot work without them.

## Launching

- **Aim for a first screen within a couple of seconds.** Anything slower reads as broken; defer network work and large asset downloads. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Best-practices)
- **Provide a launch screen on iOS, iPadOS, and tvOS only.** macOS, visionOS, and watchOS don't use one. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Best-practices)
- **Make the launch screen look like the empty first screen.** Same background and bars, current orientation and appearance; if the first screen starts as a solid color, the launch screen is just that color. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens)
- **Keep text, logos, and branding off the launch screen.** It isn't localized and isn't a splash or About window. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Launch-screens)
- **If branding is required, show a short splash at the start of onboarding** (or right after launch if there's no onboarding), only as long as a glance takes. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-content)
- **Restore state in detail.** Navigation path, scroll position, selected tab, window frames. SwiftUI: `@SceneStorage` for per-scene UI state; UIKit: state restoration. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#Best-practices)
- **iOS: launch in the device's current orientation;** a landscape-only app must handle both landscape directions. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#iOS-iPadOS)
- **tvOS live-viewing apps: consider starting playback automatically after a few idle seconds.** [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#tvOS)
- **visionOS: open in the Shared Space with a window first, even for immersive apps,** and let people choose when to enter a Full Space. [HIG](https://developer.apple.com/design/human-interface-guidelines/launching#visionOS)

## Onboarding

- **Ask first whether onboarding is needed at all.** The best case is an app people understand by using it. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- **Teach by doing.** Let people try the gesture or action safely instead of reading slides. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)
- **Prefer a set of contextual tips over one up-front flow,** shown next to the area they describe (TipKit). [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)
- **If a prerequisite flow is necessary, keep it brief and light on facts to memorize.** As a working target, a few screens, each with one idea. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)
- **Make tutorials optional, don't re-show them after a skip, and keep them findable** in help, account, or settings. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)
- **Teach your app, not the device.** No slides on how to tap, swipe, or use Control Center. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Best-practices)
- **Bundle enough content that people can start before downloads finish.** [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-content)
- **Leave license terms to the App Store page;** if legally required in-app, integrate them without blocking. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-content)
- **Postpone setup and customization; ship defaults that work for most people.** [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-requests)
- **Put a permission request in onboarding only if the app can't function without it;** otherwise ask at first use of the feature. [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-requests)
- **Let people use the app before asking for ratings or purchases.** [HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding#Additional-requests)

## Offering help and tips

- **Fit help to the task size:** an inline hint for a one- or two-step task, a tutorial for a multistep goal; always dismissible. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Best-practices)
- **Use the platform's vocabulary and the current input device.** "Tap" on iPhone, "click" on Mac; no game-controller art when someone uses the Siri Remote. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Best-practices)
- **Don't explain standard controls;** explain what your specific button does. Teach nonstandard input with a short animation rather than paragraphs. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Best-practices)
- **Choose the tip style by layout:** `.popoverTip(_:)` keeps the content flow; `TipView` inline keeps surrounding content visible. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Creating-tips)
- **Reserve tips for features of about three actions or fewer,** one or two action-oriented sentences, nothing promotional. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Creating-tips)
- **Target tips with eligibility rules and throttle them** (for example, one tip per 24 hours); hide a tip once the person has used the feature. TipKit: a tip's `rules` (parameter or event based) plus `try Tips.configure([.displayFrequency(.daily)])`. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Creating-tips)
- **Use the filled symbol of the feature in the tip,** unless the tip points straight at that same symbol. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Creating-tips)
- **Add a tip button only to take people to related settings or more information.** [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#Creating-tips)
- **macOS and visionOS tooltips (`.help(_:)`):** describe one control, start with a verb, skip the control's name, stay within about 60–75 characters, sentence case. [HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help#macOS-visionOS)

```swift
struct FavoriteTip: Tip {
    var title: Text { Text("Save for later") }
    var message: Text? { Text("Tap the star to keep this recipe in Favorites.") }
    var image: Image? { Image(systemName: "star.fill") }
}
// .popoverTip(FavoriteTip()) on the star button
```

## Accounts

### When an account is justified
- **Require an account only when core functionality needs one** (sync of personal data, messaging, purchases tied to identity). Otherwise the app works without it. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)
- **Postpone sign-in until it delivers something.** A shopping app lets people browse and fill a cart; sign-in comes at checkout. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)
- **State the reason and benefit in the sign-in view itself,** in a short friendly sentence. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)
- **Commerce: support guest checkout and offer account creation after the purchase,** reusing the name and email from Apple Pay. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)

### Authentication
- **Offer Sign in with Apple, and otherwise prefer passkeys over passwords;** if passwords stay, add two-factor. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)
- **Label the method on the button** ("Sign In with Face ID", not "Sign In") and mention only what the device supports (`LABiometryType`). [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)
- **No in-app opt-in switch for biometrics;** people enable it systemwide. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)
- **Never call an app credential a "passcode";** that word means the device passcode. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)

### Sign in with Apple
- **Make the SIWA button at least as large as other sign-in buttons and visible without scrolling.** SwiftUI: `SignInWithAppleButton(.signIn, onRequest:onCompletion:)` with `.signInWithAppleButtonStyle(.black / .white / .whiteOutline)` chosen for contrast with the background. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Displaying-buttons)
- **Respect the minimums:** 140 × 30 pt, margin of one tenth of the button height. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Button-size-and-corner-radius)
- **Custom buttons keep the approved titles** (Sign in / Sign up / Continue with Apple), black or white only, Apple-provided logo artwork; App Review checks them. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button)
- **After SIWA completes, go straight into the app** with a welcome that uses the shared name or email; no extra optional forms. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)
- **Show "Using Sign in with Apple" in the account view.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)
- **Offer linking an existing account** when the shared email matches, or from account settings. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)
- **Don't ask for a password, and don't ask for a "real" email in place of a private relay address;** use order or phone numbers for support lookups. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Collecting-data)
- **Mark any extra data as required (legal) or optional (with the benefit),** and ask for optional data later, when a feature makes it useful. Declining optional data never locks features. [HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#Collecting-data)

### Deleting accounts
- **In-app account creation means in-app deletion,** not deactivation; or a direct link to the deletion web page, not buried in a policy. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Deleting-accounts)
- **Keep the app and web deletion flows equally simple.** [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Deleting-accounts)
- **Scheduled deletion is fine if immediate deletion is also offered;** tell people when deletion completes and notify them. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Deleting-accounts)
- **Explain that App Store subscriptions keep billing until cancelled,** and how to cancel or request a refund. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Deleting-accounts)
- **Revoke Sign in with Apple tokens on deletion.** [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Deleting-accounts)

### Platform specifics
- **tvOS: let people sign in on another device** (associated domains, SIWA), keep typed input minimal, use the email keyboard screen. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#tvOS)
- **tvOS shared accounts: pick up the current user's profile automatically** instead of a profile chooser every time. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#tvOS)
- **TV provider apps: use TV Provider Authentication;** no sign-out button when signed in at the system level. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#TV-provider-accounts)
- **watchOS: rely on iCloud Keychain for AutoFill** instead of typing credentials on the watch. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#watchOS)
- **macOS: don't assume one person is signed in;** fast user switching exists. [HIG](https://developer.apple.com/design/human-interface-guidelines/privacy#macOS)

## Ratings and reviews

- **Ask only after demonstrated engagement** (finished a level, completed a significant task); never on first launch or during onboarding. [HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)
- **Ask at a natural stopping point, never mid-task or mid-game.** [HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)
- **Space requests by at least a week or two,** and only after more engagement. [HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)
- **Use the system prompt;** the system shows it at most three times per app in 365 days, and may not show it at all, so never attach UI or logic to whether it appeared. [HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)
- **Weigh resetting the summary rating on a new version** against showing fewer ratings. [HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews#Best-practices)

```swift
@Environment(\.requestReview) private var requestReview
func didFinishExport() {
    exportCount += 1
    if exportCount >= 3, lastPrompt.distance(to: .now) > 14 * 86_400 {
        lastPrompt = .now
        requestReview()   // system decides whether to show
    }
}
```
