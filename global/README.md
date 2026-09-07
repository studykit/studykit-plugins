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

On Windows, where that script has no shell to run in, use the PowerShell counterpart — same
flags, same output, same exit codes:

```powershell
./global/install.ps1
```

Re-run it after adding a definition. It refuses to overwrite anything it did not create; pass
`--force` to replace one anyway (a regular file is moved aside, never deleted). Use `--dry-run`
to see what it would do and `--uninstall` to remove its links. `CLAUDE_AGENTS_DIR` overrides the
agent destination. `install.ps1` accepts those spellings as well as `-Force`, `-DryRun`,
`-Uninstall`.

Because the definitions are linked rather than copied, installing on Windows needs symlink
creation to be permitted: turn on Developer Mode (Settings > System > For developers) and run
`install.ps1` under PowerShell 7. Windows PowerShell 5.1 cannot create a symlink without an
elevated shell even when Developer Mode is on.

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

- **`korean-translator`** — writes the Korean version of a finished English text: the text a
  Korean writer would have written, carrying exactly the claims the English carries. Any kind of
  writing, not only documentation — a report, an article, an announcement, an email, an issue
  body, a commit message, a PR description, a wiki page. It reads the genre first and writes the
  register that genre takes.

- **`korean-corrector`** — audits Korean prose on four axes (복합문, 번역체, AI 문체, register)
  and repairs each finding in place, one edit per finding. Dispatch it on Korean text that was
  just written or translated, so the text is judged by a reader rather than by its author.

  The two chain: `korean-translator` ends by naming `korean-corrector` as the next step, and
  neither is a claim auditor — they change how the text reads, never what it asserts.

  The `guard` plugin dispatches both of them by these bare names, so a project using guard's
  `/guard:answer` in Korean needs them installed here. guard ships no copy of its own: it used
  to, and the copies were retired in favour of these when the pair stopped being about
  documentation. Frontmatter and model choices are written up in `global/dev/`.
