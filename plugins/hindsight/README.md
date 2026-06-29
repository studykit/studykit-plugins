# Hindsight

Hindsight reviews your past Claude Code sessions to help future ones go better. It
reads your accumulated session history across all projects and distills two things:

- **Recurring agent mistakes** — project-independent patterns the assistant tends to
  repeat (e.g. editing a file before reading it, claiming work done that wasn't),
  captured so they can be prevented.
- **How you work and communicate** — a profile of your preferences, phrasing, and
  rhythm, captured so the assistant can adapt to you.

Both accumulate over time, and each run adds a short report. Hindsight only looks at
new session activity since the last run, so repeat runs are quick.

## Supported host

**Claude Code only.** Hindsight reads Claude Code session transcripts and uses
Claude subagents to do the analysis. It is intentionally Claude-specific and has no
Codex equivalent.

## Install

Install the `hindsight` plugin from the Studykit marketplace. It also needs
[`uv`](https://docs.astral.sh/uv/) available on your PATH (used to run the bundled
analysis script).

## Use

Invoke the skill:

```
/hindsight:review
```

The skill scans your session history, asks a cheap model to flag suspected mistakes
and usage signals, then has the top model confirm and organize them. It reports what
it found and where the accumulated patterns and profile live. The first run reviews
your whole history and can take a while; later runs only cover what's new.

Results are stored under `~/.claude/hindsight/` so they persist across projects and
sessions.
