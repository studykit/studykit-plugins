# guard — contributor notes

`guard` is two capabilities over one stdlib dispatcher (`scripts/guard_hook.py`),
Claude Code only (it relies on the `claude` CLI and Claude-specific hook payloads;
no Codex path):

1. **Evidence judge** (Stop) — a repo-reading audit that flags a turn on an
   unsupported/surface-signal technical claim or an unjustified deferral. Runs in one
   of three **modes** (`/guard:config mode`): `manual` (default — no audit at Stop, the
   judge's practical off; `/guard:audit` dispatches the `guardian` subagent for the
   last completed turn on demand), `subagent` (the Stop hook injects
   `additionalContext` with no block; the main agent dispatches the `guardian`
   subagent to run the same audit), or `headless` (an isolated `claude` runs inside
   the Stop hook and **blocks** on a violation).
2. **Approval gate** — stop file mutation until the user explicitly approves. `gate_mode`
   picks how an unapproved edit is stopped: `ask` (default) escalates to Claude Code's
   permission prompt — the user approves the edit inline and `PostToolUse` → `gate-approved`
   arms the session for the rest of the task; `deny` blocks the call to drive the
   plan→approve workflow. Approval also arms on a user message (classifier) or on the user
   approving a non-deferring plan via ExitPlanMode (`PostToolUse` → `plan-approved`). Every
   arming path is a user action — the model can arm none of them (it cannot approve its own
   `ask` prompt). Toggled by `/guard:config` (`edit_gate`), independent of the judge's `mode`.

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
