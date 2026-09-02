# Design Decision Index Authoring

The Design Decision Index is a **single curated index (Map-of-Content)** linking every project design decision with lasting reference value, so decisions are discoverable in one place instead of scattered across issues and specs. It is a singleton — one index page per project — and records *where* each decision lives and its current standing, not the full rationale (which stays at the source). It gives tasks, bugs, specs, and reviews a stable link target.

## Body shape

A `Decisions` section is required — the index itself. One entry per indexed decision, each pairing a one-sentence decision statement with a reference to where it is recorded in full, the decision date (not the edit date), and a status. Group entries by area or component once the list outgrows a flat readable list. A short `Overview` of what the index covers and how it is organized is recommended.

Add other sections only when needed — for example the issue-backed items that drove index changes.

## Entry rules

- One decision per entry; keep the statement to a single sentence.
- Link to the single source of record in the backend's reference form; do not restate the rationale here.
- Status is `active` or `superseded`. Mark a superseded decision in place and link the superseding decision or spec — never delete the entry, since the index is a stable link target.

## What to index

Index a durable decision recorded in a task or bug `Context` that has cross-cutting value beyond its own issue (promote it to a spec when it becomes a lasting contract — see `../issue/task.md`), or a decision promoted to a spec's `Decision Log`. Skip purely task-local choices whose only reader is the originating issue — indexing every trivial choice drowns the durable ones.
