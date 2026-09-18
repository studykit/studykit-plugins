---
name: settings
description: "View and change Guard settings for this project, including user-configured plan, turn, and answer reviewers and edited-document review rules. Use when the user wants to configure audits, document review actions, reference paths, or deployment knowledge. Claude Code only."
argument-hint: '[setting or desired review coverage]'
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

Show and change **guard's** settings for this project. This includes choosing document
reviewers by folder or file pattern. Configure existing reviewers; do not create or edit
reviewer definitions or run reviews as part of changing settings.

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

Start with `settings show` to inspect the current configuration before proposing changes.

Every call that **changes** a setting must be prefixed with `GUARD_SETTINGS_SKILL=1`. guard
refuses config-mutating calls without it, so a settings change traces back to the user
invoking `/guard:settings` rather than to an agent deciding on its own. `settings show` is
read-only and needs no prefix.

```
"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings show --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set <key> <value> --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings unset <key> --session ${CLAUDE_SESSION_ID}
```

Always pass `--session` so file-review switches and the automatic plan-gate switch also
update the calling session. Reviewer settings are read from the project configuration at
each invocation, so changing a reviewer does not require restarting the session.

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
The CLI validates each value and mirrors switch changes into the live session. Use it for
all configuration changes made by this command. If a change cannot be
made through the CLI, report that instead of working around it.

## Settable keys

| Key | Values | What it controls |
| --- | --- | --- |
| `audit-plan` | `on` (default) / `off` | Whether a session starts with the Claude Code plan gate armed. While armed, approved plans go to the reviewer configured in `plan_review`; without one, no review runs. Revising an audited plan holds it again at the next approval. `guard-plan on` / `guard-plan off` change the live session. |
| `plan_review` | JSON object, or `{}` | The user-supplied reviewer: `{"kind":"agent" or "skill","name":"..."}`. `{}` (the default) or an absent key means no plan review. Guard supplies no review criteria. The automatic Claude gate also requires the `audit-plan` switch; explicit `audit-plan` skill invocations do not. |
| `turn_review` | JSON object, or `{}` | The user-supplied turn reviewer: `{"kind":"agent" or "skill","name":"..."}`. Unset or `{}` means no turn review. `audit-turn` invokes only this reviewer, independently of the per-agent switches. |
| `answer_review` | JSON object, or `{}` | The user-supplied answer reviewer: `{"kind":"agent" or "skill","name":"..."}`. `answer` stops before drafting when unset or `{}`. The reviewer owns the criteria. |
| `comment-corrector` | `off` / `on` | Selects `guard:comment-corrector` for pending source files when the user runs `/guard:audit-files`. This one **edits those files in place**, so say so when the user turns it on. |
| `doc-auditor` | `off` / `on` | Enables review actions for pending project Markdown at `/guard:audit-files` checkpoints, including `AGENTS.md` and `CLAUDE.md`. A file is acted on only when it matches a `doc_review_rules` entry. |
| `doc_dir` | comma-separated project directories | Limits the ordinary Markdown documents eligible for review. An empty value means the whole project. |
| `doc_exclude` | comma-separated project directories or globs | Excludes matching Markdown—including agent instructions and references—from review. `*` stays in one directory and `**` crosses directory depth. |
| `doc_review_rules` | JSON array | Per-path actions. Each item is `{"glob":"...","action":{"kind":"agent" or "skill","name":"..."}}`. Unmatched files are not reviewed; use `doc_exclude` for explicit exclusions. Use the document-review setup below for guided configuration. |
| `refs_dir` | a project-relative path, or empty | Where guard saves cited-doc copies. Empty = the git-tracked default `wiki/ref/`, committed with the repo; a different tracked path (e.g. `docs/refs`) overrides it. |
| `knowledge_dir` | comma-separated directories, or empty | Operational knowledge directories, such as topology, environments and runbooks. Available through audit inputs and `guard-knowledge-dirs`, including to user-supplied reviewers. Guard never writes here. Absolute and `~` paths are supported; order is precedence. Empty means none configured. |

## Registering a reviewer

For `plan_review`, `turn_review`, or `answer_review`, use the exact installed agent or skill
name selected by the user. If the user has not specified its kind and name, ask for the
missing information; do not choose a built-in auditor or invent a reviewer. Guard validates
the object syntax, not whether the named reviewer is installed. Explain this distinction
when reporting a successful setting change; it does not mean a review has run.

For example, after the user chooses the reviewer, pass its JSON object as one argument:

```sh
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set turn_review '{"kind":"skill","name":"my-turn-reviewer"}' --session "${CLAUDE_SESSION_ID}"
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set answer_review '{"kind":"agent","name":"my-answer-reviewer"}' --session "${CLAUDE_SESSION_ID}"
```

These are examples, not default reviewers. The same object form applies to `plan_review`.
If an existing setting names a removed Guard skill or plan agent, explain that it must be
replaced with the user's installed reviewer or cleared. Do not silently rewrite the name,
clear the setting, or substitute an auditor. Never register a dispatcher as its own reviewer.

`turn_review` takes one JSON object as a single shell argument and replaces the whole value.
Use `set turn_review '{}'` or `unset turn_review` to disable it. The user must implement and
install the named agent or skill; never select a fallback or register `guard:audit-turn` as
its own reviewer. `/guard:audit-turn` in Claude Code and `$guard:audit-turn` in Codex use this
setting and report findings without editing the response or project files. No Stop hook
launches a review. The standalone `audit-report` skill has been removed.

`plan_review` takes one JSON object as a single shell argument and replaces the whole
value. `set plan_review '{}'` or `unset plan_review` disables plan review without changing
the gate switch. For Claude's automatic gate, after the configured review finishes and its
findings are in the plan, the caller must run `guard-plan-audited <plan file path>`; the hook
includes that instruction. The explicit `audit-plan` skill handles completion on either host.
Guard validates the action syntax but does not check that the reviewer is installed. Tell
the user when the name is not available in this session; do not substitute another reviewer.
The automatic plan gate currently runs only in Claude Code. For an explicit review, use
`/guard:audit-plan <path>` in Claude Code or `$guard:audit-plan <path>` in Codex. Do not
register `guard:audit-plan` as its own reviewer.

`answer_review` takes one JSON object and replaces the whole value. `set answer_review '{}'`
or `unset answer_review` clears it. The `answer` workflow stops before drafting without a
reviewer. Users must install the named reviewer; do not substitute another or register
`guard:answer` as its own reviewer. The reviewer reads the answer document and returns
findings; the caller applies corrections. Only this workflow creates an answer document.

The three reviewer settings are independent: `answer` uses `answer_review`, `audit-turn`
uses `turn_review`, and `audit-plan` uses `plan_review`. Guard supplies no fallback criteria.
The `claims-auditor`, `deferrals-auditor`, and `clarity-auditor` switches are retired. Explain
that users should configure their own reviewer, then remove obsolete keys with `unset` if
requested. The `audit-report`, `audit-report-*`, and individual `audit-turn-*` skills no longer exist.
Use `audit-turn` with a user-configured reviewer for turn audits.

`korean-translator` and `korean-corrector` are user-level delivery agents, without a `guard:`
prefix or audit switch. `answer` uses the translator after review for Korean readers. If
unavailable, deliver the reviewed English file and explain. `guard:docs-finder` remains
available by its description; `guard:ext-docs-auditor` can be selected by a document rule.

## Configure document-review rules

Use this flow when the user asks for document review by folder or file pattern. First show
current settings, then explain the existing built-in actions before asking the user to
supply a custom reviewer:

- `agent:guard:doc-auditor` checks ordinary project documentation for redundant or drifting content.
- `agent:guard:agents-md-auditor` checks `AGENTS.md` and `CLAUDE.md` as always-loaded instructions.
- `agent:guard:ext-docs-auditor` checks saved external references for attribution and reference hygiene.

Project and user agents or skills are also valid choices. Use their exact installed names.
If a requested action cannot be resolved, report that before changing anything and leave
its rule unchanged unless the user explicitly wants to save the unresolved name.

Inspect only the project's Markdown paths when needed to turn the request into patterns.
Use the configured reference directory for reference rules; do not assume a directory
layout. Instruction files and reference Markdown follow the same rule selection as ordinary
documents. These examples illustrate the rule structure, not a default configuration:

```json
[
  {"glob":"**/AGENTS.md","action":{"kind":"agent","name":"guard:agents-md-auditor"}},
  {"glob":"**/CLAUDE.md","action":{"kind":"agent","name":"guard:agents-md-auditor"}},
  {"glob":"docs/references/**","action":{"kind":"agent","name":"guard:ext-docs-auditor"}},
  {"glob":"docs/api/**","action":{"kind":"skill","name":"project:review-api-docs"}},
  {"glob":"docs/**","action":{"kind":"agent","name":"guard:doc-auditor"}}
]
```

An action is an `agent` or `skill`, invoked by its exact name. Exclusions belong in
`doc_exclude`, for example `["docs/generated/**", "**/draft-*.md"]`; `action: null` is invalid.
Both rule patterns and exclusion globs are project-relative. `*` stays in one directory;
`**` crosses directory depth. The most-specific matching rule wins: an exact filename such
as `**/AGENTS.md` beats a filename pattern such as `docs/**/*.md`, which beats `docs/**/*`.
Deeper literal directories break that tie, followed by literal detail and fewer wildcards.
An exact tie uses the earlier rule. Unmatched paths are not reviewed. `doc_exclude` applies
to all Markdown, including instruction files and saved references; `doc_dir` limits ordinary
Markdown coverage.

Each `set` replaces the whole list. Preserve existing rules, exclusions, and scope that the
user did not ask to change; show the complete resulting values. Explain any enabled
`doc_dir` restriction that would keep the requested ordinary documents out of review.

For rules you propose, show the exact compact JSON and ask for confirmation before saving.
A request that already specifies the exact rules counts as confirmation. Save only the
requested lists through the CLI, then enable `doc-auditor` unless the user asked only to save
inactive rules. If a write fails, report which changes succeeded and stop. Example commands:

```sh
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc_review_rules '<complete-compact-json-array>' --session "${CLAUDE_SESSION_ID}"
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc_exclude 'docs/generated/**,**/draft-*.md' --session "${CLAUDE_SESSION_ID}"
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc-auditor on --session "${CLAUDE_SESSION_ID}"
```

Pass the JSON as one safely quoted shell argument without interpolation or shell evaluation.
`doc_exclude` and `doc_dir` take comma-separated lists at the CLI, not JSON arrays. Re-run
`settings show` and report the resulting configuration. Saving settings does not run reviews;
the user runs `/guard:audit-files` when the pending edits are ready.

The file-review switches default to `off`. `comment-corrector` requires pending source files;
document review requires `doc-auditor: on` and a matching rule. The reference-index gate
remains independent of these switches.
