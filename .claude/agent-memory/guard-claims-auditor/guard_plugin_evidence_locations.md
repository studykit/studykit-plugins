---
name: guard-plugin-evidence-locations
description: Where to check guard-plugin claims about hook behavior, trust dialog, session mute, and answer-file fallback
metadata:
  type: project
---

When auditing a turn about the `guard` plugin's own runtime behavior (trust dialog, session
mute, answer-file fallback, `--session` settings scoping, deny-vs-suggestion argument), the
supporting doc is `plugins/guard/dev/design.md` (not auto-loaded, must Read directly) plus
`plugins/guard/AGENTS.md`. Source-level confirmation:

- Trust dialog being a separate gate from any permission mode, and "runs in a directory
  already trusted" being a free/no-edit path: `plugins/guard/dev/design.md` around line 1504-1512.
- `user-prompt` hook (`UserPromptSubmit`) writing `.request.md` and the draft-path line under
  the exact same gate (not muted, an agent reads the turn, prompt_id present):
  `plugins/guard/scripts/guard_core/cmd_turn.py` (`cmd_user_prompt`, ~line 42-76).
- Muted-session behavior (marker + response written, but no recommendation) is in
  `plugins/guard/scripts/guard_core/cmd_stop.py` around line 125-137 (`_audit_paused` check
  placed AFTER writing `pending_verify_prompt_id`/response, so a paused turn still records but
  never recommends).
- `settings set --session` mirrors a config change into the live session's `state/<sid>.json`:
  `plugins/guard/scripts/guard_core/cmd_settings.py` (`_apply_session_scalar`, ~line 52-65).
- The "deny enforces, a sentence only suggests" argument the design leans on elsewhere:
  `plugins/guard/dev/design.md` around line 151-158.

**Why:** A recent turn (2026-08-23) made a dense table of "verified live in an interactive
tmux session" claims plus several design-behavior citations; all of them traced cleanly to
these exact locations, so a future audit of a similar guard-behavior turn can go straight
there instead of grepping cold.

**How to apply:** For any future turn claiming things about guard's hook gating, check these
files/lines first before a broader repo search.
