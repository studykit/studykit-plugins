# CI Authoring

A CI page is the **knowledge-backed executable verification contract** — the actual commands, test layers, fixture assumptions, and remote-CI expectations agents and humans use to verify a change before marking work done. Architecture's `Test Strategy` says *why* the layers exist; CI records *how to run them*.

## Body shape

A `How To Run Tests` section is required — the literal commands expected to work in the current project, as a table with layer, command, and notes columns (the provider convention defines the literal table form): unit, integration, end-to-end/browser, and any multi-tier command, plus environment variables or setup steps safe to document. Do not present an unverified command as verified — label it clearly, or move the investigation to a research item.

Include a `Test Layout` section (where tests live and how they are named: directories by layer, naming conventions, runner config, shared fixtures) and, when the project has remote CI, a `CI Pipeline` section (pipeline name and host, trigger events, required checks, and the workflow file or pipeline URL). Add other sections only when useful — for example a minimal smoke scenario, fixtures/environment notes (store no secrets), or troubleshooting.

## Update rule

Update the CI page whenever a work item changes the verification contract — a new test layer, a regression-test convention, changed performance/compatibility verification, altered test isolation. Record the causing work item in `Change Log`.

## Content boundaries

- `architecture`'s `Test Strategy` — why the layers exist.
- CI's `How To Run Tests` — how to run them.
- a task's/bug's `Acceptance Criteria` — task-specific verification, as a completion criterion.

Do not duplicate the full CI command table into task or architecture bodies — link to the CI page instead. Use canonical page identity, not a legacy local CI file path.
