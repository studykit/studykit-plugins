---
name: guard-hook-py-style
description: plugins/guard/scripts/guard_hook.py comments are near-entirely rationale/invariant/hazard prose, not narration
metadata:
  type: project
---

`plugins/guard/scripts/guard_hook.py` (guard plugin, Claude Code + Codex) is written by an
author who already applies this repo's comment philosophy (AGENTS.md: "capture what the
code cannot express... not restate what the code already says") aggressively. On a full
audit (2026-08-22, ~2450 lines) essentially every comment/docstring stated a design
trade-off, an invariant, a hazard, or a cross-reference to another file/doc — almost none
were restatement-of-code or restatement-of-name findings.

**Why:** the file is the shared core of a Claude Code + Codex plugin with a deliberately
narrow, load-bearing design (router-as-subagent, one turn == one answer file, fail-open
everywhere), and the author writes long docstrings specifically to record the *why* behind
non-obvious choices (e.g. why Stop skips certain turn kinds, why memory is `local` vs
`user`, why a mode is a mode and not a boolean).

**How to apply:** when auditing this file (or others in this plugin with the same voice),
expect the yield to be almost entirely category 1 (wrong) or category 6 (missing) findings,
found by cross-checking a comment's factual/numeric claim against the code or against
sibling files (agents/*.md, commands/*.md, hooks/hooks.json, docs/refs/*.md) — not
redundancy findings. Read the whole file before judging; the payoff is in verifying
arithmetic/counts (e.g. "the two auditors" vs the actual number of entries in a dict) and
in checking that an overview docstring at the top of the file (the "Subcommands" summary)
stays in sync with what the per-function docstrings and code actually do — it is the part
most likely to drift when a new agent, code path, or CLI verb is added, since it's a
*summary* maintained by hand. It has drifted on both an added agent and an added verb so
far (see confirmed defects below); check every enumerated list in it (agent names, CLI
verbs, skip conditions, state-file keys) against the actual code each time.

Confirmed defects found this way (2026-08-22, v0.46.0 in progress):
- "The two read-only auditors come first" — stale after clarity-auditor was added
  (v0.44.0); should be "three" (claims/deferrals/clarity). Fixed. Re-audited 2026-08-22:
  now correctly says "three" — stays fixed.
- Top-of-file module docstring's `stop` bullet didn't mention the `!`-bash-input skip
  (present in code) and implied the router is always dispatched when "any agent is not
  off", which is false when only `comment-corrector` (a `reads="files"` agent) is
  eligible — that path bypasses the router entirely. Fixed.
- Same docstring's `session-start` bullet said "Sweep state files and turns/ dirs" but
  the code also sweeps `extracts/` dirs. Fixed.
- Same docstring's `settings` bullet described `show`/`set` but never mentioned the
  `unset <key>` verb that `cmd_settings` documents and implements (deletes a key
  entirely, the only way to clear a key `set` can't unwind). Fixed on 2026-08-22 by
  adding a clause for it.

RESOLVED (re-audited 2026-08-22, v0.46.0 in progress): the trace.log-not-swept defect
above is gone — `cmd_session_start` now unlinks `_trace_file(project_dir)` past the age
cutoff, and both docstrings' "state and logs are both age-swept" claim is now true. The
old per-defect memory file was deleted; nothing to re-report here unless the sweep
regresses again.

See also [[guard-hook-py-dead-constant]] — RESOLVED, `_CLI_MUTATING_VERBS` no longer
exists in the file as of 2026-08-22 (was a dead-code defect in an earlier audit, since
removed by someone else).

Re-audit 2026-08-22 (v0.46.0, full file re-read + cross-checks against agents/*.md,
commands/settings.md, AGENTS.md, dev/design.md, hindsight's render.py,
skills/comment-corrector/SKILL.md): every prior defect above stayed fixed, no new
category-1/6 findings. One tiny category-2 finding, the first ever in this file: a
one-line comment `# Attach to the most recent call still lacking output.` directly above
a `for t in reversed(tools): if not t["output"]: ...` loop in `_turn_slice` — pure
restatement of the four lines below it. Deleted. Otherwise the file's near-zero-redundancy
character (see above) held completely.

Also noted: `commands/settings.md` was renamed from `skills/settings/SKILL.md` mid-repo
(uncommitted at time of this audit) — do NOT flag guard_hook.py's many "the `guard:settings`
skill" comments as stale terminology over this. AGENTS.md documents the invariant
explicitly: `commands/<name>.md` and `skills/<name>/SKILL.md` produce the identical
`/guard:<name>` in Claude Code, so "skill" is this codebase's accepted loose term for
either regardless of which directory a Claude-only entry point lives in.
