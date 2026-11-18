---
tags: [macos, platforms]
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools: [Skill, Read, Glob, Grep]
---

We have an iPhone notes app ("Jot") written in SwiftUI and want a native Mac version (macOS 27). Here is the iPhone root view.
Port it to macOS: deliver the macOS SwiftUI code for the app's scene and root views plus a list of what you changed and why.

```swift
@main struct JotApp: App {
    var body: some Scene { WindowGroup { RootView() } }
}

struct RootView: View {
    var body: some View {
        TabView {
            NavigationStack { NotesList() }
                .tabItem { Label("Notes", systemImage: "note.text") }
            NavigationStack { TagsView() }
                .tabItem { Label("Tags", systemImage: "tag") }
            NavigationStack { SettingsView() }
                .tabItem { Label("Settings", systemImage: "gear") }
        }
    }
}

struct NotesList: View {
    @State private var notes: [Note] = Note.samples
    @State private var showNew = false
    var body: some View {
        List(notes) { note in
            NavigationLink(value: note) {
                VStack(alignment: .leading) {
                    Text(note.title).font(.headline)
                    Text(note.preview).font(.subheadline).foregroundStyle(.secondary)
                }
            }
            .swipeActions { Button("Delete", role: .destructive) { delete(note) } }
        }
        .navigationTitle("Notes")
        .navigationDestination(for: Note.self) { NoteEditor(note: $0) }
        .overlay(alignment: .bottomTrailing) {
            Button { showNew = true } label: {
                Image(systemName: "plus").font(.title2.bold()).padding(18)
                    .background(Circle().fill(.yellow))
            }.padding(24)
        }
        .sheet(isPresented: $showNew) { NoteEditor(note: Note()) }
    }
    func delete(_ n: Note) { notes.removeAll { $0.id == n.id } }
}
```

Put your complete answer in your reply. Don't write files.
