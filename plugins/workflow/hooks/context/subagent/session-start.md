## workflow subagent context

This subagent runs inside a workflow-configured project. The main session's
workflow launcher contract is inherited in your shell:

{{SNIPPET_LAUNCHER}}

Resolve authoring paths before any issue or knowledge pages:

{{SNIPPET_AUTHORING}}

Reference doc (read on demand) at
`{{WORKFLOW_RUNBOOK_DIR}}/issue-fetch/{{WORKFLOW_ISSUE_PROVIDER}}.md`
— fetch issues + cache projections.

Write-side runbook intents are not enumerated here; agents that need
them receive a per-agent block naming the runbook paths they use.
