---
name: review
description: 'Analyze accumulated Claude Code session transcripts across ALL projects to surface recurring agent mistakes (project-independent patterns to prevent) and a profile of how the user works and communicates. Use when the user wants to review agent mistakes or understand their own usage patterns from session history ("transcript 분석", "내 사용 패턴", "what do I keep getting wrong"). Claude Code only; reads ~/.claude/projects/ and dispatches Claude subagents. Incremental: covers only newly-appended activity each run.'
---

# hindsight — review

Mine transcript history along **two tracks** through a tiered pipeline. The
renderer is mechanical; the two judging stages are models, split by cost.

**Claude Code only.** This skill reads Claude Code session transcripts from
`~/.claude/projects/` and orchestrates Claude subagents (the `Agent` tool). It is
intentionally host-specific; there is no Codex equivalent.

- **Stage 0 — render** (`scripts/render.py`, no LLM): clean, LLM-readable
  conversation chunks of new transcript activity, incremental via a ledger.
- **Stage 1 — scan** (cheap model, Sonnet subagents): read each chunk **once**,
  returning both the **timestamps** of suspected agent mistakes and short
  **observations** about how the user works/communicates. High recall, no synthesis.
- **Stage 2 — synthesize** (top model = you, Opus): re-read flagged spots to
  confirm genuine mistakes → `findings/`; cluster observations into a
  user-communication profile → `profile/`.

State lives at `~/.claude/hindsight/` (user-level, outside the plugin install dir):

- `ledger.json` — per-transcript watermark (managed by `render.py`; never edit)
- `render/<session>__cNN.md` — readable chunks (Stage 1 input, Stage 2 re-reads)
- `render/run-<stamp>.json` — manifest of this run's chunks
- `findings/<slug>.md` — accumulated mistake patterns (track 1; append/update)
- `profile/<slug>.md` — accumulated usage/communication patterns (track 2)
- `runs/run-<stamp>.md` — one report per run (new each run)

## Steps

### 1. Render

```bash
uv run ${CLAUDE_SKILL_DIR}/scripts/render.py
```

Prints a summary and a `MANIFEST:` line. If `MANIFEST: none`, there is no new
transcript activity — tell the user and **stop**. Otherwise read the manifest JSON;
`chunks[]` lists each chunk's `file` and session/project metadata.

> A first run is a full backfill (often 100+ chunks). To scope it smaller, run the
> renderer with `--project <substr>` or `--since YYYY-MM-DD` first.

### 2. Stage 1 — scan each chunk once (Sonnet)

For each chunk, dispatch a subagent with `model: "sonnet"` (subagent_type
`general-purpose`). Process in **waves of ~8–10 chunks**, launching each wave's
Agent calls together in one message so they run concurrently. To keep orchestration
light on big backfills, you may give each subagent a small group of chunk files and
have it return JSON keyed by chunk basename.

Give each subagent this task (substitute the chunk path(s)):

> Read `<chunk file>`. It is a rendered Claude Code conversation; each line is
> prefixed with a `[timestamp]` and a role (USER / ASSISTANT / RESULT). Do TWO
> things and return ONLY a JSON object, no prose:
>
> 1. `mistake_locations`: every moment where **the assistant** plausibly erred —
>    wrong tool use, ignored instruction, bad assumption, skipped verification,
>    faulty reasoning, repeated failure, or anything the user had to correct. Favor
>    recall. Each item: `{"ts":"<timestamp of the assistant turn at fault>","hint":"<≤8 words>"}`.
> 2. `usage_observations`: short signals about how the **user** works and
>    communicates — phrasing/tone, language, how they scope and iterate requests,
>    what they prefer, how they give feedback, when they want discussion vs action.
>    Each item: `{"kind":"communication-style|preference|request-pattern|interaction-rhythm|domain-context","note":"<≤15 words>","ts":"<a representative timestamp>"}`.
>
> Return `{"mistake_locations":[...],"usage_observations":[...]}`; use empty arrays
> if nothing applies.

Collect each subagent's output tagged with its chunk `file` and session/project from
the manifest. Subagents that error or return non-JSON: skip and note the count.

### 3. Stage 2a — confirm mistakes → `findings/` (be skeptical)

For each `mistake_locations` entry, open its chunk `file`, find the `[ts]` line, and
read the surrounding turns. A flag is a hypothesis. **Confirm** only a genuine agent
mistake; **reject** when the evidence shows otherwise: the user changed their mind /
added requirements; a transient error the agent then handled; an expected probe; a
permission decline unrelated to a bad proposal; pushback on taste, not correctness.

For each confirmed mistake derive the **project-independent** failure mode: what
went wrong, the transferable root cause, and a category (`tool-usage |
instruction-adherence | verification | planning | communication | assumption |
scope`). Same failure across projects = same pattern + another example.

Group by failure mode; one file `findings/<slug>.md` per pattern. **Read `findings/`
first** and update an existing match rather than duplicating.

```markdown
---
pattern: <short name>
slug: <kebab-case>
category: <category>
occurrences: <integer count of confirmed examples>
first_seen: <run stamp>
last_seen: <run stamp>
status: open
---

## What goes wrong
<project-independent description>

## Why it happens
<root-cause hypothesis>

## Prevention hypothesis
<concrete guard: a rule, habit, check, or hook idea>

## Examples
- `<transcript>` @ <ts> — <project basename> (<branch>) — <one line>
```

### 4. Stage 2b — cluster usage → `profile/`

Cluster `usage_observations` across all chunks into stable, **project-independent**
patterns of how the user works. Anchor each with evidence. One file
`profile/<slug>.md` per pattern. **Read `profile/` first** and update an existing
match rather than duplicating.

```markdown
---
pattern: <short name>
slug: <kebab-case>
kind: communication-style | preference | request-pattern | interaction-rhythm | domain-context
occurrences: <integer count of supporting observations>
first_seen: <run stamp>
last_seen: <run stamp>
---

## Observation
<what the user consistently does — project-independent>

## How the LLM should adapt
<actionable communication/working guidance this pattern implies>

## Evidence
- `<transcript>` @ <ts> — <project basename> (<branch>) — <one line>
```

For both tracks, when updating: bump `occurrences`, set `last_seen`, append
`Examples`/`Evidence`, sharpen the body if new evidence adds nuance; never drop prior
examples. Reference examples by `transcript` + `ts` only — never paste chunk content.

### 5. Run report → `runs/`

One file per run, `runs/run-<stamp>.md` (reuse the manifest stamp). Record: chunks,
mistake/usage flag counts, confirmed vs rejected, which patterns were new/updated,
and a short narrative. Never overwrite a prior run report.

### 6. Summarize to the user

Briefly, both tracks: chunks scanned; mistakes confirmed vs rejected and which
patterns are new/updated; the top usage/communication patterns and what they imply
for how to work with the user. Note that the prevention/application step (turning
mistake patterns into rules / the output style / hooks, and folding the profile into
how you operate) is decided from the accumulated `findings/` and `profile/`.

## Notes

- Incremental via `ledger.json`. No new activity yields `MANIFEST: none` — correct,
  not an error.
- `findings/` and `profile/` accumulate across runs (patterns); run reports are kept
  per run (history).
- `render/` chunk files are disposable cache; the ledger has already advanced, so
  they will not be regenerated. Leave them, or clear `render/` after a run.
- Meta tool — not tied to any repo. Do not create issues or touch project files as
  part of a run.
