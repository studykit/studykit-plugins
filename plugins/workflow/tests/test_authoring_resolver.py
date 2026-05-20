"""Tests for workflow authoring resolver."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from authoring_resolver import (  # noqa: E402
    ResolverError,
    authoring_relative_path,
    is_authoring_file,
    resolve_authoring,
)


def _config_path(project: Path) -> Path:
    path = project / ".workflow" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _rel_paths(paths: tuple[Path, ...]) -> list[str]:
    return [str(path.relative_to(_PLUGIN_ROOT / "authoring")) for path in paths]


def test_review_github_issue_resolution_uses_absolute_authoring_files() -> None:
    resolution = resolve_authoring("review", role="issue", provider="github")

    assert resolution.artifact_type == "review"
    assert resolution.role == "issue"
    assert resolution.provider == "github"
    assert _rel_paths(resolution.files) == [
"common/issue-body.md",
        "common/issue-authoring.md",
        "common/review-authoring.md",
        "providers/github-issue-convention.md",
        "providers/github-issue-relationships.md",
        "providers/github-issue-review-authoring.md",
        "providers/github-issue-anti-patterns.md",
    ]
    assert all(path.is_absolute() for path in resolution.files)
    assert all("plugins/workflow/operator" not in str(path) for path in resolution.files)


def test_review_github_issue_authoring_uses_native_target_relationship() -> None:
    resolution = resolve_authoring("review", role="issue", provider="github")
    github_review_doc = next(
        path for path in resolution.files if path.name == "github-issue-review-authoring.md"
    )

    text = github_review_doc.read_text(encoding="utf-8")

    assert "represent the target with\nthe GitHub dependency relationship" in text
    assert "GitHub-specific rules:" not in text
    assert "## Target" not in text
    assert "## Related" not in text


def test_spec_confluence_knowledge_resolution() -> None:
    resolution = resolve_authoring("spec", provider="confluence")

    assert resolution.role == "knowledge"
    assert _rel_paths(resolution.files) == [
"common/knowledge-body.md",
        "common/prd-authoring.md",
        "common/spec-authoring.md",
        "providers/confluence-page-convention.md",
        "providers/confluence-page-spec-authoring.md",
    ]


def test_dual_artifact_requires_explicit_role() -> None:
    with pytest.raises(ResolverError, match="specify --role"):
        resolve_authoring("research", provider="jira")


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("context", None),
        ("usecase", "knowledge"),
        ("usecase", "issue"),
        ("nfr", None),
        ("spec", None),
        ("domain", None),
    ],
)
def test_prd_component_includes_prd_index(artifact_type: str, role: str | None) -> None:
    resolution = resolve_authoring(artifact_type, role=role)
    assert "common/prd-authoring.md" in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("architecture", None),
        ("ci", None),
        ("task", None),
        ("bug", None),
        ("review", None),
        ("epic", None),
        ("spike", None),
        ("research", "issue"),
        ("research", "knowledge"),
    ],
)
def test_non_prd_artifact_excludes_prd_index(artifact_type: str, role: str | None) -> None:
    resolution = resolve_authoring(artifact_type, role=role)
    assert "common/prd-authoring.md" not in _rel_paths(resolution.files)


def test_comment_scope_excludes_prd_index() -> None:
    resolution = resolve_authoring("usecase", role="issue", scope="comment")
    assert "common/prd-authoring.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type",
    ["context", "usecase", "nfr", "spec", "domain"],
)
def test_github_knowledge_prd_paths_included_for_prd_components(artifact_type: str) -> None:
    resolution = resolve_authoring(artifact_type, role="knowledge", provider="github")
    assert "providers/github-knowledge-prd-paths.md" in _rel_paths(resolution.files)


def test_github_knowledge_prd_paths_excluded_for_non_prd_type() -> None:
    resolution = resolve_authoring("architecture", role="knowledge", provider="github")
    assert "providers/github-knowledge-prd-paths.md" not in _rel_paths(resolution.files)


def test_confluence_knowledge_does_not_include_github_prd_paths() -> None:
    resolution = resolve_authoring("spec", role="knowledge", provider="confluence")
    assert "providers/github-knowledge-prd-paths.md" not in _rel_paths(resolution.files)


def test_usecase_issue_role_does_not_include_github_prd_paths() -> None:
    resolution = resolve_authoring("usecase", role="issue", provider="github")
    assert "providers/github-knowledge-prd-paths.md" not in _rel_paths(resolution.files)


def test_provider_can_be_inferred_from_workflow_config(tmp_path: Path) -> None:
    _config_path(tmp_path).write_text(
        """
version: 1
providers:
  issues:
    kind: jira
  knowledge:
    kind: github
""".lstrip(),
        encoding="utf-8",
    )

    issue_resolution = resolve_authoring("task", project=tmp_path)
    knowledge_resolution = resolve_authoring("architecture", project=tmp_path)

    assert issue_resolution.provider == "jira"
    assert "common/issue-authoring.md" in _rel_paths(issue_resolution.files)
    assert "providers/jira-issue-convention.md" in _rel_paths(issue_resolution.files)
    assert "providers/jira-issue-relationships.md" in _rel_paths(issue_resolution.files)
    assert "providers/jira-issue-task-authoring.md" in _rel_paths(issue_resolution.files)
    assert "providers/jira-issue-anti-patterns.md" in _rel_paths(issue_resolution.files)
    assert knowledge_resolution.provider == "github"
    assert _rel_paths(knowledge_resolution.files) == [
"common/knowledge-body.md",
        "common/architecture-authoring.md",
        "providers/github-knowledge-convention.md",
        "providers/github-knowledge-architecture-authoring.md",
    ]


def test_comment_scope_github_issue_resolution_uses_only_comment_relevant_files() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github", scope="comment")

    assert resolution.role == "issue"
    assert resolution.provider == "github"
    assert _rel_paths(resolution.files) == [
"providers/github-issue-convention.md",
    ]


def test_comment_scope_jira_issue_resolution_uses_only_comment_relevant_files() -> None:
    resolution = resolve_authoring("task", role="issue", provider="jira", scope="comment")

    assert resolution.role == "issue"
    assert resolution.provider == "jira"
    assert _rel_paths(resolution.files) == [
"providers/jira-issue-convention.md",
    ]


def test_invalid_provider_for_role_is_rejected() -> None:
    with pytest.raises(ResolverError, match="not valid for role 'knowledge'"):
        resolve_authoring("spec", provider="jira")


def test_require_config_fails_when_missing(tmp_path: Path) -> None:
    with pytest.raises(ResolverError, match=".workflow/config.yml was not found"):
        resolve_authoring("task", project=tmp_path, require_config=True)


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_implementation_types_include_plan_mode_authoring(artifact_type: str) -> None:
    resolution = resolve_authoring(artifact_type)
    assert "common/plan-mode-authoring.md" in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("spike", None),
        ("epic", None),
        ("review", None),
        ("research", "issue"),
        ("usecase", "issue"),
        ("spec", None),
        ("architecture", None),
    ],
)
def test_non_implementation_types_exclude_plan_mode_authoring(
    artifact_type: str, role: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, role=role)
    assert "common/plan-mode-authoring.md" not in _rel_paths(resolution.files)


def test_task_comment_scope_excludes_plan_mode_authoring() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github", scope="comment")
    assert "common/plan-mode-authoring.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_implementation_types_emit_plan_mode_note(artifact_type: str) -> None:
    resolution = resolve_authoring(artifact_type)
    assert len(resolution.notes) == 1
    note = resolution.notes[0]
    assert "plan mode" in note.lower()
    assert "retroactive" in note.lower()
    assert "notes" in resolution.to_json()
    assert resolution.to_json()["notes"] == [note]


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("spike", None),
        ("epic", None),
        ("review", None),
        ("research", "issue"),
        ("usecase", "issue"),
        ("spec", None),
        ("architecture", None),
    ],
)
def test_non_implementation_types_omit_plan_mode_note(
    artifact_type: str, role: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, role=role)
    assert resolution.notes == ()
    assert "notes" not in resolution.to_json()


def test_task_comment_scope_omits_plan_mode_note() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github", scope="comment")
    assert resolution.notes == ()
    assert "notes" not in resolution.to_json()


def test_authoring_path_classification_uses_plugin_authoring_root(tmp_path: Path) -> None:
    authoring_file = _PLUGIN_ROOT / "authoring" / "common" / "task-authoring.md"
    outside_file = tmp_path / "task-authoring.md"
    outside_file.write_text("# Task\n", encoding="utf-8")

    assert authoring_relative_path(authoring_file, plugin_root=_PLUGIN_ROOT) == (
        "common/task-authoring.md"
    )
    assert is_authoring_file(authoring_file, plugin_root=_PLUGIN_ROOT)
    assert authoring_relative_path(outside_file, plugin_root=_PLUGIN_ROOT) is None
    assert not is_authoring_file(outside_file, plugin_root=_PLUGIN_ROOT)
