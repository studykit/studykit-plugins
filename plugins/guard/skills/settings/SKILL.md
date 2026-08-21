---
name: settings
description: "View and change guard's settings for this project — one setting per audit agent, named after it (claims-auditor, deferrals-auditor, korean-corrector, comment-corrector), each off / fresh / reuse, plus router_model, refs_dir, and exempt_skills — recorded in .claude/guard.local.json. Use when the user wants to configure guard: turn the claim, deferral, Korean-naturalness, or comment check on or off, keep one of them running across turns instead of respawning it, set the router's model or refs_dir, or manage exempt skills. Claude Code only."
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
  the four agent switches take effect in the **current** session, not only in sessions
  started later.

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
| `claims-auditor` | `off` / `fresh` / `reuse` | Admits `guard:claims-auditor` — it flags statements asserted without adequate evidence. |
| `deferrals-auditor` | `off` / `fresh` / `reuse` | Admits `guard:deferrals-auditor` — it flags work punted as "TBD" / "확인 필요" that the repo could have answered. |
| `korean-corrector` | `off` / `fresh` / `reuse` | Admits `guard:korean-corrector` — it flags 번역체 phrasing and a register that is not 존댓말, and hands back the corrected text. Identifiers, paths, commands, and established loanwords (커밋, 리팩토링) are left alone. |
| `comment-corrector` | `off` / `fresh` / `reuse` | Admits `guard:comment-corrector`, for the source files the turn actually edited. Note this one **edits those files in place**, so its fixes land without being asked. |
| `router_model` | a model name, or empty | Model the **router** runs on. Empty (the default) leaves the choice to the router's own definition in the plugin's `agents/`. Every agent the router names uses its own model, so this changes which audits get picked, never how one is done. |
| `refs_dir` | a project-relative path, or empty | Where guard saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; point it at a different tracked path (e.g. `docs/refs`) to override. |
| `exempt_skills` | skill/command names, namespaced (e.g. `hindsight:review`) | Skills/commands whose finished turn guard never recommends an audit for. Managed with the `exempt` verbs above. |

Each key **is** the name of the agent it controls, so `settings set korean-corrector
reuse`, the `/guard:korean-corrector` command, and the `guard:korean-corrector` subagent
are all the same string.

### `fresh` vs `reuse`

`fresh` (what `on` means) spawns a new instance every time the agent is needed. `reuse`
keeps **one** instance for the session, named `guard-<agent>`: I dispatch it under that
name the first time and message it by name after that, so it keeps everything it has
already read and judged, and it can talk to me and to the other reused agents.

Neither is simply better:

- `reuse` buys continuity. The instance already knows this repository and this session's
  conventions, it stops re-deriving the same thing every turn, and I can go back to it —
  "you cleared this claim two turns ago; does the change I just made break it?"
- `fresh` buys independence. A verdict a reused instance got wrong is in its own history
  as settled, and every later turn inherits that error, where a new instance would have
  looked again.

Continuity is worth most where the judgment is about text and conventions — the two
correctors. Independence is worth most where it is about whether something is true — the
two auditors. Reuse lasts one session: a new session starts every agent fresh whatever
this says.

Changing a setting away from `reuse` means the instance that was running should stand
down and later turns spawn new ones — the CLI says so when it happens, and I act on it.

**Every setting ships off.** All four off is guard silent: when a turn finishes it adds
nothing to my context and makes no model call. Turning one on is what turns guard on, and
from then on each finished turn goes to guard's router — one subagent that reads the
response and names which of the switched-on agents would actually find something in it,
with a reason for each. I dispatch what it names, in parallel, and report back. A setting
only makes an agent *available* to the router; the router still has to find something in
the turn before it names it, which is why turning `korean-corrector` on costs nothing on
an English turn. The router itself is always a fresh instance — its question is about one
turn, and an instance carrying five of them can answer from the wrong one.

A setting that is off does **not** disable the matching command.
`/guard:claims-auditor`, `/guard:deferrals-auditor`, `/guard:korean-corrector` and
`/guard:comment-corrector` are you asking for that one audit now, and they work whatever
the settings say — which is the whole reason it is safe to leave them off.

The agent settings apply to the current session and become the new default; `router_model` /
`refs_dir` / `exempt_skills` are read from the file when used, so they also take effect
immediately.

## What to do

1. Run `settings show` and show the user the current settings.
2. **If `$ARGUMENTS` already names a key (and, for a scalar, a value)** — apply it
   directly with the matching command, skip the menu.
3. **Otherwise** call `AskUserQuestion` to ask which setting to change and to what: offer
   that key's valid values as options and note the current value. For an agent key, say
   what `fresh` and `reuse` mean in one line each rather than only listing them. For `exempt_skills`,
   ask which namespaced skill/command names to exempt (the user provides them), then
   record with `exempt set <names…>`.
4. Apply the change with the CLI, then relay the resulting settings the command prints
   back to the user in a short summary. Report exactly what changed.

Never write `.claude/guard.local.json` with Write/Edit — only the CLI above may change
guard's settings.
