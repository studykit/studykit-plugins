"""Tests for the preview_context script.

These guard the wiring (surfaces, provider selection, error path), not the
injected wording — that wording is owned by main_context and its fragments.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from preview_context import (  # noqa: E402
    available_agents,
    main,
    render_surface,
    resolve_config,
    synthesize_config,
)
from main_context import build_session_policy_context  # noqa: E402


def _render(surface: str, provider: str, *, agent: str | None = None) -> str:
    config = synthesize_config(provider)
    return "\n\n".join(
        render_surface(surface, config, runtime="claude", agent=agent)
    )


def test_session_surface_is_policy_wrapped() -> None:
    text = _render("session", "github")
    assert "<policy>" in text and "</policy>" in text
    assert "<launcher>" in text and "<runbook>" in text


def test_session_output_matches_runtime_builder() -> None:
    """Preview must reuse the same code path the hook injects — no second copy."""

    config = synthesize_config("github")
    direct = build_session_policy_context(
        config, plugin_root=_PLUGIN_ROOT, runtime="claude",
    )
    assert direct in _render("session", "github")


def test_provider_keyed_fragment_is_provider_specific() -> None:
    assert "issue-attach" in _render("session", "jira")
    assert "issue-attach" not in _render("session", "github")


def test_subagent_agent_block_merges_one_runbook() -> None:
    text = _render("subagent", "github", agent="issue-implementer")
    assert "<commit-prefix>" in text
    assert text.count("<runbook>") == 1


def test_subagent_base_has_no_agent_block() -> None:
    text = _render("subagent", "github", agent=None)
    assert "<commit-prefix>" not in text


def test_commit_surface_returns_prefix_snippet() -> None:
    assert "Prefix commit subjects" in _render("commit", "github")


def test_all_surface_includes_every_banner() -> None:
    text = _render("all", "github")
    assert "SessionStart (main)" in text
    assert "SubagentStart" in text
    assert "UserPromptSubmit (commit-prefix)" in text


def test_available_agents_lists_known_blocks() -> None:
    agents = available_agents()
    assert "issue-implementer" in agents
    assert agents == sorted(agents)


def test_resolve_config_without_provider_or_config_errors(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SPEC_TRACK_PROJECT_DIR", raising=False)
    with pytest.raises(SystemExit):
        resolve_config(None)


def test_main_list_agents(capsys) -> None:
    assert main(["--list-agents"]) == 0
    out = capsys.readouterr().out
    assert "issue-implementer" in out
