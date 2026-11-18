# Data entry, search, settings, drag and drop, files, sharing, printing, charts

Sources: [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data), [Searching](https://developer.apple.com/design/human-interface-guidelines/searching), [Settings](https://developer.apple.com/design/human-interface-guidelines/settings), [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop), [File management](https://developer.apple.com/design/human-interface-guidelines/file-management), [Collaboration and sharing](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing), [Printing](https://developer.apple.com/design/human-interface-guidelines/printing), [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data)

## Entering data

- **Don't ask for what the system can provide.** Read locale, contacts, or location (with permission) instead of making people type them. [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Label each field and prefill sensible defaults;** a placeholder like "name@example.com" shows the format. [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Use `SecureField` for secrets and never prefill a password;** let AutoFill, passkeys, or biometrics fill it. [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Offer choices instead of typing** (`Picker`, `Menu`, `DatePicker`) whenever the set of answers is known. [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Accept paste and drop into fields.** [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Validate as people type, not on submit;** use formatters for numbers (`TextField(value:format:)` with `.number`, `.percent`, `.currency(code:)`). [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Disable Next/Continue until required fields are filled,** so it's obvious what's missing. [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#Best-practices)
- **Help AutoFill and the keyboard:** `.textContentType(_:)` and `.keyboardType(_:)` on every field that has a matching type.
- **macOS: show clipped field contents in an expansion tooltip.** [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data#macOS)

## Searching

- **If search is central, give it a primary place:** a dedicated search tab (`Tab(role: .search)`) in tab apps, or the toolbar. On iPhone, `.searchToolbarBehavior(.minimize)` (iOS 26+) collapses a toolbar search field to a button when inactive. [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Best-practices)
- **Offer one place that searches everything;** local filter-style search in a section is a supplement. [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Best-practices)
- **Make the current scope visible** through placeholder text (`prompt:`), a scope bar (`.searchScopes`), or the title. [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Best-practices)
- **Show recent searches before typing and suggestions while typing** (`.searchSuggestions`, `.searchCompletion`). [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Best-practices)
- **Treat search history as private:** consider who may see the screen, and always let people clear it. [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Best-practices)
- **Index content for Spotlight** (Core Spotlight) with good metadata; add a Spotlight importer for custom file types and a Quick Look generator for previews. [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Systemwide-search)
- **Prefer the system open and save panels;** they include systemwide search. [HIG](https://developer.apple.com/design/human-interface-guidelines/searching#Systemwide-search)
- **No results:** `ContentUnavailableView.search`, ideally with a suggestion to broaden the query.
- The Searching page was revised in June 2026 (terminology and best practices); fetch it live before quoting wording. (2026)

## Settings

### What goes where

| Kind of option | Where |
|---|---|
| Sort, filter, show/hide, reorder in a view | In that view (toolbar menu, view options) |
| Option that only affects one task | Inside the task |
| General, rarely changed app behavior, account, notification types | In-app settings screen |
| Rarest options, or what the system lists for you (permissions, notifications) | System Settings app; offer a button that opens it (`UIApplication.openSettingsURLString`) |
| Anything the system already controls globally | Nowhere: follow the system |

### Never duplicate in-app (systemwide already)
Appearance (Light/Dark/Auto), text size (Dynamic Type), accessibility accommodations (Reduce Motion, Bold Text, Increase Contrast), scrolling behavior, biometric opt-in, system haptics for standard controls, language and region. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices), [HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode#Best-practices), [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#Best-practices)

### Rules
- **Pick defaults that suit most people,** including auto-tuned performance in games, so nobody must configure before using. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Keep the list of settings short;** each extra setting makes the rest harder to find. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Open settings the expected way:** Command-Comma in apps, Esc in games. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Detect rather than ask** (controllers, accessories, Dark Mode). [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#Best-practices)
- **Provide an in-app screen to change notification choices,** including marketing opt-in. [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications#Sending-marketing-notifications)
- **macOS:** `Settings { … }` scene, reached from the App menu (never a toolbar button; document-level options go in File); `SettingsLink` opens it from your UI. Noncustomizable toolbar of panes with the active one highlighted, window title = pane name (or "App Name Settings" for one pane), minimize and zoom dimmed, last pane restored. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#macOS)
- **watchOS: no entries in the system Settings app;** offer the few options that matter at the end of the main view or in a More menu. [HIG](https://developer.apple.com/design/human-interface-guidelines/settings#watchOS)

## Drag and drop

- **Support drag and drop broadly,** and always offer a non-drag alternative (menu commands like Move To, accessibility drag descriptors). [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Best-practices)
- **Default to move within a container and copy across containers;** between apps it's always a copy. Option key at drop time forces copy. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Accepting-drops)
- **Support multi-item drags** and, on iPad, adding items to an in-progress drag. SwiftUI multi-item: `dragContainer(for:in:_:)` (iOS 27+, macOS 26+). [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Best-practices)
- **Make drops undoable;** confirm only drops that can't be reversed. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Best-practices)
- **Provide several representations, richest first** (native object → PDF → PNG → JPEG) via `Transferable`; on drop, take the richest you support and only the relevant part. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Best-practices)
- **Feedback throughout:** translucent drag image after about 3 pt of movement, destination highlight only while hovering a valid target (`isTargeted:`), visible failure (snap back or evaporate), progress or a placeholder for slow transfers. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Providing-feedback)
- **Keep dropped content selected in the destination.** [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#Accepting-drops)
- **macOS:** allow dragging from inactive windows without activating them, show a count badge for multi-item drags, and export to Finder in a format the app can reopen. [HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop#macOS)
- **Reordering in custom stacks or grids:** `reorderContainer(for:in:isEnabled:move:)` with `.reorderable()` (iOS 27+, macOS 27+); `List` has `.onMove`.
- SwiftUI basics: `.draggable(_:)` on the source, `.dropDestination(for:action:isTargeted:)` on the target. Not supported on tvOS and watchOS.

## File management

- **Autosave.** Work is preserved unless people cancel or delete; save periodically and on close or app switch. `DocumentGroup` does this. [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Saving-work)
- **Hide file extensions by default with a way to show them.** [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Saving-work)
- **New and Open in menus with shortcuts, plus a visible Add (+) button.** [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Creating-and-opening-files)
- **Custom browsers still expose the whole file system,** starting at a sensible location. Prefer the system browser on Mac. [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Creating-and-opening-files)
- **iOS/iPadOS 18+: use the document launcher** (`DocumentGroupLaunchScene`): the primary title-card button creates a document, the secondary offers options such as templates; calm background, few accessories, gentle animation. [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Document-launcher)
- **Use Quick Look** to preview files the app can't open, and ship a generator for custom types. [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Quick-Look-previews)
- **macOS with autosave off:** show the unsaved dot on the close button and in the Window menu, prompt on close/quit; with autosave on, no dot. "Edited" in the title is fine either way until saved. [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#Finder-Sync-extensions)
- **File provider extensions:** show only relevant file types, let people choose destinations, no second top toolbar. [HIG](https://developer.apple.com/design/human-interface-guidelines/file-management#File-provider-app-extension)

## Collaboration and sharing

- **Put Share in the toolbar** (`ShareLink`, which opens the system share sheet). [HIG](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing#Best-practices)
- **Summarize permissions in a short phrase** ("Only invited people can edit") and keep custom sharing options few and grouped. [HIG](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing#Best-practices)
- **Show the Collaboration button next to Share as soon as collaboration starts;** keep its popover's custom items to essentials. [HIG](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing#Best-practices)
- **Support "send copy" alongside collaboration,** and post Messages highlight events with universal links (`SWHighlightEvent`). [HIG](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing#Best-practices)
- **Real-time shared activities:** see the SharePlay page. [HIG](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing)

## Printing

- **Make Print discoverable:** File > Print (Command-P) on Mac, a toolbar or share/action entry on iPhone and iPad. On Mac, a toolbar Print button is optional via customization. [HIG](https://developer.apple.com/design/human-interface-guidelines/printing#Best-practices)
- **Dim or remove Print when nothing can be printed or no printer exists.** [HIG](https://developer.apple.com/design/human-interface-guidelines/printing#Best-practices)
- **Use the system print panel for standard options;** add a custom panel category named after the app only for app-specific options, put advanced ones under a disclosure labeled Advanced Options, and keep print settings with the document at least until it closes. [HIG](https://developer.apple.com/design/human-interface-guidelines/printing#macOS)
- APIs: `UIPrintInteractionController` (UIKit), `NSPrintOperation` / `NSDocument` printing (AppKit). Not on tvOS or watchOS.

## Charting data

- **Chart only when there's an insight to show;** raw data people need to look up belongs in a sortable, searchable list or table. [HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)
- **Keep charts simple and reveal detail progressively** (tap for detail, switch time ranges). [HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data#Best-practices)
- **Every chart needs accessibility labels for values and an audio graph** (`.accessibilityChartDescriptor`); a visible summary doesn't replace them. [HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data#Best-practices)
- **Prefer bar and line charts;** teach any novel chart type the first time people meet it. [HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data#Designing-effective-charts)
- **Add a headline that states the takeaway** ("Rain likely after 3 PM"), plus titles and annotations. [HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data#Designing-effective-charts)
- **Size the chart to its job,** and keep type, colors, and marks consistent between a small summary chart and its expanded version. [HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data#Designing-effective-charts)
- Visual specs for marks, axes, and color: see the Charts component page (`charts`).
