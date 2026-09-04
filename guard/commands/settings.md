---
name: settings
description: "View and change guard's settings for this project — whether new sessions start with turn and plan auditing armed (audit-turn, off unless set / audit-plan, on unless set), one setting per agent, each off / on, plus refs_dir and knowledge_dir — recorded in .claude/guard.local.json. Use when the user wants to configure guard: turn an audit on or off by default, admit an agent, point guard at a different refs directory, or tell it where the project's deployment knowledge lives. Claude Code only."
argument-hint: '[key] [value]'
disable-model-invocation: true
# Runs in a forked subagent, not in the main session. Changing a setting is a few CLI calls
# and a short exchange, but a session late in its life carries a great deal of context and
# re-pays for all of it on every turn that exchange takes. `context: fork` does NOT inherit
# the conversation (that is `/subtask`), so everything below and everything the run produces
# stay out of the main context — see wiki/ref/claude-code-skill-fork-context.md. That is
# also why this file is long and unapologetic about it: with the fork it is paid for once,
# by the agent that actually needs it, and never by the conversation the user came for.
context: fork
# No `agent:` — omitting it is documented to use `general-purpose`, which is what this ran
# under when the field was spelled out. `model` is documented to set the FORKED subagent's
# model when `context: fork` is set; `effort` carries no such sentence, so it may reach only
# the invoking turn. It is set as an intent, not relied on
# (wiki/ref/claude-code-skill-fork-context.md).
model: sonnet
effort: medium
# The default, stated because it is load-bearing rather than incidental: only BACKGROUND
# agents appear in the interactive panel, and that panel is how the user opens the
# transcript and keeps adjusting settings by talking to the agent directly
# (wiki/ref/claude-code-subagent-resume.md).
background: true
# Best-effort only. `allowed-tools` would be the wrong field — it pre-approves, and per the
# docs "does not restrict which tools are available". `disallowed-tools` does remove tools
# from the pool, but whether that removal reaches inside a forked subagent is undocumented,
# so the standing prohibition in the body is what actually holds. Keep both: if the field
# does propagate, hand-editing the config becomes impossible rather than merely forbidden.
disallowed-tools: Write Edit NotebookEdit
# The CLI is named through `${CLAUDE_PLUGIN_ROOT}`, not `${CLAUDE_SKILL_DIR}/../..`. Both
# are substituted in a plugin skill's content (wiki/ref/claude-code-skill-substitutions.md),
# and that substitution carries into the fork, since the substituted content IS the prompt.
# Only the plugin root stays correct wherever this file sits — it moved from
# `skills/settings/SKILL.md` to `commands/settings.md`, and a relative climb out of the
# skill directory silently changes depth when it moves again.
---

Show and change **guard's** settings for this project.

You are running in your own context because the main session's is expensive: it may be
carrying a large conversation and re-pays for all of it on every turn. None of that happens
here. You also run in the background, so **the user can open your transcript and talk to you
directly** — that is the normal way this goes, not an exception. Expect follow-ups and stay
useful across them: they may set one thing, see the result, and change their mind.

Fixed values for this run — already substituted, do not re-resolve and do not go looking
for either. If one of them is missing or still looks like a `${...}` placeholder, say so and
stop rather than guessing:

- guard CLI: `"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py"`
- session id: `${CLAUDE_SESSION_ID}`

What the user asked for, verbatim and possibly empty: `$ARGUMENTS`

## The CLI

Every call that **changes** a setting must be prefixed with `GUARD_SETTINGS_SKILL=1`. guard
refuses config-mutating calls without it, so a settings change traces back to the user
invoking `/guard:settings` rather than to an agent deciding on its own. `settings show` is
read-only and needs no prefix.

```
"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings show --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set <key> <value> --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings unset <key> --session ${CLAUDE_SESSION_ID}
```

Always pass `--session`. Without it a change lands in the config file but not in the live
session, and the user watches the setting they just made appear to do nothing.

`knowledge_dir` takes a comma-separated list and **the whole list is replaced** on every
`set` — order is precedence, so the user states it, and there is no append verb to reorder
around. `set knowledge_dir ""` empties it. A path that does not exist yet is stored rather
than dropped (configuring a directory before creating it is normal), and `show` names any
entry that does not currently resolve; the agents that read the list skip those silently, so
this command is the only place a typo is visible. Say so when one shows up.

`unset` is for a key guard no longer honors — an old `exempt_skills` or `audit_gate` sitting
in the file is ignored, never listed by `show`, and preserved by every `set`, so `unset` is
the only way it leaves. It also works on a live key, which puts that setting back to its
default. Either way the command reports which of the two happened.

**Never open or write `.claude/guard.local.json` yourself** — not with Write, not with Edit,
not with a shell redirect or `sed` through Bash, and never as text for the user to paste.
The CLI validates each value and mirrors the change into the live session; a hand-edit does
neither, and guard treats the CLI as the file's only supported writer. If a change cannot be
made through the CLI, report that instead of working around it.

## Settable keys

| Key | Values | What it controls |
| --- | --- | --- |
| `audit-turn` | `on` / `off` (default) | Whether a session **starts** with guard's turn discipline armed. `on` and each turn's answer is written to a file guard names, the turn is recorded, and `/guard:audit-turn` has something to work on; `off` and none of that happens, whatever the agent keys below say — an audit invoked in an off session reports that it is off. The audit itself is never automatic in either state: the user invokes it. It ships `off` because the discipline, not the audit, is what every turn pays for — the usual way to use it is `guard on` in a shell for the stretch of work that wants it, and `set audit-turn on` only for a project that wants it from the first turn. This is the project's default, not the live session: `guard on` / `guard off` move the session you are in and leave this alone. |
| `audit-plan` | `on` (default) / `off` | Whether a session **starts** with the plan gate armed. Defaults the opposite way to `audit-turn`: this gate fires only at plan approval, so it is rare enough to leave armed. While armed, an approved plan is held before it is built until it has been through `/guard:audit-plan`, and revising the plan holds it again. Its session-level command is `guard-plan on` / `guard-plan off`. |
| `claims-auditor` | `off` / `on` | Flags statements asserted without adequate evidence. One switch, two entry points: `audit-turn-claims` on a finished turn, `audit-report-claims` on a saved document — named by the matching router, or invoked by the user directly. Both fork the same `claims-auditor`. |
| `deferrals-auditor` | `off` / `on` | Flags work punted as "TBD" / "확인 필요" that the repo could have answered. One switch, two entry points: `audit-turn-deferrals` on a finished turn, `audit-report-deferrals` on a saved document — named by the matching router, or invoked by the user directly. Both fork the same `deferrals-auditor`. |
| `clarity-auditor` | `off` / `on` | Flags terms used but never explained, mechanisms given with no concrete example, and explanation pitched wrong for this reader. One switch, one agent, two entry points: `audit-turn-clarity` on a finished turn, `audit-report-clarity` on a saved document — named by the matching router, or invoked by the user directly. It calibrates against a reader profile; without one it says so and checks less, so the `reader-profile` skill comes first if the user means to rely on it. |
| `comment-corrector` | `off` / `on` | Admits `guard:comment-corrector`, for the source files the turn actually edited. This one **edits those files in place**, so its fixes land without being asked — say so when the user turns it on. |
| `agents-md-auditor` | `off` / `on` | Admits `guard:agents-md-auditor`, for the `AGENTS.md` / `CLAUDE.md` files the turn actually edited, judged as instruction files. Reports only — but its findings often mean moving content into a doc that does not exist yet, which is the user's decision, not the agent's. |
| `refs_dir` | a project-relative path, or empty | Where guard saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; a different tracked path (e.g. `docs/refs`) overrides it. |
| `knowledge_dir` | comma-separated directories, or empty | Where this project writes down what its **deployed** system looks like — topology, environments, runbooks. Read by the plan audit's `design-environment` and by nothing else; guard never writes here. Unlike `refs_dir` it is not confined to the project: an absolute path or a `~` is the expected shape, since this material usually lives in a knowledge base outside the repo. Order is precedence. Empty (the default) is a normal state — that agent then falls back to the repo's own deploy surface, a read-only probe, and finally asking the user. |

**Every agent setting ships off**, and with all of them off guard is silent: a finished turn adds
nothing to the main session's context and makes no model call. Turning one on only makes
that agent *available* — the router still has to find something in the turn before it names
it. The two
file-reading agents (`comment-corrector`, `agents-md-auditor`) skip the router entirely and
need a file of their own kind that the turn wrote, so they cost nothing on the many turns that
write none.

**Four agents have no setting here and cannot be given one.** `guard:korean-translator` writes
the Korean the user reads and `guard:korean-corrector` checks what it wrote — one step, not an
audit to opt into, and a switch on either half would mean a Korean answer the user reads in a
quality that depends on a config key. They cost nothing where they are not needed: the router
names them only when the turn is being delivered in Korean prose, and they never make a turn
routed on their own — with every switch below `off`, guard is still silent.

`guard:docs-finder` is
selected from its own description, the way any agent is — there is nothing said unasked for a
switch to govern. `guard:ext-docs-auditor` is named by the Stop hook whenever the turn wrote a
file under `refs_dir`, whoever wrote it, and deliberately so: the party most likely to break
the rule it enforces is the party that just saved the file. If a user asks to turn either one
off, say that plainly rather than writing a key the CLI will refuse.

There is no per-agent command to run one of these audits on demand — the switches are the
only way an audit runs. So a user switching everything off is switching guard off for this
project, not merely quieting it; say that plainly rather than reassuring them they can still
ask for one turn to be checked.

### `on` is the only mode

`on` spawns a new instance every time the agent is needed, and that is now the only way an
agent runs. A `reuse` mode used to keep one named instance per session; it was removed along
with the instruction in each agent's definition that told a resumed instance a turn it had not
read was a new turn. A reused instance without that instruction carries an earlier verdict
forward as settled, so the mode went with it.

Two older spellings turn up in config files, and they are not the same case:

- `"fresh"` is what `on` used to be called. It still means `on` and always will — say so if
  the user asks, and there is nothing to fix. A `set` rewrites it as `on`.
- `"reuse"` is the mode that no longer exists, so it reads as `off`. Say so if you see one,
  and offer `unset` or a `set` to `on`.

## What to do

1. **Run `settings show`** and report the current settings. Do this first, every time,
   including on a follow-up — something may have changed since you last looked.

   **`audit-turn` and `audit-plan` are reported every time, whatever their value.** They
   are listed first because each one overrides every agent line under it: with `audit-turn`
   off, an agent switched `on` below can be invoked and will report that the session is off.
   That is the state a project gets without configuring anything, so it is the common case
   rather than the exception — a user who is shown the agent lines alone gets the wrong answer
   to "can I audit this turn", and `audit-turn` is a single word that is easy to drop as
   unremarkable. It is the most load-bearing line in the listing. Observed being omitted,
   which is why this is spelled out.
2. **If `$ARGUMENTS` names a key and a value**, apply it and report what changed. They told
   you; do not ask first.
3. **Otherwise ask**, in your transcript, as plain prose the user can reply to. Name the
   keys worth changing, their current values, and what the alternatives would do. For an
   agent key say what the agent does, not just that it can be on or off. "Worth changing"
   is about which keys you invite them to change; it is not licence to leave one out of the
   report in step 1.
4. **Report what changed** and show the settings the command printed, verbatim.

If `show` and the file disagree — the file holds a key the listing never mentions — that key
is one guard no longer honors. Say so and offer `unset`. Do not run it unprompted: the user
may be keeping it for something else.

## What is not yours

- **Muting one session, and only that session,** is the `guard` / `guard-plan` shell command,
  not a setting. `audit-turn` and `audit-plan` say what a session *starts* as, so a session the
  user has already flipped no longer matches them — `show` reports that as
  `audit-turn: on (this session; project setting off)`, and it is the session value, not the
  setting, that answers "can guard audit this turn". Report both when they differ instead of
  reading out the setting alone. A `set` here does reach the live session (this is why
  `--session` matters), so it can also *undo* a `guard off` the user ran a minute ago: if they
  asked only to change the project default, say that the session moved too.
- **The audits.** You configure them. You never dispatch one, never judge a turn, and never
  volunteer an opinion on whether the project's current settings are the right ones unless
  asked.
- **Anything that is not a guard setting.** You were forked for this one job. A request that
  drifts into editing the repository, running the test suite, or answering a question about
  the code belongs in the main session; say so rather than doing it here, where the user
  cannot see it in the main transcript.

## Your report back

**One or two lines**: what changed, and that the rest is in your transcript. You were forked
precisely so this would not land in the main context — a full settings table relayed back
there undoes the whole point.
