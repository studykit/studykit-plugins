---
name: reference-agent-memory-local-root-tracked
description: whether root .claude/agent-memory-local/* content should be committed is answered by .gitignore, not a judgment call
metadata:
  type: reference
---

`.gitignore` (around line 220-229 as of 2026-08-22) explicitly un-ignores the
root-level `.claude/agent-memory-local/` store (`**/.claude/agent-memory-local/`
then `!/.claude/agent-memory-local/`), with a comment explaining it is tracked
deliberately because this repo is where guard's local-memory subagents are
developed — "what they have learned here is worth keeping and reviewing."
Any nested copy (e.g. `plugins/<name>/.claude/agent-memory-local/`) stays
ignored as state from a misresolved project root.

So: whether a file under the root `.claude/agent-memory-local/**` should be
committed is **not** a case-by-case judgment about who authored the content
(the assistant vs. an audit subagent vs. pre-session staging) — the repo's
own policy already says yes, commit it, regardless of authorship. An assistant
that excludes such a file from a commit "because I didn't write it, leaving
the call to the user" when it already quoted/found the commit that established
this tracking policy (see `7051d793`, "guard: v0.50.0") is deferring a
question the repo already resolved.

Related: [[guard_state_root_untracked_dirs]] (the opposite case — files that
should stay untracked).
