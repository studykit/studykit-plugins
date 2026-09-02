---
name: setup
description: Install guard's read-only Codex claims-auditor agent in the current project's .codex/agents directory. Use when guard is installed in Codex and automatic or on-demand evidence audits need their named subagent.
disable-model-invocation: true
---

# Guard setup

This setup is needed only for Codex. It installs a project-local custom agent
named `guard_claims_auditor`; it does not change any user-level Codex
configuration.

First identify the current project's Git root. Explain that installation will
create `.codex/agents/guard_claims_auditor.toml`, then obtain the user's
explicit confirmation before making that change. A direct request to install it
counts as that confirmation.

Run the installer next to this skill with an absolute path, passing the project
root:

```sh
uv run --script <absolute-path-to-this-skill>/scripts/install_agent.py --project <git-root>
```

If the destination already exists, leave it unchanged and report that fact.
Replace it only when the user explicitly requests replacement, using `--force`.
Tell the user to start a new Codex session after installation so the named agent
is discovered.

Also tell them that guard's hooks are separate from this, and that installing and
enabling the plugin does not switch them on: Codex skips plugin-bundled hooks until
the user reviews and trusts the hook definition, and it does so silently. If guard
appears to do nothing under Codex while `codex plugin list` reports it installed and
enabled, untrusted hooks are the first thing to check — this skill cannot affect them. Dispatch this named agent in a fresh context, not with the
parent's full conversation history.
