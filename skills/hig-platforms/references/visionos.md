# visionOS

Sources: [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos), [Windows](https://developer.apple.com/design/human-interface-guidelines/windows), [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout), [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences), [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes), [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures), [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown), [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking), [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards), [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices), [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)

## What people expect
- An unbounded canvas in their own room, seen through passthrough; apps start in the **Shared Space** next to other apps; a **Full Space** hides everything else. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos)
- **Comfort above all:** content in the field of view, placed relative to the head by the system, no need to stand, turn, or reach; people may be sitting, standing, or lying down.
- **Familiar UI in windows, immersion only where it earns its place.** For each moment pick the least immersion that works. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos#Best-practices)
- Spatial Audio, SharePlay with spatial Personas, and full accessibility support (VoiceOver, Dwell Control, Head Pointer, Switch Control).

## Windows, volumes, spaces
- **Window (`WindowGroup`, default style): glass plane with close button, window bar, resize controls.** Keep the glass; opaque or removed backgrounds hurt legibility and feel heavy (`.plain` style exists for special cases). [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-windows)
- **Size windows to content:** default 1280×720 pt, opening about 2 m away; avoid empty areas; match shape to content (wide for slides, tall for web pages); set min and max sizes (`.defaultSize`, `.windowResizability`) without blocking resizing.
- **Keep 3D in a window shallow and inset;** the system clips depth that leaves the window surface. Use a volume for more. [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS)
- **Volume (`.windowStyle(.volumetric)`) for bounded 3D viewed from any angle.** Pin 2D labels with attachments; prefer dynamic scale (fixed scale for real-world objects like products); keep the default baseplate glow unless content fills the volume; choose floor-parallel or tilt-with-gaze alignment. [HIG](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-volumes)
- **Few windows.** Many windows crowd the room and make relocating the app tedious; show supplementary info in a split view, a sheet, or one adjacent window via `.defaultWindowPlacement(_:)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Best-practices)
- **`ImmersiveSpace` with `.immersionStyle(selection:in:)`:** `.mixed` blends with passthrough (no boundary), `.progressive` partly replaces it (Crown adjusts within 120–360° or your range), `.full` replaces it. Progressive and full create a ~1.5 m boundary; leaving it fades the experience. [HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Immersion-styles)
- **Launch in the Shared Space or `.mixed`;** let people choose to go deeper with a clear Enter control, and leave with a clear Exit control whose label says whether it returns or quits. Never require the Crown to back out. [HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Transitioning-between-immersive-styles)
- **Pick the style for the movement involved;** if people may walk beyond 1.5 m, use `.mixed`. Don't make people move: bring objects to them. [HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Promoting-comfort)
- **Dim or tint passthrough subtly** (`.preferredSurroundingsEffect(_:)`) to focus attention; avoid bright tints.
- **Environments:** expansive, grounded with a floor mesh, low-contrast periphery, gentle animation, real meshes over flat 360° images, varied assets, soundscape that ducks for media. [HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Creating-an-environment)

## Ornaments and bars
- **Tab bar is a vertical ornament on the window's leading side;** it expands when looked at, so give every tab a symbol and a short label. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#visionOS)
- **Toolbar is an ornament along the bottom edge,** slightly in front of the window. Use the system toolbar; never make a vertical toolbar; avoid pull-down menus in it (they cover window controls); keep the window from shrinking narrower than the toolbar, since there's no menu bar fallback. [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars#visionOS)
- **Custom ornaments** (`.ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`) for persistent controls like Now Playing; usually visible, no wider than the window, borderless buttons on glass, few of them. [HIG](https://developer.apple.com/design/human-interface-guidelines/ornaments#Best-practices)
- **Supplemental content goes in an adjacent window, not an ornament.** [HIG](https://developer.apple.com/design/human-interface-guidelines/layout#visionOS)
- **Volumes:** one extra ornament at most, never on the toolbar's or tab bar's edge.

## Eyes
- **You get no gaze data before a tap;** system components report the tap. [HIG](https://developer.apple.com/design/human-interface-guidelines/eyes)
- **Spacing: item centers at least 60 pt apart, or 16 pt clear margin around each;** no overlapping interactive elements. [HIG](https://developer.apple.com/design/human-interface-guidelines/eyes#Making-items-easy-to-see)
- **Round interactive shapes;** corners pull the eye off center. [HIG](https://developer.apple.com/design/human-interface-guidelines/eyes#Encouraging-interaction)
- **One hover shape for compound controls** (image plus label): `.contentShape(.hoverEffect, …)` with `.hoverEffect()`.
- **Calm surroundings:** no motion next to what people are looking at, no repeating textures filling the view, readable content at least 1 m away.
- **Custom hover effects run outside your process:** define a resting and a hovered state, keep one primary view constant, choose no/short/long delay (tooltips get the long one), use them sparingly, test on device. [HIG](https://developer.apple.com/design/human-interface-guidelines/eyes#Custom-hover-effects)

## Hands and other inputs
- **Indirect gestures first** (look + pinch, hands resting); direct touch for nearby objects and short interactions only. Standard gestures work both ways. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#visionOS)
- **Custom gestures need a Full Space and hand-tracking permission;** keep them comfortable, offer a one-hand or low-movement alternative, never tie them to a specific hand. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Designing-custom-gestures-in-visionOS)
- **The palm-up look and hand roll belong to Home and Control Center.** Don't anchor content to hands or wrists; in a Full Space you may require a tap first with `.persistentSystemOverlays(.hidden)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/gestures#Working-with-system-overlays-in-visionOS)
- **Virtual hands** match real hand pose, aren't oversized, and fade out to real hands when tracking drops. [HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Displaying-virtual-hands)
- **Digital Crown is system-only:** volume, immersion amount, recenter (press and hold), Home. Apps receive nothing from it. [HIG](https://developer.apple.com/design/human-interface-guidelines/digital-crown#Apple-Vision-Pro)
- **Keyboards:** the Command-hold overlay lists shortcuts flat by category, so titles must make sense without their submenu. A connected keyboard still shows a typing overlay. [HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards#visionOS)
- **Pointer** follows where people look; nothing to implement. Focus effects for keyboard/controller are separate from the gaze hover effect. [HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#visionOS)

## Spatial layout
- **Center key content in the field of view; never lock content to the head.** Anchor it in the room. [HIG](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view)
- **Depth shows hierarchy** (a sheet pulls forward, the window recedes); no depth on text; few distinct depth planes. [HIG](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Depth)
- **Points are angles;** dynamic scale keeps windows legible at any distance. Fixed scale only for noninteractive life-size objects. [HIG](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Scale)
- **Floor plane** for large content that rises from the ground.
- Text minimum 12 pt (default 17); buttons 60×60 pt default. [HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-games#Look-stunning-on-every-display)

## Multitasking
- One window is active at a time; others recede and turn translucent with a feathered edge, so **don't alter window edges**. Closing a window backgrounds the app. [HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking#visionOS)
- **Keep video playing when people look away;** expect audio to duck unless you're the Now Playing app.
- Drops into empty space can open your app if dragged content carries an `NSUserActivity`.

## Porting checklist (iPhone/iPad → Vision Pro)
- [ ] Run the iPad layout in a glass window first; remove custom opaque backgrounds.
- [ ] Bottom tab bar → system `TabView` (becomes the leading vertical ornament); actions in the system toolbar ornament.
- [ ] Hit targets spaced 60 pt center to center; rounded shapes; hover shapes on custom controls.
- [ ] Hover-only or gaze-dependent logic removed (no gaze data).
- [ ] Set default, min, and max window sizes shaped to content.
- [ ] 3D content: shallow inline in windows, or a volume; immersive space only for signature moments with clear Enter/Exit.
- [ ] Nothing head-locked, nothing requiring walking or raised arms for long.
- [ ] Shortcut titles descriptive without submenus.
- [ ] Test with VoiceOver, Dwell Control, and a game controller if it's a game.
