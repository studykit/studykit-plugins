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

<jira-format>
Any issue body or comment you write is rendered as Jira wiki markup, not
Markdown — a Markdown body publishes and renders as literal punctuation.
Emit wiki markup directly: `h2. Name` headings, `*` bullets, `# ` numbered
items, a doubled-brace pair for inline monospace, `{code:lang}...{code}`
blocks, `[label|url]` links, `||a||b||` table headers. Never emit
`## heading`, `- [ ] task`, backticks, fenced blocks, or `[label](url)`.

Two traps: Jira reads `-text-` as strikethrough, so escape a hyphen sitting
at a word's outer edge (`\-max\-tries\-`, `\->`) — but leave ordinary
hyphenated words (`back-off`, `well-known`) alone. And keep a space outside
the inline-monospace braces next to Korean or other CJK text, or the
monospace may not render at all.
</jira-format>

<jira-task-review>
Before presenting or publishing an LLM-authored Jira `task` issue draft, write
the complete candidate body to a draft file and dispatch the configured review
agent `{{SPECTRACK_JIRA_TASK_REVIEW_AGENT}}` with that absolute path. Ask it
to review scope, context, acceptance criteria, and internal consistency only;
it must not publish or otherwise mutate the tracker. Address its actionable
findings in the draft, then run the Jira markup check and present the reviewed
draft to the user for confirmation. Do not publish until the review, markup
check, and user confirmation are complete.
</jira-task-review>

<jira-comment-review>
Before presenting or publishing any LLM-authored Jira comment draft, write the
complete candidate text to a draft file and dispatch the configured review
agent `{{SPECTRACK_JIRA_COMMENT_REVIEW_AGENT}}` with that absolute path. Ask
it to review accuracy, relevance, and internal consistency only; it must not
publish or otherwise mutate the tracker. Address its actionable findings in
the draft, then run the Jira markup check and present the reviewed draft to the
user for confirmation. Do not publish until the review, markup check, and user
confirmation are complete.
</jira-comment-review>

<commands>
Issue CLI. Run `spectrack issue --help` to list the verbs available for
this project's backend, then `spectrack issue <verb> --help` for a verb's
flags and usage.
</commands>
