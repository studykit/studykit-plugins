# guard — contributor notes

`guard` supports Claude Code and Codex. Shared state/configuration helpers live in
`scripts/guard_hook.py`; runtime payload parsing and hook output stay in host adapters.
Requires Python 3.11+ (the dispatcher uses `enum.StrEnum`).

1. **Evidence judge** (Stop) — a repo-reading audit that flags a turn on an
   unsupported/surface-signal claim or an unjustified deferral. Runs in one
   of three modes set by `audit_gate` (`/guard:settings audit_gate`): `manual` (default —
   no audit at Stop, the judge's practical off; `/guard:audit-evidence` dispatches the `evidence-auditor`
   subagent for the last completed turn on demand), `subagent` (the Stop hook injects
   `additionalContext` with no block; the main agent dispatches the `evidence-auditor`
   subagent to run the same audit), or `headless` (an isolated `claude` runs inside
   the Stop hook and **blocks** on a violation). What the audit looks for is two further
   switches: `audit_claims` (statements asserted without adequate evidence) and
   `audit_deferrals` (work punted that the repo could answer), each on/off and
   independent of the mode. Both off skips the audit in every mode.
2. **Approval gate** — stop file mutation until the user explicitly approves. `edit_gate`
   is one tri-state setting: `off` disables the gate; `ask` (default) escalates an
   unapproved edit to Claude Code's permission prompt — the user approves the edit inline
   and `PostToolUse` → `gate-approved` arms the session for the rest of the task; `deny`
   blocks the call to drive the plan→approve workflow. Approval also arms on a user message
   (classifier) or on the user approving a non-deferring plan via ExitPlanMode (`PostToolUse`
   → `plan-approved`). Every arming path is a user action — the model can arm none of them
   (it cannot approve its own `ask` prompt). Set by `/guard:settings` (`edit_gate`),
   independent of the judge's `audit_gate`.

3. **Refs index** (PostToolUse) — a file saved into the refs directory must be listed in
   that directory's `AGENTS.md`; `refs-index` blocks the turn until it is. Independent of
   both gates above.

Claude slices turns from its transcript. Codex saves each documented `turn_id`'s prompt,
tool activity, and final response in a guard-owned record because its transcript format is
not a stable hook interface. Codex projects must run `$guard:setup` once to install the
project-local `guard_evidence_auditor` named agent. State is host-specific under
`.claude/guard/` or `.codex/guard/`.

The source is the truth for control flow, and its comments carry the *why* next to the
code. When editing, record what must not regress — don't restate function bodies here.

## Deeper detail

Everything else lives in **`dev/design.md`** (not auto-loaded — open it when working in
this area): the hook table, storage schema, the runtime facts verified against the real
CLI (transcript slicing, `!`-command and background-task handling, hook-payload
guarantees, the config scope flags), the full design invariants, the config reference,
and the manual-testing recipe.
