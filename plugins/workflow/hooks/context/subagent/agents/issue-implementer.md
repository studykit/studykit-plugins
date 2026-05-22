## issue-implementer subagent context

{{SNIPPET_COMMIT_PREFIX}}

Per-verb syntax (flags, body-file lifecycle, freshness-drift handling)
lives in the runbook at
`{{WORKFLOW_RUNBOOK_DIR}}/<intent>/{{WORKFLOW_ISSUE_PROVIDER}}.md`:

- `issue-write` — shared body-bearing write procedure
- `issue-new` — publish a new issue (used for the review publish flow)
- `issue-link` — relationships (used for the blocked-by link)
- `issue-update` — update body and state (used for the writeback)
- `issue-state` — provider terminal-transition verbs (when combining
  `--state` on update)

### Publish a review (blocker handling)

Blocker-handling flow: publish a `review` issue via `workflow issue new
--type review` with a body file drafted at the resolver-returned path.
Capture the returned review ref from the script's JSON output.

### Link the implementation task as blocked by the review

Writeback link: mark the implementation task as `--blocked-by` the
newly published review via `workflow issue link`.

### Refresh the implementation task's body (handoff Resume / closed snapshot)

Writeback flow: refresh the implementation task's body via `workflow
issue update` with a temp body file (handoff / paused `Resume`
snapshot or closed snapshot). Combine `--state` on the same call to
close — see `issue-update/{{WORKFLOW_ISSUE_PROVIDER}}.md` and
`issue-state/{{WORKFLOW_ISSUE_PROVIDER}}.md` for the provider's state
syntax.
