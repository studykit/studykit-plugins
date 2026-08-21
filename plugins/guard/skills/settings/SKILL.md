---
name: settings
description: "View and change guard's settings for this project — the evidence judge (audit_gate) and the three axes it checks (audit_claims, audit_deferrals, audit_korean), model, effort, refs_dir, and exempt_skills — recorded in .claude/guard.local.json. Use when the user wants to configure guard: change the audit_gate mode, turn the claim, deferral, or Korean-naturalness check on or off, set model/effort/refs_dir, or manage exempt skills. Claude Code only."
argument-hint: '[key] [value]'
context: fork
model: sonnet
disable-model-invocation: true
allowed-tools: Bash, AskUserQuestion
---

You configure **guard** for this project. Every setting lives in
`.claude/guard.local.json` and you change it **only** through guard's CLI — never by
editing that file with Write/Edit. The CLI is the one supported writer: it validates
each value and mirrors the change into the live session, which a hand-edit does not.

Fixed values for this run (already substituted — do not re-resolve):

- guard CLI: `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py"`
- session id: `${CLAUDE_SESSION_ID}` — pass it as `--session ${CLAUDE_SESSION_ID}` so
  `audit_gate` / `audit_claims` / `audit_deferrals` / `audit_korean` changes take effect
  in the **current** session, not only in sessions started later.

## Commands

Every command that **changes** a setting must be prefixed with `GUARD_SETTINGS_SKILL=1`.
guard refuses config-mutating calls without it, so that a settings change is something
the user asked for through this skill rather than something an agent did on its own.
Read-only commands (`settings show`, `exempt list`) need no prefix.

- **Show current settings:**
  `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" settings show --session ${CLAUDE_SESSION_ID}`
- **Change one scalar setting:**
  `GUARD_SETTINGS_SKILL=1 "${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" settings set <key> <value> --session ${CLAUDE_SESSION_ID}`
- **Manage the exempt list** (`exempt_skills`, a list — not settable via `settings set`):
  `GUARD_SETTINGS_SKILL=1 "${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" exempt list | set <names…> | add <names…> | remove <names…> | clear`

## Settable keys

| Key | Values | What it controls |
| --- | --- | --- |
| `audit_gate` | `manual` / `headless` | How the Stop-time audit runs. `manual` (default) = no audit at Stop; audit on demand with `/guard:audit-claims`, `/guard:audit-deferrals`, `/guard:correct-korean`. `headless` = one in-hook judge per enabled axis, in parallel, blocking on a violation. |
| `audit_claims` | `on` / `off` | Axis 1 of the judge — flags statements asserted without adequate evidence. `off` stops the judge checking claims. |
| `audit_deferrals` | `on` / `off` | Axis 2 of the judge — flags work punted as "TBD" / "확인 필요" that the repo could have answered. `off` stops the judge checking deferrals. |
| `audit_korean` | `on` / `off` | Axis 3 of the judge — **off by default**. When a response is in Korean, flags 번역체 (translated-sounding) phrasing and a register that is not 존댓말. An English response is never flagged, and identifiers, paths, commands, and established loanwords (커밋, 리팩토링) are left alone. |
| `model` | a model name (e.g. `haiku`, `sonnet`) | Model the **headless** judge runs on. |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` | **Headless** judge reasoning effort. |
| `refs_dir` | a project-relative path, or empty | Where guard saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; point it at a different tracked path (e.g. `docs/refs`) to override. |
| `exempt_skills` | skill/command names, namespaced (e.g. `hindsight:review`) | Skills/commands whose finished turn the judge skips. Managed with the `exempt` verbs above. |

`audit_gate` picks **how** the audit runs; `audit_claims`, `audit_deferrals`, and
`audit_korean` pick **what** it looks for. They are independent — turning all three
axes off stops the audit entirely, whatever `audit_gate` says. `audit_korean` starts
off because most projects answer in English, where it reports nothing.

An axis switched off is still auditable on demand: the switch governs the automatic
Stop-time audit, while `/guard:audit-<axis>` is the user asking for that one audit
now. So `audit_claims off` does not make `/guard:audit-claims` stop working.

`audit_gate` and the three `audit_*` axes apply to the current session and become the
new default; `model` / `effort` / `refs_dir` / `exempt_skills` are read from the file
when used, so they also take effect immediately.

## What to do

1. Run `settings show` and show the user the current settings.
2. **If `$ARGUMENTS` already names a key (and, for a scalar, a value)** — apply it
   directly with the matching command, skip the menu.
3. **Otherwise** call `AskUserQuestion` to ask which setting to change and to what: offer
   that key's valid values as options and note the current value. For `exempt_skills`,
   ask which namespaced skill/command names to exempt (the user provides them), then
   record with `exempt set <names…>`.
4. Apply the change with the CLI, then relay the resulting settings the command prints
   back to the user in a short summary. Report exactly what changed.

Never write `.claude/guard.local.json` with Write/Edit — only the CLI above may change
guard's settings.
