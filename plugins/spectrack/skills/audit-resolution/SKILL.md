---
name: audit-resolution
description: "Validate the recorded root cause and proposed approach or fix of a published workflow `task` or `bug` issue against the actual code and git history. Use when the user wants an independent resolution audit for an existing issue."
argument-hint: "<issue-ref>"
disable-model-invocation: true
allowed-tools:
  - Agent
---

# Audit Resolution

Dispatcher for validating an issue's recorded diagnosis. The audit checks
whether the issue's recorded root cause is the actual cause, and whether the
recorded approach or fix would actually resolve it — judged against the real
code and its git history, not the issue's internal plausibility.

## Flow

1. **Parse the issue ref.** Take the first `$ARGUMENTS` token as the issue ref.
   If there is no recognizable ref, abort with `Usage: <issue-ref>`.

2. **Dispatch `resolution-auditor`.** Call `Agent` with `subagent_type:
   spectrack:resolution-auditor`, naming the published issue ref (published
   mode). It fetches the issue, validates the recorded cause and approach
   against the code read-only, appends a single verdict comment to the issue,
   and returns a `<report>` with a `verdict`.

3. **Report.** Emit the auditor's `<report>` without adding new conclusions.

$ARGUMENTS
