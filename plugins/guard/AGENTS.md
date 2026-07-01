# guard — contributor notes

`guard` is two capabilities over one stdlib dispatcher (`scripts/guard_hook.py`),
Claude Code only (it relies on the `claude` CLI and Claude-specific hook payloads;
no Codex path):

1. **Evidence judge** (Stop) — a repo-reading audit that flags a turn on an
   unsupported/surface-signal technical claim or an unjustified deferral. Runs in one
   of two **modes**: `headless` (an isolated `claude` runs inside the Stop hook and
   **blocks** on a violation) or `subagent` (the Stop hook injects `additionalContext`
   with no block; the main agent dispatches the `guardian` subagent to do the same
   audit).
2. **Approval gate** — block file mutation until the user explicitly approves.

The source is the truth for control flow. When editing, record *why* / *what must not
regress*, not a walkthrough of function bodies.

**A turn is the transcript's `promptId`.** guard keeps no turn buffer; at Stop it
reads the turn from Claude Code's transcript (`transcript_path` + `prompt_id`, both in
the Stop payload), sliced by `prompt_id`. State lives under
`${CLAUDE_PROJECT_DIR}/.claude/guard/` (`state/`, `sessions/`, `verified/`, and
`turns/` for subagent-mode slices).

## Runtime facts (verified; do not regress)

Confirmed against the installed CLI / real payloads, not memory. Re-verify before
changing anything that depends on them.

- **`prompt_id` is common to every hook** (PreToolUse and Stop included) and equals
  the transcript record's `promptId`. This is what lets the gate's `gated_prompt_id`
  match the same turn's Stop. Needs Claude Code ≥ 2.1.196 (seen on 2.1.197). Saved:
  `.claude/guard/refs/stop-hook-input.md`.
- **Transcript slice**: the anchor record has `promptId == prompt_id`; a typed prompt
  has `origin={"kind":"human"}` + str content, a `!`-command turn has `origin=None` +
  str content with `<bash-input>`/`<bash-stdout>` — **both carry the promptId**, so
  slice on promptId, NOT origin. Derived records (assistant text,
  tool_use/tool_result, further `!` commands) have `promptId=None`; the slice ends at
  the next different non-empty promptId. Skip `isMeta:true` (guard's own feedback).
- **`!` commands fold into the preceding typed turn** — they never open their own
  promptId; a pure bash-only turn is not observed (verified 2.1.197).
- **A Stop hook may inject `additionalContext` without `decision`** and the
  conversation continues — the subagent-dispatch mechanism.
  `stop_hook_active: true` ⇒ guard already blocked this turn; Stop returns at once.
- **Fail open, always exit 0.** Blocking is a stdout decision payload, never a
  non-zero exit; any judge failure leaves state untouched and does not block.
- **Approval is armed only by a user message** (explicit-implementation classifier
  verdict); the `turn` skill and the model cannot arm it.
- **Refs exemption**: the gate lets an unapproved write through only when the target
  resolves inside `.claude/guard/refs/` — scoped to `refs/` ONLY (never the wider
  tree, so the model can't write `state/` to self-arm), both paths `resolve()`d.

## Deeper detail

Full hook table, storage schema, the complete design invariants, config reference,
and the manual-testing recipe are in **`dev/design.md`** (not auto-loaded — open it
when working in that area).
