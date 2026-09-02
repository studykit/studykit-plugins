"""Tests for the Hermes plugin adapter."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent


class FakeHermesContext:
    def __init__(self) -> None:
        self.hooks: dict[str, Any] = {}
        self.skills: dict[str, Path] = {}

    def register_hook(self, name: str, callback: Any) -> None:
        self.hooks[name] = callback

    def register_skill(self, name: str, path: Path) -> None:
        self.skills[name] = path


def _load_plugin_module():
    spec = importlib.util.spec_from_file_location(
        "spectrack_hermes_plugin", _PLUGIN_ROOT / "__init__.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_config(project: Path) -> None:
    config_path = project / ".spectrack" / "config.yml"
    config_path.parent.mkdir(parents=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
    path: wiki/spectrack
issue_id_format: github
""".strip()
        + "\n",
        encoding="utf-8",
    )


def test_registers_hermes_hook_and_skills() -> None:
    plugin = _load_plugin_module()
    ctx = FakeHermesContext()

    plugin.register(ctx)

    assert "pre_llm_call" in ctx.hooks
    assert ctx.skills["handoff"] == _PLUGIN_ROOT / "skills" / "handoff" / "SKILL.md"


def test_pre_llm_call_injects_spectrack_context_once(tmp_path, monkeypatch) -> None:
    _write_config(tmp_path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SPECTRACK_PROJECT_DIR", raising=False)
    plugin = _load_plugin_module()
    ctx = FakeHermesContext()
    plugin.register(ctx)

    first = ctx.hooks["pre_llm_call"](
        session_id="hermes-session-1",
        is_first_turn=True,
        user_message="start",
        conversation_history=[],
        model="test-model",
        platform="cli",
    )
    second = ctx.hooks["pre_llm_call"](
        session_id="hermes-session-1",
        is_first_turn=False,
        user_message="next",
        conversation_history=[],
        model="test-model",
        platform="cli",
    )

    assert first is not None
    assert "Issue provider for this project: `github`" in first["context"]
    assert f'`"{_PLUGIN_ROOT}/scripts/spectrack" <script>`' in first["context"]
    assert second is None


def test_pre_llm_call_skips_unconfigured_project(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SPECTRACK_PROJECT_DIR", raising=False)
    plugin = _load_plugin_module()
    ctx = FakeHermesContext()
    plugin.register(ctx)

    assert ctx.hooks["pre_llm_call"](
        session_id="hermes-session-2",
        is_first_turn=True,
        user_message="start",
        conversation_history=[],
        model="test-model",
        platform="cli",
    ) is None
