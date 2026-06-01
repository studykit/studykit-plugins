<runbook>

Per-verb syntax (flags, body-file lifecycle, conflict handling)
lives in the runbook at
`{{WORKFLOW_RUNBOOK_DIR}}/<intent>/{{WORKFLOW_ISSUE_PROVIDER}}.md`:

- `issue-fetch` — fetch the implementation issue, plus any review or
  prerequisite ref the implementer's report names. Read the cached
  body and every `comment-*.md` projection.
- `issue-comment` — append the single audit comment carrying
  `## Verdict` / `## Reasoning` / `## Actionable` / `## Notes`. This is
  the only write this agent performs; on append failure the agent
  falls back to a local sidecar file.

</runbook>
