## workflow subagent context

This subagent runs inside a workflow-configured project. The main session's
workflow launcher contract is inherited in your shell:

{{WORKFLOW_LAUNCHER_BLOCK}}

To fetch or refresh an issue (the common read):

{{WORKFLOW_ISSUE_FETCH_BLOCK}}

Cache projections under `.workflow-cache/` are read-only — refresh them
through the matching fetch script, and never edit `issue.md` or
`comment-*.md` in place.
