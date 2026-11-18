# Layout and organization components

Sources: [Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes), [Collections](https://developer.apple.com/design/human-interface-guidelines/collections), [Column views](https://developer.apple.com/design/human-interface-guidelines/column-views), [Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls), [Labels](https://developer.apple.com/design/human-interface-guidelines/labels), [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), [Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups), [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views), [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views)

Sidebars and tab bars are in navigation-and-search.md; glass under sidebars and bars is covered by the `hig-liquid-glass` skill.

## Choosing between components in this group

| Situation | Component | API |
|---|---|---|
| Rows of mostly text: settings, messages, items to select, edit, reorder | List | `List`, `Form` + `Section` |
| Many attributes per item in sortable columns (Mac, regular-width iPad) | Table | `Table(_:selection:sortOrder:)` |
| Hierarchical rows with disclosure triangles (Mac) | Outline view | `List(_:children:)`, `OutlineGroup` |
| Deep hierarchy people walk back and forth in, no sorting needed (Mac) | Column view | AppKit `NSBrowser` (no SwiftUI view) |
| Image-heavy items or items of varied size, in a grid or row | Collection | `LazyVGrid` / `LazyHGrid` in `ScrollView` |
| Several hierarchy levels visible at once (sidebar, list, detail) | Split view | `NavigationSplitView` |
| A small group of related controls with a border or title | Box | `GroupBox` |
| Hide advanced options until needed | Disclosure control | `DisclosureGroup` |
| Read-only text, optionally with an icon | Label | `Text`, `Label`, `LabeledContent` |
| Mac: switch between a few mutually exclusive panes inside a window | Tab view | `TabView` (macOS automatic style), `NSTabView` |
| Same need on iPhone/iPad | Segmented control, not a tab view | `Picker` + `.pickerStyle(.segmented)` |
| tvOS: focusable media tiles (posters, cast, cards) | Lockup | `.buttonStyle(.card)`, TVUIKit lockup views |

Tie-breakers:
- **List vs. collection:** text reads best in rows; switch to a grid only when images dominate or sizes vary.
- **Table vs. outline view vs. column view (Mac):** flat data → table; hierarchy plus attribute columns → outline view; deep hierarchy browsed level by level → column view. On iPad and visionOS use a split view for hierarchy.
- **Disclosure control vs. navigation:** a disclosure control expands in place; drilling into a new screen uses a row with a disclosure indicator (`NavigationLink`).
- **Tab view vs. tab bar:** a tab view is a bordered pane switcher inside one window; app-level sections use a tab bar or sidebar (navigation-and-search.md). On macOS, a SwiftUI `TabView` with the automatic style draws this bordered tab view, not a tab bar; use a sidebar for app sections there.

## Lists and tables

Use for: text-centric data in rows, hierarchies people navigate (Settings), multicolumn productivity data. Not for: many images or items of mixed size (collection), hierarchical Mac data with columns (outline view).

- **Give selection feedback that matches the row's job.** Rows that lead into a hierarchy (in a split view) stay highlighted; rows that set an option flash briefly and then show a checkmark. `List(selection:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#Best-practices)
- **Use the info (detail disclosure) button only to show details about a row, never to navigate.** Drilling in uses the disclosure indicator that `NavigationLink` adds. [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#iOS-iPadOS-visionOS)
- **Don't add a section index to a list whose rows have trailing accessories**; both live on the trailing edge and get hit by mistake. [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#iOS-iPadOS-visionOS)
- **Keep row text short; for long content show titles only and open a detail view.** For names that differ at the end, truncate in the middle. `.truncationMode(.middle)` [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#Content)
- **Let people reorder when it makes sense, even if they can't add or delete.** On iOS, multi-selection requires edit mode. `.onMove`, `EditButton`; iOS 27+: `reorderable()` + `reorderContainer(for:isEnabled:move:)` for stacks and grids. [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#Best-practices)
- **Pick the system list style for the data and platform** (grouped/inset grouped for settings, plain for content, bordered with alternating rows on Mac) instead of styling rows by hand. `.listStyle(_:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#Style)
- **macOS tables: sortable by clicking a column heading (again reverses), resizable columns, alternating row colors for wide tables, noun column headings in title case.** `Table(sortOrder:)`, `.alternatingRowBackgrounds()` [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#macOS)

SwiftUI: `List`, `Form`, `Table` (in compact width only the first column shows, so make it informative), `.swipeActions`; iOS 27+ `swipeActionsContainer()` for swipe actions outside `List`. UIKit `UICollectionView` list layout / `UITableView`, AppKit `NSTableView`.
Platforms: tvOS: focused rows grow and round their corners, so don't pre-mask adjacent images; watchOS: keep lists short (offer "more") and detail views short enough for vertical paging. [HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables#watchOS)

## Collections

Use for: visual, image-based content in a row or grid. Not for: text (list).

- **Stick to the system row or grid layout; skip novel custom layouts** that confuse people or upstage the content. [HIG](https://developer.apple.com/design/human-interface-guidelines/collections#Best-practices)
- **Pad items enough that focus and hover effects don't overlap neighbors.** [HIG](https://developer.apple.com/design/human-interface-guidelines/collections#Best-practices)
- **Animate inserts, deletes, and reorders** so people can follow changes. [HIG](https://developer.apple.com/design/human-interface-guidelines/collections#Best-practices)
- **Don't change the layout while someone is interacting with it** unless they asked for it (e.g. a layout toggle). [HIG](https://developer.apple.com/design/human-interface-guidelines/collections#iOS-iPadOS)

SwiftUI: `LazyVGrid`, `LazyHGrid`, `Grid`; iOS 27+ `reorderable()` for drag reordering in grids. UIKit `UICollectionView` (compositional layout), AppKit `NSCollectionView`.
Platforms: not available on watchOS.

## Split views

Use for: showing two or three levels of the hierarchy side by side (Mail), or panes that surround a canvas (Keynote). Not for: compact width as the primary layout.

- **Keep the current selection highlighted in every pane that leads to the detail.** [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#Best-practices)
- **Design for every width.** iPad windows resize freely: check narrow, intermediate, and wide, and make sure people can still move between panes logically; on iPhone `NavigationSplitView` collapses to a stack. (2025) [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#iPadOS)
- **macOS: set minimum and maximum pane sizes so the divider never disappears, and prefer the 1 pt thin divider.** `.navigationSplitViewColumnWidth(min:ideal:max:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#macOS)
- **Let people hide panes and offer more than one way back:** a toolbar button plus a menu command with a shortcut. `SidebarCommands()`, `.inspector(isPresented:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#macOS)
- **Support drag and drop between panes.** [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#Best-practices)
- **visionOS: show supplementary information in a split view rather than opening a new window.** [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#visionOS)

SwiftUI: `NavigationSplitView` (2 or 3 columns), `HSplitView`/`VSplitView` (macOS), `.inspector`. iOS 27.1+ `ArrangementView` lays out two related views side by side or stacked and adapts to the iPhone Duo fold; don't nest it in or around a `NavigationSplitView`. UIKit `UISplitViewController`, AppKit `NSSplitViewController`.
Platforms: tvOS: one title above the whole split view, 1/3–2/3 or half split; watchOS: list or detail full screen, multiple detail pages in a vertical page `TabView`. [HIG](https://developer.apple.com/design/human-interface-guidelines/split-views#watchOS)

## Outline views

Use for: hierarchical, text-based data with optional attribute columns, often in the leading pane of a Mac split view. Not for: flat data (table).

- **Show hierarchy only in the first column**; other columns hold attributes like size and date. [HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views#Best-practices)
- **Always provide column headings in a multicolumn outline view** (nouns, title case, no trailing colon). [HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views#Best-practices)
- **Remember which containers people expanded** and restore them next time. AppKit `autosaveExpandedItems` [HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views#Best-practices)
- **Sort within each level when people click the primary heading; let them resize columns.** [HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views#Best-practices)
- **Editable cells: single click edits, double click opens**; Option-click on a triangle expands all descendants. [HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views#Best-practices)
- **Add a toolbar search field when the outline is long**, and truncate in the middle rather than clipping. [HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views#Best-practices)

SwiftUI: `List(_:children:)`, `OutlineGroup`, `DisclosureGroup` rows. AppKit `NSOutlineView`.
Platforms: macOS only per HIG; on iPad use a split view or a sidebar with disclosure groups.

## Column views

Mac-only browser (Finder column view) for deep hierarchies. Root level in the first column, show a preview/info for a selected leaf, and let people resize columns. No SwiftUI view: use AppKit `NSBrowser`, or a three-column `NavigationSplitView` on other platforms. [HIG](https://developer.apple.com/design/human-interface-guidelines/column-views#Best-practices)

## Disclosure controls

Use for: progressive disclosure of details or advanced options in place. Not for: moving to another screen (navigation link).

- **Keep the most used controls visible at the top; hide advanced ones by default.** [HIG](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls#Best-practices)
- **Label a disclosure triangle with what it reveals** ("Advanced Options"). [HIG](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls#Disclosure-triangles)
- **Mac disclosure button (expands a control, as in the Save sheet): place it next to what it expands, and use at most one per view.** [HIG](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls#Disclosure-buttons)

SwiftUI: `DisclosureGroup`, `Section(isExpanded:)` in lists and sidebars. AppKit `NSButton` bezel styles `.disclosure` / `.pushDisclosure`.
Platforms: iOS, iPadOS, visionOS via SwiftUI `DisclosureGroup`; not available on tvOS or watchOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls#iOS-iPadOS-visionOS)

## Labels

Use for: small amounts of read-only text in buttons, rows, and views. Not for: editable text (text field), long text (text view).

- **Express importance with the four system label colors** (label, secondary, tertiary for unavailable items, quaternary for watermarks) instead of custom grays. `.foregroundStyle(.secondary)` etc. [HIG](https://developer.apple.com/design/human-interface-guidelines/labels#Best-practices)
- **Make useful label text selectable** (errors, addresses, IPs). `.textSelection(.enabled)` [HIG](https://developer.apple.com/design/human-interface-guidelines/labels#Best-practices)
- **Use `Label(_:systemImage:)` for icon plus text** so lists, menus, and toolbars can show the form that fits their context.
- **watchOS: use the system date and timer text** so it fits the space and updates itself. `Text(_:style:)` [HIG](https://developer.apple.com/design/human-interface-guidelines/labels#watchOS)

Checklist: system fonts with Dynamic Type; keep custom styling legible.
SwiftUI: `Text`, `Label`, `LabeledContent`. AppKit: `NSTextField` with `isEditable = false`. [HIG](https://developer.apple.com/design/human-interface-guidelines/labels#macOS)

## Boxes

Use for: visually grouping a few related controls or facts. Not for: whole-window grouping or nested sub-grouping.

- **Keep a box small relative to its container, and don't nest boxes**; use spacing and alignment for subgroups. [HIG](https://developer.apple.com/design/human-interface-guidelines/boxes#Best-practices)
- **Title only when it clarifies:** a short phrase in sentence case with no ending punctuation (a colon only in a Mac settings pane). [HIG](https://developer.apple.com/design/human-interface-guidelines/boxes#Content)

SwiftUI: `GroupBox`; on iOS settings-style screens a `Form` `Section` is usually the right grouping. AppKit `NSBox`.
Platforms: macOS shows the title above the box; iOS uses secondary/tertiary background colors; not available on tvOS or watchOS.

## Tab views

Use for: a Mac window with a few closely related, self-contained panes. Not for: app-level navigation (tab bar or sidebar), iOS (segmented control).

- **Keep each pane self-contained**: controls in a pane affect only that pane. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views#Best-practices)
- **Label tabs with nouns in title case; use at most six tabs**, and switch to a pop-up button only when there are too many panes for tabs. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views#Best-practices)
- **Inset the tab view from the window edges** with a margin of window body. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views#Anatomy)

SwiftUI: `TabView` on macOS (automatic style). AppKit `NSTabView`.
Platforms: iOS/iPadOS: use a segmented control instead; watchOS: `TabView` shows as pages (`.tabViewStyle(.verticalPage)`); not available on tvOS or visionOS. [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views#watchOS)

## Lockups

tvOS only: a content view plus header and footer that grow together on focus (cards, caption buttons, monograms, posters). Leave room for the focus growth, keep sizes consistent within a row, and prefer a photo over initials in monograms. SwiftUI: `.buttonStyle(.card)` or a borderless button with an image; TVUIKit `TVLockupView`, `TVPosterView`, `TVMonogramContentView`, `TVCardView`. [HIG](https://developer.apple.com/design/human-interface-guidelines/lockups#Best-practices)
