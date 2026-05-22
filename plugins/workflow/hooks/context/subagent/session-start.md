<launcher>

This subagent runs inside a workflow-configured project. The main session's
workflow launcher contract is inherited in your shell:

{{SNIPPET_LAUNCHER}}

</launcher>

<authoring-resolver>

Resolve authoring paths before any issue or knowledge pages:

{{SNIPPET_AUTHORING}}

</authoring-resolver>

<runbook>

Reference doc (read on demand) at
`{{WORKFLOW_RUNBOOK_DIR}}/issue-fetch/{{WORKFLOW_ISSUE_PROVIDER}}.md`
— fetch issues + cache projections.

</runbook>
