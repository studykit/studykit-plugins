# GitHub Knowledge PRD Paths

Path convention for PRD-component knowledge pages stored as repository Markdown files.

Read after:

- `../common/prd-authoring.md`
- `./github-knowledge-convention.md`

## Scope

Use this rule for `context`, `usecase`, `nfr`, `spec`, and `domain` knowledge pages stored in this repository.

## Storage path

Place every PRD-component page under:

```text
wiki/prd/
```

Use type-based subdirectories (`wiki/prd/usecases/`, `wiki/prd/specs/`, `wiki/prd/nfr/`, `wiki/prd/domain/`) when more than one page of a type is expected. A single `context` page can live at `wiki/prd/context.md` directly.

## Identity

The repository-relative path under `wiki/prd/` is the canonical page identity.

Do not place PRD-component pages elsewhere under `wiki/`. Do not keep duplicate copies outside `wiki/prd/`.

## Cross-references

When linking between PRD-component pages, use repository-relative Markdown links rooted at the linking page's location.

## Common mistakes

- Storing PRD-component pages directly under `wiki/` instead of `wiki/prd/`.
- Splitting a single PRD set across multiple top-level directories.
- Creating duplicate copies of a PRD-component page outside `wiki/prd/`.
