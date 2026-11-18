# Inclusion, right-to-left, and localization-friendly layout

Sources: [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion), [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left), [Color](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type). Dev docs: `/documentation/swiftui/preparing-views-for-localization`.

## Inclusive copy

- **Address people as "you"; keep "we" for the app or company.** "The user" sounds distant, and "we" used for the reader can read as condescending. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Define a technical term before using it, or replace it with plain words.** Plain sentences also translate better. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Replace idioms and slang with literal phrasing.** Some idioms have exclusionary origins ("grandfathered in"), and all of them break in translation. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Use humor rarely, if at all.** It doesn't travel across cultures and gets old on the tenth view of the same empty state. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Welcoming-language)
- **Write without gendered pronouns when gender is irrelevant.** Use plurals or role nouns ("Members can edit"), which also avoids gender-agreement problems in localized strings. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)
- **Never use a disability as a metaphor for something bad; write people-first.** Lead with the person's goals; ask a community how it self-identifies. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Accessibility)

Quick rewrites agents should apply when generating UI strings:

| Avoid | Prefer |
|---|---|
| "The user must enable notifications" | "Turn on notifications to get reminders" |
| "He or she can share his or her list" | "Members can share lists" |
| "Blacklist / whitelist" | "Block list / allow list" |
| "Sanity check" | "Quick check" |
| "Crippled / lame / blind to" (as negatives) | Say what is actually wrong: "limited", "weak", "unaware of" |
| "Whoopsie! We goofed :)" | "Couldn't save the note. Check your connection and try again." |

## Personal data and assumptions

- **Don't ask for gender unless you need it; if you do, offer more than two options.** Include nonbinary, self-identify, and decline to state, and consider asking for pronouns. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)
- **Don't build forms around one family or life shape.** "Mother/Father" fields, a single "spouse", or two-parent family plans exclude many households; use "Parent or guardian", "Partner", "Family member". [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Avoiding-stereotypes)
- **Choose security questions everyone can answer.** College, first car, or travel questions assume a life many people haven't had; prefer universal ones (first friend's name). [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Avoiding-stereotypes)
- **Let people customize avatars, emoji, and characters instead of assigning a gender.** For a generic person glyph use a nongendered SF Symbol (`person`, `figure.stand`). [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Gender-identity)

## Imagery

- **Show a real range of people: race, age, body type, ability, family form.** A fitness app's demo moves come from varied bodies, including people with disabilities. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#People-and-settings)
- **Avoid role stereotypes.** Not only male doctors and female nurses; not villains coded by ethnicity. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#People-and-settings)
- **Keep settings relatable.** Showy affluence in sample content can make the app feel out of touch. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#People-and-settings)
- **Check color meaning per locale.** White, red, and green carry different meanings across cultures; if color signals something, verify it signals the same thing everywhere you ship. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Languages)

## Right-to-left: what SwiftUI does for you

SwiftUI mirrors layout automatically when the locale is RTL (Arabic, Hebrew, Persian, Urdu):
`HStack` order, `.leading`/`.trailing` alignment and padding, navigation and back chevrons,
`List` disclosure indicators, `Slider` and `ProgressView` direction, swipe-action edges, and SF
Symbols that have directional variants. Your job is to avoid defeating it.

- **Use `.leading`/`.trailing`, never `.left`/`.right` or hard-coded x offsets.** Edge sets, `Alignment`, `alignmentGuide`, and `padding(.leading, ...)` all mirror; absolute offsets and `.left` don't. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Text-alignment)
- **Don't mirror a whole view to "fix" RTL.** `.flipsForRightToLeftLayoutDirection(true)` mirrors pixels; use it only on a custom directional image or drawing that lacks an RTL variant. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Interface-icons)
- **Read `@Environment(\.layoutDirection)` in custom drawing and gestures.** A custom swipe-to-advance or a `Canvas` progress arc must reverse its direction; a map pan must not. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Controls)
- **Keep direction for things that point at real directions or screen areas.** "Text align right", a compass, a "move window to the right" control stay as they are. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Controls)

## Right-to-left: text and numbers

- **Align short labels (one or two lines) with the interface; align paragraphs with their own language.** An English paragraph in an Arabic UI stays left-aligned; `.leading` follows the UI direction, so set paragraph alignment from the content's language. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Text-alignment)
- **Mirror the alignment of every item in a list, even items in another script.** Mixed alignment in one list is hard to scan. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Text-alignment)
- **Never reverse the digits of a number.** Phone numbers, card numbers, and "541" read the same in every locale. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Numbers-and-characters)
- **Reverse sequences of numerals that show progress or order, not the numerals.** Slider min/max labels, rating scales, and step indicators "1 2 3" run right to left. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Numbers-and-characters)
- **Let the system pick the numeral system.** Format with `value.formatted()`, `Date.FormatStyle`, and `.currency(code:)`; Arabic locales may use Eastern Arabic digits, Hebrew uses Western. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Numbers-and-characters)
- **Size RTL text about 2 pt larger next to all-caps Latin text.** Arabic and Hebrew have no capitals and look small beside uppercase labels. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Controls)

## Which icons and images flip

| Flip in RTL | Don't flip |
|---|---|
| Back/forward, next/previous, chevrons for navigation order | Logos, even with text in them |
| Progress, sliders, rating direction, step order | Checkmark and other universal marks |
| Icons depicting lines of text or reading direction (`list.bullet`, paragraph glyphs) | Clocks, real-world objects; icons that mean a literal side ("align left") |
| Icons showing forward/backward motion (speaker sound waves, undo/redo arrows) | Tools slanted for right-handed use (pen, brush) |
| Order of a row of images when order matters (chronological, ranked) | Photos, illustrations, artwork (make a new version if direction is baked in) |
| A badge that represents actual UI that itself flips | The prohibition slash, magnifying glass, or a handed tool inside a flipped base |

- **Use SF Symbols; they ship RTL variants and localized glyphs (signature, rich text, I-beam) for Arabic and Hebrew.** For custom symbols and images, set their direction in the asset catalog instead of flipping in code. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Interface-icons)
- **Rebalance complex custom icons rather than mirroring blindly.** A cart badge may need to move to stay balanced; a tool inside the icon keeps its handedness while the base flips. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Interface-icons)
- **Replace letters inside custom icons.** Make a localized version when the icon shows script (font size "Aa"), or a text-free design when letters are incidental. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Interface-icons)
- **Never flip a copyrighted image.** Flipping can change meaning and may violate the license. [HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left#Images)

## Localization-friendly layout

These follow from the Dynamic Type and RTL rules: a layout that reflows at AX sizes and mirrors
cleanly usually survives translation too.

- **Let text grow in both directions.** Translations into German, Finnish, or Russian are often far longer than English, while CJK is shorter but taller; never fix button or label widths, and allow wrapping. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Languages)
- **Build strings from whole sentences with placeholders, never by concatenation.** Word order changes per language; use `Text("\(count) photos selected")` with string catalog plural variants, and add `comment:` so translators know the context. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Languages)
- **Put no text in images.** Text in images can't be translated, scaled, or read by VoiceOver. [HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion#Languages)
- **Keep accessibility labels localized too.** `accessibilityLabel("Favorite")` takes a `LocalizedStringKey`; a label passed as a non-localized `String` variable won't be translated. [HIG](https://developer.apple.com/design/human-interface-guidelines/voiceover#Descriptions)

## Testing RTL and localization

- Xcode scheme > Run > Options > App Language: "Right-to-Left Pseudolanguage" mirrors the UI with
  English strings; "Double-Length Pseudolanguage" exposes truncation; also run in Arabic or Hebrew.
- Previews: `.environment(\.layoutDirection, .rightToLeft)` and `.environment(\.locale, Locale(identifier: "ar"))`.
- Check: navigation chevrons, sliders and progress, swipe actions, custom drawings and gestures,
  number formatting, mixed-script lists, and that no logo or photo got mirrored.
