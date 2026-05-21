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
    PLAN_MODE_TRIGGER_NOTE,
    TASK_AUDIT_TRIGGER_NOTE,
    ResolverError,
    authoring_relative_path,
    is_authoring_file,
    main as authoring_resolver_main,
    notes_anchor,
    reading_list_anchor,
    render_cache_hit_reference,
    resolve_authoring,
)
from workflow_session_state import read_authoring_resolution  # noqa: E402


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
    assert PLAN_MODE_TRIGGER_NOTE in resolution.notes


def test_task_emits_audit_trigger_note() -> None:
    resolution = resolve_authoring("task")
    assert TASK_AUDIT_TRIGGER_NOTE in resolution.notes
    assert "task-size-auditor" in TASK_AUDIT_TRIGGER_NOTE


def test_bug_omits_audit_trigger_note() -> None:
    resolution = resolve_authoring("bug")
    assert TASK_AUDIT_TRIGGER_NOTE not in resolution.notes


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


def test_task_comment_scope_omits_notes() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github", scope="comment")
    assert resolution.notes == ()


@pytest.mark.parametrize(
    "artifact_type,role,scope,expected_reading,expected_notes",
    [
        ("task", "issue", "content", "task-issue-reading-list", "task-issue-notes"),
        ("bug", "issue", "content", "bug-issue-reading-list", "bug-issue-notes"),
        ("spike", "issue", "content", "spike-issue-reading-list", None),
        ("spec", "knowledge", "content", "spec-knowledge-reading-list", None),
        (
            "task",
            "issue",
            "comment",
            "task-issue-comment-reading-list",
            None,
        ),
    ],
)
def test_to_markdown_emits_expected_anchor_headings(
    artifact_type: str,
    role: str,
    scope: str,
    expected_reading: str,
    expected_notes: str | None,
) -> None:
    resolution = resolve_authoring(
        artifact_type, role=role, provider="github", scope=scope
    )
    rendered = resolution.to_markdown()

    assert f"## {expected_reading}\n" in rendered
    if expected_notes is None:
        assert "-notes" not in rendered
    else:
        assert f"## {expected_notes}\n" in rendered


def test_to_markdown_lists_files_relative_to_a_declared_base() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github")
    rendered = resolution.to_markdown()

    reading_section, _, _ = rendered.partition("\n\n## ")
    lines = reading_section.splitlines()
    base_lines = [line for line in lines if line.startswith("Base: ")]
    bullet_lines = [line for line in lines if line.startswith("- ")]

    assert len(base_lines) == 1
    base = Path(base_lines[0].removeprefix("Base: "))
    assert base.is_absolute()
    assert bullet_lines == [
        f"- {path.relative_to(base)}" for path in resolution.files
    ]
    assert all(path.is_absolute() for path in resolution.files)


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("spike", None),
        ("epic", None),
        ("review", None),
        ("spec", None),
        ("architecture", None),
        ("ci", None),
        ("context", None),
        ("domain", None),
        ("nfr", None),
    ],
)
def test_to_markdown_omits_notes_section_for_noteless_types(
    artifact_type: str, role: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, role=role)
    rendered = resolution.to_markdown()

    assert resolution.notes == ()
    assert "-notes" not in rendered


@pytest.mark.parametrize(
    "scope,expected_reading,expected_notes",
    [
        ("content", "task-issue-reading-list", "task-issue-notes"),
        ("comment", "task-issue-comment-reading-list", "task-issue-comment-notes"),
    ],
)
def test_anchor_helpers_apply_comment_suffix_for_comment_scope(
    scope: str, expected_reading: str, expected_notes: str
) -> None:
    assert reading_list_anchor("task", "issue", scope) == expected_reading
    assert notes_anchor("task", "issue", scope) == expected_notes


def test_render_cache_hit_reference_with_notes_anchor() -> None:
    rendered = render_cache_hit_reference(
        "task-issue-reading-list", "task-issue-notes"
    )

    assert rendered == (
        "- See `task-issue-reading-list` above.\n"
        "- See `task-issue-notes` above — triggers apply to this call too.\n"
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_render_cache_hit_reference_without_notes_anchor() -> None:
    rendered = render_cache_hit_reference("spike-issue-reading-list")

    assert rendered == (
        "- See `spike-issue-reading-list` above.\n"
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_render_cache_hit_reference_includes_raw_recovery_hint() -> None:
    """Narrow contract: cache-hit output names the `--raw` token.

    The exact prose may evolve, but the bullet must always contain the
    `--raw` token so the model can find the escape hatch when the anchor
    body has dropped out of context.
    """

    with_notes = render_cache_hit_reference(
        "task-issue-reading-list", "task-issue-notes"
    )
    without_notes = render_cache_hit_reference("spike-issue-reading-list")

    assert "`--raw`" in with_notes
    assert "`--raw`" in without_notes


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


_RESOLVER_SESSION_ID = "session-resolver-test"


@pytest.fixture
def resolver_session(monkeypatch: pytest.MonkeyPatch) -> tuple[str, str]:
    monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", _RESOLVER_SESSION_ID)
    monkeypatch.setenv("WORKFLOW_SESSION_ID", _RESOLVER_SESSION_ID)
    monkeypatch.delenv("CODEX_THREAD_ID", raising=False)
    return "claude", _RESOLVER_SESSION_ID


def _resolver_args(tmp_path: Path, *, provider: str = "github", artifact: str = "task") -> list[str]:
    return [
        "--type",
        artifact,
        "--role",
        "issue",
        "--provider",
        provider,
        "--project",
        str(tmp_path),
    ]


def test_main_first_call_emits_sections_and_persists(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    runtime, session_id = resolver_session

    exit_code = authoring_resolver_main(_resolver_args(tmp_path))

    assert exit_code == 0
    out = capsys.readouterr().out
    assert "## task-issue-reading-list" in out
    assert "## task-issue-notes" in out

    entry = read_authoring_resolution(
        tmp_path, runtime, session_id, "task-issue-reading-list"
    )
    assert entry is not None
    assert entry["key"] == {
        "type": "task",
        "role": "issue",
        "provider": "github",
        "scope": "content",
    }
    assert entry["body"]
    assert entry["body"][0] == "## task-issue-reading-list"
    assert entry["emitted_at"]


def test_main_repeat_call_emits_bullet_only_form(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    args = _resolver_args(tmp_path)
    authoring_resolver_main(args)
    capsys.readouterr()

    exit_code = authoring_resolver_main(args)

    assert exit_code == 0
    out = capsys.readouterr().out
    assert out == (
        "- See `task-issue-reading-list` above.\n"
        "- See `task-issue-notes` above — triggers apply to this call too.\n"
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_main_repeat_call_for_noteless_type_omits_notes_bullet(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    args = _resolver_args(tmp_path, artifact="spike")
    authoring_resolver_main(args)
    capsys.readouterr()

    authoring_resolver_main(args)
    out = capsys.readouterr().out

    assert out == (
        "- See `spike-issue-reading-list` above.\n"
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_main_raw_flag_forces_section_emission(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    runtime, session_id = resolver_session
    base = _resolver_args(tmp_path)

    authoring_resolver_main(base)
    capsys.readouterr()
    first_entry = read_authoring_resolution(
        tmp_path, runtime, session_id, "task-issue-reading-list"
    )

    authoring_resolver_main(base + ["--raw"])
    out = capsys.readouterr().out

    assert "## task-issue-reading-list" in out
    second_entry = read_authoring_resolution(
        tmp_path, runtime, session_id, "task-issue-reading-list"
    )
    assert first_entry is not None
    assert second_entry is not None
    assert second_entry["key"] == first_entry["key"]
    assert second_entry["emitted_at"] >= first_entry["emitted_at"]


def test_main_provider_drift_triggers_refresh(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    runtime, session_id = resolver_session

    authoring_resolver_main(_resolver_args(tmp_path, provider="github"))
    capsys.readouterr()

    authoring_resolver_main(_resolver_args(tmp_path, provider="jira"))
    out = capsys.readouterr().out

    assert "## task-issue-reading-list" in out
    entry = read_authoring_resolution(
        tmp_path, runtime, session_id, "task-issue-reading-list"
    )
    assert entry is not None
    assert entry["key"]["provider"] == "jira"


def test_main_without_session_emits_sections_without_persisting(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
    monkeypatch.delenv("CODEX_THREAD_ID", raising=False)
    monkeypatch.delenv("WORKFLOW_SESSION_ID", raising=False)

    exit_code = authoring_resolver_main(_resolver_args(tmp_path))

    assert exit_code == 0
    out = capsys.readouterr().out
    assert "## task-issue-reading-list" in out

    hook_state_dir = tmp_path / ".workflow-cache" / "hook-state"
    if hook_state_dir.exists():
        assert not list(hook_state_dir.iterdir())
