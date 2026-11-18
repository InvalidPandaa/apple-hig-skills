---
tags: [review]
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools: [Skill, Read, Glob, Grep]
---

Review this SwiftUI screen from an iOS 27 recipe app against Apple's Human Interface Guidelines. List every problem you find, why it's a problem, and how to fix it. Then give the corrected code.

```swift
struct RecipeDetailView: View {
    let recipe: Recipe
    @State private var showDeleteAlert = false
    @State private var saved = false

    var body: some View {
        ZStack(alignment: .top) {
            ScrollView {
                VStack(alignment: .leading, spacing: 8) {
                    AsyncImage(url: recipe.imageURL).frame(height: 260).clipped()
                    Text(recipe.title).font(.system(size: 28, weight: .heavy))
                    Text(recipe.subtitle).font(.system(size: 13)).foregroundColor(Color(red: 0.7, green: 0.7, blue: 0.7))
                    HStack {
                        Circle().fill(recipe.isVegan ? .green : .red).frame(width: 8, height: 8)
                        Text("\(recipe.minutes) min")
                    }
                    ForEach(recipe.steps, id: \.self) { step in
                        Text(step).font(.system(size: 15))
                    }
                    Button("Submit") { saved.toggle() }
                        .padding(.vertical, 6).frame(maxWidth: .infinity)
                        .background(Color.orange).foregroundColor(.white).cornerRadius(4)
                }.padding(.horizontal, 8)
            }
            HStack {
                Image(systemName: "chevron.left").frame(width: 24, height: 24).onTapGesture { dismiss() }
                Spacer()
                Image(systemName: saved ? "heart.fill" : "heart").frame(width: 24, height: 24)
                    .onTapGesture { saved.toggle() }
                Image(systemName: "trash").frame(width: 24, height: 24)
                    .onTapGesture { showDeleteAlert = true }
            }
            .padding(12)
            .background(.ultraThinMaterial)
            .background(RoundedRectangle(cornerRadius: 20).fill(.ultraThinMaterial))
        }
        .toolbar(.hidden, for: .navigationBar)
        .toolbar(.hidden, for: .tabBar)
        .alert("Are you sure?", isPresented: $showDeleteAlert) {
            Button("Yes") { delete() }
            Button("No") {}
        }
        .animation(.spring(response: 0.9, dampingFraction: 0.3), value: saved)
    }
}
```

Put your complete answer in your reply. Don't write files.
