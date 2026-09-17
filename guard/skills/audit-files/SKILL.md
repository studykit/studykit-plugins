---
name: audit-files
description: Audit the repository files accumulated in Guard's pending queue and clear only the revisions that were successfully checked.
disable-model-invocation: true
---

# Audit pending edited files

This is an explicit checkpoint. It replaces automatic file audits at every Stop event.

## Read the checkpoint

Resolve `scripts/checkpoint.py` relative to this `SKILL.md` and run that concrete path with
`show`, the current host, and the current session id. On Claude Code,
`${CLAUDE_SKILL_DIR}/scripts/checkpoint.py` is already the concrete script path. Use
`CLAUDE_CODE_SESSION_ID` on Claude Code and `CODEX_THREAD_ID` on Codex:

```text
<checkpoint-script> show --host <claude|codex> --session <session-id>
```

Parse its one-line JSON result. If `files` is empty, report that there are no pending files
and stop. Do not inspect the worktree for extra candidates: the queue is the checkpoint's
scope.

## Dispatch

Dispatch every entry in `groups` concurrently. An entry with `kind: agent` names the agent;
an entry with `kind: skill` names the skill. Give it the listed absolute `paths` and NOTHING
else—not what was being changed, what seems risky, or what you want checked. If
`conditional` is true, dispatch only paths this session actually changed according to this
session's tool activity; a shared worktree diff alone is not ownership evidence.

Wait for all reports, then apply only findings their own disposition permits. Every listed
file has an enabled matching audit rule. If `truncated` contains a positive count, say that
the checkpoint is partial.

## Complete safely

Run the same script with `complete`, passing the returned `token` and session id:

```text
<checkpoint-script> complete <token> --host <claude|codex> --session <session-id>
```

Completion removes only files whose contents still match the checkpoint snapshot. If its JSON
reports `remaining` greater than zero, files changed while the audits were running remain
pending; say so and leave them for another checkpoint. Never claim that those revisions were
audited.
