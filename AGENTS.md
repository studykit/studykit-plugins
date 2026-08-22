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

## Language Requirements

**All documentation must be written in English.** When creating or editing markdown files, README files, CLAUDE.md files, or any other documentation, always use English.

## Shipped Definitions Must Be Repo-Portable

Everything this repository publishes gets installed into **someone else's repository**.
That applies to every plugin here, not one of them: `plugins/*/agents/*.md`,
`plugins/*/skills/*/SKILL.md`, and any instruction text a plugin injects at runtime
(hook context, dispatch playbooks, command bodies).

So a shipped definition must not name anything that exists only here — `dev/design.md`,
`wiki/ref/...`, `guide/...`, this repo's env vars, or the plugin's own command surface as
though the target project had it — and must not carry a measurement taken against this
repo. Teach the agent **how to find** the equivalent wherever it lands instead: "look for a
README or CONTRIBUTING section on testing, a `docs/` or `dev/` document, a Makefile target,
a CI workflow, a test directory".

The failure is silent, which is why this is a rule rather than a preference. A hardcoded
path does not raise an error in a stranger's checkout; the agent reads the absence as "this
project has no such thing" and its verdict changes without anyone noticing.

Rationale, measurements and this-repo specifics belong in the plugin's `dev/` notes or its
`AGENTS.md` — the files that stay behind. A frontmatter comment citing `wiki/ref/...` for a
design decision is fine: it addresses contributors, not the agent. When editing a shipped
definition, ask whether the sentence would still be true in a repository you have never
seen.

## Agent Instruction Files

Do **not** write detailed implementation content into any `AGENTS.md` file: no long procedures, step-by-step walkthroughs, code-level specifics, or internal mechanics. Keep that detail in the deeper docs it belongs to (deeper docs, `dev/` design notes, source) and link to it from `AGENTS.md` instead of inlining it.

- **Omit anything the code already shows.** If a fact is evident from reading the source — file/module layout, function names, control flow, which file handles what — leave it out; it only drifts out of date. Capture the *why* and the constraints the code cannot express, not a restatement of the code.
- **Detailed rationale belongs in code comments, not `AGENTS.md`** — and only when the code alone does not make it clear. If reading the code answers the question, no comment is needed either.
- **Keep a way to run the tests.** `AGENTS.md` may say how to test the component; when those instructions grow long, replace them with a pointer to the file that holds them (e.g. under `dev/`).

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

