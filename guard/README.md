# Guard

Guard provides user-configured turn, plan, and answer reviews, and configurable
review actions for files changed by Claude Code or Codex.

## Turn reviews

Implement and install your reviewer, then set `turn_review` in `.claude/guard.local.json`
for Claude Code or `.codex/guard.local.json` for Codex:

```json
{
  "turn_review": {"kind": "agent", "name": "my-turn-reviewer"}
}
```

Use `"kind": "skill"` to register a skill instead. Supply the exact name supported by the
host. Guard does not choose review criteria or substitute a built-in reviewer. An absent
setting or `{}` means no turn review; `audit-turn` cannot be registered as its own reviewer.

Run `/guard:audit-turn` in Claude Code or `$guard:audit-turn` in Codex to review the last
completed auditable response. Append a turn id to select an earlier one. The reviewer receives
a JSON file with `turn_id`, `user` (the request), `assistant` (the response), `tools` (recorded
activity), and `source_path` for context. It should read that evidence and return findings
without changing the evidence or project files. The result is reported in the conversation.

Each invocation starts a fresh review. Turn reviews never run automatically at Stop.
Guard's hooks must be active to make the session's evidence available; missing evidence or
an unavailable reviewer is reported as an error, not a successful review.

The individual `audit-turn-claims`, `audit-turn-deferrals`, and `audit-turn-clarity` skills
have been removed. Use `audit-turn` with your own `turn_review` agent or skill. Replace any
reviewer setting that names a removed skill with an installed reviewer.

## Answer documents

Install your reviewer and register it in your host's `guard.local.json`:

```json
{
  "answer_review": {"kind": "skill", "name": "my-answer-reviewer"}
}
```

Use `"kind": "agent"` for an agent. Run `/guard:answer <question>` in Claude Code or
`$guard:answer <question>` in Codex. Guard writes an English answer document, asks the exact
configured reviewer to read it and return findings, and applies corrections within the
question's scope. The reviewer owns the criteria. Missing configuration or an unavailable
reviewer stops the workflow before drafting; `answer` cannot review itself.

Documents are saved under `.claude/answers/` or `.codex/answers/`. For Korean readers, the
installed user-level `korean-translator` translates the reviewed document. If unavailable,
Guard delivers the reviewed English file and explains the missing translation.

The `audit-report` and `audit-report-*` skills have been removed. The `claims-auditor`,
`deferrals-auditor`, and `clarity-auditor` switches are retired and have no effect. Replace
those settings with `answer_review` or `turn_review`; use `audit-files` and
`file_review_rules` for reviews of changed files. Claude's settings command identifies
retired keys and can remove them with `unset`.

## Plan reviews

Implement and install your own plan-review agent or skill, then register its exact invocation
name in `.claude/guard.local.json` for Claude Code or `.codex/guard.local.json` for Codex:

```json
{
  "audit-plan": "on",
  "plan_review": {"kind": "agent", "name": "my-plan-reviewer"}
}
```

Use `"kind": "skill"` for a skill. Guard supplies no built-in plan reviewers or review criteria;
an absent `plan_review` or `{}` skips review. The registered reviewer determines what to check.

Review an existing plan file with `/guard:audit-plan <path>` in Claude Code or
`$guard:audit-plan <path>` in Codex. Each invocation requests a fresh review, even when the
automatic gate is off or the plan was already reviewed. The assistant applies agreed findings
to the plan and records completion. Changes of approach are brought back to you first;
reviewing a plan does not start implementation.

Claude Code also requests the configured review after you approve a plan and before
implementation. The `audit-plan` setting controls this automatic gate; `guard-plan on`,
`guard-plan off`, and `guard-plan status` control or report its session switch. A changed plan
is reviewed again at its next approval. Codex supports explicit invocation only.

When upgrading from a version with bundled plan reviewers, replace any `plan_review` value
that names a removed Guard reviewer with your own reviewer, or clear it with `{}`.
Do not register `guard:audit-plan` as the reviewer: it is the dispatcher itself.

## Edited-file checkpoints

Configure `file_review_rules` in `.claude/guard.local.json` or `.codex/guard.local.json`.
In Claude Code, `/guard:settings` helps choose rules and exclusions. Each rule maps a
project-relative glob to an installed agent or skill:

```json
{
  "file_review_rules": [
    {"glob": "**/*.py", "action": {"kind": "agent", "name": "guard:comment-corrector"}},
    {"glob": "**/*.md", "action": {"kind": "agent", "name": "guard:doc-auditor"}},
    {"glob": "**/AGENTS.md", "action": {"kind": "agent", "name": "guard:agents-md-auditor"}},
    {"glob": "config/**/*.json", "action": {"kind": "skill", "name": "my-config-review"}}
  ],
  "files_exclude": ["generated/**", "!generated/handwritten.py", "vendor/**"]
}
```

These are examples, not defaults. The bundled `guard:comment-corrector` edits source comments
in place and is available in Claude Code. For Codex source review, select your own installed
agent or skill. `$guard:setup` installs the bundled Codex document reviewers.

`*` matches within one directory; `**` crosses directories, including zero levels.
The most specific rule wins: an exact filename beats a filename pattern, then literal
directory depth and detail decide; an exact tie uses the first rule. Unmatched and excluded
files are not reviewed. All file types, including extensionless files, can match a rule.

Guard records matching edits without running a review automatically. Run `/guard:audit-files`
in Claude Code or `$guard:audit-files` in Codex when ready. The checkpoint groups pending
paths by the selected agent or skill and retains revisions changed during review.

A matching rule is the only opt-in; there is no additional agent switch. An empty
`file_review_rules` list selects no files. `files_exclude` uses globs for every file type.
`doc_dir` limits ordinary Markdown directories. Exclusions apply equally to Markdown, source
code, configuration files, and extensionless files.

Exclusions run in list order: `!pattern` restores matching files, and the last matching
pattern wins. In the example, `generated/handwritten.py` is restored after `generated/**`
excludes the tree. Restored files still need a matching `file_review_rules` entry.
Use `\\!name.py` in JSON to exclude a filename beginning with a literal `!`.
These are Guard's project-relative file globs with negation, not the full `.gitignore`
syntax; an exception can restore a file inside an excluded tree directly.

The reference-index requirement remains immediate: a new saved reference must still be added
to the reference directory's index before work continues.

## Herdr integration

When working inside Herdr, install the companion plugin directly from the marketplace
repository:

```sh
herdr plugin install studykit/studykit-plugins/guard
```

During local development, link the working tree instead:

```sh
herdr plugin link /absolute/path/to/studykit-plugins/guard
```

It provides two actions—show pending files and audit pending files—and a popup pane listing the
queue for the focused Claude Code or Codex session. In the popup, use the arrow keys or `j`/`k`
to move the cursor, Space to select or deselect multiple files, and Enter to open the current
file in `$VISUAL` or `$EDITOR`; Guard falls back to `nvim`, `vim`, then `vi`. Press `a` to start
an audit for the selected files, or for the entire queue when nothing is selected. Press `c` to
clear only the selected files after confirmation, `r` to refresh, or `q` to close. Clearing
invalidates an audit already in progress; files edited afterward are added to a fresh queue.

To display the pending count in the expanded Herdr Agent sidebar, add `$guard_pending` to an
Agent row in `~/.config/herdr/config.toml`, for example:

```toml
[ui.sidebar.agents]
rows = [
  ["state_icon", "agent", "state_text"],
  ["$guard_pending"],
  ["workspace", "tab"],
]
```

The token disappears when the checkpoint queue is empty. Guard continues to work normally
when the Herdr plugin is not installed.
