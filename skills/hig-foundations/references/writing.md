# Writing

Sources: [Writing](https://developer.apple.com/design/human-interface-guidelines/writing), [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#Content), [Menus](https://developer.apple.com/design/human-interface-guidelines/menus#Labels), [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#Content), [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications#Content), [Branding](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)

## Voice and tone

- **Define the voice once, from who the audience is and how they should feel,** and keep a term list so the same thing always has the same name. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Getting-started)
- **Vary tone with the situation:** plain and direct for a payment error, warmer for a reached goal. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Getting-started)
- **Cut every word that isn't needed; read it aloud when unsure.** [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Getting-started)
- **Plain language, no jargon, no gendered terms;** write so it localizes and reads well in VoiceOver. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Getting-started)
- **Brand voice may include occasional exclamation marks or emoji** where the brand calls for it, but never in errors or alerts. [HIG](https://developer.apple.com/design/human-interface-guidelines/branding#Best-practices)

## Labels and buttons

- **Start button and link labels with a verb, and be literal:** "Pay", not "Make it happen!"; "Learn more about pricing", not "Click here". [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Alert buttons: one or two words describing the result** ("Delete", "View All"); "OK" only in purely informational alerts; never "Yes"/"No"; the cancel button is always "Cancel". [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Buttons)
- **Segment labels are nouns or noun phrases.** [HIG](https://developer.apple.com/design/human-interface-guidelines/segmented-controls#Content)
- **Multi-step flows use one consistent vocabulary:** "Get Started" to begin, then either "Continue" or "Next" (pick one) or a label naming the next step, "Done" to finish. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Name settings for what they do when on;** people infer off. Add a short description if the label isn't enough; link straight to a setting rather than describing its path. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Use device-correct verbs:** tap on iPhone, iPad and Watch; click on Mac; "choose" when alert text has to mention a button, and name it by its exact title, unquoted. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Content)

## Capitalization

Choose a style per element type and apply it everywhere in the app. Title case reads formal, sentence case casual. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)

| Element | Style | Punctuation |
|---|---|---|
| Buttons, alert buttons | Title-style ("Save to Library") | None |
| Menu items | Title-style | None |
| Segmented control labels | Title-style | None |
| Alert title that is a fragment | Title-style | None |
| Alert title that is a full sentence | Sentence-style | Ending punctuation |
| Alert message | Sentence-style, complete sentences | Yes |
| Notification body | Sentence case, complete sentences | Yes; don't truncate yourself |

Title-style: capitalize all words but short function words (a, the, and, or, of, in, to...), and capitalize the final word no matter what it is. [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Labels)

Games may use their own style, but consistently. [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Labels)

## Pronouns and addressing people

- **Address people as "you", not "the user" or "the player".** [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Drop possessives where context is clear:** "Playlists", not "Your Playlists"; if you use "my" or "your", don't switch between them. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Avoid "we",** which leaves it unclear who is speaking ("Unable to Load Photos" instead of "We can't get your photos right now"). If used at all, reserve it for the company. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)

## Errors

- **Prevent the error first; if it happens, show it next to the cause.** [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Say how to fix it, not what was wrong:** "Enter a 5-digit ZIP code" beats "ZIP code is wrong"; "Use a date after today" beats "Past dates aren't allowed"; never a bare "Invalid input". [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **No blame, no "Oops"/"Uh-oh".** [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Alert titles describe what happened and why, in at most two lines;** never a bare "Error" or an error code. Don't explain the buttons. [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts#Content)
- **If many people hit the same error, change the interaction** instead of polishing the message. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)

## Screens, fields, empty states, delivery

- **Most important information first; split multiple ideas across screens.** [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Label every text field and show format hints as placeholder** (an example value, or a short description of what goes there). [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Empty states give the next step and a button for it;** don't put lasting information there, it disappears. `ContentUnavailableView` with a title, description and action. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Pick the channel by urgency:** inline text, alert, action sheet or notification. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)
- **Adapt length to the device:** brief on iPhone and Watch, brief and large on TV where several people may read it. [HIG](https://developer.apple.com/design/human-interface-guidelines/writing#Best-practices)

## Inclusive wording

- **Watch the tone:** an academic register signals "for experts only". [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Define technical terms or replace them; replace idioms and colloquialisms** (they don't translate and some have exclusionary origins). [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Use humor rarely;** it translates badly and wears thin on repetition. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Avoid unnecessary gender:** "Members can edit the shared list" instead of "his or her list". If gender is truly required, offer inclusive options and let people give pronouns. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)
- **People-first disability language; never use a disability as a metaphor for something bad.** [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Accessibility)
- **Don't assume shared experiences** (college, a first car) in examples or security questions. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Avoiding-stereotypes)

## Quick rewrite examples

| Before | After |
|---|---|
| "Oops! We couldn't save your note." | "Unable to Save Note" + "Check your connection and try again." |
| Button "Yes" | "Delete Draft" |
| "Click here to learn more" (iPhone) | "Learn More About Sync" |
| "Your Settings" / "My Library" mixed | "Settings" / "Library" |
| "Invalid date" | "Enter a date after today." |
| "The user can invite his friends" | "You can invite friends" |
