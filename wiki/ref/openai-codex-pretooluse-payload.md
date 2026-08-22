# Codex — `PreToolUse` payload, and what it does NOT carry

Source: https://learn.chatgpt.com/docs/hooks
Retrieved: 2026-08-23 (against `codex-cli 0.147.0` installed locally)

Fetched to settle one question: can a Codex `PreToolUse` hook tell which subagent is making
a tool call? It cannot.

## Common input fields (every event)

> | Field | Type | Meaning |
> | --- | --- | --- |
> | `session_id` | string | Current Codex session id |
> | `transcript_path` | string/null | Path to the session transcript file |
> | `cwd` | string | Working directory for the session |
> | `hook_event_name` | string | Current hook event name |
> | `model` | string | Active model slug |
> | `permission_mode` | string | Describes the current permission mode |
> | `turn_id` | string | Active Codex turn id |

## `PreToolUse` fields

> | Field | Type | Meaning |
> | --- | --- | --- |
> | `turn_id` | string | Active Codex turn id |
> | `tool_name` | string | Canonical hook tool name |
> | `tool_use_id` | string | Tool-call id for this invocation |
> | `tool_input` | JSON value | Tool-specific input |

**No `agent_id` and no `agent_type`.** Those two are documented for `SubagentStart` and
`SubagentStop` only.

## Bearing on guard

This is the difference that stops guard's `pre-write` restriction from being ported. On
Claude Code the same event carries `agent_type` — a plugin subagent reports the
plugin-scoped name, observed as `guard:korean-corrector` — so one hook can decide whether the
caller is a report-only agent. On Codex the event cannot answer that question at all, so a
hook registered there would either deny every write or none.

A correlation design is the only route: `SubagentStart` does carry `agent_id`/`agent_type`
(plus the parent `session_id`, per `guide/adapter-guide.md`), so identity could be recorded
there and looked up from `PreToolUse` by a field both events share. What has to be measured
before building it: whether a Codex subagent's `PreToolUse` reports the SUBAGENT's
`session_id` or the parent's. If it reports the parent's, no lookup can separate the
subagent's writes from the main thread's and the approach is dead.

Note the adapter guide's `agent_type` line refers to `SubagentStart` specifically; reading it
as a general property of Codex hook payloads is what made this look wired-able before the
page was checked.
