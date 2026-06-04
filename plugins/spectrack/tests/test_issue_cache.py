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

from issue.cache import (  # noqa: E402
    FreshnessMetadata,
    WorkflowFreshnessConflict,
    check_provider_freshness,
    comments_fingerprint,
    content_fingerprint,
    relationships_fingerprint,
    require_provider_freshness,
)


def test_gitignore_excludes_workflow_cache_root() -> None:
    assert ".spectrack-cache/" in (_REPO_ROOT / ".gitignore").read_text(encoding="utf-8")


def test_provider_freshness_allows_matching_fingerprint() -> None:
    result = require_provider_freshness(
        FreshnessMetadata(fingerprint="abc12345", target="issue"),
        provider_fingerprint="abc12345",
        artifact="GitHub issue #39 issue",
    )

    assert result.ok is True
    assert result.status == "fresh"


def test_provider_freshness_conflicts_on_fingerprint_mismatch() -> None:
    with pytest.raises(WorkflowFreshnessConflict) as excinfo:
        require_provider_freshness(
            FreshnessMetadata(fingerprint="abc12345", target="issue"),
            provider_fingerprint="def67890",
            artifact="GitHub issue #39 issue",
        )

    result = excinfo.value.result
    assert result.status == "conflict"
    assert result.cached_fingerprint == "abc12345"
    assert result.provider_fingerprint == "def67890"
    assert "changed on the provider" in str(excinfo.value)


def test_provider_freshness_blocks_missing_cached_fingerprint() -> None:
    result = check_provider_freshness(
        FreshnessMetadata(fingerprint=None, target="issue"),
        provider_fingerprint="abc12345",
        artifact="GitHub issue #39 issue",
    )

    assert result.ok is False
    assert result.status == "missing_fingerprint"


def test_provider_freshness_allows_missing_provider_fingerprint() -> None:
    result = require_provider_freshness(
        FreshnessMetadata(fingerprint="abc12345", target="issue"),
        provider_fingerprint=None,
        artifact="GitHub issue #39 issue",
    )

    assert result.ok is True
    assert result.status == "provider_fingerprint_unavailable"


def test_provider_freshness_skips_pending_new_artifact() -> None:
    result = require_provider_freshness(
        None,
        provider_fingerprint=None,
        artifact="GitHub issue pending creation",
        pending_new=True,
    )

    assert result.ok is True
    assert result.status == "pending_new"


def test_content_fingerprint_is_deterministic_and_content_sensitive() -> None:
    """The fingerprint is provider-clock-independent: identical title+body
    always hash the same, and any change flips the value. This replaces the
    issue #97 timestamp-precision regression, which no longer applies."""

    base = content_fingerprint("Title", "Body")

    assert base == content_fingerprint("Title", "Body")
    assert base != content_fingerprint("Title", "Body changed")
    assert base != content_fingerprint("Title changed", "Body")


def test_relationships_fingerprint_is_order_independent() -> None:
    """Per-target relationship fingerprints normalize list order so a
    reordered provider projection never produces a spurious conflict."""

    assert relationships_fingerprint(
        {"blocked_by": [1, 2, 3], "parent": 9}
    ) == relationships_fingerprint({"parent": 9, "blocked_by": [3, 1, 2]})


def test_comments_fingerprint_tracks_identity_and_revision() -> None:
    items = [{"id": "1", "updated_at": "2026-05-14T00:00:00Z"}]

    assert comments_fingerprint(items) == comments_fingerprint(
        [{"id": "1", "updated_at": "2026-05-14T00:00:00Z"}]
    )
    assert comments_fingerprint(items) != comments_fingerprint(
        [{"id": "1", "updated_at": "2026-05-14T00:09:00Z"}]
    )
    assert comments_fingerprint([]) != comments_fingerprint(items)
