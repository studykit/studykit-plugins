"""Lock the strict-isolation contract for the issue-* snippet composer.

Under ``config.issues.kind=github`` the composed snippet must not contain
Jira-specific tokens (``--epic``, ``<KEY>``, ``--subtask-``, ``<verb>``);
under ``config.issues.kind=jira`` the composed snippet must not contain
GitHub-specific tokens (``<ref>``, ``--state-reason``, `` close ``, `` reopen ``
static verbs). The ``unsupported`` / ``filesystem`` providers must keep
reading a single file (no ``common.md`` prepended).
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_main_context import _read_snippet  # noqa: E402


_INTENTS = (
    "issue-fetch",
    "issue-drafts",
    "issue-write",
    "issue-writeback",
    "issue-relationships",
)

_JIRA_ONLY_TOKENS = ("--epic", "<KEY>", "--subtask-", "<verb>")
_GITHUB_ONLY_TOKENS = ("<ref>", "--state-reason", " close ", " reopen ")


@pytest.mark.parametrize("intent", _INTENTS)
def test_github_composition_excludes_jira_tokens(intent: str) -> None:
    composed = _read_snippet(intent, "github")
    for token in _JIRA_ONLY_TOKENS:
        assert token not in composed, (
            f"Jira-only token {token!r} leaked into the github "
            f"composition for {intent!r}:\n{composed}"
        )


@pytest.mark.parametrize("intent", _INTENTS)
def test_jira_composition_excludes_github_tokens(intent: str) -> None:
    composed = _read_snippet(intent, "jira")
    for token in _GITHUB_ONLY_TOKENS:
        assert token not in composed, (
            f"GitHub-only token {token!r} leaked into the jira "
            f"composition for {intent!r}:\n{composed}"
        )


@pytest.mark.parametrize("intent", _INTENTS)
def test_github_composition_prepends_common(intent: str) -> None:
    composed = _read_snippet(intent, "github")
    common_path = (
        _PLUGIN_ROOT / "hooks" / "context" / "snippets" / intent / "common.md"
    )
    assert common_path.exists(), f"missing common.md for {intent!r}"
    common = common_path.read_text(encoding="utf-8").strip()
    assert composed.startswith(common[: min(80, len(common))]), (
        f"common.md prefix not detected at the head of the {intent!r} composition "
        f"under github"
    )


@pytest.mark.parametrize("intent", _INTENTS)
def test_jira_composition_prepends_common(intent: str) -> None:
    composed = _read_snippet(intent, "jira")
    common_path = (
        _PLUGIN_ROOT / "hooks" / "context" / "snippets" / intent / "common.md"
    )
    common = common_path.read_text(encoding="utf-8").strip()
    assert composed.startswith(common[: min(80, len(common))]), (
        f"common.md prefix not detected at the head of the {intent!r} composition "
        f"under jira"
    )


@pytest.mark.parametrize("intent", _INTENTS)
def test_unsupported_provider_reads_single_file(intent: str) -> None:
    """``unsupported`` does NOT prepend common.md."""
    composed = _read_snippet(intent, "unsupported")
    unsupported_path = (
        _PLUGIN_ROOT / "hooks" / "context" / "snippets" / intent / "unsupported.md"
    )
    expected = unsupported_path.read_text(encoding="utf-8").strip()
    assert composed == expected, (
        f"unsupported.md content should be returned verbatim for {intent!r}; "
        f"common.md must not be prepended"
    )


@pytest.mark.parametrize("intent", _INTENTS)
def test_filesystem_provider_reads_single_file(intent: str) -> None:
    """``filesystem`` does NOT prepend common.md."""
    composed = _read_snippet(intent, "filesystem")
    filesystem_path = (
        _PLUGIN_ROOT / "hooks" / "context" / "snippets" / intent / "filesystem.md"
    )
    expected = filesystem_path.read_text(encoding="utf-8").strip()
    assert composed == expected, (
        f"filesystem.md content should be returned verbatim for {intent!r}; "
        f"common.md must not be prepended"
    )
