# GitHub Knowledge Design Decision Index Authoring

Provider-specific binding for the `decision-index` knowledge page stored as a repository Markdown file.

Read after:

- `../../../contracts/knowledge/decision-index.md`
- `./convention.md`

## Final body structure

Common required sections are defined by `../../../contracts/knowledge/decision-index.md`:

- `## Overview`
- `## Decisions`

Common optional sections are defined by `../../../contracts/knowledge/decision-index.md` and `../../../contracts/knowledge/body.md`:

- `## Related Work`
- `## Change Log`

Render each `Decisions` entry as a GFM list item linking the source issue or spec; group entries under `### <area>` subheadings once the flat list grows long.
