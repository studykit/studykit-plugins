---
name: handover
description: "Create a session handover file a fresh session can resume the work from, and record it so the session that replaces this one is offered it. Use when the user asks to hand off, wrap up, or write a handover before clearing the conversation."
argument-hint: "[--commit] [additional requirements]"
# The user's skill, never the model's. A handover is a decision about when this session ends,
# and a model that reached for it on its own would be answering that question for them. The
# description above is therefore never in context (`wiki/ref/claude-code-skill-invocation-paths.md`);
# it is autocomplete text, so it says what the user is choosing rather than baiting a match.
disable-model-invocation: true
# Both bundled commands, pre-approved so writing a handover does not open with a permission
# prompt for guard's own scripts. `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PLUGIN_ROOT}` substitute
# in `allowed-tools` exactly as they do in the body (`wiki/ref/claude-code-skill-substitutions.md`),
# so these match however the plugin is installed. The PATH wrapper is named alongside the
# `uv run` line it wraps: a rule for one never matches the other.
allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/handover-context.sh), Bash(guard-handover:*), Bash(uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py handover-written:*)
---

# Session handover

Create a self-contained handover so a fresh session can resume this work from the file alone.
Assume the next session cannot see this conversation.

## Context

!`"${CLAUDE_SKILL_DIR}/scripts/handover-context.sh"`

If no fields appeared above, this runtime does not run injected commands in skill content. Run
`scripts/handover-context.sh`, next to this `SKILL.md`, yourself and read its output instead.

## What to do

- Commit nothing unless `$ARGUMENTS` contains `--commit`. What to commit is the user's
  decision, and the conversation that would catch a bad one is about to end, so the flag is
  how they make it — its absence is an answer, not a gap for you to fill.
- With `--commit`, commit this session's non-handover work first: split it into meaningful
  commits with specific messages, leave unrelated changes unstaged and note them in the
  handover, and skip entirely if there is nothing to commit. The handover file itself is never
  committed either way.
- Write the handover to `<handover-dir>/<next-number>-<filename-timestamp>-<slug>.md`, using the
  fields from Context plus a short kebab-case slug. Never overwrite an existing file; bump the
  number until the path is unique.
- Leave the handover file uncommitted as an untracked file.
- Last, record it: `guard-handover <absolute path to the handover file>`. That is what lets the
  session a `/clear` opens next offer to read it; without it the file is written and nothing
  points the next session at it. Run it after the file exists — it checks the path.
  If the command is missing, or it reports it has no session to record against, stop there
  rather than working around it: the handover file is the deliverable, and the recording only
  decides whether the next session is offered it.

## Writing the handover

Write in English, and make it genuinely self-contained — enough for the next session to pick up
without this conversation. Point to `git show` / `git diff` instead of pasting large diffs, and
link durable records (issues, PRs, design docs) when relevant. Treat each handover as a
point-in-time snapshot: to record a later state, create a new handover rather than editing an
old one.

You decide the structure and which sections to include based on what this session actually
needs. Things usually worth capturing: the goal, current state, what changed (with commit refs),
key files, decisions and why, validation run and its results, known risks, next steps, and any
open questions or judgment calls the next session must make on its own. Omit what does not
apply; add what does.

Apply `$ARGUMENTS` as extra constraints, minus `--commit` — that flag is consumed above
and is not a constraint on what the handover says.

## Output

Report only:

- handover file path (left uncommitted)
- pre-handover commit SHA(s) — `skipped` with nothing to commit, `not requested` without `--commit`
- whether the recording step succeeded
