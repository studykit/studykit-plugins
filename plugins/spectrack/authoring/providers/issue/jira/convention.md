# Jira Issue Provider Convention

Provider-wide convention rules for issue-backed items stored as Jira issues.

## Scope

Use these rules for issue-backed items stored in Jira.

This file defines Jira-wide issue writing rules only.

## Body markup

Jira Data Center issue descriptions and comments render as **Jira wiki markup**, not GitHub Markdown. Emit wiki markup when writing any Jira issue body or comment.

Canonical section names from common authoring map to `h2. Name` headings. Use `h3. Name` / `h4. Name` for subsections.

Wiki markup has no native task-list. Where common authoring asks for a completion-oriented checklist (for example, `Acceptance Criteria` items), emit each item as a normal bulleted line (`* item`). Do not write `- [ ]` or `- [x]`; those render as literal text in Jira.

## Markdown leakage

Jira Data Center descriptions and comments render as Jira wiki markup, not Markdown. Markdown forms that look correct but render as literal text in Jira include:

- Markdown headings such as `## Description`. Use `h2. Description` instead.
- Markdown bold `**text**`. Use `*text*` instead.
- Markdown bulleted lists with `- item`. Use `* item` instead.
- Markdown checklist items `- [ ] item`. Use a plain bullet `* item` (wiki markup has no native task list).
- Markdown inline code with backticks. Use `{{text}}` instead.
- Markdown fenced code blocks with triple backticks. Use `{code:lang}…{code}` or `{noformat}…{noformat}` instead.
- Markdown link form `[label](url)`. Use `[label|url]` instead.
- Markdown tables with `| --- |` separator rows. Use `||header|| | row |` instead.

## Accidental strikethrough

Jira renders `-text-` as strikethrough, so stray hyphen pairs in literals (`@body-K`, `->`, `1-2`) can strike through unintentionally. `{{...}}` is styling, not a raw block — it does not suppress this. For such strings use `{noformat}`/`{code}`, or escape the hyphen inline as `\-`.

## Smart Commits

Use Jira Smart Commit commands only when the workflow intentionally wants Jira command side effects.

Do not use Smart Commit commands merely to mention an issue.
