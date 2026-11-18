# Evals

Four cases, each taken from a baseline test run while the skills were written. Each case folder has
`prompt.md` (the task) and `graders/` (pass/fail criteria judged by an LLM, plus a `skill-fired`
indicator).

| Case | Checks |
|---|---|
| `settings-brief-conflict` | Flags the in-app theme picker as a HIG conflict, cites HIG pages, builds native settings |
| `mac-port` | Sidebar, Settings scene, menu commands with shortcuts, context menu, undo, search |
| `review-recipe-detail` | Severity-ranked, linked findings, and all five planted core violations |
| `liquid-glass-editor` | No glass on content or glass on glass, accent tint, system button styles |

Run them with and without the plugin (the runner adds the no-plugin arm automatically):

```sh
claude plugin eval . --allow-tools "Bash(python3:*)" WebFetch
claude plugin eval . --case mac-port --runs 1 --ablation none   # quick single-arm check
```

## Results while developing (2026-11-18)

These were judged by hand against the grader criteria. Agents got the same prompts; the
"with skills" agents were told where the skills are.

| Case | Opus, no skills | Haiku, no skills | Haiku, with skills | Opus, with skills |
|---|---|---|---|---|
| settings-brief-conflict | fail: built the theme picker without comment | fail: same | pass: conflict listed first, linked | pass |
| mac-port | fail: no undo, no search | – | pass | – |
| review-recipe-detail | fail: grouped by topic, not severity; no links | fail: severity tags, but no HIG links | pass: Blocker/Major/Minor, 12 links | – |
| liquid-glass-editor | fail: `.plain` + `glassEffect` | fail: `.tint(.blue)`, manual `glassEffect` on buttons | pass: `.buttonStyle(.glass)`, accent tint | – |
