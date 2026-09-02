---
name: report
description: 'Show the accumulated hindsight findings and user profile as a ranked Markdown report, without re-scanning transcripts. Claude Code only.'
disable-model-invocation: true
---

# hindsight — report

Present the **already-accumulated** hindsight state as one readable report. This
skill does not analyze transcripts — that is the `review` skill's job, which fills
`findings/` and `profile/`. `report` only aggregates and shows what is already
there, so it is cheap, deterministic, and safe to run any time.

**Claude Code only.** It reads the user-level state at `~/.claude/hindsight/`
(outside the plugin install dir), written by the `review` skill.

## Steps

### 1. Render the report

```bash
uv run ${CLAUDE_SKILL_DIR}/scripts/report.py
```

The script is mechanical (no LLM): it reads `findings/*.md` and `profile/*.md`,
ranks them, and prints a Markdown report to stdout. Findings come first, **open**
before mitigated and by occurrence count; the user profile follows, by occurrence
count.

If it prints `No hindsight state at …` (exit 1), nothing has been analyzed yet —
tell the user to run `/hindsight:review` first and **stop**.

### 2. Relay it

Show the rendered Markdown report to the user as-is. Do not re-summarize or
re-interpret it — the skill's value is the deterministic, complete view. Add at most
one short orienting line if helpful (e.g. how many open findings there are).

## Options

Pass flags through when the user asks for a narrower or different view:

- `--track findings|profile|both` — limit to one track (default `both`).
- `--status open|mitigated|all` — filter findings by status (default `all`).
- `--brief` — ranked headings only, no body excerpts (a quick index).
- `--full` — include each pattern's full body (What goes wrong / Why / Prevention /
  Examples for findings; Observation / Adapt / Evidence for profile).
- `--out <path>` — also write the report to a file (still prints to stdout).

Examples:

```bash
# Only the open mistakes still worth preventing, as a quick index
uv run ${CLAUDE_SKILL_DIR}/scripts/report.py --track findings --status open --brief

# Everything, full detail, saved to a file
uv run ${CLAUDE_SKILL_DIR}/scripts/report.py --full --out ~/hindsight-report.md
```

## Notes

- Read-only view. It never writes to `findings/`, `profile/`, or `runs/`, and never
  touches project files.
- Counts a `runs/` total and the latest run stamp for context only.
- Meta tool — not tied to any repo.
