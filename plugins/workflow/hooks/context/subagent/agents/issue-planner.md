<runbook>

Per-verb syntax (flags, body-file lifecycle, conflict handling)
lives in the runbook at
`{{WORKFLOW_RUNBOOK_DIR}}/<intent>/{{WORKFLOW_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch issues + cache projections. Read both the issue
  body and every cached `comment-*.md` projection. Re-fetch every cited
  related issue 1 hop out (parent, blocked-by, blocks, and other workflow
  refs the body or comments name) and read their body + comments too.
- `issue-write` — shared body-bearing write procedure.
- `issue-new` — publish a new issue (used for the review publish flow when
  a blocker fires).
- `issue-comment` — append a comment (used for the plan comment).
- `issue-link` — relationships (used for the `blocked-by` link to a review).
- `issue-update` — update body (used for the body refresh; no `--state`
  transition — this agent never closes an issue).

</runbook>
