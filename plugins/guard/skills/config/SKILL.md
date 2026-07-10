---
name: config
description: "View and change guard's settings for this project — the approval gate (edit_gate), the evidence-judge mode, gate_mode, model, effort, refs_dir, and exempt_skills — recorded in .claude/guard.local.json. Use when the user wants to configure guard: turn the approval gate on/off, change the audit mode, set gate_mode/model/effort/refs_dir, or manage exempt skills. Claude Code only."
argument-hint: '[key] [value]'
context: fork
agent: general-purpose
model: claude-sonnet-5
disable-model-invocation: true
allowed-tools: Bash, AskUserQuestion
---

You configure **guard** for this project. Every setting lives in
`.claude/guard.local.json` and you change it **only** through guard's CLI — never by
editing that file with Write/Edit, because guard's approval gate blocks writes to its own
config by design. The CLI is the one supported writer.

Fixed values for this run (already substituted — do not re-resolve):

- guard CLI: `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py"`
- session id: `${CLAUDE_SESSION_ID}` — pass it as `--session ${CLAUDE_SESSION_ID}` so
  `edit_gate` / `mode` changes take effect in the **current** session, not only in
  sessions started later.

## Commands

- **Show current settings:**
  `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" config show --session ${CLAUDE_SESSION_ID}`
- **Change one scalar setting:**
  `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" config set <key> <value> --session ${CLAUDE_SESSION_ID}`
- **Manage the exempt list** (`exempt_skills`, a list — not settable via `config set`):
  `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" exempt list | set <names…> | add <names…> | remove <names…> | clear`

## Settable keys

| Key | Values | What it controls |
| --- | --- | --- |
| `edit_gate` | `on` / `off` | The approval gate — holds back file edits until you approve. |
| `mode` | `manual` / `subagent` / `headless` | The evidence judge. `manual` = off (audit only on demand via `/guard:audit`); `subagent` = in-session guardian each turn; `headless` = in-hook judge that blocks. |
| `gate_mode` | `ask` / `deny` | How an unapproved edit is stopped — `ask` prompts inline, `deny` blocks it outright. |
| `model` | a model name (e.g. `haiku`, `sonnet`) | Model the **headless** judge runs on. |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` | **Headless** judge reasoning effort. |
| `refs_dir` | a project-relative path, or empty | Where the Grounded style saves cited-doc copies. Empty = the git-ignored default `.claude/guard/refs/`; a tracked path (e.g. `docs/refs`) keeps them under git. |
| `exempt_skills` | skill/command names, namespaced (e.g. `hindsight:review`) | Skills/commands whose finished turn the judge skips. Managed with the `exempt` verbs above. |

`edit_gate` and `mode` apply to the current session and become the new default;
`gate_mode` / `model` / `effort` / `refs_dir` are read from the file when used, so they
also take effect immediately.

## What to do

1. Run `config show` and show the user the current settings.
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
