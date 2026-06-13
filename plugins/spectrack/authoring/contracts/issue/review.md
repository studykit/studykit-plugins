# Review Authoring

A workflow review item captures a single concern about a target — something wrong, missing, unsettled, or worth surfacing for separate tracking apart from the target's normal work.

Use an existing issue comment when the feedback is local to one issue and resolvable as part of its normal work. Create a review item when the feedback needs separate ownership, prioritization, discussion, or completion criteria — not for every comment.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`

## One concern per item

Each review item carries exactly one concern. Do not pack several unrelated findings into one — split them so each can be owned, tracked, and resolved independently.

When multiple concerns share a single root cause whose resolution clears them all, treat the root cause as the one concern and name the related symptoms in `Evidence` or `Description`, not in separate sections.

Publishing agents that surface concern categories (`finding`, `gap`, `question`, or a domain-specific set) carry that vocabulary in the agent's own body, not as a binding contract here. When a category is needed for filtering, encode it as an issue label or provider field at publish time, not as a body field.

## Review target rules

A review item must identify the specific issue, knowledge page, or small set of reviewed content that must change or answer the concern. If the concern is truly cross-cutting, say so explicitly in `Description`.

Choose the narrowest useful target:

- The issue whose body, acceptance criteria, plan, or discussion must change.
- The knowledge page whose content must change.
- A small set of reviewed items when the same concern applies to all.

Do not list every related item or invent placeholder targets.

## Resolution criteria

A review is complete only when every target item reflects the resolution.

- Knowledge targets: the page should include a `Change Log` entry linking back to the review item or to the causing issue that resolved it.
- Issue targets: the issue should include the relevant body change, or an explicit comment explaining why no content change was needed.

If the fix is deferred, do not treat the review as complete merely because a follow-up task was created, unless the team explicitly treats that handoff as resolution.

## Body shape

Review bodies are deliberately compact.

Required section:

- `Description` — the concern, why it matters, and what would resolve it. The first paragraph is the conclusion (see below). For a cross-cutting review with no specific target, `Description` must explain why.

Beyond `Description`, each author adds sections as the concern needs (see `./body.md`).

## Description and the conclusion paragraph

The first paragraph of `Description` is the conclusion: a reader who reads only it can decide what to do. In plain prose it states:

- What the concern is.
- What target it lands on (when not obvious from the title).
- Why a reader should care (one short clause is usually enough).

Reasoning, evidence, sub-points, and remediation belong in later paragraphs or in a purpose-specific section the author adds per `./body.md`. Do not start the body with a section header, a bulleted list, or scaffolding — the first thing the reader sees is the conclusion in sentences. Keep the body short; long discussion belongs in comments or linked evidence.

This mirrors the verdict-comment shape the workflow auditors use (`agents/implementation-auditor.md`, `agents/task-size-auditor.md`): the first paragraph names the verdict in natural prose, everything else backs it up.

## Common mistakes

- Missing target identity for a target-specific review.
- Packing several unrelated concerns into one review item.
- Using a page comment instead of a review item for feedback that needs workflow tracking.
- Treating a review as complete before the target item was updated.
- Duplicating long discussion in the issue body instead of comments.

## Do not

- Store a review as a knowledge page.
- Create placeholder targets.
- Use one review item for multiple unrelated concerns.
- Start the body with anything other than a conclusion paragraph in prose.
