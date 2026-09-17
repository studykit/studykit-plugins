---
name: doc-review-rules
description: "Configure Guard's per-path document review rules: choose agent or skill actions for document globs, exclude paths, and enable checkpoint review. Use when the user wants different document reviewers by folder or file pattern. Claude Code only."
argument-hint: '[desired document review coverage]'
disable-model-invocation: true
context: fork
model: sonnet
effort: medium
background: true
disallowed-tools: Write Edit NotebookEdit
---

Configure document-review rules for this project. You are a configuration helper: do not
create or edit reviewer agents or skills, and do not review documents yourself.

Fixed values for this run — already substituted. If either is missing or still looks like a
placeholder, say so and stop:

- guard CLI: `${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py`
- session id: `${CLAUDE_SESSION_ID}`

The user's request, possibly empty: `$ARGUMENTS`

First run:

```sh
"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings show --session ${CLAUDE_SESSION_ID}
```

Tell the user that Guard already provides these actions before asking them to invent or install
one:

- `agent:guard:doc-auditor` — checks ordinary project documentation for redundant or drifting content.
- `agent:guard:agents-md-auditor` — checks `AGENTS.md` and `CLAUDE.md` as always-loaded instructions.
- `agent:guard:ext-docs-auditor` — checks saved external references for source attribution and reference hygiene.

These names are ready to use when Guard is installed. Project or user actions remain valid
alternatives when their exact agent or skill names resolve.

Then inspect only the project's Markdown paths when that helps turn the request into globs.
`AGENTS.md` and `CLAUDE.md` follow the same rules as ordinary documents; use a pattern such as
`**/AGENTS.md` when they need a dedicated action.
Reference Markdown follows the same rules too; use `wiki/ref/**` (or the configured refs path)
with `guard:ext-docs-auditor` when the reference-specific review is wanted.
Explain the candidate rules in this form:

```json
[
  {"glob": "**/AGENTS.md", "action": {"kind": "agent", "name": "guard:agents-md-auditor"}},
  {"glob": "wiki/ref/**", "action": {"kind": "agent", "name": "guard:ext-docs-auditor"}},
  {"glob": "docs/api/**", "action": {"kind": "skill", "name": "project:review-api-docs"}},
  {"glob": "docs/**", "action": {"kind": "agent", "name": "project:doc-reviewer"}}
]
```

Explain exclusions separately as a `doc_exclude` list, for example:

```json
["docs/generated/**", "**/draft-*.md"]
```

An action is either an `agent`, dispatched as its exact `subagent_type`, or a `skill`, run by
its exact name. Exclusions belong in `doc_exclude`; `action: null` is invalid. Patterns in both
settings are project-relative:
`*` stays in one directory and `**` crosses directory depth. The most-specific matching rule
wins, and the filename decides first: a rule whose last segment names the file exactly
(`**/AGENTS.md`) beats one whose last segment is a pattern (`Github/**/*.md`), which beats a
bare wildcard (`Github/**/*`). Deeper literal directories break that tie, so
`Github/AGENTS.md` still wins over `**/AGENTS.md`, then literal detail and fewer wildcards. An
exact tie uses the earlier rule. A path that has no matching rule is not reviewed.

Before changing anything, show the exact compact JSON values and ask the user to confirm them.
A request that already gives exact rules counts as confirmation. On confirmation, enable
`doc-auditor` unless the user explicitly asks only to save inactive rules, then set the rules
through the CLI only:

```sh
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc-auditor on --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc_exclude 'docs/generated/**,**/draft-*.md' --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc_review_rules '<compact-json-array>' --session ${CLAUDE_SESSION_ID}
```

Pass the compact JSON array as one shell argument without interpolation or shell evaluation.
Never edit `.claude/guard.local.json` directly. Re-run `settings show` after a successful
change and report the resulting rules. If the named agent or skill cannot be
resolved in this project, report that fact and leave the rule unchanged unless the user asks
to keep it anyway.
