"""Tests for shared workflow cache primitives."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
_REPO_ROOT = _PLUGIN_ROOT.parent.parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_cache import (  # noqa: E402
    FreshnessMetadata,
    WorkflowFreshnessConflict,
    check_provider_freshness,
    require_provider_freshness,
)


def test_gitignore_excludes_workflow_cache_root() -> None:
    assert "/.workflow-cache/" in (_REPO_ROOT / ".gitignore").read_text(encoding="utf-8")


def test_provider_freshness_allows_clean_cache_metadata() -> None:
    result = require_provider_freshness(
        FreshnessMetadata(
            source_updated_at="2026-05-13T12:00:00Z",
            fetched_at="2026-05-13T12:34:56Z",
        ),
        provider_updated_at="2026-05-13T12:00:00Z",
        artifact="GitHub issue #39 issue",
    )

    assert result.ok is True
    assert result.status == "fresh"


def test_provider_freshness_blocks_stale_provider_timestamp() -> None:
    with pytest.raises(WorkflowFreshnessConflict) as excinfo:
        require_provider_freshness(
            FreshnessMetadata(
                source_updated_at="2026-05-13T12:00:00Z",
                fetched_at="2026-05-13T12:34:56Z",
            ),
            provider_updated_at="2026-05-13T13:00:00Z",
            artifact="GitHub issue #39 issue",
        )

    assert excinfo.value.result.status == "stale"
    assert "Refresh the provider cache before writing" in str(excinfo.value)


def test_provider_freshness_blocks_missing_local_metadata() -> None:
    result = check_provider_freshness(
        FreshnessMetadata(source_updated_at=None, fetched_at="2026-05-13T12:34:56Z"),
        provider_updated_at="2026-05-13T12:00:00Z",
        artifact="GitHub issue #39 issue",
    )

    assert result.ok is False
    assert result.status == "missing_metadata"


def test_provider_freshness_allows_missing_provider_timestamp() -> None:
    result = require_provider_freshness(
        FreshnessMetadata(
            source_updated_at="2026-05-13T12:00:00Z",
            fetched_at="2026-05-13T12:34:56Z",
        ),
        provider_updated_at=None,
        artifact="GitHub issue #39 issue",
    )

    assert result.ok is True
    assert result.status == "provider_timestamp_unavailable"


def test_provider_freshness_skips_pending_new_artifact() -> None:
    result = require_provider_freshness(
        None,
        provider_updated_at=None,
        artifact="GitHub issue pending creation",
        pending_new=True,
    )

    assert result.ok is True
    assert result.status == "pending_new"
