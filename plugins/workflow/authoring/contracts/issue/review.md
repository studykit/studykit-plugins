# Workflow Review Authoring

A workflow review item captures a single concern about a target —
something wrong, missing, unsettled, or worth surfacing for separate
tracking apart from the target's normal work.

Use an existing issue comment when the feedback is local to that issue and can
be resolved as part of that issue's normal work. Create a review item when the
feedback needs separate ownership, prioritization, discussion, or completion
criteria.

Companion contracts:

- `./body.md`
- Issue rules: `./common.md`

Do not create a review item for every comment. Use comments for local
discussion. Use a review item when the feedback must be tracked independently.

## One concern per item

Each review item carries exactly one concern. Do not pack several unrelated
findings into a single review — split into separate items so each can be
owned, tracked, and resolved independently.

When multiple concerns share a single root cause and resolving the root cause
resolves them all, treat the root cause as the one concern and name the
related symptoms in `Evidence` or `Description` — not in separate sections.

Publishing agents that surface a vocabulary of concern categories
(`finding`, `gap`, `question`, or a domain-specific set) carry that
vocabulary inside the agent's own body — not as a binding contract here.
When a category is needed for filtering, encode it as an issue label or
provider field at publish time, not as a body field.

## Review target rules

A review item must identify the specific issue, knowledge page, or small set of
reviewed content that must change or answer the concern. If the concern is truly
cross-cutting, say so explicitly in the `Description` section.

Choose the narrowest useful target:

- The issue whose body, acceptance criteria, plan, or discussion must change.
- The knowledge page whose content must change.
- A small set of reviewed items when the same concern applies to all of them.

Do not list every related item. Do not invent placeholder targets.

## Resolution criteria

Treat a review as complete only when every target item reflects the resolution.

For knowledge targets, the target page should include a `Change Log` entry that links back to the review item or to the causing issue that resolved the review.

For issue targets, the target issue should include the relevant body change or an explicit comment explaining why no content change was needed.

If the fix is deferred, do not treat the review as complete merely because a follow-up task was created unless the team explicitly treats that handoff as resolution.

## Body shape

Review bodies are deliberately compact.

Required sections:

- `Description` — the concern, why it matters, and what would resolve it.
  The first paragraph is the conclusion (see the conclusion-paragraph
  rule below).

Target-specific reviews must identify the target according to the selected authoring files. For truly cross-cutting reviews, the `Description` section must explain why there is no specific target.

Beyond `Description`, each review author decides which sections
their reviews need based on the review's purpose. See `./body.md`'s
tailoring guidance.

## Description and the conclusion paragraph

The first paragraph of the `Description` section is the conclusion
paragraph. A reader who reads only that paragraph can decide what to do.

The conclusion paragraph states, in plain prose:

- What the concern is.
- What target it lands on (when the target is not obvious from the title).
- Why a reader should care (one short clause is usually enough).

Reasoning, evidence, sub-points, and remediation details belong in
later paragraphs of `Description` or in any purpose-specific section
the author adds per `./body.md`'s tailoring guidance. Do not
start the review body with a section header, a bulleted list, or
scaffolding — the first thing the reader sees should be the
conclusion in sentences.

Keep the body short. Long discussion belongs in comments or in linked
evidence, not in the body.

This mirrors the verdict-comment shape the workflow auditors already
use (`agents/implementation-auditor.md`, `agents/task-size-auditor.md`):
first paragraph names the verdict in natural prose; everything else
backs it up.

## Common mistakes

- Missing target identity for a target-specific review.
- Burying the conclusion under a heading, a bullet list, or
  reasoning paragraphs.
- Packing several unrelated concerns into one review item.
- Using a page comment instead of a review item for feedback that needs workflow tracking.
- Treating a review as complete before the target item was updated.
- Duplicating long discussion in the issue body instead of comments.

## Do not

- Do not store review as a knowledge page.
- Do not create placeholder targets.
- Do not use one review item for multiple unrelated concerns.
- Do not start the body with anything other than a conclusion
  paragraph in prose.
