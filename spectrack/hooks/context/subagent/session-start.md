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

<jira-task-review>
Before presenting or publishing an LLM-authored Jira `task` issue draft, write
the complete candidate body to a draft file and dispatch the configured review
agent `{{SPECTRACK_JIRA_TASK_REVIEW_AGENT}}` with that absolute path. Ask it
to review scope, context, acceptance criteria, and internal consistency only;
it must not publish or otherwise mutate the tracker. Address its actionable
findings in the draft, then present the reviewed
draft to the user for confirmation. Do not publish until the review and user confirmation are complete.
</jira-task-review>

<jira-comment-review>
Before presenting or publishing any LLM-authored Jira comment draft, write the
complete candidate text to a draft file and dispatch the configured review
agent `{{SPECTRACK_JIRA_COMMENT_REVIEW_AGENT}}` with that absolute path. Ask
it to review accuracy, relevance, and internal consistency only; it must not
publish or otherwise mutate the tracker. Address its actionable findings in
the draft, then present the reviewed draft to the
user for confirmation. Do not publish until the review and user
confirmation are complete.
</jira-comment-review>

<commands>
Run `spectrack --help` to discover top-level commands, then
`spectrack <command> --help` for its options. For issue work, run
`spectrack issue --help` to list this project's backend verbs, then
`spectrack issue <verb> --help` for a verb's flags and usage.
</commands>

{{SNIPPET_JIRA_CLOUD}}
