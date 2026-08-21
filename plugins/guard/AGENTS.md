# guard — contributor notes

`guard` supports Claude Code and Codex. Shared state/configuration helpers live in
`scripts/guard_hook.py`; runtime payload parsing and hook output stay in host adapters.
Requires Python 3.11+ (`enum.StrEnum`).

**guard makes no model call.** When a turn finishes it asks the main agent, through
`additionalContext`, to dispatch one subagent — `guard:router` — that reads the turn and
names which of guard's audit agents would actually find something in it, with a reason
for each; the main agent then dispatches those, concurrently. guard audits nothing
itself, every audit criterion lives in an agent definition under `agents/`, and the
router's per-agent cue lives in `agents/router.md`. One home per criterion is the point
of the shape.

The router used to be a `claude -p` child guard spawned from the hook. It is worth
knowing why it is not, because the reasons are all still true: a spawned child blocked
the Stop hook for its whole runtime at the end of every turn, needed `--safe-mode` or
guard's own Stop hook fired inside it and recursed, needed an explicit tool denylist
because omitting `--allowedTools` leaves a child fully tooled, could not use `--bare`
without breaking OAuth users, and turned spawn/timeout/exit-code/parse into four failure
paths guard had to tell apart from a clean verdict. As a subagent, none of that exists.

1. **Audit recommendation** (Stop) — every turn is marked as the on-demand target, so the
   user-invoked `/guard:claims-auditor`, `/guard:deferrals-auditor`,
   `/guard:korean-corrector` and `/guard:comment-corrector` work whatever the settings
   say. The four per-agent settings then decide what reaches the main agent unasked. Each
   is named after the agent it controls, so one string is the setting, the state key, the
   command, and the `subagent_type`. All four ship `off`: guard installed is guard
   available, not guard running, and with none on the hook emits nothing at all.

   The value is a mode, not a boolean — `off` / `fresh` / `reuse` — so how an agent runs
   is the same setting as whether it runs, and no separate reuse list can name an agent
   that is off. `reuse` holds one named instance (`guard-<agent>`) open for the session and
   resumes it with `SendMessage` instead of respawning, trading a new instance's per-turn
   independence for continuity; that is the user's call, not a default (`AgentMode` says
   why, `wiki/ref/claude-code-subagent-resume.md` says what the runtime guarantees). Three
   things follow and must not regress: the standing policy is stated once at SessionStart
   rather than in every recommendation; a mode change away from `reuse` is reported by the
   settings CLI, because guard has no other way to tell the session to stop addressing an
   instance guard itself cannot see; and the router is always fresh, since its question is
   about one turn and an instance carrying five can answer from the wrong one.

   The router chooses from the ELIGIBLE set, and eligibility is mechanical only: the
   mode being anything but `off`, plus — for a `reads="files"` agent — at least one source file the turn
   actually wrote. Everything requiring judgment is the router's.

   Four things must not regress:

   - The recommendation is `additionalContext`, never `decision: "block"`. The docs give
     both the same continuation and loop protections, but block reads as a hook error and
     a recommendation is guard working (`wiki/ref/claude-code-stop-hook-decision-control.md`).
   - It names **agents**, never guard's own skills. Those are
     `disable-model-invocation: true` because they are the user's entry point, so a hook
     must not reach through them.
   - The roster and the STEP 2 dispatch blocks cover the same eligible set. The blocks are
     the real bound on what can be dispatched: a key the router invents has no block, so
     a switched-off agent stays unreachable even if the router names it anyway.
   - guard writes the turn record's **response** section itself, from the Stop payload's
     `last_assistant_message`. That is the text being audited, so it must not pass through
     the author's hands; the main session appends only what guard cannot see — the
     request, the tool activity, and earlier evidence the claims rest on. That second half
     is asked for as inclusion, never selection, because the author curating its own
     evidence is the failure that shape invites.

2. **Post-edit** (PostToolUse on the write tools) — records the turn's edited source
   files for a later `comment-corrector` recommendation, and blocks until a file saved
   in the refs directory is listed in that directory's `AGENTS.md`. Both independent of
   the agent settings.

guard keeps no copy of a turn. It reads the transcript only to learn how a turn was
*opened* (`_turn_identity`), and both users of that are skips: a `task-notification` turn
is a background agent reporting in, and recommending an audit there puts guard in a loop
with itself; a turn opened by a control command or an exempt skill has nothing to audit.

Codex is different by necessity: its transcript is not a stable hook interface, so its
adapter keeps its own turn record, and it has one named agent rather than a set — a
router that can only forward to that same agent decides nothing, so Codex recommends the
whole eligible set, unrouted, and is correspondingly noisier. Projects must run
`$guard:setup` once to install it. State is host-specific under `.claude/guard/` or
`.codex/guard/`.

The source is the truth for control flow, and its comments carry the *why* next to the
code. When editing, record what must not regress — don't restate function bodies here.

## Deeper detail

Everything else lives in **`dev/design.md`** (not auto-loaded — open it when working in
this area): the hook table, storage schema, the runtime facts verified against the real
CLI, the full design invariants, the config reference, and the manual-testing recipe.
