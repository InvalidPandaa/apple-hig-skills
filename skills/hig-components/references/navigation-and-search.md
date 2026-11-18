# Navigation and search components

Sources: [Path controls](https://developer.apple.com/design/human-interface-guidelines/path-controls), [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields)

Split views are in layout-and-organization.md and toolbars in menus-and-actions.md. Glass, tinting, and content under floating bars are covered by the `hig-liquid-glass` skill.

## Choosing between components in this group

| Situation | Component | API |
|---|---|---|
| A handful of top-level sections on iPhone | Tab bar | `TabView { Tab(...) }` |
| Many sections or user-picked collections on iPad (and Mac, visionOS) | Tab bar that converts to a sidebar | `TabView` + `.tabViewStyle(.sidebarAdaptable)`, `TabSection` |
| Sidebar only, no tab bar form (typical Mac app, deep content) | Sidebar in a split view | `NavigationSplitView` + `List(selection:)` + `.listStyle(.sidebar)` |
| Actions on the current view | Toolbar, not a tab bar | `.toolbar` |
| App-wide search with suggestions, categories, discovery | Search tab | `Tab(role: .search)` |
| Search within the current list or view | Search field in the toolbar or inline | `.searchable(text:placement:prompt:)` |
| Narrow a search to clear categories | Scope bar | `.searchScopes(_:activation:_:)` |
| Filter a search by entities (a person, a content type) | Search tokens | `.searchable(text:tokens:placement:prompt:token:)` |
| Mac: a text field holding editable entities (mail recipients) | Token field | AppKit `NSTokenField` |
| Mac: show where a file lives | Path control | AppKit `NSPathControl` |

Tie-breakers:
- **Tab bar vs. sidebar (iOS/iPadOS):** start with a tab bar; add the sidebar form when there are more destinations than fit. Use `NavigationSplitView` only when the sidebar must never become a tab bar.
- **Sidebar levels:** at most two levels in the sidebar; deeper data adds a content column (three-column split view).
- **Search placement on iPhone:** search is a destination → search tab; search matters in one view → bottom toolbar if there's room, else top; search filters one list among several → inline field above that list.

## Tab bars

Use for: moving between top-level sections while each keeps its own navigation state. Not for: actions on content (toolbar), steps of a flow.

- **Navigation only, never actions** (no "Compose" or "Add" tab). [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Keep the tab bar visible as people move through sections**; only modal views cover it. Don't hide it with `.toolbar(.hidden, for: .tabBar)` on pushed screens. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Never disable or remove a tab because its content is empty**; show an explanation inside it. `ContentUnavailableView` [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Avoid the More overflow tab**: limit tabs so all fit in compact width; when people customize, default to five or fewer. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iPadOS)
- **Single-word labels with filled SF Symbols; badges only for critical news.** `Tab("Inbox", systemImage: "tray.fill")`, `.badge(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **Keep labels monochrome or pick a clearly different accent when content is colorful** (see `hig-liquid-glass`). [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices)
- **iOS 26+: the bar floats on glass at the bottom; with an accessory (mini player) it can minimize on scroll and pull the accessory inline.** `.tabViewBottomAccessory { }`, `.tabBarMinimizeBehavior(.onScrollDown)`; read `tabViewBottomAccessoryPlacement` to adapt the accessory. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iOS)
- **A search tab takes the separate slot at the trailing end by default; iOS 27+ can give that slot to one other tab instead.** Only one tab can be prominent, and it is still a destination, not an action. `Tab(..., role: .prominent)` [SwiftUI](https://developer.apple.com/documentation/swiftui/tabrole/prominent)

SwiftUI: `TabView`, `Tab`, `TabSection`, `.tabViewStyle(.tabBarOnly / .sidebarAdaptable)`, `.tabViewCustomization(_:)`. UIKit `UITabBarController` (`UITab`, `UITabBarController.MinimizeBehavior`).
Platforms:
- iPadOS: tab bar at the top, optionally with a button that turns it into a sidebar; let people add/remove tabs (`TabViewCustomization`), choose the initial form with `.defaultAdaptableTabBarPlacement(_:)`. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iPadOS)
- visionOS: vertical bar on the window's leading side that expands on gaze; give every tab a symbol and a short label; a sidebar inside a tab must never switch tabs. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#visionOS)
- tvOS: fixed 68 pt bar at the top that can scroll away with single-view content; live-viewing apps order tabs live, recorded, other. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars#tvOS)
- macOS: no extra HIG guidance; View > Show Tab Bar refers to window tabs, and Mac apps usually switch sections with a sidebar. Not available on watchOS (use a vertical page `TabView`).

## Sidebars

Use for: navigating top-level areas or collections (folders, playlists) when there's room. Not for: compact width (tab bar), more than two levels (add a content column).

- **On iPhone and iPad, try a tab bar first**; `.sidebarAdaptable` gives both forms with a switch button and adapts to rotation and resizing. (2026: guidance on the adaptable style clarified.) [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#iOS-iPadOS)
- **Let rich content run beneath the floating sidebar**, by scrolling under it or with a background extension effect on the detail's hero view. `.backgroundExtensionEffect()` (26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **Icons follow the accent color by default, and on Mac the person's system accent; use a fixed color only sparingly and with meaning** (Mail's yellow VIP). `.listItemTint(_:)` (2026) [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **At most two levels; group with disclosure controls and short group titles.** `Section(isExpanded:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **Let people customize and hide the sidebar, but show it by default**; iPad uses the edge swipe, Mac a toolbar button plus View > Show/Hide Sidebar. `SidebarCommands()`, `NavigationSplitView(columnVisibility:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **Use SF Symbols or custom symbols, not bitmaps.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#Best-practices)
- **macOS: respect the system sidebar icon size (small/medium/large) instead of fixing row heights and fonts; auto-collapse in narrow windows; keep critical actions away from the bottom edge.** [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#macOS)

SwiftUI: `NavigationSplitView` with `List(selection:)` and `.listStyle(.sidebar)`, or `TabView` + `.sidebarAdaptable`. UIKit `UISplitViewController` + `UICollectionLayoutListConfiguration(appearance: .sidebar)`, AppKit `NSSplitViewController` sidebar item.
Platforms: visionOS: the window widens for the sidebar, so hiding is rarely needed; deep apps can put a sidebar inside a tab. Not available on watchOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars#visionOS)

## Search fields

Use for: finding items in a collection by typed terms. Not for: systemwide search (see the HIG Searching page).

- **Placeholder says what can be searched; search as people type; show recent and suggested terms.** `prompt:`, `.searchSuggestions { }`, `.searchCompletion(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Best-practices)
- **Put the most relevant results first and group them by category.** [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Best-practices)
- **Scope bars for clear categories, starting broad; tokens for common entities, offered through suggestions** so people learn them. `.searchScopes`, `.searchable(text:tokens:...)` [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Scope-bars-and-tokens)

iOS placement (2025, terminology refined 2026):
- **Search tab, standard style: a landing page with suggestions and categories for exploration** (Apple TV). `Tab(role: .search) { NavigationStack { ... } }` + `.searchable` on the `TabView` [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-a-tab)
- **Search tab, button appearance: tapping focuses the field with the keyboard, and dismissing returns to the previous tab**, for quick lookups. `.tabViewSearchActivation(.searchTabSelection)` (26+) [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-a-tab)
- **In a toolbar, prefer the bottom when there's room; use the top when bottom content must stay uncovered (Wallet's passes).** `.searchToolbarBehavior(.minimize)` (26+) shows it as a button; `DefaultToolbarItem(kind: .search, placement: .bottomBar)` (26+) positions it among other bottom items. [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-in-a-toolbar)
- **Inline field above the list it filters when search is local to that view**, optionally keeping it pinned in the top bar while scrolling. `.searchable(placement: .navigationBarDrawer(displayMode: .always))` [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#Search-as-an-inline-field)

iPadOS and macOS (keep both the same):
- **Default: trailing side of the toolbar**, searching across split-view columns while the selection stays visible. [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#iPadOS-macOS)
- **Top of the sidebar when it filters the sidebar itself** (Settings). `.searchable(placement: .sidebar)` [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#iPadOS-macOS)
- **A dedicated search tab or sidebar item for discovery-heavy apps; focus its field on arrival, except on iPad with only the on-screen keyboard.** [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#iPadOS-macOS)
- **When an iPad window gets compact, keep search above the content list column.** [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#iPadOS-macOS)

SwiftUI: `.searchable`, `.searchScopes`, `.searchSuggestions`, `.searchFocused(_:)`. UIKit `UISearchController`, AppKit `NSSearchField` / `NSSearchToolbarItem`.
Platforms: tvOS: a keyboard search screen with results below; lead with popular and recent suggestions. watchOS: the field opens a full-screen text input. [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields#tvOS)

## Token fields

macOS only. A text field that turns entries into selectable, draggable tokens (Mail recipients). Give tokens a context menu, add tokenizing keys beyond the comma (Return), and delay suggestions slightly so they don't distract while typing. AppKit `NSTokenField` (`tokenizingCharacterSet`, `completionDelay`); for search on any platform use SwiftUI search tokens instead. [HIG](https://developer.apple.com/design/human-interface-guidelines/token-fields#Best-practices)

## Path controls

macOS only. Shows a file's path as a linear list (standard) or a pop-up menu (pop up); editable path controls accept drops and, in pop-up style, a Choose item. Place it in the window body, never the toolbar or status bar (Finder's path bar sits at the bottom of the body). AppKit `NSPathControl`; no SwiftUI view. [HIG](https://developer.apple.com/design/human-interface-guidelines/path-controls#Best-practices)
