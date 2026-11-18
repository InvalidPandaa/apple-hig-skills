# Games

Sources: [Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games), [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls), [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards), [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Settings](https://developer.apple.com/design/human-interface-guidelines/settings), [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)

## What players expect
- **Play right after install.** Ship as much playable content as possible in the initial download, keep it to 30 minutes or less, fetch the rest in the background. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Jump-into-gameplay)
- **Good defaults without a settings trip:** resolution and quality from the device, paired controllers detected, system accessibility settings honored.
- **Learn by playing;** a written tutorial is a reference, not a gate.
- **Permission requests at the moment they matter** (hand tracking right before hands are first used); rating prompts only after real playtime.
- **Settings open with Esc in games** (Command-Comma in apps); Command-Q still quits. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Pause when people switch away, resume exactly where they were.** [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)

## Display
| Platform | Text default / min | Button default / min |
|---|---|---|
| iOS, iPadOS | 17 / 11 pt | 44×44 / 28×28 pt |
| macOS | 13 / 10 pt | 28×28 / 20×20 pt |
| tvOS | 29 / 23 pt | 66×66 / 56×56 pt |
| visionOS | 17 / 12 pt | 60×60 / 28×28 pt |
| watchOS | 16 / 12 pt | 44×44 / 28×28 pt |

[HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Look-stunning-on-every-display)
- **Resolution-independent art,** or match device resolution; vector art in visionOS because the system rescales it.
- **Respect safe areas** (rounded corners, camera housing, Dynamic Island, Home indicator).
- **In-game menus adapt to 16:10, 19.5:9, 4:3 and both orientations on iPhone/iPad** with relative layouts; device-specific layouts only as a last resort.
- **Support full screen** on Mac, iPhone, iPad; a Full Space on visionOS.
- **iPhone Duo:** playable in every pose; orientation lock is fine but fill the screen, prefer changing aspect ratio to letterboxing, fill unavoidable bars with art. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)

## Input per platform
| Platform | Default | Also |
|---|---|---|
| iOS | Touch | Controller |
| iPadOS | Touch | Controller, keyboard, mouse, trackpad, Pencil |
| macOS | Keyboard, mouse, trackpad | Controller, touch |
| tvOS | Remote | Controller, keyboard, mouse, trackpad |
| visionOS | Eyes and hands | Controller, keyboard, mouse, trackpad, spatial controller |
| watchOS | Touch | — |

[HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Enable-intuitive-interactions)
- **Always support the platform default; controllers are an addition.** Only tvOS and visionOS may require a controller (`GCRequiresControllerUserInteraction`); then detect its absence and ask people to connect one. [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Physical-controllers)
- **Watch for pointer-to-touch ports:** control size and menu behavior break first.

## Touch controls (iPhone, iPad)
Use the Touch Controller framework for virtual controls. [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Touch-controls)
- **Prefer direct interaction** (tap an object to select it) over adding a virtual button.
- **Movement on the left, camera on the right, both as large as possible;** spawn the thumbstick where the thumb lands; pan the camera with direct touch, not a second stick.
- **Frequent buttons near the thumb and at least 44×44 pt; menus at the top, at least 28×28 pt;** clear of the Home indicator and Dynamic Island.
- **Visible press state that shows around the finger, plus sound and haptics.**
- **Button art shows the action (a sword), never "A", "X", or "R1".**
- **Show controls only when relevant;** hide movement controls until a touch.
- **Fold combos into one control;** use double tap or touch and hold for variants (charged attack), one control for walk/sprint.

## Physical controllers
- **Detect paired controllers automatically; no manual setup.**
- **Show the connected controller's own labels and colors,** using the SF Symbols the Game Controller framework provides; with several controllers, match the one in use, per player in multiplayer.
- **Menu navigation outside gameplay:** A activates, B cancels or goes back, shoulder buttons switch screens or sections, sticks and d-pad move selection, Menu opens settings or pauses, Home is reserved. [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Physical-controllers)
- **visionOS spatial controllers** (such as PlayStation VR2 Sense) mirror hands: look and pull a trigger for indirect, reach and pull for direct. [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#visionOS)

## Keyboard (Mac, iPad)
- **Single-key bindings first** (I for Inventory, M for Map, Space for the main action). [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Keyboards)
- **Remap Control-based bindings to Command** on Apple keyboards; Command sits next to Space.
- **Put related actions on neighboring keys** near WASD or the number row.
- **Let players rebind everything;** keep standard system shortcuts like Command-Q working. [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#Best-practices)

## Per-platform notes
- **tvOS:** swipe = d-pad, press = primary, Play/Pause = secondary or skip intro, Back opens a pause menu (Back again resumes) so repeated presses don't quit. [HIG](https://developer.apple.com/design/human-interface-guidelines/remotes#Buttons)
- **visionOS:** fully immersive games use `.progressive` or `.full` only if players stay within ~1.5 m; virtual hands fade to real ones on tracking loss; you may defer the palm-up Home indicator in a Full Space (`persistentSystemOverlays`). See `visionos.md`.
- **macOS:** don't redefine systemwide trackpad gestures even in-game. [HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Best-practices)
- **iOS, iPadOS:** simultaneous gesture recognition is fine for joystick plus buttons; defer system edge gestures only during gameplay. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Custom-gestures)

## Accessibility and inclusion
- **Never color alone; subtitle and describe cutscenes.** [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Welcome-everyone)
- **Let players adjust type size, control mapping, motion intensity, sound balance.**
- **Avatars and names cover a wide range of identities; avoid stereotypes in characters and enemies.**

## Apple technologies
- Game Center (achievements, leaderboards, challenges, multiplayer), GameSave for cross-device progress, Core Haptics (also on controllers), Spatial Audio via multichannel audio. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Adopt-Apple-technologies)

## Porting checklist (PC/console game → Apple platforms)
- [ ] Initial download playable within 30 minutes; background asset download.
- [ ] Touch controls on iPhone/iPad; keyboard and mouse on Mac; remote on TV; eyes and hands on Vision Pro.
- [ ] Controller glyphs follow the connected device; UI navigation follows the A/B/shoulder/Menu table.
- [ ] Text and buttons meet the per-platform minimums.
- [ ] Menus reflow across aspect ratios, orientations, and iPhone Duo poses; safe areas respected.
- [ ] Rebindable keys; Command-based bindings on Mac; Esc for settings.
- [ ] Pause on switch-away and on audio interruptions; resume in place.
- [ ] Game Center and GameSave integrated; haptics where they add feel.
