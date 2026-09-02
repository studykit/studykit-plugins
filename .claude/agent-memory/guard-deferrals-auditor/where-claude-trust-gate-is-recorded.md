---
name: where-claude-trust-gate-is-recorded
description: Where to check whether a directory is already trusted by Claude Code, for "the trust dialog blocked the interactive run" deferrals
metadata:
  type: reference
---

When a turn defers an interactive `claude` run because the workspace trust dialog needs a
keypress, check whether an already-trusted path was available instead of a fresh directory:

`~/.claude.json` → `projects.<abs path>.hasTrustDialogAccepted`. Trust is keyed on the path,
so recreating a previously trusted throwaway path (e.g. the one named in
`guard/dev/design.md` `## Testing against the real CLI`) skips the dialog with no
config edit. Verified once by launching `claude` in such a path under tmux — no dialog.

design.md's own recipe states the alternative: "sends one extra Enter, or runs in a directory
already trusted."

Re-derive the verdict each time; this entry only says where to look. See
[[where-guard-testing-recipes-live]].
