---
name: audit-resolution
description: "Validate the recorded root cause and proposed approach or fix of a published workflow `task` or `bug` issue against the actual code and git history. Use when the user wants an independent resolution audit for an existing issue."
---

# Audit Resolution

Workflow for validating an issue's recorded diagnosis. The audit checks
whether the issue's recorded root cause is the actual cause, and whether the
recorded approach or fix would actually resolve it — judged against the real
code and its git history, not the issue's internal plausibility.

## Flow

1. **Parse the issue ref.** Take the first recognizable issue ref from the
   user's request.
   If there is no recognizable ref, abort with `Usage: <issue-ref>`.

2. **Audit directly.** Fetch the issue, read its body and comments, and inspect
   the named code and relevant git history read-only. Check whether the recorded
   cause explains the observed behavior and whether the approach or landed fix
   resolves it without contradicting the Acceptance Criteria.

3. **Report.** Present the evidence-backed verdict. Draft an issue comment only
   after agreeing its content with the user, then publish it on confirmation.
