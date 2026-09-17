---
name: settings
description: "View and change Guard settings for this project, including edited-document review rules. Use when the user wants to configure audits, document review actions, reference paths, or deployment knowledge. Claude Code only."
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
in the file is ignored and preserved by every `set`, so `unset` is the only way it leaves. A
key guard USED to honor is a separate case: `show` lists it on a `(retired)` line saying what
replaced it, because a project was getting behaviour from it and no longer is. It also works on a live key, which puts that setting back to its
default. Either way the command reports which of the two happened.

**Never open or write `.claude/guard.local.json` yourself** — not with Write, not with Edit,
not with a shell redirect or `sed` through Bash, and never as text for the user to paste.
The CLI validates each value and mirrors the change into the live session; a hand-edit does
neither, and guard treats the CLI as the file's only supported writer. If a change cannot be
made through the CLI, report that instead of working around it.

## Settable keys

| Key | Values | What it controls |
| --- | --- | --- |
| `audit-plan` | `on` (default) / `off` | Whether a session **starts** with the plan gate armed. It is the one audit the user does not invoke — the gate fires on its own at plan approval — which is why it is the only one a project answers for in advance. While armed, an approved plan is held before it is built until it has been through `/guard:audit-plan`, and revising the plan holds it again. This is the project's default, not the live session: `guard-plan on` / `guard-plan off` move the session you are in and leave this alone. |
| `plan_review` | JSON object, or `{}` | **Who** reviews a held plan: `{"kind":"agent" or "skill","name":"..."}`. `{}` (the default) means Guard's own plan review, `skill:guard:audit-plan`. This does not decide whether a plan is held — `audit-plan` above does. |
| `claims-auditor` | `off` / `on` | Flags statements asserted without adequate evidence. One switch, two entry points: `audit-turn-claims` on a finished turn, `audit-report-claims` on a saved document — named by the matching router, or invoked by the user directly. Both fork the same `claims-auditor`. |
| `deferrals-auditor` | `off` / `on` | Flags work punted as "TBD" / "확인 필요" that the repo could have answered. One switch, three entry points: `audit-turn-deferrals` on a finished turn, `audit-report-deferrals` on a saved document, `audit-plan-deferrals` on an approved plan — named by the matching router or by the plan review, or invoked by the user directly. All three fork the same `deferrals-auditor`. |
| `clarity-auditor` | `off` / `on` | Flags terms used but never explained, mechanisms given with no concrete example, and explanation pitched wrong for this reader. One switch, one agent, three entry points: `audit-turn-clarity` on a finished turn, `audit-report-clarity` on a saved document, `audit-plan-clarity` on an approved plan — named by the matching router or by the plan review, or invoked by the user directly. It calibrates against a reader profile; without one it says so and checks less, so the `reader-profile` skill comes first if the user means to rely on it. |
| `comment-corrector` | `off` / `on` | Selects `guard:comment-corrector` for pending source files when the user runs `/guard:audit-files`. This one **edits those files in place**, so say so when the user turns it on. |
| `doc-auditor` | `off` / `on` | Enables review actions for pending project Markdown at `/guard:audit-files` checkpoints, including `AGENTS.md` and `CLAUDE.md`. A file is acted on only when it matches a `doc_review_rules` entry. |
| `doc_dir` | comma-separated project directories | Limits the ordinary Markdown documents eligible for review. An empty value means the whole project. |
| `doc_exclude` | comma-separated project directories or globs | Excludes matching Markdown—including agent instructions and references—from review. `*` stays in one directory and `**` crosses directory depth. |
| `doc_review_rules` | JSON array | Per-path actions. Each item is `{"glob":"...","action":{"kind":"agent" or "skill","name":"..."}}`. Unmatched files are not reviewed; use `doc_exclude` for explicit exclusions. Use `/guard:doc-review-rules` for guided setup. |
| `refs_dir` | a project-relative path, or empty | Where guard saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; a different tracked path (e.g. `docs/refs`) overrides it. |
| `knowledge_dir` | comma-separated directories, or empty | Where this project writes down what its **deployed** system looks like — topology, environments, runbooks. Read by the plan audit's `plan-environment` and by nothing else; guard never writes here. Unlike `refs_dir` it is not confined to the project: an absolute path or a `~` is the expected shape, since this material usually lives in a knowledge base outside the repo. Order is precedence. Empty (the default) is a normal state — that agent then falls back to the repo's own deploy surface, a read-only probe, and finally asking the user. |

`plan_review` takes one JSON object as a single shell argument, and it **replaces the whole
value**; `set plan_review '{}'` puts Guard's own review back. Two things to tell the user
before changing it. A reviewer that is not `guard:audit-plan` has to run `guard-plan-audited
<plan file path>` when it finishes, or the gate keeps holding the plan — the hook says so when
it fires, but the reviewer they name has to be one that will act on it. And Guard does not
check that the name resolves: if the agent or skill is not installed, the dispatch finds
nothing and the plan stays held. Say so when the name is not one you can see in this project.

When reporting `doc_review_rules`, tell the user that Guard already ships
`agent:guard:doc-auditor`, `agent:guard:agents-md-auditor`,
and `agent:guard:ext-docs-auditor`. Briefly describe the matching
specialty; do not make a built-in action sound like something they must install separately.

**Every agent setting ships off**, and with all of them off guard says almost nothing: a
finished turn adds nothing to the main session's context and makes no model call. The refs
index gate remains independent of review rules, so a reference saved without being indexed is
still blocked. Turning one on only makes
that agent *available* — the router still has to find something in the turn before it names
it. The two
file-reading `comment-corrector` skips the router and needs a source file this turn wrote.
Document review actions likewise need both `doc-auditor: on` and a matching rule.

**Four agents have no setting here and cannot be given one.** `korean-translator` writes the
Korean the user reads and `korean-corrector` checks what it wrote — one step, not an audit to
opt into, and a switch on either half would mean a Korean answer the user reads in a quality
that depends on a config key. They cost nothing where they are not needed, because they only
run over a DOCUMENT: `/guard:answer` dispatches the translator when the reader reads another
language, the router names it for a file the user points at, and the corrector is reached
by the translator's own report. An ordinary turn produces no document, so nothing is translated
there at all. They never make a turn routed on their own — with every switch below `off`, they
are dropped too.

Those two are also the only pair here guard does not ship: they are **user-level** agents,
installed once per machine rather than with this plugin, which is why their names carry no
`guard:` prefix. A machine without them translates nothing — guard says so and hands over the
English rather than translating it in the main session.

`guard:docs-finder` is selected from its own description, the way any agent is — there is
nothing said unasked for a switch to govern. `guard:ext-docs-auditor` may be selected by a
document review rule at an explicit file checkpoint. If a user asks to turn either one off,
say that plainly rather than writing a key the CLI will refuse.

**The plan review ignores these keys entirely.** `/guard:audit-plan` invokes its seven
critics by name, `audit-plan-deferrals` and `audit-plan-clarity` among them, and reads no
switch. A user who approved a plan and had it held for review gets the whole review, in a
project with every key below `off`. Do not offer to turn a plan critic off here; there is no
key for one.

**What a switch decides is what happens WITHOUT being asked, and what the routers may
offer — not what the user can run.** Only `guard-candidates` reads these keys, and only
`/guard:audit-turn`, `/guard:audit-report` and `/guard:answer` run it. The per-audit
commands do not: `/guard:audit-turn-claims`, `/guard:audit-turn-clarity` and
`/guard:audit-turn-deferrals` (and their `audit-report-` counterparts) are invoked by name
and run whatever the switches say.

Switching everything off means the routers and file checkpoint find no configured audit to
name — while a user who types a per-audit command still gets that audit. Say it that way if
they ask; do not tell them the audit cannot happen.

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

   **The first two lines are reported every time, whatever they say.** `file checkpoint`
   reports this session's pending path count and reminds the user that Stop does not launch
   audits; `audit-plan` reports the independent plan gate. A user shown only the agent lines
   cannot tell whether there is checkpoint work waiting.
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
may be keeping it for something else. A key guard *used* to honor is named in the listing
itself, on a `(retired)` line that says what replaced it; `audit-turn` is one, retired in
v0.124.0 now that every audit on that path is invoked by the user. Read that line out — a
project carrying the key was getting behaviour it no longer gets.

## What is not yours

- **Changing the live plan gate** is the `guard-plan` shell command, not a setting.
  `audit-plan` has a key, and it says what a session *starts* as — a session the
  user has already flipped no longer matches it, and `show` reports that as
  `audit-plan: on (this session; project setting off)`. It is the session value, not the
  setting, that answers whether the plan gate is running right now, so report both when they differ instead
  of reading out the setting alone. A `set audit-plan` does reach the live session (this is why
  `--session` matters), so it can also *undo* a `guard-plan off` the user ran a minute ago: if
  they asked only to change the project default, say that the session moved too.
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
