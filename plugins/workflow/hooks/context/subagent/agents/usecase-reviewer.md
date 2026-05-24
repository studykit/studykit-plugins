<runbook>

Per-verb syntax (flags, body-file lifecycle, freshness-drift handling)
lives in the runbook at
`{{WORKFLOW_RUNBOOK_DIR}}/<intent>/{{WORKFLOW_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch every `usecase` ref the caller named, plus
  every `prior-review-refs` entry. Read the cached body for use
  cases and (for prior reviews) the body only — comments are not
  needed for deduplication.
- `issue-new` — publish the per-finding `review` issue (one finding
  per item). Used with `--type review`, `--related <usecase-ref>`,
  and (when the provider supports labels) `--label usecase-reviewer`
  so `source` is encoded at publish time.
- `issue-link` — used only when a finding spans multiple use cases
  and the additional `--related` links could not be set at publish
  time.
- `issue-comment` — used only on prior open `review` issues that the
  agent dedups a new finding against this run. The comment carries
  the re-raised concern so the trail is visible. Never used on
  `usecase` issues themselves.

</runbook>
