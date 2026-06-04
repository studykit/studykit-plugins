<runbook>

Per-verb syntax (flags, body-file lifecycle, conflict handling)
lives in the runbook at
`{{SPECTRACK_RUNBOOK_DIR}}/<intent>/{{SPECTRACK_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch every `usecase` ref the caller named in a
  single `issue-fetch` call (the verb accepts multiple refs). Read
  the cached body only; comments are not needed for exploration.
  Do not fetch any other refs.

</runbook>
