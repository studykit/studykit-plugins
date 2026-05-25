# GitHub Issue Relationships

Provider-specific relationship rules for issue-backed items stored as GitHub Issues.

Read with `../../../contracts/issue/common.md`, `./convention.md`.

## Boundary

Issue relationships are not issue metadata fields. Do not store parent, child, dependency, or related issue state in provider metadata fields or issue body fallbacks when native storage is available.

Use GitHub-native relationships when available:

- Parent and child relationships use GitHub sub-issue metadata.
- Blocking relationships use GitHub issue dependency metadata.
- Soft related references use the type-specific body section only when no native relationship is available or when the relationship is intentionally human-readable context.

## Relationship intents

When running `workflow issue link` to apply a GitHub Issue relationship, supply the source issue, canonical relationship intent, and target issue reference.

Use these canonical intents:

- `parent`: the source issue becomes a sub-issue of the target issue.
- `blocked_by`: the source issue is blocked by the target issue.

If the natural wording is "source has child target", invert the source and target and use `parent`. If the natural wording is "source blocks target", invert the source and target and use `blocked_by`.

Use same-repository GitHub issue references such as `#66` for targets.

GitHub provider-native writes do not support a generic `related` relationship. Use a type-specific body section only when the relationship is intentionally human-readable context.

## Body boundary

Do not duplicate GitHub-native parent, child, or dependency relationships in issue body sections. Read `./anti-patterns.md` for forbidden body sections.

Apply provider relationship changes through `workflow issue link`. The main assistant supplies the relationship intent and target references; the script owns provider invocation and cache refresh.
