---
name: doc-review-rules
description: "Configure Guard's per-path document review rules: choose agent or skill actions for document globs, exclude paths, and enable the edited-document hook. Use when the user wants different document reviewers by folder or file pattern. Claude Code only."
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

Then inspect only the project's Markdown paths when that helps turn the request into globs.
Explain the candidate rules in this form:

```json
[
  {"glob": "docs/generated/**", "action": null},
  {"glob": "docs/api/**", "action": {"kind": "skill", "name": "project:review-api-docs"}},
  {"glob": "docs/**", "action": {"kind": "agent", "name": "project:doc-reviewer"}}
]
```

An action is either an `agent`, dispatched as its exact `subagent_type`, a `skill`, run by its
exact name, or `null` to exclude the matching files from review. Patterns are project-relative:
`*` stays in one directory and `**` crosses directory depth. The most-specific matching rule
wins — deeper literal directories first, then literal detail and fewer wildcards. A tie uses
the earlier rule. A path that has no matching rule is not reviewed.

Before changing anything, show the exact compact JSON value and ask the user to confirm it.
A request that already gives exact rules counts as confirmation. On confirmation, enable
`doc-auditor` unless the user explicitly asks only to save inactive rules, then set the rules
through the CLI only:

```sh
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc-auditor on --session ${CLAUDE_SESSION_ID}
GUARD_SETTINGS_SKILL=1 "${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" settings set doc_review_rules '<compact-json-array>' --session ${CLAUDE_SESSION_ID}
```

Pass the compact JSON array as one shell argument without interpolation or shell evaluation.
Never edit `.claude/guard.local.json` directly. Re-run `settings show` after a successful
change and report the resulting rules. If the named agent or skill cannot be
resolved in this project, report that fact and leave the rule unchanged unless the user asks
to keep it anyway.
