---
name: hig-platforms
description: Use when building, porting, or reviewing a native app or game for a specific Apple device (iPhone, iPad, Mac, Apple Watch, Apple TV, Apple Vision Pro, iPhone Duo), when a brief says "same app on Mac/iPad/Watch/TV", when an iPhone layout looks stretched or wrong on another device, or when choosing per-platform navigation, windows, menu bar and shortcuts, focus, remote, Digital Crown, eyes-and-hands, pointer, touch on Mac, or fold and vertical-bar handling.
---
# Designing for each Apple platform

Each device has its own posture, distance, input, and session length; give every platform the same care, share the information architecture and model, and rebuild the chrome with that platform's system components.

## Platform at a glance

| Platform | Primary navigation | Primary input | Typical layout | Key don'ts |
|---|---|---|---|---|
| iPhone | `TabView` (floating glass tab bar, search tab) + `NavigationStack` | Multi-Touch, one hand | Single column, controls in reach at the bottom | Hide the tab bar; custom gestures for standard actions; layout by device idiom |
| iPad | Tab bar at top that can become a sidebar (`.sidebarAdaptable`), `NavigationSplitView` | Touch + keyboard, pointer, Apple Pencil | 2–3 columns, resizable windows | Blow up the iPhone layout; leading toolbar items under window controls; full-screen modals for small tasks |
| Mac | Sidebar split view + window toolbar + menu bar | Keyboard + pointer (touch is secondary, 2026) | Multiple resizable windows, inspector on trailing side | Commands only in the toolbar; settings button in toolbar; bigger controls for touch |
| iPhone Duo | Same as iPhone/iPad; bars move to a vertical side strip (iOS 27.1) | Touch, two displays, hinge poses | Compact on outer, regular on inner, split around the fold | Custom layout per pose; fixed widths; overriding vertical bar placement |
| Apple Watch | Shallow `NavigationStack`, vertical page `TabView` | Digital Crown, tap, double tap, Action button | One glanceable screen | Deep hierarchies; acting on Crown presses; primary action in scrolling views |
| Apple TV | Top tab bar + focus-driven grids | Siri Remote (swipe, press), controller | Edge-to-edge art, 60/80 pt safe margins | Pointers; responding to stray taps during video; Back to "previous screen" instead of parent |
| Vision Pro | Glass window with vertical tab bar ornament, toolbar ornament at bottom | Eyes + indirect pinch, direct touch nearby | Windows, volumes, optional immersive space | Launch fully immersive; head-locked content; removing window glass; tight targets |
| Games | Platform defaults + in-game menus | Each platform's default input, controllers optional | Full screen, any aspect ratio | Requiring a controller without fallback; text below platform minimums |

## Quick decisions

| Need / situation | Do this (API) | Source |
|---|---|---|
| iPhone app must also ship on iPad | Keep the tab structure, switch to `.tabViewStyle(.sidebarAdaptable)` or `NavigationSplitView`, show one more level of hierarchy | [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados#Best-practices) |
| iPad or iPhone app goes to Mac | Sidebar instead of tab bar, toolbar at top, every command in the menu bar via `.commands`, `Settings` scene | [HIG](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst#Integrate-the-Mac-experience) |
| Layout must survive iPhone Duo, Split View, iPad windows | Size classes, safe areas, scene bounds; never `userInterfaceIdiom` or screen size | [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices) |
| Custom view may sit in the fold or under a camera | `GeometryProxy.reservedRegions(kind:)` or `ArrangementView` (iOS 27.1+) | [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Reserved-regions) |
| Watch companion app | Glanceable single screen, Crown-driven vertical pages, complications and notifications first | [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos#Best-practices) |
| Apple TV version | Make every element focusable, larger focused assets, handle Back/Play-Pause | [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#tvOS) |
| Vision Pro version | Start in a glass window in the Shared Space; add a volume or `ImmersiveSpace` only for key moments | [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos#Best-practices) |
| Game on several devices | Each platform's default input first, controllers as an addition, text/button minimums per platform | [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Enable-intuitive-interactions) |

## Rules

### Cross-platform
- **Give each platform the same level of care.** A port is done when it feels native to people who use only that device, not when it compiles. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)
- **Never port an iPhone layout 1:1.** Larger displays show more hierarchy at once (list and detail side by side); smaller ones show less; TV and Vision Pro change the input model entirely. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Best-practices)
- **Share structure, not chrome.** Keep the same sections, data model, terms, and state; let `TabView`, `NavigationSplitView`, toolbars, menus, and ornaments render per platform instead of drawing your own bars. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#Best-practices)
- **Decide layout by available space, not by device.** Use size classes and container geometry; iPad windows, iPhone Mirroring, and iPhone Duo all give an "iPhone" or "iPad" app many sizes. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#Size-classes)
- **Support each platform's default input, always.** Touch on iPhone/iPad, keyboard and pointer on Mac, remote on TV, eyes and hands on Vision Pro; controllers, Pencil, and keyboards are additions. [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Physical-controllers)
- **Give every action more than one input path.** A gesture, a hover reveal, or a touch-only control must never be the only way in. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Best-practices)
- **Leave system gestures alone.** Edge swipes, three-finger undo, four-finger app switching on iPad, Mission Control gestures on Mac, the palm-up overlay on Vision Pro, Crown presses on Watch belong to the system. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Custom-gestures)
- **Respect standard keyboard shortcuts everywhere a keyboard can attach.** Command-Z, Command-F, Command-Comma, Command-W mean the same thing in every app; add custom shortcuts only for frequent app-specific commands. [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#Standard-keyboard-shortcuts)
- **Be ready for multitasking on every platform but Watch.** Save and restore context, pause attention-requiring activity when people switch away, finish user-started work in the background. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#Best-practices)
- **Call it a "window" in UI text.** Never "scene", even though that is the API name. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#Best-practices)

### Platform highlights that agents miss (details in references)
- **Mac: put every command in the menu bar, including every toolbar item.** People can hide or customize the toolbar, and Full Keyboard Access reaches commands through menus. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#macOS)
- **Mac: disable unavailable menu items, never hide them.** A stable menu teaches people what the app can do. [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Best-practices)
- **Mac with touch (2026): enlarge hit areas, keep control sizes and layout unchanged.** Touch is a secondary input; hover-only controls need a tap reveal or a context-menu path. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#macOS)
- **iPad: move leading toolbar items inward when window controls appear.** In windowed mode the close/tile controls sit at the toolbar's leading edge. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS)
- **iPad: in the menu bar, Settings opens your page in the system Settings app.** Put an in-app preferences item beneath it in the same group. (iPadOS 26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#iPadOS)
- **iPhone Duo: keep system bar placement on the vertical axis.** Top of the strip is Back/Close, then the prominent action; give every item a title and a symbol. (iOS 27.1+) [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Vertical-controls)
- **Watch: don't set a double-tap primary action in a list, scroll view, or vertical tabs.** Double tap already scrolls there. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Double-tap)
- **TV: Back opens the parent screen, not necessarily the previous one; in gameplay it opens a pause menu.** [HIG](https://developer.apple.com/design/human-interface-guidelines/remotes#Best-practices)
- **Vision Pro: you never get gaze data before a tap.** Hover effects run out of process, so design them as two static states, not as gaze-triggered logic. [HIG](https://developer.apple.com/design/human-interface-guidelines/eyes#Custom-hover-effects)
- **Vision Pro: space targets 60 pt center to center.** Eyes jitter; crowded targets cause mis-selection. [HIG](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Best-practices)

### Basics (one line each, models know these)
- Dynamic Type, Dark Mode, orientation changes, safe areas, system accent color, VoiceOver labels, Reduce Motion: support on every platform.

## Brief conflicts
Raise the conflict, cite the link, propose the alternative, then follow the person's decision.

| Request | Why it conflicts | Compliant alternative |
|---|---|---|
| "Mac app identical to the iPad app, bottom tab bar included" | Mac apps put navigation in a sidebar and actions at the top of the window [HIG](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst#Navigation) | Sidebar split view, tabs also listed in the View menu, toolbar at top |
| "Gear button in the Mac toolbar for settings" | Settings belong in the app menu with Command-Comma [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#macOS) | `Settings` scene; toolbar keeps frequent commands |
| "Hide menu items that don't apply right now" | Menu bar items stay visible and disable [HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Best-practices) | `.disabled(...)` on the command |
| "Make controls bigger on Mac for touch screens" | Layout and control sizes stay the same; only hit areas grow [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#macOS) | Larger `contentShape`, standard controls, expandable variants |
| "Pin our toolbar to the top/bottom on iPhone Duo" | Vertical side bars are a core pattern of the device [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Vertical-controls) | Keep default; `.toolbarVerticalBehavior(.disabled)` only for full-screen video or a non-scrolling calculator-like view |
| "Vision Pro app opens straight into full immersion" | Launch in the Shared Space or `mixed`; people choose when to go deeper [HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Best-practices) | Window first, clear Enter/Exit control for the immersive moment |
| "Show a cursor on Apple TV" | tvOS navigation is focus-based [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#tvOS) | Focus grid; free movement only inside gameplay |
| "Watch app mirrors all iPhone features" | Watch interactions are brief and glanceable [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos#Best-practices) | A few timely tasks, plus complications and actionable notifications |
| "Game requires a controller" (iPhone, iPad, Mac) | Only tvOS and visionOS may require one [HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls#Physical-controllers) | Touch controls or keyboard/mouse fallback |

## Common mistakes
- Shipping the iPhone layout stretched on iPad or Mac, or branching layout on `userInterfaceIdiom` instead of size class.
- Mac port without undo for delete, without search (Command-F), without a complete menu bar, Window menu, or keyboard shortcuts (baseline gap).
- Custom window frames, title bars, or tab bars drawn by hand instead of system chrome.
- Toolbar-only commands on Mac; a settings button in the toolbar; menu items that vanish.
- Ignoring iPhone Duo entirely: fixed widths, content in the fold, text-only toolbar items that cannot go vertical, a private overflow menu.
- watchOS apps with deep push navigation and horizontal paging instead of Crown-driven vertical pages.
- tvOS screens where some elements cannot receive focus, or focused items that grow into neighbors.
- visionOS windows with opaque backgrounds, deep 3D in a window, content anchored to the head, vertical toolbars.
- Games that hard-code a 16:9 layout, use "A/X/R1" art on touch buttons, or show Xbox glyphs while a PlayStation controller is connected.

## References
- `references/ios.md`: iPhone expectations, tab/search/toolbar idioms, Action button, Camera Control, system integrations.
- `references/ipados.md`: windows, sidebar-adaptable tabs, iPad menu bar, pointer effects, keyboard focus, Apple Pencil and Scribble, iPhone→iPad checklist.
- `references/macos.md`: menu bar and commands, shortcuts, Settings scene, windows, toolbars, sidebars, inspectors, pointer, undo, drag and drop, touch on Mac, Mac Catalyst, port checklist.
- `references/iphone-duo.md`: poses, reserved regions, arrangement views, vertical bars and their APIs (new Sept 2026). Read before touching any iPhone layout code.
- `references/watchos.md`: Digital Crown, double tap, Action button, toolbars, complications, port checklist.
- `references/tvos.md`: focus model, Siri Remote buttons, safe areas and grids, TV integrations, port checklist.
- `references/visionos.md`: windows, volumes, immersive spaces, ornaments, eyes and hands, spatial layout, port checklist.
- `references/games.md`: launch, text and button minimums, touch controls, controller mapping, key bindings, per-platform game notes.

## Look it up live
Most relevant slugs: `designing-for-ios`, `designing-for-ipados`, `designing-for-macos`, `designing-for-iphone-duo`, `designing-for-watchos`, `designing-for-tvos`, `designing-for-visionos`, `designing-for-games`, `the-menu-bar`, `keyboards`, `windows`, `pointing-devices`, `gestures`, `focus-and-selection`, `remotes`, `digital-crown`, `eyes`, `spatial-layout`, `immersive-experiences`, `game-controls`, `mac-catalyst`, `multitasking`.

```
python3 ../apple-hig/scripts/hig.py fetch designing-for-iphone-duo --section "Vertical controls"
python3 ../apple-hig/scripts/hig.py fetch /documentation/swiftui/arrangementview
```
