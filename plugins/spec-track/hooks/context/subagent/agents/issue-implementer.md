<commit-prefix>

{{SNIPPET_COMMIT_PREFIX}}

</commit-prefix>

<runbook>

Per-verb syntax (flags, body-file lifecycle, conflict handling)
lives in the runbook at
`{{SPEC_TRACK_RUNBOOK_DIR}}/<intent>/{{SPEC_TRACK_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch the issue + cache projections (only when an
  `issue-ref` is supplied, for spec context)
- `issue-update` — refresh the issue body's `Resume` at handoff
  (body-only writeback; this agent never transitions issue state)

</runbook>
