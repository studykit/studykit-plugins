<runbook>

Per-verb syntax (flags, body-file lifecycle, conflict handling)
lives in the runbook at
`{{SPEC_TRACK_RUNBOOK_DIR}}/<intent>/{{SPEC_TRACK_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch the implementation issue. Read the cached body
  and every `comment-*.md` projection.
- `issue-comment` — append the single audit comment carrying
  `## Verdict` / `## Reasoning` / `## Actionable` / `## Notes`. This is
  the only write this agent performs; on append failure the agent
  falls back to a local sidecar file.

</runbook>
