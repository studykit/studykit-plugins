# Plan Mode Body Drafting

Use plan mode to converge on a `task` or `bug` issue body before invoking the
provider write. Plan mode forces context gathering before action, blocks file
edits until alignment, and produces a single approval gate — the agreed plan
text becomes the body of the issue.

Companion contracts:

- `./issue-body.md`
- `./task-authoring.md` (for `task`)
- `./bug-authoring.md` (for `bug`)

## When to use

Use plan mode when the issue body needs converged content for a planned
implementation or fix that has not yet been executed. Plan mode is the
alignment gate before the change lands; once the code is in, the alignment
has already happened elsewhere.

Skip plan mode for:

- Retroactive issues created after the change is already implemented,
  typically to carry a commit-ref prefix or otherwise track completed work.
  The convergence happened in the prior conversation or commit; the body
  just records what was done.
- Exploratory items (`spike`, `research`) where the body grows after the
  issue is created.
- Trivial updates that touch a single field or short bullet.
- Coordination items (`epic`, `review`) where the body coordinates other
  work rather than describing implementation.

## Skeleton

Enter plan mode with the required body skeleton in place, then fill each
section through conversation. Add optional sections from `./issue-body.md`
(`Out of Scope`, `Alternatives Considered`, `Risks`, `Interface Contracts`,
`Environment` for bug) only when content for them surfaces.

`task` required sections (`./task-authoring.md`):

- `Description`
- `Change Plan` (when expected scope is known)
- `Unit Test Strategy`
- `Acceptance Criteria`

`bug` required sections (`./bug-authoring.md`):

- `Description`
- `Reproduction`
- `Unit Test Strategy`
- `Acceptance Criteria`

## Content routing

Route plan-mode-style content to the right section so it does not collapse
into `Description`:

| Plan-mode content | Target section |
| --- | --- |
| Motivation, problem, why now | `Description` |
| High-level approach | `Description` |
| Files, packages, APIs to touch | `Change Plan` |
| Test scenarios, isolation, locations | `Unit Test Strategy` |
| Observable completion conditions | `Acceptance Criteria` |
| Reproduction steps (bug) | `Reproduction` |
| Deferred or excluded work | `Out of Scope` |
| Alternatives evaluated and rejected | `Alternatives Considered` |
| Regression hazards, blast radius concerns | `Risks` |
| Pending decisions, input requests | `Open Questions` |

If content does not fit any section above, prefer a new well-named section
over squeezing it into `Description`. Section taxonomy lives in
`./issue-body.md`.

## Handoff

After plan approval, the agreed plan text is the body. Write it to the body
file path verbatim, then invoke the provider publish or update flow with
that body file.
