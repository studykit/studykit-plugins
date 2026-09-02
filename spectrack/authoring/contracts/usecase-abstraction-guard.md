# Use Case Abstraction Guard

Companion to `./usecase.md` § Abstraction discipline. That
contract names *what* must stay user-level on both the issue and
knowledge sides; this file is the *converter* — concrete before/after
rewrites for the most common implementation leaks, plus the per-field
obligations that apply when authoring or reviewing a use case body.

Scope: every use case body authored under the workflow `usecase`
type, on both the issue and the knowledge-page roles. Apply the
guard before publishing any use case body and again whenever the
body is materially revised.

## Principle

A use case describes what an actor does and what the actor observes.
It does not describe how the system delivers the outcome. Anything
naming a technology, storage layer, infrastructure component, or
internal system action ("the system queries…", "data is stored…",
"triggers a request…") belongs in a `spec`, `architecture`, or
implementation `task`, not in a use case.

## How to convert

Common implementation phrasings and their user-level equivalents.

| Implementation phrasing | User-level phrasing |
|---|---|
| the system queries the database for matching records | matching results appear on screen |
| sends a webhook to the integration service | the connected tool is notified |
| caches the result for 5 minutes | results load instantly on the next visit |
| the API returns a 200 status | the action completes successfully |
| writes a row to the audit table | the change is recorded so the actor can review it later |
| publishes a message to the event queue | other parts of the product react to the change |
| invalidates the session token | the actor is signed out |
| retries with exponential backoff | the request is attempted again in the background |

The conversions are illustrative, not exhaustive. The rule is to
restate the leak from the actor's vantage point — what they ask for,
what they see, what they can verify.

## Where to apply

Every required and optional use case field has an abstraction
obligation. Apply the guard per field:

| Field | Obligation |
|---|---|
| Goal | Must express what the actor wants, not how the system delivers it. |
| Actors | Must name specific roles (person or system from the actor's perspective), not internal services or modules. |
| Situation | Must describe an observable trigger, not a system event. |
| Flow | Every step must be a user action or an observable system response — no internal calls, no data movement, no state mutations. |
| Expected Outcome | Must be verifiable by a person, not a system state. |
| Validation | User-visible input constraints (formats, limits, required fields). Not schema or storage rules. |
| Error Handling | What the actor sees when things fail, with the user-visible recovery path. Not exception types, HTTP codes, or retry policies. |

When a field cannot be expressed at this level without losing meaning
— typically because the use case is actually about a system-to-system
interaction with no human actor — the artifact is probably a `spec`
or `architecture` page, not a use case. Reclassify rather than
softening the abstraction discipline.

## Common slip surfaces

- **Flow steps that name the storage layer.** "The record is saved
  to the user table." Rewrite as the observable confirmation the
  actor receives.
- **Outcomes phrased as system state.** "The flag is set to true."
  Rewrite as what the actor can verify ("the toggle in the settings
  panel shows on").
- **Error handling phrased as exception names.** "A `ValidationError`
  is raised." Rewrite as the message and recovery path the actor
  sees.
- **Situations phrased as background jobs.** "Every 5 minutes the
  cron checks." Rewrite as the observable trigger from the actor's
  perspective, or move the cycle into an NFR.

## Out of scope

This guard does not police section presence, body shape, or
provider markup — those live in `./issue/usecase.md`,
`./knowledge/usecase.md`, `./knowledge/body.md`, and the
provider convention files (each side
file lists its own body shape; the dual-role overview is in
`./usecase.md`). The guard polices only the abstraction
level of the prose in each body section.
