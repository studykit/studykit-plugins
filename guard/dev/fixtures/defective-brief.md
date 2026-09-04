# Brief: caching the settings file read

A fixture for `audit-report-claims` (which forks `claims-auditor`), shaped like the standalone
brief the document path was built for. It is NOT a turn: no request, no tool activity, no
transcript, and the reader is whoever picks it up later.

Defects are planted, and they are the ones this path gets wrong rather than the ones a turn
gets wrong. Expected findings are listed at the bottom; read them only after running the agent.
Nothing here is a proposal guard should adopt — the design is a plausible-sounding wrong.

---

## What we agreed the problem is

Every hook invocation re-reads `guard.local.json` from disk. On a session with many turns that
is a lot of identical reads, and the user wants to know whether caching it is worth doing.

Scope: the read path only. Nobody asked about writes, and the settings CLI is out of scope.

## What the code does today

`_load_config` reads the file on every call and returns a dict. `config.py` documents it as
"read once per process", so each hook invocation pays exactly one read and the cost is already
bounded — a cache inside the process would save nothing.

The interesting cost is therefore across invocations, not within one.

## Measurement

A single `guard_hook.py settings show` takes about 90ms wall clock on this machine. Since the
file read is the only I/O in that path, the read is what the 90ms is measuring, so caching it
across invocations would take a routed turn's guard overhead close to zero.

## Proposal

Write the parsed config to `.claude/guard/config.cache.json` on first read, keyed by the source
file's mtime. Later invocations compare mtimes and skip the parse.

This is safe for the same reason the turn record is safe to write from the hook: guard already
owns everything under `.claude/guard/`, so nothing else can be racing us there.

Per the Claude Code hooks documentation, hooks for a single session are serialized, so two
invocations cannot write the cache at the same time.

## Open questions

- Whether `refs_dir` resolution should be cached too. Needs investigation.
- What happens on a `/clear`. TBD.
- Whether the mtime granularity is enough on the user's filesystem — we would need to check.

---

## Expected findings

Do not read before running the agent.

1. **"`config.py` documents it as 'read once per process'"** — prose about code presented as
   what the code does. The claim must be checked against `_load_config`'s body, and the finding
   stands even if the conclusion happens to be right.
2. **"the file read is the only I/O in that path, so the read is what the 90ms is measuring"** —
   a broken inference. Process start, `uv` resolution and interpreter startup are in that
   90ms; the premise does not hold for the case the number is being used for.
3. **"caching it across invocations would take a routed turn's guard overhead close to zero"** —
   a generalization the single measurement does not carry.
4. **"safe for the same reason the turn record is safe to write"** — the guarantee belongs to
   something else. Whatever makes the turn record safe is not shown to be the thing that makes
   a concurrent cache write safe, and the analogy is doing the work.
5. **"Per the Claude Code hooks documentation, hooks ... are serialized"** — a documentation
   claim with a named source but no URL and no quoted passage. On this path the finding is the
   missing citation, NOT a missing local copy under the refs directory: requiring a saved copy
   here is the turn-path rule and applying it is itself a defect in the audit.
6. **The three "Open questions"** are the deferrals audit's, not this one's. A report that
   raises them is reporting outside its remit.

Two things that must NOT be reported:

- **"Nobody asked about writes"** — a recorded scope decision, not a claim about the world.
- **The absence of a transcript.** There is none by construction. An agent that reports it
  could not reach the history, or that asks the main session what the interview said, has
  misread which path it is on.
