# Claude Code session transcript (`*.jsonl`) — schema

Reference for the session-management workstream (browse stored sessions, render
a stored transcript). Not auto-loaded; open it when working on session reading.
`../AGENTS.md` is the always-loaded map and points here.

## Provenance and stability

This is **not an officially documented format.** It is reverse-engineered from
real transcript files and is **Claude Code version-dependent** — fields can
appear, disappear, or change between releases. Anthropic does not publish a
stable schema for these files, so treat everything here as observed, not
guaranteed, and re-check against real files before building on a field.

Derived empirically from a sample of 21 session files across 10 projects (3363
lines; 1979 `message` payloads), on Claude Code `version` `2.1.198`. Presence
percentages below are frequency in that sample, not a contract. A reader can
regenerate the same tables by scanning `~/.claude/projects/*/*.jsonl` and
grouping by `type` / `message.role` / content-block `type`.

Any reader (index metadata extraction, transcript rendering) must tolerate
missing/unknown fields and skip malformed lines rather than assume this shape.

## File layout

- Path: `~/.claude/projects/<project-slug>/<session-uuid>.jsonl`, one directory
  per project, one file per session.
- `<project-slug>` is the project's absolute path with `/` replaced by `-`. It
  is lossy for display; the true path is in each entry's `cwd` field, so prefer
  `cwd` over decoding the slug.
- **JSONL**: one JSON object per line, each independently parseable. A truncated
  or malformed final line is normal (a session may be mid-write) — skip it.

## Entry types (the line-level `type`)

Two broad families:

- **Conversation entries** carry the shared envelope below: `user`, `assistant`,
  `system`, `attachment`.
- **Sidecar entries** are thin, envelope-less bookkeeping records keyed only by
  `sessionId`: `ai-title`, `last-prompt`, `mode`, `permission-mode`,
  `queue-operation`, `file-history-snapshot`, `agent-setting`.

## Conversation envelope

Present on `user` / `assistant` / `system` / `attachment` (100% in sample unless
noted):

```
type          str      entry discriminator
uuid          str      this entry's id
parentUuid    str|null previous entry's uuid; null at the root (forms a tree)
sessionId     str
timestamp     str      ISO-8601
cwd           str      real project path (prefer over the slug)
gitBranch     str
version       str      Claude Code version that wrote it
userType      str
entrypoint    str
isSidechain   bool     true for subagent / sidechain entries
```

Optional/among-these: `slug` (~50%), `isMeta` (system-injected entry, a display
skip candidate), `permissionMode`, and the type-specific fields below.

### `user`
- `promptId` (req), `message` (req; see below).
- `toolUseResult` (~75%, `dict|list|str`) and `sourceToolAssistantUUID` (~75%)
  appear on entries that are actually tool results rather than human prompts.
- `isMeta` (~3%) marks non-human injected prompts.

### `assistant`
- `requestId` (req), `message` (req).
- Attribution when relevant: `attributionMcpServer` / `attributionMcpTool`
  (~12%), `attributionSkill`, `attributionPlugin`.
- `error` / `isApiErrorMessage` on API-error turns.

### `system`
- `subtype` (req) plus a variable bag: `isMeta` (~92%), `durationMs` /
  `messageCount` (~79%), and hook telemetry (`hookCount`, `hookInfos`,
  `hookErrors`, `hookAdditionalContext`, `stopReason`, ~8% each). Not
  conversation content.

### `attachment`
- `attachment` (req, `dict`).

## `message` payload (the conversation content)

`user.message` and `assistant.message` are **Anthropic Messages API message
objects**.

- `user.message`: `{ role: "user", content }` — only these two fields.
- `assistant.message` (100% in sample): `model`, `id`, `type`, `role`,
  `content`, `stop_reason`, `stop_sequence`, `stop_details`, `usage`,
  `diagnostics`.

`content` is **either a string or an array of blocks** — arrays dominate
(1811 vs 168 strings in sample). A string is raw text; wrappers like
`<command-name>…` / `<local-command-caveat>…` show up here and are display noise.

### Content blocks

| block `type` | fields | side |
|---|---|---|
| `text` | `type`, `text` | assistant, user |
| `thinking` | `type`, `thinking`, `signature` | assistant |
| `tool_use` | `type`, `id`, `name`, `input` (dict), `caller` (dict) | assistant |
| `tool_result` | `tool_use_id`, `type`, `content` (`str`\|`list`), `is_error` (~41%) | user |

- `tool_result` pairs to its call by `tool_use_id`. Its `content` may itself be a
  block array (e.g. images), not just a string.

## Compact schema

```
Line =
  | ConversationEntry   # user | assistant | system | attachment
  | SidecarEntry        # ai-title | last-prompt | mode | permission-mode
                        #   | queue-operation | file-history-snapshot | agent-setting

ConversationEntry {
  type, uuid, parentUuid: str|null, sessionId, timestamp,
  cwd, gitBranch, version, userType, entrypoint, isSidechain: bool,
  message?: AnthropicMessage,   # user / assistant
  attachment?: object,          # attachment
  ...typeSpecific               # promptId, requestId, subtype, isMeta, ...
}

AnthropicMessage { role: "user"|"assistant", content: str | Block[] }

Block = Text{ text }
      | Thinking{ thinking, signature }
      | ToolUse{ id, name, input, caller }
      | ToolResult{ tool_use_id, content, is_error? }

# sidecars (envelope-less, keyed by sessionId)
ai-title             { type, aiTitle, sessionId }
last-prompt          { type, leafUuid, sessionId, lastPrompt? }
mode                 { type, mode, sessionId }
queue-operation      { type, operation, timestamp, sessionId, content? }
file-history-snapshot{ type, messageId, snapshot, isSnapshotUpdate }
```

## Implications for session management

- **Index / list metadata** (browse subtask): a session's title comes from an
  `ai-title` record's `aiTitle`; its project/branch/start time come from the
  first conversation entry's `cwd` / `gitBranch` / `timestamp`. `sessionId` is
  the filename stem. None of this needs reading the whole file.
- **Rendering** (transcript subtask): a stored transcript carries far more than
  the live viewer shows. The live path only renders user prompts and assistant
  `text`; stored files also hold `thinking`, `tool_use`, `tool_result`,
  `system`, `attachment`, and sidecar records. Rendering is therefore a
  filtering decision — which block/entry types to surface — mapped onto the
  events the viewer already understands. Skip candidates: `isMeta` entries, all
  sidecar types, and `<command-*>` / caveat-wrapped strings.
