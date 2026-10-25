---
name: settings
description: Configure this project's Guard reviewers, file patterns, exclusions, and Stop-time review questions. Select existing reviewers or help create project-local reviewers from the user's criteria.
disable-model-invocation: true
---

# Configure project reviews

Work only on the project and settings the user requested. Guard supplies routing and review
consent, not review criteria or a default reviewer. Use the user's exact agent or skill name;
an unavailable reviewer is an error, never a reason to substitute another.

## Inspect the project

Resolve `scripts/settings.py` relative to this `SKILL.md`. Identify the target project root,
current host (`claude` or `codex`), and the native session id. Claude substitutes its current
session id here: `${CLAUDE_SESSION_ID}`. Codex exposes `CODEX_THREAD_ID` to shell commands.
Use the value for the active host and pass concrete values:

```text
uv run --script <settings-script> --host <host> --project <project-root> --session <session-id> show
```

If a required value is unavailable, report that instead of guessing. Inspect the existing
configuration before proposing any change. Keep unrelated settings, rules, exclusions, and
their order. This skill never changes user-global settings or installs Guard-owned agents.

## Choose or create a reviewer

Find available project agents and skills using the host's installed definitions and the
project's own instructions. Claude project agents normally live under `.claude/agents/`;
Codex project agents under `.codex/agents/`. Project skill locations and any shared-folder or
symlink conventions belong to the target project. Do not assume a plugin prefix or derive an
agent's name from its filename: use its declared native name.

For each requested scope, establish:

- Which files or folders to review, including exclusions.
- The user's review criteria or the project requirements that own them.
- The exact agent or skill to run and whether it may edit or only report findings.
- Whether the user wants a Stop-time question or only explicit checkpoints.

If an appropriate reviewer exists, show its name and scope. If none exists, offer to create
a project-local agent or skill from the user's criteria. Do not invent domain-specific
criteria. A request that already specifies its name, criteria, and creation scope authorizes
that creation; otherwise show the proposed definition and get the missing decision first.
Never overwrite an existing definition without authorization.

Create native definitions for the requested host: a Claude agent is Markdown with `name`
and `description` frontmatter; a Codex agent is TOML with `name`, `description`, and
`developer_instructions`. Leave model selection inherited unless the user specifies it.
For both hosts, keep the same approved criteria while using each host's format and exact
name in its own Guard configuration. Follow the project's conventions for reviewer skills.
An instruction to avoid edits is not a host-enforced read-only sandbox. Explain any required
session restart before the newly created reviewer can be invoked.

## Propose and save settings

`file_review_rules` is a JSON array. Each rule names a project-relative `glob`, an `action`
object with `kind: agent|skill` and `name`, and optional `on_stop: manual|ask`. Omitted
`on_stop` means `manual`. `ask` offers a question after a normal Stop; accepting authorizes
only the selected file review. Decline or cancel leaves those revisions unreviewed.

Examples use placeholder project reviewers, not defaults:

```json
[
  {"glob":"src/**","action":{"kind":"agent","name":"source-reviewer"},"on_stop":"ask"},
  {"glob":"docs/**/*.md","action":{"kind":"skill","name":"review-project-docs"},"on_stop":"manual"}
]
```

`*` stays within a directory; `**` crosses directories. The most-specific matching rule
wins, so a more-specific manual rule can override a broader ask rule. `files_exclude` is an
ordered list of project-relative patterns; a later `!pattern` restores a matching file.
`doc_dir` scopes ordinary Markdown documents only, not other file types.

Show the complete resulting rule list and exclusions before saving a proposal. Exact changes
already requested by the user need no second confirmation. Save through the helper, never
by editing `.claude/guard.local.json` or `.codex/guard.local.json` directly:

```text
GUARD_SETTINGS_SKILL=1 uv run --script <settings-script> --host <host> --project <project-root> --session <session-id> set file_review_rules '<complete-json-array>'
GUARD_SETTINGS_SKILL=1 uv run --script <settings-script> --host <host> --project <project-root> --session <session-id> set files_exclude '<comma-separated-patterns>'
```

Quote each path and JSON value as one shell argument. Each `set` replaces that whole value.
`plan_review`, `turn_review`, and `answer_review` independently take one action object or `{}`;
they do not inherit file rules. `audit-plan` takes `on|off`. `knowledge_dir`, `doc_dir`, and
`files_exclude` take comma-separated lists. `unset <key>` removes only the requested key.

The helper validates configuration shape, not host discovery. Verify the selected reviewer
exists before saving; do not present a successful setting write as proof that a review ran.
Never select `guard:audit-files` as its own file reviewer.

Run `show` again and summarize the resulting settings and any host hook-trust or discovery
steps still required. Saving settings or creating a reviewer does not run a review.
