---
description: Review SwiftUI/UIKit/AppKit code, a screenshot or a PR against Apple's Human Interface Guidelines
argument-hint: [file, folder, screenshot or PR; defaults to the current changes]
---

Review this against Apple's Human Interface Guidelines: $ARGUMENTS

If no target is given, review the UI files changed in the working tree (`git diff --name-only`, Swift files only), or ask which screen to review if nothing changed.

Use the `hig-review` skill. Follow its process, severity levels and report format exactly, and verify each non-basic rule with `hig.py` before you cite it. Don't edit any files. Offer to apply the fixes at the end.
