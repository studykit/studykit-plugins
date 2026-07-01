# guard — contributor notes

`guard` is two capabilities over one stdlib dispatcher (`scripts/guard_hook.py`),
Claude Code only (it relies on the `claude` CLI and Claude-specific hook payloads;
no Codex path):

1. **Evidence judge** (Stop) — a repo-reading audit that flags a turn on an
   unsupported/surface-signal technical claim or an unjustified deferral. Runs in one
   of two **modes**: `headless` (an isolated `claude` runs inside the Stop hook and
   **blocks** on a violation) or `subagent` (the Stop hook injects `additionalContext`
   with no block; the main agent dispatches the `guardian` subagent to run the same
   audit).
2. **Approval gate** — block file mutation until the user explicitly approves.

A **turn is the transcript's `promptId`.** guard keeps no turn buffer; at Stop it
slices the turn from Claude Code's transcript (`transcript_path` + `prompt_id`). State
lives under `${CLAUDE_PROJECT_DIR}/.claude/guard/`.

The source is the truth for control flow, and its comments carry the *why* next to the
code. When editing, record what must not regress — don't restate function bodies here.

## Deeper detail

Everything else lives in **`dev/design.md`** (not auto-loaded — open it when working in
this area): the hook table, storage schema, the runtime facts verified against the real
CLI (transcript slicing, `!`-command and background-task handling, hook-payload
guarantees, the config scope flags), the full design invariants, the config reference,
and the manual-testing recipe.
