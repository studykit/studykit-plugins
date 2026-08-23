# Claude Code — MCP servers in a plugin, and why a plugin agent cannot declare its own

Source: <https://code.claude.com/docs/en/plugins-reference> and
<https://code.claude.com/docs/en/plugins>
Retrieved: 2026-08-23
Local path: `wiki/ref/claude-code-plugin-mcp-servers.md`

Two facts that together decide how a plugin-shipped agent reaches an MCP tool. They point in
opposite directions, which is why both are recorded here.

## A plugin-shipped agent may NOT declare `mcpServers`

From the plugins reference, on plugin agents:

> Plugin agents support `name`, `description`, `model`, `effort`, `maxTurns`, `tools`,
> `disallowedTools`, `skills`, `memory`, `background`, and `isolation` frontmatter fields. The
> only valid `isolation` value is `"worktree"`. **For security reasons, `hooks`, `mcpServers`,
> and `permissionMode` are not supported for plugin-shipped agents.**

The subagent frontmatter table says the same thing more briefly — `mcpServers`: "MCP servers
available to this subagent. **Ignored for plugin subagents.**"
(`wiki/ref/claude-code-subagent-frontmatter.md`, fetched 2026-08-21).

Note the failure mode: **ignored**, not rejected. An `mcpServers:` block in a plugin agent's
frontmatter is silently inert, so the agent runs without the tool it appears to declare and
nothing reports the omission.

## A plugin MAY ship the server itself

From the plugin structure table:

> | `.mcp.json` | Plugin root | MCP server configurations |

Same file layout rule as every other component — it goes at the **plugin root**, never inside
`.claude-plugin/`:

> **Common mistake**: Don't put `commands/`, `agents/`, `skills/`, or `hooks/` inside the
> `.claude-plugin/` directory. Only `plugin.json` goes inside `.claude-plugin/`. All other
> directories must be at the plugin root level.
>
> The plugin root is the individual plugin's own directory: the one you pass to `--plugin-dir`
> or that contains `.claude-plugin/plugin.json`. It is never `~/.claude/`. For example, Claude
> Code doesn't read a `.mcp.json` placed at `~/.claude/.mcp.json`.

The manifest may point elsewhere instead — `plugin.json` accepts `"mcpServers":
"./mcp-config.json"`.

Config shape, with `${CLAUDE_PLUGIN_ROOT}` substituted:

```json
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": { "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data" }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"]
    }
  }
}
```

Integration behaviour, quoted:

> * Plugin MCP servers start automatically when the plugin is enabled
> * Servers appear as standard MCP tools in Claude's toolkit
> * Plugin servers can be configured independently of user MCP servers
> * If you run `/reload-plugins` mid-session, Claude Code keeps the live connections of
>   servers whose configuration is unchanged

## What follows for scoping a tool to one agent

The scoping has to happen in `tools`, which plugin agents *do* support. MCP patterns are valid
there — `mcp__<server>` / `mcp__<server>__*` grants every tool from that server, and `mcp__*`
in `disallowedTools` removes every MCP tool
(`wiki/ref/claude-code-subagent-frontmatter.md`).

So the reachable arrangement is: the server is declared **plugin-wide** in `.mcp.json`, and each
agent's `tools` allowlist decides whether it sees the server's tools. Two consequences the docs
state rather than imply:

- "Servers appear as standard MCP tools in Claude's toolkit" — the server is **session-wide**
  once the plugin is enabled. `tools` bounds what each *agent* may call; it does not stop the
  main conversation from calling the same tool. There is no documented way for a plugin to
  ship a server that only one of its agents can reach.
- An agent whose `tools` is an explicit list is unaffected, since `tools` is an allowlist when
  present. An agent that omits `tools` "inherits every tool available to subagents" and would
  pick the MCP tools up.

## Not covered here

Whether Codex plugins support a `.mcp.json` equivalent. Both pages above are Claude Code docs;
anything cross-runtime needs its own check against the Codex plugin docs.
