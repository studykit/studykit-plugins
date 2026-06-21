<issue-provider>
Issue provider for this project: `{{SPECTRACK_ISSUE_PROVIDER}}`.
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

<commands>
Issue CLI. Run `spectrack issue --help` to list the verbs available for
this project's backend, then `spectrack issue <verb> --help` for a verb's
flags and usage.
</commands>
