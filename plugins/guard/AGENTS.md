# guard — contributor notes

`guard` supports Claude Code and Codex. Shared state/configuration helpers live in
`scripts/guard_hook.py`; runtime payload parsing and hook output stay in host adapters.
Requires Python 3.11+ (the dispatcher uses `enum.StrEnum`).

1. **Evidence judge** (Stop) — a repo-reading audit of the finished turn, run in one of
   two modes set by `audit_gate` (`/guard:settings`): `manual` (default — no audit at
   Stop; it only records the turn as the pending target, and the user audits on demand
   with `/guard:audit-claims`, `/guard:audit-deferrals`, or `/guard:audit-korean`, each
   dispatching its own auditor subagent) or `headless` (**one isolated `claude` per
   enabled axis, spawned in parallel** inside the Stop hook, blocking on a violation).
   Three independent axis switches pick what is checked: `audit_claims` (asserted
   without adequate evidence), `audit_deferrals` (work punted the repo could answer),
   and `audit_korean` (a Korean response reading as translated English — **off by
   default**, and a no-op on a non-Korean response). All three off skips the audit.

   Why a judge per axis rather than one judging all three: each carries only its own
   axis text, and each gets only the tools that axis needs — the Korean axis needs no
   repository access at all, which is most of its speed. The axis text must NOT be
   trimmed when split; a shortened Korean prompt was measured demanding that
   `prompt_id`, 커밋 and `git rebase` be translated, so the loanword and identifier
   protections are load-bearing. The parent hook stays the only writer of state and the
   only place blocking is decided, and an axis whose judge failed is reported as
   UNCHECKED rather than folded into a pass.

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
project-local `guard_claims_auditor` named agent. State is host-specific under
`.claude/guard/` or `.codex/guard/`.

The source is the truth for control flow, and its comments carry the *why* next to the
code. When editing, record what must not regress — don't restate function bodies here.

## Deeper detail

Everything else lives in **`dev/design.md`** (not auto-loaded — open it when working in
this area): the hook table, storage schema, the runtime facts verified against the real
CLI (transcript slicing, `!`-command and background-task handling, hook-payload
guarantees, the config scope flags), the full design invariants, the config reference,
and the manual-testing recipe.
