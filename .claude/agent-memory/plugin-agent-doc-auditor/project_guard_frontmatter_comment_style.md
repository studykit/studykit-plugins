---
name: project-guard-frontmatter-comment-style
description: guard plugin's agents/*.md frontmatter comments habitually mix load-bearing tool/model rationale with pure design-history prose — audit each sentence separately
metadata:
  type: project
---

`plugins/guard/agents/*.md` frontmatter carries long `#` comments above `tools:` and
`model:` explaining why each grant exists (e.g. router.md: why `Bash` is scoped to one
command, why no `memory:`, why `model: opus` not a cheaper model). Much of this is
legitimate axis-4-adjacent rationale that argues for the grant itself and is short.

But the same comment blocks accumulate second-order history sentences layered on top —
e.g. "The command's NAME is spelled below for the same reason: while the dispatch named
it, the main agent was still relaying an instruction it never follows" (added to
`router.md` alongside the `guard-candidates` self-fetch change). That sentence explains
*why the design changed* (dispatch used to pass it, now it doesn't), which is
contributor-facing history, not something the router needs to act correctly. It also
duplicates prose already in `plugins/guard/AGENTS.md` under "What guard is".

**Why:** per root `AGENTS.md` § Shipped Definitions Must Be Repo-Portable, this repo's
own audit for shipped definitions (`plugin-agent-doc-auditor`) is stricter than that
section on citations — no repo path may appear at all in a shipped definition, and
per axis 3, rationale/history belongs in the plugin's own contributor notes
(`plugins/guard/AGENTS.md`, `plugins/guard/dev/design.md`), not the frontmatter comment
that ships. guard's own `AGENTS.md` explicitly says as much: "agents/*.md ... are
installed into repositories that are not this one ... Those belong here or in `dev/`."

**How to apply:** when auditing any `plugins/guard/agents/*.md` frontmatter comment,
don't treat the whole comment block as one unit — split it sentence by sentence.
A sentence that justifies *why this grant is scoped the way it is* (load-bearing,
keep) is different from a sentence that narrates *what the design used to be / why it
changed* (history, flag as axis-3 finding, fix = move to `plugins/guard/AGENTS.md` or
`dev/design.md`). guard's own contributor notes already carry near-duplicate prose for
most of these, so check there before assuming the sentence needs a new home.
