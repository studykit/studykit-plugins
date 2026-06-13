# CI Authoring

Authoring contract for the `ci` knowledge page — the workspace reference for how agents and humans verify behavior changes: commands, test layers, fixture assumptions, and remote CI expectations.

The canonical CI page is knowledge-backed, stored in the configured knowledge backend; optional filesystem projection is used only when configured.

Knowledge body rules: `./body.md`.

## Purpose

Records the executable verification contract for the project. Architecture explains the testing *strategy*; CI records the *actual commands and environment assumptions* authors use before marking implementation work done.

## Identity

Use canonical page identity. Suggested title: `CI` or `Test And CI`. Do not require a legacy local CI file path or workflow-local numeric ID.

## Required body sections

### `How To Run Tests`

Required. Record the literal commands expected to work in the current project, as a table with columns for layer, command, and notes (the provider convention defines the literal table form):

- Unit-test command.
- Integration-test command, if applicable.
- End-to-end or browser-test command, if applicable.
- Multi-tier verification command, if available.
- Required environment variables or setup steps safe to document.

Do not present unverified commands as verified. Label an unverified command clearly, or move the investigation to a research item.

### `Test Layout`

Required. Describe where tests live and how they are named: test directories by layer, naming conventions, runner configuration files, and shared fixtures or test utilities.

### `CI Pipeline`

Required when the project has remote CI. Describe the remote pipeline that validates branches and pull requests: pipeline name and host, trigger events, required checks, and the relevant workflow file or pipeline URL (e.g., CI workflow URL/filename, external pipeline URL, or CI dashboard URL).

## Optional body sections

- `Smoke Scenario` — one minimal user-observable interaction proving the system starts and performs the core behavior.
- `Fixtures And Environment` — test databases, service emulators, seed data, secrets handling, container setup. Do not store secrets.
- `Troubleshooting` — known local failure modes and fixes.
- `Related Work` — work items that changed the CI contract.
- `Change Log` — required for material updates. See `./body.md`.

## Update rules

Update the CI page when a work item changes the verification contract — e.g., a task adds a test layer, a bug fix introduces a regression-test convention, a spec changes performance/compatibility verification, an architecture decision changes test isolation, or a review item identifies missing guidance. Every material update adds a `Change Log` entry linking to the causing work item.

## Content boundaries

- Architecture's `Test Strategy` — why the test layers exist.
- CI's `How To Run Tests` — how to run them.
- Task's / Bug's `Acceptance Criteria` — task-specific verification / regression coverage, captured as a completion criterion.

Do not duplicate the full CI command table into task or architecture bodies; link to the CI page instead.

## Completion criteria

A CI page update is done when required sections are present, commands are verified or explicitly marked unverified, remote CI links are current when applicable, and the update has a `Change Log` entry for the causing work item.

## Common mistakes

- Duplicating architecture rationale instead of linking to architecture.
- Adding task-specific verification details that belong in a task or bug.
- Relying on a legacy local CI file as canonical identity when the CI page is knowledge-backed.
- Omitting the work item that caused a CI contract change.
