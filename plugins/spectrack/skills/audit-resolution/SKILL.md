---
name: audit-resolution
description: "Validate the recorded root cause and proposed approach/fix of a published `task` or `bug` issue against the actual code and git history. Dispatches `resolution-auditor` in published mode, which appends a single verdict comment to the issue and returns a verdict. This skill dispatches and passes the report through."
argument-hint: "<issue-ref>"
disable-model-invocation: true
allowed-tools:
  - Agent
---

# Audit Resolution

Dispatcher for validating an issue's recorded diagnosis. The agent checks
whether the issue's recorded root cause is the actual cause, and whether the
recorded approach/fix would actually resolve it — judged against the real code
and its git history, not the issue's internal plausibility. The skill owns
dispatch only; `agents/resolution-auditor.md` is the source of truth for what
the agent does and which verdicts it returns.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the issue ref.
   If there is no recognizable ref, abort with `Usage: <issue-ref>`.

2. **Dispatch `resolution-auditor`.** Call `Agent` with `subagent_type:
   spectrack:resolution-auditor`, naming the published issue ref (published
   mode). It fetches the issue, validates the recorded cause and approach
   against the code read-only, appends a single verdict comment to the issue,
   and returns a `<report>` with a `verdict`.

3. **Pass through.** Emit the auditor's `<report>`. The skill adds nothing on
   top.

$ARGUMENTS
