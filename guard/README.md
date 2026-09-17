# Guard

Guard provides explicit audits for assistant turns and documents, a plan-approval gate, and
configurable review actions for files changed by Claude Code or Codex.

## Edited-file checkpoints

Guard records changed files only when the enabled audit settings and document-review rules
select them, but does not audit them at every response boundary. Run `/guard:audit-files` in
Claude Code or `$guard:audit-files` in Codex when the current batch of edits is ready for review.
The checkpoint groups pending paths by the rules in
`.claude/guard.local.json` or `.codex/guard.local.json`, runs the selected audits, and removes
only file revisions that did not change while review was running.

The reference-index requirement remains immediate: a new saved reference must still be added
to the reference directory's index before work continues.

## Herdr integration

When working inside Herdr, install the companion plugin directly from the marketplace
repository:

```sh
herdr plugin install studykit/studykit-plugins/guard
```

During local development, link the working tree instead:

```sh
herdr plugin link /absolute/path/to/studykit-plugins/guard
```

It provides two actions—show pending files and audit pending files—and a popup pane listing the
queue for the focused Claude Code or Codex session.

To display the pending count in the expanded Herdr Agent sidebar, add `$guard_pending` to an
Agent row in `~/.config/herdr/config.toml`, for example:

```toml
[ui.sidebar.agents]
rows = [
  ["state_icon", "agent", "state_text"],
  ["$guard_pending"],
  ["workspace", "tab"],
]
```

The token disappears when the checkpoint queue is empty. Guard continues to work normally
when the Herdr plugin is not installed.
