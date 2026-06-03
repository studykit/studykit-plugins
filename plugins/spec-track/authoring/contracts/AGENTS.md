# Common Authoring Instructions

Files in this directory define provider-neutral workflow authoring contracts only.

- Do not include provider-specific rules, examples, API details, transport notes, or relationship handling.
- Do not add references or links from common authoring files to provider-specific authoring files.
- Put provider-specific guidance in `../providers/`.
- Keep common files semantic; the authoring resolver supplies provider-specific files separately when needed.

## Backend-agnostic prose

Write common file prose so a reader unfamiliar with the selected backend can still understand the rule. Do not name specific backends (GitHub, Jira, filesystem, etc.) and do not use "provider" as authoring vocabulary inside contract files. Reach for neutral substitutes such as:

- "the configured issue backend" / "the configured knowledge backend"
- "the matching rendering convention"
- "native link form from the rendering convention"
- "backend fields" / "backend status" / "backend workflow"

"Provider" remains a valid term when describing the `../providers/` directory boundary in this AGENTS file — that is a structural term, not authoring vocabulary.

## Body markup boundary

Common files describe **section meaning** (what a section is for, when it is required, what it must contain). They do not define the literal markup form used to render that section.

The literal markup for headings, paragraphs, lists, inline emphasis, links, code blocks, tables, checklists, and any provider-only constructs (panels, info macros, smart links, etc.) is defined by the matching provider convention file:

- `../providers/issue/github/convention.md`
- `../providers/knowledge/github/convention.md`
- `../providers/issue/jira/convention.md`

When a common file references a section, refer to it by its canonical Title Case name without a literal heading prefix. For example, write `Description section` or `the Description section`, not `## Description`. The provider convention turns the canonical name into the correct heading form (`## Description`, `h2. Description`, `<h2>Description</h2>`, etc.).

When a common file shows a body shape, prefer a list of section names and their required/optional status. If a literal example is genuinely needed for clarity, isolate it into a provider-specific file rather than embedding markup into common.
