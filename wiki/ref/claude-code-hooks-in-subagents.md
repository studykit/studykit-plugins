# Claude Code — hooks inside subagents (`agent_id` / `agent_type`)

Source: https://code.claude.com/docs/en/hooks.md
Retrieved: 2026-08-23

Whether a tool call made by a subagent fires the same hooks as one made in the main
conversation, and how a hook tells the two apart.

## Tool events fire inside a subagent

> Hooks from settings files, managed policy settings, and plugins also run inside
> [subagents](/docs/en/sub-agents). When a subagent calls a tool, tool events such as
> `PreToolUse` and `PostToolUse` fire the same configured hooks as in the main conversation,
> and the input carries the `agent_id` and `agent_type` common input fields that identify the
> subagent.

## The two identifying fields

From the common-input-fields table:

> | Field | Description |
> | --- | --- |
> | `agent_id` | Unique identifier for the subagent. Present only when the hook fires inside a subagent call. Use this to distinguish subagent hook calls from main-thread calls. |
> | `agent_type` | Agent name (for example, `"Explore"` or `"security-reviewer"`). Present when the session uses `--agent` or the hook fires inside a subagent. For subagents, the subagent's type takes precedence over the session's `--agent` value. See SubagentStart for the values custom and plugin subagents report and how to write a matcher against a plugin-scoped name. |

`session_id` is unchanged — the subagent's tool call carries the same session id as the main
conversation, and `agent_id` is the only field that separates them.

## A plugin subagent reports the plugin-scoped name

From the `SubagentStart` section:

> For subagents shipped by a plugin, the agent type is the plugin-scoped identifier such as
> `my-plugin:reviewer`, not the bare frontmatter name. The colon places a plugin-scoped name
> on the regular-expression path, so anchor the matcher with `^` and `$` for an exact match:
> `^my-plugin:reviewer$`.

Two consequences follow from putting that paragraph beside the matcher table, and are noted
here as **derived** rather than as the page speaking:

- An unanchored `my-plugin:reviewer` also matches any longer name sharing that prefix, which
  is what the anchoring instruction is guarding against.
- A colon-free matcher such as `reviewer` stays on the *exact-match* path and is compared
  against the whole scoped string, so it matches nothing for a plugin subagent.

## `SubagentStop`

> `SubagentStop`: When a subagent finishes

It receives `last_assistant_message`, the same field `Stop` gets for the final assistant text.

## Not stated on this page

- No version requirement is documented for `SubagentStart` itself. The version notes in that
  area (v2.1.191, v2.1.195, v2.1.196) are about matcher separators, hyphens in the exact-match
  set, and `prompt_id` respectively.
- The `SubagentStart` example payload carries no `permission_mode`, `prompt_id` or `effort`
  key, and the common-fields table states `permission_mode` is not sent to every event — so a
  hook reading `permission_mode` on that event is resting on something undocumented.
