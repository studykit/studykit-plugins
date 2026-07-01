# Studykit Plugin Marketplace

This is the plugin marketplace directory - a collection of Claude Code and Codex plugins for various use cases.

## Version Management

Claude plugin versions live in each plugin's `plugins/<name>/.claude-plugin/plugin.json` (top-level `version` field, SemVer). Plugin entries in `.claude-plugin/marketplace.json` MUST NOT set `version` — if `version` is set in both places, `plugin.json` wins silently and a stale marketplace value would be masked.

Codex plugin manifests at `plugins/<name>/.codex-plugin/plugin.json` carry their own top-level `version` field. When a plugin supports both runtimes, bump the Claude and Codex `version` strings together and keep them identical.

When a new plugin is added or new features are added to an existing plugin, update the relevant marketplace files accordingly — `.claude-plugin/marketplace.json` for Claude and `.agents/plugins/marketplace.json` for Codex (registration only, not version).

## Claude and Codex Compatibility

Plugins should be designed and maintained to run in both Claude Code and Codex whenever possible. Avoid hardcoding agent-specific assumptions unless the feature is explicitly agent-specific. Keep shared behavior, scripts, documentation, and metadata portable across both environments, and clearly isolate any Claude-only or Codex-only implementation details.

Start with `guide/AGENTS.md` when adding or changing plugin manifests, hooks, skills, agents, commands, runtime scripts, or marketplace metadata. Use `guide/cross-runtime-guide.md` for cross-runtime architecture and marketplace/version policy, and `guide/adapter-guide.md` for adapter, hook, skill, and script runtime compatibility.

When developing or changing skills, hooks, plugins, or agents, always check the current official Claude Code and Codex documentation before relying on runtime behavior, manifest schemas, metadata fields, placeholders, environment variables, hook payloads, tool names, or marketplace behavior. Do not rely on memory or repository examples alone when an official behavior may have changed.

## Global Directory

The `global/` directory manages rules, subagents, skills, hooks, and MCP configurations intended for installation to `~/.claude/`. These are user-level components that apply globally across all projects, not specific to any single plugin.

## Language Requirements

**All documentation must be written in English.** When creating or editing markdown files, README files, CLAUDE.md files, or any other documentation, always use English.

## Agent Instruction Files

When creating an `AGENTS.md` instruction file, always create a sibling `CLAUDE.md` file that imports it with exactly `@AGENTS.md`. Keep shared instructions in `AGENTS.md`; use `CLAUDE.md` only as the Claude Code import shim unless a location explicitly requires Claude-only instructions.

Every `AGENTS.md` file must be organized as a map of contents: a concise, navigable index that orients the reader and points to where the detail actually lives (deeper docs, `dev/` design notes, source), rather than inlining long procedures or walkthroughs.

## Plugin README Scope

Each plugin's `plugins/<name>/README.md` is written for **end users who install the plugin from the marketplace**. It is not a contributor guide and is not context for the assistant at runtime.

Keep it scoped to user-visible surface:

- What the plugin does at a high level.
- Supported backends / providers / integrations.
- How to install and configure the plugin (config files, bootstrap skills).
- The slash commands, skills, or agents the plugin exposes and what each one does for the user.
- Pointers to deeper schema / reference docs (e.g. under `wiki/`).

Do **not** put in `README.md`:

- Directory or file-structure listings (script paths, hook layout, authoring tree, cache layout, internal module names).
- Hook-injected context, snippet substitution, runbook internals, or any other runtime-injected text.
- Test commands, validation, or anything else only contributors run.
- Implementation details of launchers, scripts, caches, or other plugin internals.

Contributor- and runtime-facing guidance lives in `AGENTS.md` files and under each plugin's `dev/`; runtime-injected context lives under `hooks/context/` (or the equivalent path for that plugin). When in doubt, ask whether a plugin user — not an author of the plugin — needs the information to install, configure, or invoke the plugin. If not, it does not belong in `README.md`.

