<commit-prefix>

{{SNIPPET_COMMIT_PREFIX}}

</commit-prefix>

<runbook>

Per-verb syntax (flags, body-file lifecycle, conflict handling)
lives in the runbook at
`{{WORKFLOW_RUNBOOK_DIR}}/<intent>/{{WORKFLOW_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch issues + cache projections
- `issue-write` — shared body-bearing write procedure
- `issue-new` — publish a new issue (used for the review publish flow)
- `issue-comment` — append the optional summary comment when there are
  decisions / open questions / notes worth recording (Step 10)
- `issue-link` — relationships (used for the blocked-by link)
- `issue-update` — update body and state (used for the writeback)
- `issue-state` — provider terminal-transition verbs (when combining
  `--state` on update)

</runbook>
