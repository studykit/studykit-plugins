# guard — contributor notes

`guard` is two capabilities over one stdlib dispatcher (`scripts/guard_hook.py`),
Claude Code only (it relies on the `claude` CLI and Claude-specific hook payloads;
no Codex path):

1. **Evidence judge** (Stop) — a repo-reading audit that flags a turn on an
   unsupported/surface-signal technical claim or an unjustified deferral. Runs in one
   of two **modes**: `headless` (an isolated `claude` runs inside the Stop hook and
   **blocks** on a violation) or `subagent` (the Stop hook injects `additionalContext`
   with no block; the main agent dispatches the `guardian` subagent to do the same
   audit).
2. **Approval gate** — block file mutation until the user explicitly approves.

The source is the truth for control flow. When editing, record *why* / *what must not
regress*, not a walkthrough of function bodies.

**A turn is the transcript's `promptId`.** guard keeps no turn buffer; at Stop it
reads the turn from Claude Code's transcript (`transcript_path` + `prompt_id`, both in
the Stop payload), sliced by `prompt_id`. State lives under
`${CLAUDE_PROJECT_DIR}/.claude/guard/` (`state/`, `sessions/`, `verified/`, and
`turns/` for subagent-mode slices).

## Runtime facts (verified; do not regress)

Confirmed against the installed CLI / real payloads, not memory. Re-verify before
changing anything that depends on them.

- **`prompt_id` is common to every hook** (PreToolUse and Stop included) and equals
  the transcript record's `promptId`. This is what lets the gate's `gated_prompt_id`
  match the same turn's Stop. Needs Claude Code ≥ 2.1.196 (seen on 2.1.197). Saved:
  `.claude/guard/refs/stop-hook-input.md`.
- **Transcript slice**: the anchor record has `promptId == prompt_id` (a typed prompt:
  `origin={"kind":"human"}` + str content). Derived records — assistant text,
  tool_use/tool_result — have `promptId=None` and stay in the slice; the slice ends at
  the next different non-empty promptId. Skip `isMeta:true` (guard's own feedback).
- **`!` commands inherit the preceding typed prompt's promptId** — they do NOT open
  their own turn (verified 2.1.197: `!git push` after a reply carried that reply's
  promptId; the `<bash-input>`/`<bash-stdout>` records also carry it). Their output
  lands in the slice AFTER the response guard already judged, so the evidence arrives
  later than the claims it would support. guard therefore does **not** treat `!` output
  as evidence and **does not judge** a turn whose slice contains a `!` command:
  `_read_turn_from_transcript` sets `has_user_command` and `cmd_stop` skips
  (`skip_user_command`).
- **A Stop hook may inject `additionalContext` without `decision`** and the
  conversation continues — the subagent-dispatch mechanism.
  `stop_hook_active: true` ⇒ guard already blocked this turn; Stop returns at once.
- **Fail open, always exit 0.** Blocking is a stdout decision payload, never a
  non-zero exit; any judge failure leaves state untouched and does not block.
- **Approval is armed only by a user message** (explicit-implementation classifier
  verdict); the `turn` skill and the model cannot arm it.
- **Control turns / exempt commands are not judged at Stop.** `/guard:turn` and
  `/guard:mode` open a real transcript turn whose response is a one-line relay with no
  evidence; `cmd_stop` skips it via `command_name` (from the transcript's expanded
  `<command-name>…`), matching the approval classifier's UserPromptSubmit skip. Without
  it the Stop judge falsely blocked the relay (session b30dbaec). The same path skips
  any skill/command listed in the `exempt_skills` config key (default `[]`), named with
  its plugin namespace (`plugin:skill`) — a user-invoked skill reaches the transcript
  as a namespaced `<command-name>` just like a command. Both modes honor it.
- **Gate exemptions** (unapproved writes that still pass): (1) `.claude/guard/refs/`
  — the evidence-first store, scoped to `refs/` ONLY; (2) **git-ignored** targets
  (`git check-ignore`) — scratch/temp, local config `**/*.local.*`, skill docs like
  `/handoff` → `.handover/`; not tracked project source. Guard's OWN config
  (`.claude/guard.local.json`) + state tree (`.claude/guard/`) are **excluded** from
  the git-ignore exemption (`_is_guard_owned`) — both are git-ignored, so without the
  exclusion the model could `Write` `state/` to self-arm or edit `guard.local.json` to
  disable the judge. All paths `resolve()`d; `git check-ignore` fails toward gating.

## Deeper detail

Full hook table, storage schema, the complete design invariants, config reference,
and the manual-testing recipe are in **`dev/design.md`** (not auto-loaded — open it
when working in that area).
