# Studykit Plugins

A curated plugin repository that is compatible with both **Claude Code** and **OpenAI Codex**.

## Repository layout

- `<plugin-name>/`: shared plugin content
- `<plugin-name>/.claude-plugin/plugin.json`: Claude plugin manifest
- `<plugin-name>/.codex-plugin/plugin.json`: Codex plugin manifest
- `.claude-plugin/marketplace.json`: Claude marketplace catalog
- `.agents/plugins/marketplace.json`: Codex marketplace catalog

## Codex compatibility

This repository now includes a repo-scoped Codex marketplace at:

- `.agents/plugins/marketplace.json`

Each Codex plugin follows the structure described in the OpenAI Codex plugin documentation:

- `.codex-plugin/plugin.json` for the plugin manifest
- optional `skills/`, `.mcp.json`, `.app.json`, and `assets/` at the plugin root

Official reference:

- https://developers.openai.com/codex/plugins/build

## Use this repository in Codex

1. Open this repository in Codex.
2. Restart Codex if the marketplace was added while Codex was already running.
3. Open the plugin directory.
4. Select the **Studykit Plugins** marketplace.
5. Install or enable the plugins you want.

Codex reads the repo marketplace from `.agents/plugins/marketplace.json`.

## Use this repository in Claude Code

Claude compatibility is preserved through the existing Claude marketplace files:

- `.claude-plugin/marketplace.json`
- `<plugin-name>/.claude-plugin/plugin.json`

## Compatibility policy

For compatibility and versioning rules, see `AGENTS.md`.

## Available plugins

- `doc-util` — reading and searching various document formats including CHM files
- `korea-gov-data` — extract and organize Open API specifications from KOSIS (Korean Statistical Information Service)
- `dom-analyzer` — HTML/XML DOM structure analysis toolkit with hierarchy visualization
- `spectrack` — provider-backed workflow over GitHub Issues, Jira, GitHub repository wiki directory, and Confluence with issue and knowledge authoring contracts
- `obsidian` — generate query blocks, modify templates, and run CLI commands for Obsidian knowledge management (Dataview, Tasks, Jira Issue, Templater, CLI)
- `plantuml` — PlantUML diagram reference, creation, and validation
- `structurizr` — Structurizr DSL diagram composition, C4 model visualization, and architecture documentation
- `d2` — D2 diagram composition, rendering, and visualization
- `guard` — on-demand audit agents that review a finished turn, or a document, for unsupported claims, deferrals the repo could answer, unclear explanation, unnatural Korean, and drifted `AGENTS.md` / saved reference docs, plus a session `handover` skill
- `peers` — set up Claude Code sessions in other directories on this machine, delegate work to them, and introduce two of them so they settle a cross-repository question directly

`structurizr`, `d2` and `peers` are Claude Code only; the rest run in both Claude Code and Codex.
