---
name: project_guard_agents_md_style
description: guard/AGENTS.md's dense "invariants that fail silently" catalog is an intentional, established convention — not itself an axis-3 finding — but merges tend to re-narrate anecdotes/quotes already fully recorded in dev/*.md instead of pointing at them
metadata:
  type: project
---

`guard/AGENTS.md` carries a long "Invariants that fail silently" section written in dense,
narrative prose (why something is the way it is, quoting retired file contents, citing version
numbers). This is the plugin's established convention throughout the file, not something a
single edit introduced — do not flag the style itself as failing axis 3 ("not a map") just for
being long or narrative, since that judgment was presumably already made for the file as a whole.

What IS worth flagging: when a session merges two definitions (e.g. `agents/turn-router.md` +
`agents/report-router.md` -> `agents/router.md`, guard v0.128.0), the invariant bullet added to
AGENTS.md to record the merge sometimes re-narrates the rationale — including a quote from the
retired file's own prose ("the same triage step as guard's turn router") — that is *also*
recorded, near-verbatim, in `dev/agent-frontmatter-rationale.md`. That is axis-2 duplication:
two copies of one historical anecdote that will drift, exactly the pattern the merge itself was
justified by (README/agent duplication). AGENTS.md's line should point at the `dev/` file's
section for the anecdote and only state the operative invariant itself.

**Why:** Found 2026-09-10 auditing `guard/AGENTS.md` after the turn-router/report-router merge;
verified both files contained the same quoted sentence via grep.
**How to apply:** When auditing `guard/AGENTS.md` (or similarly-styled AGENTS.md files) after a
merge/rename, grep the new prose's distinctive phrases against the `dev/` files it cites — a
hit means the anecdote was copied rather than pointed to.
