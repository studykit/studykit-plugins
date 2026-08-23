---
name: where-guard-testing-recipes-live
description: Where the guard plugin's own run/test recipes live, for checking "needs a live runtime" deferrals in this repo
metadata:
  type: reference
---

For deferrals about guard's *behaviour* ("not verified against a real session/host"), the
recipes are in `plugins/guard/dev/design.md` — headings to grep for:

- `## Manual testing` — headless, deterministic hook-by-hook recipe; states it runs without
  the CLI or auth.
- `## Testing against the real CLI` — `claude --plugin-dir`, `--debug-file`, `GUARD_TRACE=1`,
  plus a `tmux` block for the interactive-only `UserPromptExpansion` paths.
- `## Codex: hooks must be trusted, or guard is silent` — the Codex-side recipe
  (`codex plugin add`, isolated `CODEX_HOME`, `--dangerously-bypass-hook-trust`).

Also `plugins/guard/dev/handoff-audit-workflow.md`.

Re-check these headings still exist before citing them; design.md is edited often. Whether a
given deferral is resolvable must be re-derived from the repo each time — this entry only
says where to look.
