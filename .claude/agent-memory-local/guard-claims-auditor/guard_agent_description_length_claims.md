---
name: guard-agent-description-length-claims
description: How to verify claims about frontmatter `description` char-length comparisons across plugins/guard/agents/*.md
metadata:
  type: reference
---

When a guard turn edits an agent's YAML frontmatter `description` and cites char counts
(e.g. "336자 → 235자", "median X", "below agent Y"), the turn typically runs a Python
snippet with `yaml.safe_load` and `len(d['description'])` — check the tool activity extract
for that exact output before recomputing by hand.

A naive re-parse (e.g. joining stripped lines of the raw block after `description: |`) will
undercount by ~1 char vs `yaml.safe_load`'s folded-scalar handling (trailing newline/space
folding differs). Do not treat a 1-char mismatch from a manual reparse as a contradiction —
prefer re-running the same `yaml.safe_load` + `len()` approach the turn used, or trust the
tool-activity output directly, over a hand-rolled parse.

Example verified 2026-08-22: turn claimed 336→235 chars for `agents-md-auditor.md`,
clarity-auditor at 254, median 178 across guard's 9 agent files — all matched the turn's own
`uv run --with pyyaml ...` output in the transcript extract exactly. A hand-rolled awk/python
join gave 234/253/177 (off by 1) and would have been a false positive for "unsupported."

Update 2026-08-22 (turn 329c1d39): a second such turn (shortening all 9 agents'
descriptions to one line, 1723->878 chars, max 125) matched the transcript's own
`yaml.safe_load`+`len()` output exactly (878 TOTAL, router 125 max). Also checked in this
turn: the `-auditor`/`-corrector` suffix-as-contract claim is real and documented at
`plugins/guard/dev/design.md:603` ("Two agents report; two correct... suffix is the
contract"). The dispatch-paths-use-subagent_type claim is grounded in
`hooks/context/dispatch-playbook.md:72`, `scripts/guard_hook.py:1655`, and
`skills/simply-explain/SKILL.md:84` all hardcoding `subagent_type`. A cited line range
(`agents/router.md` "114~160행") was slightly short of the section's true end (168, before
`## Output`) but directionally correct — treated as non-blocking, not an unsupported claim.
