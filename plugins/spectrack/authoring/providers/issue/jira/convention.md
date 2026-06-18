# Jira Issue Provider Convention

Jira Data Center issue descriptions and comments render as **Jira wiki markup**, not GitHub Markdown. Emit wiki markup when writing any Jira issue body or comment.

Canonical section names from common authoring map to `h2. Name` headings. Use `h3. Name` / `h4. Name` for subsections.

Avoid Markdown-only forms that render as literal text in Jira, such as `## heading`, `- [ ] task`, backtick code, fenced code blocks, and `[label](url)`. Use Jira forms such as `h2. Heading`, `* item`, `{{text}}`, `{code:lang}...{code}`, and `[label|url]`.

## Accidental strikethrough

Jira renders `-text-` as strikethrough, so stray hyphen pairs in literals (`@body-K`, `->`, `1-2`) can strike through unintentionally. `{{...}}` is styling, not a raw block — it does not suppress this. For such strings use `{noformat}`/`{code}`, or escape the hyphen inline as `\-`.

## Inline monospace spacing

When inline monospace `{{...}}` appears next to Korean or other CJK text, keep a space outside the delimiter. Jira may fail to render monospace markup when a CJK character is immediately adjacent to `{{` or `}}`.

Use `Korean text {{value}} Korean text`, not `Korean text{{value}}Korean text`.


