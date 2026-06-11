# GitHub Knowledge Design Decision Index Authoring

Provider-specific binding for the `decision-index` knowledge page stored as a repository Markdown file.

Read after:

- `../../../contracts/knowledge/decision-index.md`
- `./convention.md`

## Scope

Use this binding for the GitHub repository Markdown Design Decision Index page. It is a singleton — one page per repository. The final body structure is listed below.

## Final body structure

Use this final GitHub repository Markdown body structure for the `decision-index` page.

Common required sections are defined by `../../../contracts/knowledge/decision-index.md`:

- `## Overview`
- `## Decisions`

Common optional sections are defined by `../../../contracts/knowledge/decision-index.md` and `../../../contracts/knowledge/body.md`:

- `## Related Work`
- `## Change Log`

Render each `Decisions` entry as a GFM list item linking the source issue or spec; group entries under `### <area>` subheadings once the flat list grows long.
