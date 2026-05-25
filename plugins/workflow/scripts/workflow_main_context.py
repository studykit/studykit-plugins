#!/usr/bin/env python3
"""Workflow main-assistant context helpers.

Prompt fragments live in Markdown files under ``hooks/context/`` so injected
wording can be maintained without editing hook logic. The directory sits beside
the hook scripts that consume it (not under ``agents/``) so the Claude Code
plugin runtime does not register each fragment as a fake agent. Main-session
fragments live under ``hooks/context/main/``; subagent fragments live under
``hooks/context/subagent/``; the only remaining inline snippets are
``hooks/context/snippets/authoring.md`` (single file, used at both
``SessionStart`` and ``SubagentStart``) and
``hooks/context/snippets/launcher/<runtime>.md`` (runtime-keyed), and
``hooks/context/snippets/prd-path.md`` (single file, used at both
``SessionStart`` and ``SubagentStart``). On-demand reference docs that the
assistant ``Read``s when the injected text points at them live under
``authoring/runbook/`` (not under ``hooks/context/``), so they sit on the
same ``authoring/`` read-tracking contract as the rest of the authoring
tree.

Template placeholders use ``{{NAME}}`` (double braces) so they stay visually
distinct from real ``$NAME`` shell variables in the same text.
``{{SNIPPET_AUTHORING}}``, ``{{SNIPPET_LAUNCHER}}``, and
``{{SNIPPET_PRD_PATH}}`` substitute the three inlined snippet files;
``{{WORKFLOW_RUNBOOK_DIR}}`` resolves to
``<plugin_root>/authoring/runbook``; ``{{WORKFLOW_ISSUE_PROVIDER}}`` resolves
to the active issue provider (``github``/``jira``/``filesystem``). Fetch /
write / link / etc. usage is *not* inlined — both ``main/session-start.md``
and ``subagent/session-start.md`` point at intent-keyed runbook docs
(``authoring/runbook/<intent>/<provider>.md``) which the agent reads on
demand. The Codex launcher snippet additionally has
``{{WORKFLOW_PLUGIN_ROOT}}`` resolved to the absolute plugin root before
injection so Codex shell tool calls can use literal paths.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

_PLUGIN_ROOT = Path(__file__).resolve().parents[1]
_CONTEXT_ROOT = _PLUGIN_ROOT / "hooks" / "context"
_KNOWN_ISSUE_PROVIDERS = {"github", "jira", "filesystem"}
_KNOWN_RUNTIMES = {"claude", "codex"}

_PLACEHOLDER_RE = re.compile(r"\{\{(\w+)\}\}")


def render(text: str, ctx: dict[str, str]) -> str:
    """Substitute ``{{NAME}}`` placeholders against ``ctx``.

    Raises ``KeyError`` if a placeholder is unresolved so that a forgotten
    wire-up surfaces at test time rather than leaking a literal placeholder
    into the injected text.
    """

    def sub(match: re.Match[str]) -> str:
        name = match.group(1)
        if name not in ctx:
            raise KeyError(f"unresolved placeholder: {{{{{name}}}}}")
        return ctx[name]

    return _PLACEHOLDER_RE.sub(sub, text)


def build_commit_prefix_context() -> str:
    """Return commit-prefix guidance injected into main assistant prompts."""

    return _read_fragment("snippets/commit-prefix.md").strip()


def build_session_policy_context(
    config: Any,
    *,
    plugin_root: Path | None = None,
    runtime: str | None = None,
) -> str:
    """Return SessionStart policy guidance injected into main assistant sessions."""

    text = _read_fragment("main/session-start.md").strip()
    if plugin_root is None:
        return _wrap_policy(text)
    resolved_plugin_root = plugin_root.expanduser().resolve()
    runbook_dir = resolved_plugin_root / "authoring" / "runbook"
    issue_provider = _provider_segment(config, "issues", _KNOWN_ISSUE_PROVIDERS)
    rendered = render(text, {
        "SNIPPET_LAUNCHER": _build_launcher_block(runtime, resolved_plugin_root),
        "SNIPPET_AUTHORING": _read_fragment("snippets/authoring.md").strip(),
        "SNIPPET_PRD_PATH": _read_fragment("snippets/prd-path.md").strip(),
        "WORKFLOW_RUNBOOK_DIR": str(runbook_dir),
        "WORKFLOW_ISSUE_PROVIDER": issue_provider,
    })
    return _wrap_policy(rendered)


def build_subagent_policy_context(
    config: Any,
    *,
    plugin_root: Path | None = None,
    runtime: str | None = None,
    agent_type: str | None = None,
) -> str:
    """Return SubagentStart context guidance injected into subagent prompts."""

    text = _read_fragment("subagent/session-start.md").strip()
    if plugin_root is None:
        return _wrap_policy(text)
    resolved_plugin_root = plugin_root.expanduser().resolve()
    runbook_dir = resolved_plugin_root / "authoring" / "runbook"
    issue_provider = _provider_segment(config, "issues", _KNOWN_ISSUE_PROVIDERS)
    rendered = render(text, {
        "SNIPPET_LAUNCHER": _build_launcher_block(runtime, resolved_plugin_root),
        "SNIPPET_AUTHORING": _read_fragment("snippets/authoring.md").strip(),
        "SNIPPET_PRD_PATH": _read_fragment("snippets/prd-path.md").strip(),
        "WORKFLOW_RUNBOOK_DIR": str(runbook_dir),
        "WORKFLOW_ISSUE_PROVIDER": issue_provider,
    })
    agent_block = _build_agent_context_block(agent_type, issue_provider, runbook_dir)
    merged = _merge_runbook_blocks(rendered, agent_block)
    return _wrap_policy(merged)


_RUNBOOK_BLOCK_RE = re.compile(
    r"\n?<runbook>\s*\n?(?P<body>.*?)\n?\s*</runbook>\n?",
    re.DOTALL,
)


def _merge_runbook_blocks(base: str, per_agent: str) -> str:
    """Combine a base subagent context with an optional per-agent block.

    If ``per_agent`` carries its own ``<runbook>...</runbook>`` block, the
    base's ``<runbook>`` is stripped first so the merged text emits a
    single ``<runbook>``. Any empty ``<runbook>`` (whitespace-only body)
    is removed from the combined text — agents without listed intents
    do not get an empty tag injected.
    """

    def has_runbook(text: str) -> bool:
        return _RUNBOOK_BLOCK_RE.search(text) is not None

    def strip_empty_runbooks(text: str) -> str:
        def replace(match: re.Match[str]) -> str:
            body = match.group("body").strip()
            return "" if not body else match.group(0)

        return _RUNBOOK_BLOCK_RE.sub(replace, text)

    if per_agent and has_runbook(per_agent):
        base = _RUNBOOK_BLOCK_RE.sub("\n\n", base, count=1)
        base = base.rstrip()
    combined = f"{base}\n\n{per_agent}" if per_agent else base
    combined = strip_empty_runbooks(combined)
    # Collapse 3+ consecutive newlines that the strip-and-merge can leave behind.
    combined = re.sub(r"\n{3,}", "\n\n", combined)
    return combined.strip()


def _wrap_policy(text: str) -> str:
    return f"<policy>\n{text.strip()}\n</policy>"


def _build_agent_context_block(
    agent_type: str | None,
    issue_provider: str,
    runbook_dir: Path,
) -> str:
    """Build the agent-specific context block appended at SubagentStart."""

    name = _agent_type_segment(agent_type)
    if name is None:
        return ""
    template_path = _CONTEXT_ROOT / "subagent" / "agents" / f"{name}.md"
    try:
        template = template_path.read_text(encoding="utf-8").strip()
    except OSError:
        return ""
    substitutions = {
        "WORKFLOW_RUNBOOK_DIR": str(runbook_dir),
        "WORKFLOW_ISSUE_PROVIDER": issue_provider,
    }
    if name == "issue-implementer":
        substitutions["SNIPPET_COMMIT_PREFIX"] = _read_fragment(
            "snippets/commit-prefix.md"
        ).strip()
    return render(template, substitutions)


def _agent_type_segment(agent_type: str | None) -> str | None:
    """Normalise the harness-reported agent_type to a bare agent name."""

    if not agent_type:
        return None
    text = str(agent_type).strip().lower()
    if not text:
        return None
    # Strip a plugin namespace prefix (e.g., "workflow:issue-implementer").
    if ":" in text:
        text = text.rsplit(":", 1)[-1]
    return text or None


def _build_launcher_block(runtime: str | None, plugin_root: Path) -> str:
    segment = _runtime_segment(runtime)
    block = _read_fragment(f"snippets/launcher/{segment}.md").strip()
    if segment == "codex":
        block = block.replace("{{WORKFLOW_PLUGIN_ROOT}}", str(plugin_root))
    return block


def _provider_segment(config: Any, role: str, known: set[str]) -> str:
    kind = _provider_kind(config, role)
    return kind if kind in known else "unsupported"


def _runtime_segment(runtime: str | None) -> str:
    if runtime is None:
        return "unsupported"
    text = str(runtime).strip().lower()
    return text if text in _KNOWN_RUNTIMES else "unsupported"


def _read_fragment(name: str) -> str:
    try:
        return (_CONTEXT_ROOT / name).read_text(encoding="utf-8")
    except OSError:
        return ""


def _provider_kind(config: Any, role: str) -> str | None:
    provider = getattr(config, role, None)
    kind = getattr(provider, "kind", None)
    if kind is None:
        return None
    text = str(kind).strip().lower()
    return text or None
