# Jira Issue Authoring Anti-Patterns

Read this with:

- `../../../contracts/issue/common.md`
- `./convention.md`

## Work history body sections

Do not create a `Log` section for Jira issue work history. Use Jira comments, history, and worklog for discussion and audit history.

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

See `./convention.md` for the full markup mapping.
