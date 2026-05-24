<runbook>

Per-verb syntax (flags, body-file lifecycle, freshness-drift handling)
lives in the runbook at
`{{WORKFLOW_RUNBOOK_DIR}}/<intent>/{{WORKFLOW_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch every `usecase` ref the caller named. Read
  the cached body only; the mock is grounded in the use case
  bodies, not in comments or in other refs.

</runbook>
