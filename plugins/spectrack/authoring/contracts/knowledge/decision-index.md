# Design Decision Index Authoring

The Design Decision Index is a **single curated index (Map-of-Content)** that links every design decision across the project with lasting reference value, so decisions are discoverable in one place instead of scattered across issue bodies and specs.

It is curated knowledge, stored in the configured knowledge backend, not the issue backend. It is a singleton: one index page per project. It records *where* each decision lives and its current standing — not the full rationale, which stays at the source.

Companion contracts:

- `./body.md`

## Purpose

Use it to:

- Find where a design decision was made and recorded in full.
- See active versus superseded decisions at a glance.
- Give tasks, bugs, specs, and reviews a stable link target when they build on a prior decision.

Do not use it for:

- The full decision rationale or rejected-alternative analysis — those live at the source (a spec's `Decision Log` / `Rejected Alternatives`, or the issue `Context` that records an issue-local decision's rationale).
- Raw discussion or a work log.
- A roadmap or milestone plan.

## Body shape

Required sections:

- `Overview` — what the index covers and how entries are organized.
- `Decisions` — the index itself. One entry per indexed decision, each pairing a one-sentence decision statement with a reference to where it is recorded in full, the date, and its status. Group entries by area or component once the list grows past a flat readable list.
- `Change Log` — required for material updates. See `./body.md`.

Optional sections:

- `Related Work` — issue-backed items that drove index changes. See `./body.md`.

## Entry rules

- One decision per entry; keep the statement to a single sentence.
- Each entry links to the single source of record in the backend's reference form; do not restate the rationale here.
- Status is `active` or `superseded`. Mark a superseded decision in place and link the superseding decision or spec — do not delete the entry. The index is a stable link target, so entries persist.
- Record the decision date, not the index-edit date.

## What to index

- A durable design decision recorded in a task or bug `Context` that has lasting cross-cutting reference value beyond its own issue (promote it to a spec when it becomes a lasting contract — see `../issue/task.md`).
- A decision promoted to a spec's `Decision Log`.

Skip purely task-local decisions whose only reader is the originating issue; indexing every trivial choice drowns the durable ones.

## Common mistakes

- Restating full rationale here instead of linking to the source of record.
- Deleting a superseded entry instead of marking it `superseded` with a link forward.
- Indexing every task-local decision, burying the durable ones.
- Creating per-area copies of the index instead of grouping within the one page.
