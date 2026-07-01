---
name: exempt
description: "Choose which skills/commands guard's evidence judge skips at Stop, and record the choice in .claude/guard.local.json (exempt_skills). Use when the user wants to exempt a skill from guard's review, manage the exempt list, or asks which skills are exempt. Claude Code only."
argument-hint: '[skill names, optional]'
---

Let the user pick which skills/commands guard's evidence judge should skip at Stop
(the `exempt_skills` config), then record their confirmed choice. A skill's finished
turn is often a report or relay, not claims about the codebase — exempting it avoids
guard falsely flagging that turn.

Do this, in order:

1. **Read the current setting.** Run:
   `"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" exempt list`
   It prints `exempt_skills: <names>` (or `(none)`).

2. **Build the candidate list.** Use the skills available in THIS session (your
   available-skills context) with their exact invokable names, INCLUDING the plugin
   namespace (`plugin:skill`, e.g. `hindsight:review`) or the bare name for an
   un-namespaced skill (e.g. `deep-research`). Exclude guard's own `guard:turn`,
   `guard:mode`, and `guard:exempt`. If the user already named specific skills in
   their message, you may skip straight to step 4 with those.

3. **Ask the user to choose.** Call `AskUserQuestion` with `multiSelect: true`,
   listing the candidate skills. In each option's description note whether it is
   currently exempt (from step 1) so the user sees the existing state. The user's
   selection is the full set they want exempt.

4. **Record the confirmed set.** Run the script with the complete chosen set:
   `"${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py" exempt set <name1> <name2> …`
   (use `exempt clear` if the user chose none). Names may be given with or without the
   leading `/`; case is ignored.

5. **Relay** the resulting `exempt_skills` line to the user in one sentence.

Do NOT edit `.claude/guard.local.json` with the Write/Edit tools — guard's approval
gate blocks writes to its own config by design. The `exempt` script above is the only
supported writer; it changes just the `exempt_skills` key (never `enabled`/`mode`).
