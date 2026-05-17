"""Tests for Jira issue cache carrier paths and draft parsing."""

from __future__ import annotations

import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_jira_data_center_client import JiraDataCenterSite  # noqa: E402
from workflow_jira_issue_cache import JiraDataCenterIssueCache, is_jira_issue_cache_body_path  # noqa: E402


def jira_site() -> JiraDataCenterSite:
    return JiraDataCenterSite(base_url="https://jira.example.test", authority="jira.example.test")


def test_jira_issue_cache_body_path_recognizer_matches_pending_draft_layout(tmp_path: Path) -> None:
    draft_body = tmp_path / ".workflow-cache" / "jira" / "jira.example.test" / "issues-pending" / "draft-1" / "issue.md"
    snapshot = tmp_path / ".workflow-cache" / "jira" / "jira.example.test" / "issues" / "TEST-1234" / "snapshot.md"
    issue_json = tmp_path / ".workflow-cache" / "jira" / "jira.example.test" / "issues" / "TEST-1234" / "issue.json"

    assert is_jira_issue_cache_body_path(draft_body, tmp_path)
    assert not is_jira_issue_cache_body_path(snapshot, tmp_path)
    assert not is_jira_issue_cache_body_path(issue_json, tmp_path)
    assert not is_jira_issue_cache_body_path(tmp_path / "issue.md", tmp_path)


def test_jira_issue_cache_paths_are_provider_specific(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()

    assert cache.issue_dir(site, "test-1234") == (
        tmp_path / ".workflow-cache" / "jira" / "jira.example.test" / "issues" / "TEST-1234"
    )
    assert cache.issue_json_file(site, "TEST-1234").name == "issue.json"
    assert cache.snapshot_file(site, "TEST-1234").name == "snapshot.md"


def test_jira_pending_issue_draft_parses_frontmatter_and_raw_body(tmp_path: Path) -> None:
    cache = JiraDataCenterIssueCache.for_project(tmp_path)
    site = jira_site()
    draft_path = cache.pending_issue_file(site, "draft-1")
    draft_path.parent.mkdir(parents=True)
    draft_path.write_text(
        """---
title: Draft Jira issue
labels:
  - task
state: open
---

Draft body.
""",
        encoding="utf-8",
    )

    draft = cache.read_pending_issue_draft(site, "draft-1")

    assert draft.local_id == "draft-1"
    assert draft.title == "Draft Jira issue"
    assert draft.labels == ("task",)
    assert draft.state == "open"
    assert draft.body == "Draft body.\n"
