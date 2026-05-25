# Jira Issue Authoring Anti-Patterns

Jira can store hierarchy, issue links, and remote links as provider-native relationships. Do not duplicate those relationships in the issue body.

Read this with:

- `../../../contracts/issue/body.md`
- `../../../contracts/issue/authoring.md`
- `./convention.md`
- `./relationships.md`

## Relationship body sections

Do not create dedicated relationship sections for Jira-native hierarchy, issue links, or remote links, or narrow semantic reference sections that belong in `Related`.

Avoid these sections (any equivalent heading in any markup form):

- `Parent`
- `Children`
- `Dependencies`
- `Blocked`
- `Blocked By`
- `Blocking`
- `Target`
- `Follow-Up`
- `Blockers`
- `Depends On`
- `Waiting On`
- blocked-on slots inside `Resume`

Use provider-native relationships instead:

- Parent and child relationships -> Jira parent/subtask or configured hierarchy fields.
- Blocking and related relationships -> configured Jira issue links.
- External references -> Jira remote links when configured.

If rationale, sequencing, or discussion is useful to humans, write it in a Jira comment or in the coordinating issue narrative. Do not duplicate the machine relationship in the issue body.

## Body relationship fallbacks

These body sections may still appear when the relationship is not stored natively and the section carries human-readable context:

- `Related`
- `Dependencies`

Do not use those sections as a disguised parent, child, blocked-by, or sequencing list.

Do not create fallback sections only to mirror Jira issue links, hierarchy, or remote links. In particular:

- Do not add `Related` only to repeat a Jira issue link or remote link.
- Do not add `Target`; use a provider-native relationship or `Related`.
- Do not add `Follow-Up`; use `Related`.
- Do not use `Dependencies` for soft related work, parent links, or implementation links.

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
