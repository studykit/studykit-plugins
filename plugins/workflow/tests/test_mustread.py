"""Tests for the workflow mustread (authoring resolver) script."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from mustread import (  # noqa: E402
    PLAN_MODE_TRIGGER_NOTE,
    TASK_AUDIT_TRIGGER_NOTE,
    ResolverError,
    authoring_relative_path,
    is_authoring_file,
    main as mustread_main,
    notes_anchor,
    reading_anchor,
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
    resolution = resolve_authoring("review", role="issue", provider="github", purpose="author")

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
    resolution = resolve_authoring("review", role="issue", provider="github", purpose="author")
    github_review_doc = next(
        path for path in resolution.files if path.name == "github-issue-review-authoring.md"
    )

    text = github_review_doc.read_text(encoding="utf-8")

    assert "represent the target with\nthe GitHub dependency relationship" in text
    assert "GitHub-specific rules:" not in text
    assert "## Target" not in text
    assert "## Related" not in text


def test_dual_artifact_requires_explicit_role() -> None:
    with pytest.raises(ResolverError, match="specify --role"):
        resolve_authoring("research", provider="jira", purpose="author")


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
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
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
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    assert "common/prd-authoring.md" not in _rel_paths(resolution.files)


def test_comment_scope_excludes_prd_index() -> None:
    resolution = resolve_authoring("usecase", role="issue", scope="comment", purpose="author")
    assert "common/prd-authoring.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize("role", ["issue", "knowledge"])
def test_usecase_includes_abstraction_guard(role: str) -> None:
    resolution = resolve_authoring("usecase", role=role, purpose="author")
    assert "common/usecase-abstraction-guard.md" in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("context", None),
        ("nfr", None),
        ("spec", None),
        ("domain", None),
        ("task", None),
        ("review", None),
        ("research", "issue"),
        ("research", "knowledge"),
    ],
)
def test_non_usecase_excludes_abstraction_guard(
    artifact_type: str, role: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    assert "common/usecase-abstraction-guard.md" not in _rel_paths(resolution.files)


def test_usecase_comment_scope_excludes_abstraction_guard() -> None:
    resolution = resolve_authoring("usecase", role="issue", scope="comment", purpose="author")
    assert "common/usecase-abstraction-guard.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,role,expected",
    [
        ("usecase", "issue", "common/usecase-issue-authoring.md"),
        ("usecase", "knowledge", "common/usecase-knowledge-authoring.md"),
        ("research", "issue", "common/research-issue-authoring.md"),
        ("research", "knowledge", "common/research-knowledge-authoring.md"),
    ],
)
def test_dual_type_returns_role_specific_authoring_file(
    artifact_type: str, role: str, expected: str
) -> None:
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    rels = _rel_paths(resolution.files)
    assert expected in rels


@pytest.mark.parametrize(
    "artifact_type,role,unexpected",
    [
        ("usecase", "issue", "common/usecase-knowledge-authoring.md"),
        ("usecase", "knowledge", "common/usecase-issue-authoring.md"),
        ("research", "issue", "common/research-knowledge-authoring.md"),
        ("research", "knowledge", "common/research-issue-authoring.md"),
    ],
)
def test_dual_type_excludes_other_role_authoring_file(
    artifact_type: str, role: str, unexpected: str
) -> None:
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    rels = _rel_paths(resolution.files)
    assert unexpected not in rels


@pytest.mark.parametrize("artifact_type", ["usecase", "research"])
@pytest.mark.parametrize("role", ["issue", "knowledge"])
def test_dual_type_includes_common_authoring_file(
    artifact_type: str, role: str
) -> None:
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    rels = _rel_paths(resolution.files)
    assert f"common/{artifact_type}-authoring.md" in rels


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("usecase", "issue"),
        ("usecase", "knowledge"),
        ("research", "issue"),
        ("research", "knowledge"),
    ],
)
def test_dual_type_common_authoring_precedes_role_specific(
    artifact_type: str, role: str
) -> None:
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    rels = _rel_paths(resolution.files)
    common = f"common/{artifact_type}-authoring.md"
    role_specific = f"common/{artifact_type}-{role}-authoring.md"
    assert rels.index(common) < rels.index(role_specific)


@pytest.mark.parametrize(
    "artifact_type",
    ["context", "usecase", "nfr", "spec", "domain"],
)
def test_github_knowledge_prd_paths_included_for_prd_components(artifact_type: str) -> None:
    resolution = resolve_authoring(artifact_type, role="knowledge", provider="github", purpose="author")
    assert "providers/github-knowledge-prd-paths.md" in _rel_paths(resolution.files)


def test_github_knowledge_prd_paths_excluded_for_non_prd_type() -> None:
    resolution = resolve_authoring("architecture", role="knowledge", provider="github", purpose="author")
    assert "providers/github-knowledge-prd-paths.md" not in _rel_paths(resolution.files)


def test_usecase_issue_role_does_not_include_github_prd_paths() -> None:
    resolution = resolve_authoring("usecase", role="issue", provider="github", purpose="author")
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

    issue_resolution = resolve_authoring("task", project=tmp_path, purpose="author")
    knowledge_resolution = resolve_authoring("architecture", project=tmp_path, purpose="author")

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
    resolution = resolve_authoring("task", role="issue", provider="github", scope="comment", purpose="author")

    assert resolution.role == "issue"
    assert resolution.provider == "github"
    assert _rel_paths(resolution.files) == [
"providers/github-issue-convention.md",
    ]


def test_comment_scope_jira_issue_resolution_uses_only_comment_relevant_files() -> None:
    resolution = resolve_authoring("task", role="issue", provider="jira", scope="comment", purpose="author")

    assert resolution.role == "issue"
    assert resolution.provider == "jira"
    assert _rel_paths(resolution.files) == [
"providers/jira-issue-convention.md",
    ]


def test_invalid_provider_for_role_is_rejected() -> None:
    with pytest.raises(ResolverError, match="not valid for role 'knowledge'"):
        resolve_authoring("spec", provider="jira", purpose="author")


def test_require_config_fails_when_missing(tmp_path: Path) -> None:
    with pytest.raises(ResolverError, match=".workflow/config.yml was not found"):
        resolve_authoring("task", project=tmp_path, require_config=True, purpose="author")


@pytest.mark.parametrize(
    "artifact_type,role",
    [
        ("task", None),
        ("epic", None),
        ("bug", None),
        ("spike", None),
        ("review", None),
        ("research", "issue"),
        ("usecase", "issue"),
    ],
)
def test_issue_resolution_excludes_decomposition_patterns(
    artifact_type: str, role: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    assert "common/decomposition-patterns.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_implementation_types_emit_plan_mode_note(artifact_type: str) -> None:
    resolution = resolve_authoring(artifact_type, purpose="author")
    assert PLAN_MODE_TRIGGER_NOTE in resolution.notes


def test_task_emits_audit_trigger_note() -> None:
    resolution = resolve_authoring("task", purpose="author")
    assert TASK_AUDIT_TRIGGER_NOTE in resolution.notes
    assert "task-size-auditor" in TASK_AUDIT_TRIGGER_NOTE


def test_bug_omits_audit_trigger_note() -> None:
    resolution = resolve_authoring("bug", purpose="author")
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
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    assert resolution.notes == ()


def test_task_comment_scope_omits_notes() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github", scope="comment", purpose="author")
    assert resolution.notes == ()


@pytest.mark.parametrize(
    "artifact_type,role,scope,expected_reading,expected_notes",
    [
        ("task", "issue", "content", "task-issue", "task-issue"),
        ("bug", "issue", "content", "bug-issue", "bug-issue"),
        ("spike", "issue", "content", "spike-issue", None),
        ("spec", "knowledge", "content", "spec-knowledge", None),
        (
            "task",
            "issue",
            "comment",
            "task-issue-comment",
            None,
        ),
    ],
)
def test_to_markdown_emits_expected_anchor_tags(
    artifact_type: str,
    role: str,
    scope: str,
    expected_reading: str,
    expected_notes: str | None,
) -> None:
    resolution = resolve_authoring(
        artifact_type, role=role, provider="github", scope=scope,
        purpose="author",
    )
    rendered = resolution.to_markdown()

    assert f'<reading anchor="{expected_reading}">' in rendered
    assert "</reading>" in rendered
    if expected_notes is None:
        assert "<notes " not in rendered
    else:
        assert f'<notes anchor="{expected_notes}">' in rendered
        assert "</notes>" in rendered


def test_to_markdown_lists_files_relative_to_a_declared_base() -> None:
    resolution = resolve_authoring("task", role="issue", provider="github", purpose="author")
    rendered = resolution.to_markdown()

    reading_section, _, _ = rendered.partition("</reading>")
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
    resolution = resolve_authoring(artifact_type, role=role, purpose="author")
    rendered = resolution.to_markdown()

    assert resolution.notes == ()
    assert "<notes " not in rendered


@pytest.mark.parametrize(
    "scope,expected",
    [
        ("content", "task-issue"),
        ("comment", "task-issue-comment"),
    ],
)
def test_anchor_helpers_apply_comment_suffix_for_comment_scope(
    scope: str, expected: str
) -> None:
    assert reading_anchor("task", "issue", scope, "author") == expected
    assert notes_anchor("task", "issue", scope, "author") == expected


def test_render_cache_hit_reference_with_notes_anchor() -> None:
    rendered = render_cache_hit_reference("task-issue", "task-issue")

    assert rendered == (
        '- See `<reading anchor="task-issue">` above.\n'
        '- See `<notes anchor="task-issue">` above — '
        "triggers apply to this call too.\n"
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_render_cache_hit_reference_without_notes_anchor() -> None:
    rendered = render_cache_hit_reference("spike-issue")

    assert rendered == (
        '- See `<reading anchor="spike-issue">` above.\n'
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_actors_type_is_rejected() -> None:
    with pytest.raises(ResolverError, match="unsupported artifact type"):
        resolve_authoring("actors", role="knowledge", purpose="author")


def test_author_purpose_for_usecase_issue_bundles_actors_with_provider() -> None:
    resolution = resolve_authoring(
        "usecase", role="issue", provider="github",
        purpose="author",
    )
    rels = _rel_paths(resolution.files)

    assert "common/usecase-issue-authoring.md" in rels
    assert "common/actors-authoring.md" in rels
    assert "providers/github-knowledge-actors-authoring.md" in rels
    assert rels.index("common/usecase-issue-authoring.md") < rels.index(
        "common/actors-authoring.md"
    )


def test_author_purpose_for_usecase_knowledge_bundles_actors_with_provider() -> None:
    resolution = resolve_authoring(
        "usecase", role="knowledge", provider="github",
        purpose="author",
    )
    rels = _rel_paths(resolution.files)

    assert "common/usecase-knowledge-authoring.md" in rels
    assert "common/actors-authoring.md" in rels
    assert "providers/github-knowledge-actors-authoring.md" in rels


def test_author_purpose_for_usecase_without_provider_omits_provider_actors_file() -> None:
    resolution = resolve_authoring(
        "usecase", role="issue", purpose="author"
    )
    rels = _rel_paths(resolution.files)

    assert "common/actors-authoring.md" in rels
    assert "providers/github-knowledge-actors-authoring.md" not in rels


def test_review_purpose_for_usecase_issue_bundles_actors_companion() -> None:
    resolution = resolve_authoring(
        "usecase", role="issue", provider="github", purpose="review"
    )

    assert resolution.purpose == "review"
    assert _rel_paths(resolution.files) == [
        "common/review/usecase-issue-review-criteria.md",
        "common/review/actors-review-criteria.md",
        "common/issue-body.md",
        "common/issue-authoring.md",
        "common/review-authoring.md",
        "providers/github-issue-convention.md",
        "providers/github-issue-relationships.md",
        "providers/github-issue-review-authoring.md",
        "providers/github-issue-anti-patterns.md",
    ]
    assert resolution.notes == ()


def test_review_purpose_omits_target_type_authoring_files() -> None:
    resolution = resolve_authoring(
        "usecase", role="issue", provider="github", purpose="review"
    )
    rels = _rel_paths(resolution.files)

    assert "common/usecase-authoring.md" not in rels
    assert "common/usecase-issue-authoring.md" not in rels
    assert "common/usecase-abstraction-guard.md" not in rels
    assert "providers/github-issue-usecase-authoring.md" not in rels


def test_review_purpose_anchor_includes_review_suffix() -> None:
    resolution = resolve_authoring(
        "usecase", role="issue", provider="github", purpose="review"
    )

    assert resolution.reading_anchor == "usecase-issue-review"


def test_review_purpose_rejects_comment_scope() -> None:
    with pytest.raises(ResolverError, match="purpose 'review' does not apply"):
        resolve_authoring(
            "usecase", role="issue", purpose="review", scope="comment"
        )


def test_review_purpose_missing_file_raises() -> None:
    with pytest.raises(ResolverError, match="does not exist"):
        resolve_authoring(
            "usecase", role="knowledge", purpose="review"
        )


def test_resolve_authoring_requires_purpose_keyword() -> None:
    with pytest.raises(TypeError, match="purpose"):
        resolve_authoring("task", role="issue")  # type: ignore[call-arg]


def test_main_requires_purpose_argument(
    capsys: pytest.CaptureFixture[str],
    tmp_path: Path,
) -> None:
    args = [
        "--type",
        "task",
        "--role",
        "issue",
        "--provider",
        "github",
        "--project",
        str(tmp_path),
    ]

    with pytest.raises(SystemExit):
        mustread_main(args)

    err = capsys.readouterr().err
    assert "--purpose" in err


def test_author_purpose_returns_authoring_contract_without_review_files() -> None:
    resolution = resolve_authoring(
        "usecase", role="issue", provider="github",
        purpose="author",
    )

    assert resolution.purpose == "author"
    rels = _rel_paths(resolution.files)
    assert "common/usecase-issue-authoring.md" in rels
    assert "common/actors-authoring.md" in rels
    assert "common/review/actors-review-criteria.md" not in rels
    assert "common/review/usecase-issue-review-criteria.md" not in rels
    assert resolution.reading_anchor == "usecase-issue"


def test_render_cache_hit_reference_includes_raw_recovery_hint() -> None:
    """Narrow contract: cache-hit output names the `--raw` token.

    The exact prose may evolve, but the bullet must always contain the
    `--raw` token so the model can find the escape hatch when the anchor
    body has dropped out of context.
    """

    with_notes = render_cache_hit_reference("task-issue", "task-issue")
    without_notes = render_cache_hit_reference("spike-issue")

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


def _resolver_args(
    tmp_path: Path,
    *,
    provider: str = "github",
    artifact: str = "task",
    purpose: str = "author",
) -> list[str]:
    return [
        "--type",
        artifact,
        "--role",
        "issue",
        "--provider",
        provider,
        "--project",
        str(tmp_path),
        "--purpose",
        purpose,
    ]


def test_main_first_call_emits_sections_and_persists(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    runtime, session_id = resolver_session

    exit_code = mustread_main(_resolver_args(tmp_path))

    assert exit_code == 0
    out = capsys.readouterr().out
    assert '<reading anchor="task-issue">' in out
    assert '<notes anchor="task-issue">' in out

    reading_entry = read_authoring_resolution(
        tmp_path, runtime, session_id, tag="reading", anchor="task-issue"
    )
    assert reading_entry is not None
    assert reading_entry["key"] == {
        "type": "task",
        "role": "issue",
        "provider": "github",
        "scope": "content",
        "purpose": "author",
    }
    assert reading_entry["emitted_at"]

    notes_entry = read_authoring_resolution(
        tmp_path, runtime, session_id, tag="notes", anchor="task-issue"
    )
    assert notes_entry is not None
    assert notes_entry["key"] == reading_entry["key"]


def test_main_repeat_call_emits_bullet_only_form(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    args = _resolver_args(tmp_path)
    mustread_main(args)
    capsys.readouterr()

    exit_code = mustread_main(args)

    assert exit_code == 0
    out = capsys.readouterr().out
    assert out == (
        '- See `<reading anchor="task-issue">` above.\n'
        '- See `<notes anchor="task-issue">` above — '
        "triggers apply to this call too.\n"
        "- If the anchor body is no longer in context, rerun this command "
        "with `--raw` to re-emit it.\n"
    )


def test_main_repeat_call_for_noteless_type_omits_notes_bullet(
    capsys: pytest.CaptureFixture[str],
    resolver_session: tuple[str, str],
    tmp_path: Path,
) -> None:
    args = _resolver_args(tmp_path, artifact="spike")
    mustread_main(args)
    capsys.readouterr()

    mustread_main(args)
    out = capsys.readouterr().out

    assert out == (
        '- See `<reading anchor="spike-issue">` above.\n'
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

    mustread_main(base)
    capsys.readouterr()
    first_entry = read_authoring_resolution(
        tmp_path, runtime, session_id, tag="reading", anchor="task-issue"
    )

    mustread_main(base + ["--raw"])
    out = capsys.readouterr().out

    assert '<reading anchor="task-issue">' in out
    second_entry = read_authoring_resolution(
        tmp_path, runtime, session_id, tag="reading", anchor="task-issue"
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

    mustread_main(_resolver_args(tmp_path, provider="github"))
    capsys.readouterr()

    mustread_main(_resolver_args(tmp_path, provider="jira"))
    out = capsys.readouterr().out

    assert '<reading anchor="task-issue">' in out
    entry = read_authoring_resolution(
        tmp_path, runtime, session_id, tag="reading", anchor="task-issue"
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

    exit_code = mustread_main(_resolver_args(tmp_path))

    assert exit_code == 0
    out = capsys.readouterr().out
    assert '<reading anchor="task-issue">' in out

    hook_state_dir = tmp_path / ".workflow-cache" / "hook-state"
    if hook_state_dir.exists():
        assert not list(hook_state_dir.iterdir())
