---
name: settings
description: "View and change guard's settings for this project — one setting per agent, each off / fresh / reuse, plus router_model and refs_dir — recorded in .claude/guard.local.json. Use when the user wants to configure guard: turn an audit on or off, delegate documentation lookups, keep an agent running across turns instead of respawning it, or set the router's model or refs_dir. Claude Code only."
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
| `claims-auditor` | `off` / `fresh` / `reuse` | Admits `guard:claims-auditor` — it flags statements asserted without adequate evidence. |
| `deferrals-auditor` | `off` / `fresh` / `reuse` | Admits `guard:deferrals-auditor` — it flags work punted as "TBD" / "확인 필요" that the repo could have answered. |
| `clarity-auditor` | `off` / `fresh` / `reuse` | Admits `guard:clarity-auditor` — it flags terms used but never explained, mechanisms given with no concrete example, and explanation pitched wrong for this reader. It calibrates against a reader profile; without one it says so and checks less, so `/guard:reader-profile` comes first if the user means to rely on it. |
| `korean-corrector` | `off` / `fresh` / `reuse` | Admits `guard:korean-corrector` — it flags 번역체 phrasing and a register that is not 존댓말, and hands back the corrected text. Identifiers, paths, commands, and established loanwords (커밋, 리팩토링) are left alone. |
| `comment-corrector` | `off` / `fresh` / `reuse` | Admits `guard:comment-corrector`, for the source files the turn actually edited. This one **edits those files in place**, so its fixes land without being asked — say so when the user turns it on. |
| `agents-md-auditor` | `off` / `fresh` / `reuse` | Admits `guard:agents-md-auditor`, for the `AGENTS.md` / `CLAUDE.md` files the turn actually edited, judged as instruction files. Reports only — but its findings often mean moving content into a doc that does not exist yet, which is the user's decision, not the agent's. |
| `ext-docs-fetcher` | `off` / `fresh` / `reuse` | Admits `guard:ext-docs-fetcher` — the only agent on the **network**, and the only one reached from both ends of a turn. With it on, the session stops running WebFetch/WebSearch itself and dispatches this instead: it reports the local path of documentation already saved here, or fetches the primary source and saves it, and says which it did. **It writes to the repository** — new files under `refs_dir` and rows in that directory's index — so say that when the user turns it on. |
| `ext-docs-auditor` | `off` / `fresh` / `reuse` | Admits `guard:ext-docs-auditor`, for the files under `refs_dir` the turn actually wrote. It checks that a reference is a reference: a trustworthy source named, content attributed rather than recalled, and nothing in it about **this** repository — the last being the rule that actually gets broken. Reports only. |
| `router_model` | a model name, or empty | Model the **router** runs on. Empty (the default) leaves the choice to the router's own definition in the plugin's `agents/`. Every agent the router names brings its own model, so this changes which audits get picked, never how one is done. |
| `refs_dir` | a project-relative path, or empty | Where guard saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; a different tracked path (e.g. `docs/refs`) overrides it. |

**Every setting ships off**, and with all of them off guard is silent: a finished turn adds
nothing to the main session's context and makes no model call. Turning one on only makes
that agent *available* — the router still has to find something in the turn before it names
it, which is why turning `korean-corrector` on costs nothing on an English turn. The three
file-reading agents (`comment-corrector`, `agents-md-auditor`, `ext-docs-auditor`) skip the router
entirely and need a file of their own kind that the turn wrote, so they cost nothing on the
many turns that write none. `ext-docs-fetcher` is the one that also runs *before* an answer, off a
policy stated once at session start.

A setting that is off does **not** disable the matching command. `/guard:claims-auditor`,
`/guard:deferrals-auditor`, `/guard:clarity-auditor` and `/guard:korean-corrector` are the
user asking for that one audit now, and they work whatever the settings say — which is the
whole reason it is safe to leave them off. Say this to a user who hesitates to switch
something off.

### `fresh` vs `reuse`

`fresh` (what "on" means) spawns a new instance every time the agent is needed. `reuse`
keeps **one** instance for the session, named `guard-<agent>`: the main session dispatches
it under that name once and messages it by name afterwards, so it keeps everything it has
already read and judged.

Neither is simply better:

- `reuse` buys continuity — the instance already knows this repository and this session's
  conventions and stops re-deriving them every turn.
- `fresh` buys independence — a verdict a reused instance got wrong sits in its own history
  as settled, and every later turn inherits that error where a new instance would look
  again.

Continuity is worth most where the judgment is about text and conventions: the correctors.
Independence is worth most where it is about whether something is true: the auditors. Reuse
lasts one session — a new session starts every agent fresh whatever this says.

A mode moved **away** from `reuse` makes the CLI print a stand-down note. Pass it through
verbatim: it is guard's only channel for telling the main session to stop addressing an
instance guard itself cannot see.

## What to do

1. **Run `settings show`** and report the current settings. Do this first, every time,
   including on a follow-up — something may have changed since you last looked.
2. **If `$ARGUMENTS` names a key and a value**, apply it and report what changed. They told
   you; do not ask first.
3. **Otherwise ask**, in your transcript, as plain prose the user can reply to. Name the
   keys worth changing, their current values, and what the alternatives would do. For an
   agent key give one line on `fresh` and one on `reuse` rather than only listing them.
4. **Report what changed** and show the settings the command printed, including any
   stand-down note, verbatim.

If `show` and the file disagree — the file holds a key the listing never mentions — that key
is one guard no longer honors. Say so and offer `unset`. Do not run it unprompted: the user
may be keeping it for something else.

## What is not yours

- **Muting for one session** is `/guard:toggle`, not a setting. A `settings set` writes
  `guard.local.json` and changes what the project does from now on; the toggle is session
  state only. If that is what the user actually wants, say so and let them run it — you
  cannot, and should not try.
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
