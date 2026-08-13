---
name: settings
description: "View and change guard's settings for this project — the approval gate (edit_gate), the evidence judge (evidence_gate), model, effort, refs_dir, exempt_skills, and writable_dirs — recorded in .claude/guard.local.json. Use when the user wants to configure guard: disable the approval gate or switch it between ask/deny, change the evidence_gate mode, set model/effort/refs_dir, manage exempt skills, or choose folders the gate lets edits through (writable_dirs). Claude Code only."
argument-hint: '[key] [value]'
context: fork
model: sonnet
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
  `edit_gate` / `evidence_gate` changes take effect in the **current** session, not only in
  sessions started later.

## Commands

Every command that **changes** a setting must be prefixed with `GUARD_SETTINGS_SKILL=1`.
guard refuses config-mutating calls without it, so that a settings change is something
the user asked for through this skill rather than something an agent did on its own.
Read-only commands (`settings show`, `exempt list`, `writable list`) need no prefix.

- **Show current settings:**
  `"${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" settings show --session ${CLAUDE_SESSION_ID}`
- **Change one scalar setting:**
  `GUARD_SETTINGS_SKILL=1 "${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" settings set <key> <value> --session ${CLAUDE_SESSION_ID}`
- **Manage the exempt list** (`exempt_skills`, a list — not settable via `settings set`):
  `GUARD_SETTINGS_SKILL=1 "${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" exempt list | set <names…> | add <names…> | remove <names…> | clear`
- **Manage the writable folders** (`writable_dirs`, a list — not settable via `settings set`):
  `GUARD_SETTINGS_SKILL=1 "${CLAUDE_SKILL_DIR}/../../scripts/guard_hook.py" writable list | set <dirs…> | add <dirs…> | remove <dirs…> | clear`

## Settable keys

| Key | Values | What it controls |
| --- | --- | --- |
| `edit_gate` | `ask` / `deny` / `off` | The approval gate — holds back file edits until you approve. `off` disables it; `ask` prompts inline; `deny` blocks an unapproved edit outright. |
| `evidence_gate` | `manual` / `subagent` / `headless` | The evidence judge. `manual` = off (audit only on demand via `/guard:audit-evidence`); `subagent` = in-session evidence auditor each turn; `headless` = in-hook judge that blocks. |
| `model` | a model name (e.g. `haiku`, `sonnet`) | Model the **headless** judge runs on. |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` | **Headless** judge reasoning effort. |
| `refs_dir` | a project-relative path, or empty | Where the Grounded style saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; point it at a different tracked path (e.g. `docs/refs`) to override. |
| `refs_format` | `footnote` / `obsidian` | Reference-mark syntax the Grounded style uses. `footnote` (default) = numbered `[^1]` marks with footnote definitions; `obsidian` = `[[#^some-id]]` same-note block links with descriptive ids, which become real jump targets when you read answers in an Obsidian vault. Injected into each session at start. The Stop hook blocks an answer that mixes the two forms, uses a non-numeric footnote id, or leaves a mark with no entry. |
| `exempt_skills` | skill/command names, namespaced (e.g. `hindsight:review`) | Skills/commands whose finished turn the judge skips. Managed with the `exempt` verbs above. |
| `writable_dirs` | project-relative folders (e.g. `build`, `docs/generated`) | Folders the approval gate lets edits through without asking. Managed with the `writable` verbs above. |

`edit_gate` and `evidence_gate` apply to the current session and become the new default;
`model` / `effort` / `refs_dir` / `exempt_skills` / `writable_dirs` are read from the
file when used, so they also take effect immediately. `refs_format` is injected at
session start, so a change to it takes effect in the **next** session.

The `writable` CLI **rejects** a folder it cannot honor — absolute paths, `..`, the
project root, and anything inside guard's own `.claude/guard` files — and prints why on
stderr. That is not a failure to work around: relay the reason to the user and let them
pick another folder. Never try to reach the same result by editing the config file.

## What to do

1. Run `settings show` and show the user the current settings.
2. **If `$ARGUMENTS` already names a key (and, for a scalar, a value)** — apply it
   directly with the matching command, skip the menu.
3. **Otherwise** call `AskUserQuestion` to ask which setting to change and to what: offer
   that key's valid values as options and note the current value. For `exempt_skills`,
   ask which namespaced skill/command names to exempt (the user provides them), then
   record with `exempt set <names…>`. For `writable_dirs`, ask which project-relative
   folders the gate should stop asking about (the user provides them), then record with
   `writable set <dirs…>`.
4. Apply the change with the CLI, then relay the resulting settings the command prints
   back to the user in a short summary. Report exactly what changed.

Never write `.claude/guard.local.json` with Write/Edit — only the CLI above may change
guard's settings.
