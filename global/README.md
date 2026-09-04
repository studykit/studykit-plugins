# Global definitions

Definitions installed into your **user-level** Claude directory rather than into a project or a
plugin. This directory mirrors the layout of `~/.claude`, so `global/agents/` lands in
`~/.claude/agents/`.

Agents here are the ones you reach with `claude --agent <name>`, by picking one when dispatching
a session in `claude agents`, or by @-mention. All three resolve names from `~/.claude/agents`,
which is outside any repository — so the definitions live here, under version control, and get
**linked** into place rather than copied. An edit in this checkout is live in the next session;
there is no reinstall step.

## Install

```sh
./global/install.sh
```

Re-run it after adding a definition. It refuses to overwrite anything it did not create; pass
`--force` to replace one anyway (a regular file is moved aside, never deleted). Use `--dry-run`
to see what it would do and `--uninstall` to remove its links. `CLAUDE_AGENTS_DIR` overrides the
agent destination.

## Agents

- **`think-board`** — a thinking partner. It asks questions until your request is clear,
  researches what the two of you decided to find out, and drafts documents — but takes no
  action you have not approved. It does not implement code.

  ```sh
  claude --agent think-board
  ```

  Its "nothing without your approval" rule is prose in the agent's own body, not an enforced
  boundary — run it in manual or auto mode and the permission system is what actually holds the
  line. Under `bypassPermissions` nothing does.
