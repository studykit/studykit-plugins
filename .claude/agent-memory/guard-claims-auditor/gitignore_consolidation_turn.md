---
name: gitignore-consolidation-turn
description: Session context for the guard memory:project/local investigation and .gitignore consolidation (2026-08-22 session 0f38b566)
metadata:
  type: project
---

Session `0f38b566` (2026-08-22) did a multi-turn investigation into why
`plugins/guard/agents/claims-auditor.md` has `memory: project` instead of
`local`. Verified via `git show <commit>:plugins/guard/agents/claims-auditor.md`
that the field's history is `6a577696`=`local` -> `ef5a5bcd`=removed ->
`d8fed879`=`project`, matching the working tree. The user confirmed ownership
of this decision directly in-turn ("'memory: project' 로 내가 바꾼거라").

Separately, turn `3c2fe26d` consolidated `.gitignore`'s `agent-memory`/
`agent-memory-local` rules (previously containing a self-contradicting
`!/.claude/agent-memory-local/` negation) after confirming intent — `local`
should never be tracked at any depth, `project` only at repo root.

**How to apply:** if asked to re-verify the `memory:` field provenance for
guard's auditor agents, `git show <commit>:<path> | grep '^memory:'` across
6a577696/ef5a5bcd/d8fed879 settles it directly — no need to search transcript
for the original user instruction wording, which predates this transcript's
searchable window (likely compacted away at turn `66ff0960`, "/compact").
