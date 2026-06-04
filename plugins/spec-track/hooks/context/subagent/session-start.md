<issue-provider>

Issue provider for this project: `{{SPEC_TRACK_ISSUE_PROVIDER}}`.

</issue-provider>

<launcher>

This subagent runs inside a workflow-configured project. The main session's
workflow launcher contract is inherited in your shell:

{{SNIPPET_LAUNCHER}}

</launcher>

<authoring-resolver>

Resolve authoring paths before any issue or knowledge pages:

{{SNIPPET_AUTHORING}}

</authoring-resolver>

<prd-path>

Resolve PRD-component page locations before reading or writing them:

{{SNIPPET_PRD_PATH}}

</prd-path>

<runbook>

Reference doc (read on demand) at
`{{SPEC_TRACK_RUNBOOK_DIR}}/issue-fetch/{{SPEC_TRACK_ISSUE_PROVIDER}}.md`
— fetch issues + cache projections.

</runbook>
