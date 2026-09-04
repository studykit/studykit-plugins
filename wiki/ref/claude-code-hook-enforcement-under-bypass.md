# Enforcing an approval gate: hooks vs permission rules, and what survives `bypassPermissions`

Sources, retrieved 2026-09-03 via the raw `.md` endpoints:
- https://code.claude.com/docs/en/permissions.md
- https://code.claude.com/docs/en/permission-modes.md
- https://code.claude.com/docs/en/hooks.md

## What a `PreToolUse` hook can do

From `permissions.md`, § "Extend permissions with hooks":

> [Claude Code hooks](/docs/en/hooks-guide) let you register custom shell commands that evaluate
> permissions at runtime. When Claude Code makes a tool call, PreToolUse hooks run before the
> permission prompt, for every tool except [`EndConversation`](/docs/en/tools-reference#endconversation-tool-behavior).
> The hook output can deny the tool call, force a prompt, or skip the prompt to let the call proceed.

> Hook decisions don't bypass permission rules. Claude Code evaluates deny and ask rules
> regardless of what a PreToolUse hook returns: a matching deny rule blocks the call, and a
> matching ask rule still prompts even when the hook returned `"allow"` or `"ask"`. This
> preserves the deny-first precedence described in [Manage permissions](#manage-permissions),
> including deny rules set in managed settings.

> A blocking hook also takes precedence over allow rules. A hook that exits with code 2 stops the
> tool call before permission rules are evaluated, so the block applies even when an allow rule
> would otherwise let the call proceed.

From `hooks.md`, on the `if` filter:

> Because the `if` filter is best-effort, use the [permission system](/docs/en/permissions) rather
> than a hook to enforce a hard allow or deny.

## What `bypassPermissions` skips, and what it does not

From `permission-modes.md`, § "Available modes" lead-in:

> Deny rules block in every mode, including `bypassPermissions`. ... Allow rules have no effect in
> `bypassPermissions`.

§ "Skip all checks with bypassPermissions mode":

> `bypassPermissions` mode disables permission prompts and safety checks so tool calls execute
> immediately, including writes to [protected paths](#protected-paths).
>
> The [actions no mode auto-approves](#actions-no-mode-auto-approves) still prompt in this mode.

§ "Actions no mode auto-approves":

> Claude Code doesn't auto-approve the following in any mode, including `bypassPermissions`. ...
>
> * Tools matched by an explicit [ask rule](/docs/en/permissions#manage-permissions)
> * Connector tools your organization [set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), in sessions where that setting reaches Claude Code
> * Tools that require user interaction: the built-in `AskUserQuestion` tool and MCP tools marked [`requiresUserInteraction`](/docs/en/mcp#require-approval-for-a-specific-tool)
> * `rm` and `rmdir` removals targeting a [critical path](#critical-paths), which no allow rule or `PreToolUse` hook `"allow"` approves
> * The [cross-session messaging safeguards](#skip-all-checks-with-bypasspermissions-mode)

So an **`ask` permission rule** is documented to survive `bypassPermissions`; an `allow` rule is
documented not to matter there; a `deny` rule is documented to block there.

## `PreToolUse` decision values

From `hooks.md` (already recorded in `claude-code-pretooluse-permission-decision.md`):
`hookSpecificOutput.permissionDecision` takes `"allow"`, `"deny"`, `"ask"`, `"defer"`; with
`"ask"` the `permissionDecisionReason` is shown in the permission dialog.

## What the shell-command hole looks like

`hooks.md` shows a Bash `PreToolUse` payload carrying the literal command:

> ```json
> {
>   "tool_name": "Bash",
>   "tool_input": {
>     "command": "rm -rf /tmp/build",
>     "description": "Run test suite",
>     "timeout": 120000,
>     "run_in_background": false
>   }
> }
> ```

So a hook receives the raw command string and *can* pattern-match a redirect, `tee`, or `cp`.
Whether such matching is complete is not a documented property — it is the hook author's parsing.

Permission rules cannot close it either. From `permissions.md`:

> You can't match a tool's primary content field this way: `command` for Bash and PowerShell,
> `file_path` for Read, Edit, and Write ... A rule like `Bash(command:rm *)` would be bypassable
> by a compound command, so Claude Code ignores it and emits a startup warning.

## Not settled by these pages

- Whether a **hook's own `"ask"` decision** still produces a prompt under `bypassPermissions`.
  The pages state this for an `ask` *rule*, never for a hook's `ask` *decision*. Do not assume
  the two behave alike; measure before relying on it.
- Whether an agent's frontmatter `permissionMode` overrides a session started in
  `bypassPermissions`.
- `hooks.md` does not state whether agent-frontmatter hooks are ignored for plugin subagents;
  `claude-code-subagent-frontmatter.md` in this directory does say so for the `hooks` field.
