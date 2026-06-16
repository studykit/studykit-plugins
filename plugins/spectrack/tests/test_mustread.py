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
    BACKLOG_TRIGGER_NOTE,
    RETROACTIVE_PUBLISH_STATE_GITHUB,
    RETROACTIVE_TRIGGER_NOTE,
    USECASE_INTERVIEW_NOTE,
    USECASE_SKILL_PATH,
    ResolverError,
    authoring_relative_path,
    is_authoring_file,
    main as mustread_main,
    notes_anchor,
    reading_anchor,
    render_cache_hit_reference,
    resolve_authoring,
)
from mustread import _resolution_key  # noqa: E402
from session_state import read_authoring_resolution  # noqa: E402


def _config_path(project: Path) -> Path:
    path = project / ".spectrack" / "config.yml"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _rel_paths(paths: tuple[Path, ...]) -> list[str]:
    return [str(path.relative_to(_PLUGIN_ROOT / "authoring")) for path in paths]


def _mode_for(artifact_type: str) -> str | None:
    """A valid `--mode` for task/bug content authoring; ``None`` elsewhere.

    Lets parametrized tests that mix task/bug with other types supply the
    now-required mode only where it applies.
    """
    return "backlog" if artifact_type in {"task", "bug"} else None


def test_bare_review_resolution_uses_absolute_authoring_files() -> None:
    resolution = resolve_authoring("review", side="issue", provider="github")

    assert resolution.artifact_type == "review"
    assert resolution.side == "issue"
    assert resolution.target is None
    assert resolution.provider == "github"
    assert _rel_paths(resolution.files) == [
        "contracts/issue/common.md",
        "contracts/issue/review.md",
        "providers/issue/github/convention.md",
    ]
    assert all(path.is_absolute() for path in resolution.files)
    assert all("plugins/spectrack/operator" not in str(path) for path in resolution.files)


def test_dual_artifact_requires_explicit_side() -> None:
    with pytest.raises(ResolverError, match="specify --side"):
        resolve_authoring("research", provider="jira")


@pytest.mark.parametrize(
    "artifact_type,side",
    [
        ("context", None),
        ("usecase", "knowledge"),
        ("usecase", "issue"),
        ("nfr", None),
        ("spec", None),
        ("domain", None),
    ],
)
def test_prd_component_includes_prd_index(artifact_type: str, side: str | None) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
    assert "contracts/prd.md" in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,side",
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
def test_non_prd_artifact_excludes_prd_index(artifact_type: str, side: str | None) -> None:
    resolution = resolve_authoring(artifact_type, side=side, mode=_mode_for(artifact_type))
    assert "contracts/prd.md" not in _rel_paths(resolution.files)


def test_comment_scope_excludes_prd_index() -> None:
    resolution = resolve_authoring("usecase", side="issue", scope="comment")
    assert "contracts/prd.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize("side", ["issue", "knowledge"])
def test_usecase_includes_abstraction_guard(side: str) -> None:
    resolution = resolve_authoring("usecase", side=side)
    assert "contracts/usecase-abstraction-guard.md" in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,side",
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
    artifact_type: str, side: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, side=side, mode=_mode_for(artifact_type))
    assert "contracts/usecase-abstraction-guard.md" not in _rel_paths(resolution.files)


def test_usecase_comment_scope_excludes_abstraction_guard() -> None:
    resolution = resolve_authoring("usecase", side="issue", scope="comment")
    assert "contracts/usecase-abstraction-guard.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,side,expected",
    [
        ("usecase", "issue", "contracts/issue/usecase.md"),
        ("usecase", "knowledge", "contracts/knowledge/usecase.md"),
        ("research", "issue", "contracts/issue/research.md"),
        ("research", "knowledge", "contracts/knowledge/research.md"),
    ],
)
def test_dual_type_returns_side_specific_authoring_file(
    artifact_type: str, side: str, expected: str
) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
    rels = _rel_paths(resolution.files)
    assert expected in rels


@pytest.mark.parametrize(
    "artifact_type,side,unexpected",
    [
        ("usecase", "issue", "contracts/knowledge/usecase.md"),
        ("usecase", "knowledge", "contracts/issue/usecase.md"),
        ("research", "issue", "contracts/knowledge/research.md"),
        ("research", "knowledge", "contracts/issue/research.md"),
    ],
)
def test_dual_type_excludes_other_side_authoring_file(
    artifact_type: str, side: str, unexpected: str
) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
    rels = _rel_paths(resolution.files)
    assert unexpected not in rels


@pytest.mark.parametrize("artifact_type", ["usecase", "research"])
@pytest.mark.parametrize("side", ["issue", "knowledge"])
def test_dual_type_includes_common_authoring_file(
    artifact_type: str, side: str
) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
    rels = _rel_paths(resolution.files)
    assert f"contracts/{artifact_type}.md" in rels


@pytest.mark.parametrize(
    "artifact_type,side",
    [
        ("usecase", "issue"),
        ("usecase", "knowledge"),
        ("research", "issue"),
        ("research", "knowledge"),
    ],
)
def test_dual_type_common_authoring_precedes_side_specific(
    artifact_type: str, side: str
) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
    rels = _rel_paths(resolution.files)
    common = f"contracts/{artifact_type}.md"
    side_specific = f"contracts/{side}/{artifact_type}.md"
    assert rels.index(common) < rels.index(side_specific)


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

    issue_resolution = resolve_authoring("task", project=tmp_path, mode="backlog")
    knowledge_resolution = resolve_authoring("architecture", project=tmp_path)

    assert issue_resolution.provider == "jira"
    assert "contracts/issue/common.md" in _rel_paths(issue_resolution.files)
    assert "providers/issue/jira/convention.md" in _rel_paths(issue_resolution.files)
    assert knowledge_resolution.provider == "github"
    assert _rel_paths(knowledge_resolution.files) == [
        "contracts/knowledge/body.md",
        "contracts/knowledge/architecture.md",
        "providers/knowledge/github/convention.md",
        "providers/knowledge/github/architecture.md",
    ]


def test_decision_index_resolution_uses_knowledge_files() -> None:
    resolution = resolve_authoring("decision-index", provider="github")

    assert resolution.side == "knowledge"
    assert _rel_paths(resolution.files) == [
        "contracts/knowledge/body.md",
        "contracts/knowledge/decision-index.md",
        "providers/knowledge/github/convention.md",
        "providers/knowledge/github/decision-index.md",
    ]


def test_comment_scope_github_issue_resolution_uses_only_comment_relevant_files() -> None:
    resolution = resolve_authoring("task", side="issue", provider="github", scope="comment")

    assert resolution.side == "issue"
    assert resolution.provider == "github"
    assert _rel_paths(resolution.files) == [
        "providers/issue/github/convention.md",
    ]


def test_comment_scope_jira_issue_resolution_uses_only_comment_relevant_files() -> None:
    resolution = resolve_authoring("task", side="issue", provider="jira", scope="comment")

    assert resolution.side == "issue"
    assert resolution.provider == "jira"
    assert _rel_paths(resolution.files) == [
        "providers/issue/jira/convention.md",
    ]


def test_invalid_provider_for_side_is_rejected() -> None:
    with pytest.raises(ResolverError, match="not valid for role 'knowledge'"):
        resolve_authoring("spec", provider="jira")


def test_require_config_fails_when_missing(tmp_path: Path) -> None:
    with pytest.raises(ResolverError, match=".spectrack/config.yml was not found"):
        resolve_authoring("task", project=tmp_path, require_config=True, mode="backlog")


@pytest.mark.parametrize(
    "artifact_type,side",
    [
        ("bug", None),
        ("spike", None),
        ("review", None),
        ("research", "issue"),
        ("usecase", "issue"),
    ],
)
def test_issue_resolution_excludes_decomposition_patterns(
    artifact_type: str, side: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, side=side, mode=_mode_for(artifact_type))
    assert "contracts/issue/decomposition-patterns.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize("artifact_type", ["task", "epic"])
def test_decomposition_eligible_types_include_decomposition_patterns(
    artifact_type: str,
) -> None:
    resolution = resolve_authoring(artifact_type, mode=_mode_for(artifact_type))
    rels = _rel_paths(resolution.files)
    assert "contracts/issue/decomposition-patterns.md" in rels
    assert rels.index(f"contracts/issue/{artifact_type}.md") < rels.index(
        "contracts/issue/decomposition-patterns.md"
    )


@pytest.mark.parametrize("artifact_type", ["task", "bug", "spike"])
def test_runtime_grounded_types_include_grounding_rule(artifact_type: str) -> None:
    resolution = resolve_authoring(
        artifact_type, side="issue", mode=_mode_for(artifact_type)
    )
    assert "contracts/issue/runtime-grounded-claims.md" in _rel_paths(resolution.files)


@pytest.mark.parametrize(
    "artifact_type,side",
    [
        ("epic", None),
        ("review", None),
        ("research", "issue"),
        ("usecase", "issue"),
    ],
)
def test_non_runtime_grounded_issue_types_exclude_grounding_rule(
    artifact_type: str, side: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, side=side, mode=_mode_for(artifact_type))
    assert "contracts/issue/runtime-grounded-claims.md" not in _rel_paths(
        resolution.files
    )


@pytest.mark.parametrize("artifact_type", ["task", "epic"])
def test_decomposition_patterns_excluded_from_comment_scope(
    artifact_type: str,
) -> None:
    resolution = resolve_authoring(
        artifact_type, side="issue", provider="github", scope="comment"
    )
    assert "contracts/issue/decomposition-patterns.md" not in _rel_paths(resolution.files)


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_task_bug_content_requires_mode(artifact_type: str) -> None:
    with pytest.raises(ResolverError, match="requires --mode"):
        resolve_authoring(artifact_type, side="issue")


@pytest.mark.parametrize(
    "artifact_type,kwargs",
    [
        ("spike", {"side": "issue"}),
        ("epic", {"side": "issue"}),
        ("spec", {"side": "knowledge"}),
        ("task", {"side": "issue", "scope": "comment"}),
        ("task", {"target": "usecase", "side": "issue"}),
    ],
)
def test_mode_rejected_where_it_does_not_apply(
    artifact_type: str, kwargs: dict[str, str]
) -> None:
    # `--target` only validates with `--type review`; route that case through
    # review so the rejection under test is the mode rejection, not the target.
    art = "review" if kwargs.get("target") else artifact_type
    with pytest.raises(ResolverError, match="only applies to task/bug"):
        resolve_authoring(art, mode="backlog", **kwargs)


def test_invalid_mode_is_rejected() -> None:
    with pytest.raises(ResolverError, match="unsupported authoring mode"):
        resolve_authoring("task", side="issue", mode="bogus")


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_backlog_mode_reads_spec_and_backlog_framing(artifact_type: str) -> None:
    resolution = resolve_authoring(
        artifact_type, side="issue", provider="github", mode="backlog"
    )
    rels = _rel_paths(resolution.files)

    # Backlog is the open spec: it reads the type's spec contract plus the
    # backlog framing, with the framing after the contract it frames.
    assert f"contracts/issue/{artifact_type}.md" in rels
    assert "contracts/issue/backlog.md" in rels
    assert rels.index(f"contracts/issue/{artifact_type}.md") < rels.index(
        "contracts/issue/backlog.md"
    )
    # Common rules (incl. body conventions), the runtime-grounded-claim rule,
    # and provider conventions still apply.
    assert "contracts/issue/common.md" in rels
    assert "contracts/issue/runtime-grounded-claims.md" in rels
    assert "providers/issue/github/convention.md" in rels


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_backlog_mode_emits_only_backlog_note(artifact_type: str) -> None:
    resolution = resolve_authoring(
        artifact_type, side="issue", provider="github", mode="backlog"
    )
    assert BACKLOG_TRIGGER_NOTE in resolution.notes
    assert RETROACTIVE_TRIGGER_NOTE not in resolution.notes
    assert RETROACTIVE_PUBLISH_STATE_GITHUB not in resolution.notes


@pytest.mark.parametrize("artifact_type", ["task", "bug"])
def test_retroactive_mode_notes(artifact_type: str) -> None:
    resolution = resolve_authoring(
        artifact_type, side="issue", provider="github", mode="retroactive"
    )
    assert RETROACTIVE_TRIGGER_NOTE in resolution.notes
    assert RETROACTIVE_PUBLISH_STATE_GITHUB in resolution.notes
    assert BACKLOG_TRIGGER_NOTE not in resolution.notes
    # The type spec contract is read; backlog adds its framing on top.
    rels = _rel_paths(resolution.files)
    assert f"contracts/issue/{artifact_type}.md" in rels
    assert "contracts/issue/backlog.md" not in rels


def test_mode_participates_in_cache_key(tmp_path: Path) -> None:
    retroactive = resolve_authoring(
        "task", side="issue", provider="github", mode="retroactive"
    )
    backlog = resolve_authoring("task", side="issue", provider="github", mode="backlog")
    assert retroactive.mode == "retroactive"
    assert backlog.mode == "backlog"
    assert _resolution_key(retroactive) != _resolution_key(backlog)


@pytest.mark.parametrize(
    "artifact_type,side",
    [
        ("spike", None),
        ("epic", None),
        ("review", None),
        ("research", "issue"),
        ("spec", None),
        ("architecture", None),
    ],
)
def test_non_implementation_types_omit_notes(
    artifact_type: str, side: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
    assert resolution.notes == ()


def test_usecase_issue_emits_interview_note() -> None:
    resolution = resolve_authoring("usecase", side="issue")
    assert USECASE_INTERVIEW_NOTE in resolution.notes
    # The note must point the agent at the use-case skill to follow inline.
    assert str(USECASE_SKILL_PATH) in USECASE_INTERVIEW_NOTE


@pytest.mark.parametrize(
    "side,scope",
    [
        ("issue", "comment"),
        ("knowledge", "content"),
    ],
)
def test_usecase_omits_interview_note_off_issue_content_surface(
    side: str, scope: str
) -> None:
    resolution = resolve_authoring("usecase", side=side, scope=scope)
    assert USECASE_INTERVIEW_NOTE not in resolution.notes


def test_non_usecase_omits_interview_note() -> None:
    resolution = resolve_authoring("task", side="issue", mode="backlog")
    assert USECASE_INTERVIEW_NOTE not in resolution.notes


def test_task_comment_scope_omits_notes() -> None:
    resolution = resolve_authoring("task", side="issue", provider="github", scope="comment")
    assert resolution.notes == ()


@pytest.mark.parametrize(
    "artifact_type,side,scope,expected_reading,expected_notes",
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
    side: str,
    scope: str,
    expected_reading: str,
    expected_notes: str | None,
) -> None:
    mode = "backlog" if artifact_type in {"task", "bug"} and scope == "content" else None
    resolution = resolve_authoring(
        artifact_type, side=side, provider="github", scope=scope, mode=mode
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
    resolution = resolve_authoring("task", side="issue", provider="github", mode="backlog")
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
    "artifact_type,side",
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
    artifact_type: str, side: str | None
) -> None:
    resolution = resolve_authoring(artifact_type, side=side)
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
    assert reading_anchor("task", "issue", scope, None) == expected
    assert notes_anchor("task", "issue", scope, None) == expected


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
        resolve_authoring("actors", side="knowledge")


def test_usecase_issue_author_bundles_actors_with_provider() -> None:
    resolution = resolve_authoring(
        "usecase", side="issue", provider="github"
    )
    rels = _rel_paths(resolution.files)

    assert "contracts/issue/usecase.md" in rels
    assert "contracts/knowledge/actors.md" in rels
    assert "providers/knowledge/github/actors.md" in rels
    assert rels.index("contracts/issue/usecase.md") < rels.index(
        "contracts/knowledge/actors.md"
    )


def test_usecase_knowledge_author_bundles_actors_with_provider() -> None:
    resolution = resolve_authoring(
        "usecase", side="knowledge", provider="github"
    )
    rels = _rel_paths(resolution.files)

    assert "contracts/knowledge/usecase.md" in rels
    assert "contracts/knowledge/actors.md" in rels
    assert "providers/knowledge/github/actors.md" in rels


def test_usecase_author_without_provider_omits_provider_actors_file() -> None:
    resolution = resolve_authoring("usecase", side="issue")
    rels = _rel_paths(resolution.files)

    assert "contracts/knowledge/actors.md" in rels
    assert "providers/knowledge/github/actors.md" not in rels


def test_review_target_usecase_issue_bundles_actors_companion() -> None:
    resolution = resolve_authoring(
        "review", target="usecase", side="issue", provider="github"
    )

    assert resolution.target == "usecase"
    assert _rel_paths(resolution.files) == [
        "contracts/quality/usecase-issue-criteria.md",
        "contracts/usecase-abstraction-guard.md",
        "contracts/quality/actors-criteria.md",
        "contracts/issue/common.md",
        "contracts/issue/review.md",
        "providers/issue/github/convention.md",
    ]
    assert resolution.notes == ()


def test_review_target_omits_target_type_authoring_files() -> None:
    resolution = resolve_authoring(
        "review", target="usecase", side="issue", provider="github"
    )
    rels = _rel_paths(resolution.files)

    assert "contracts/usecase.md" not in rels
    assert "contracts/issue/usecase.md" not in rels
    assert "providers/issue/github/usecase.md" not in rels


def test_review_target_anchor_includes_review_suffix() -> None:
    resolution = resolve_authoring(
        "review", target="usecase", side="issue", provider="github"
    )

    assert resolution.reading_anchor == "usecase-issue-review"


def test_review_target_rejects_comment_scope() -> None:
    with pytest.raises(ResolverError, match="--target does not apply to comment scope"):
        resolve_authoring(
            "review", target="usecase", side="issue", scope="comment"
        )


def test_review_target_missing_file_raises() -> None:
    with pytest.raises(ResolverError, match="does not exist"):
        resolve_authoring(
            "review", target="usecase", side="knowledge"
        )


def test_target_requires_type_review() -> None:
    with pytest.raises(ResolverError, match="--target is only valid with --type review"):
        resolve_authoring("task", target="usecase", side="issue")


def test_target_review_value_is_rejected() -> None:
    with pytest.raises(ResolverError, match="--target review is not supported"):
        resolve_authoring("review", target="review", side="issue")


def test_bare_review_returns_authoring_contract_without_review_files() -> None:
    resolution = resolve_authoring(
        "review", side="issue", provider="github"
    )

    assert resolution.target is None
    rels = _rel_paths(resolution.files)
    assert "contracts/issue/common.md" in rels
    assert "contracts/issue/review.md" in rels
    assert "contracts/quality/usecase-issue-criteria.md" not in rels
    assert resolution.reading_anchor == "review-issue"


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
    authoring_file = _PLUGIN_ROOT / "authoring" / "contracts" / "issue" / "task.md"
    outside_file = tmp_path / "task.md"
    outside_file.write_text("# Task\n", encoding="utf-8")

    assert authoring_relative_path(authoring_file, plugin_root=_PLUGIN_ROOT) == (
        "contracts/issue/task.md"
    )
    assert is_authoring_file(authoring_file, plugin_root=_PLUGIN_ROOT)
    assert authoring_relative_path(outside_file, plugin_root=_PLUGIN_ROOT) is None
    assert not is_authoring_file(outside_file, plugin_root=_PLUGIN_ROOT)


_RESOLVER_SESSION_ID = "session-resolver-test"


@pytest.fixture
def resolver_session(monkeypatch: pytest.MonkeyPatch) -> tuple[str, str]:
    monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", _RESOLVER_SESSION_ID)
    monkeypatch.setenv("SPECTRACK_SESSION_ID", _RESOLVER_SESSION_ID)
    monkeypatch.delenv("CODEX_THREAD_ID", raising=False)
    return "claude", _RESOLVER_SESSION_ID


def _resolver_args(
    tmp_path: Path,
    *,
    provider: str = "github",
    artifact: str = "task",
    mode: str | None = None,
) -> list[str]:
    if mode is None and artifact in {"task", "bug"}:
        mode = "backlog"
    args = [
        "--type",
        artifact,
        "--side",
        "issue",
        "--provider",
        provider,
        "--project",
        str(tmp_path),
    ]
    if mode is not None:
        args += ["--mode", mode]
    return args


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
        "side": "issue",
        "provider": "github",
        "scope": "content",
        "target": None,
        "mode": "backlog",
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
    monkeypatch.delenv("SPECTRACK_SESSION_ID", raising=False)

    exit_code = mustread_main(_resolver_args(tmp_path))

    assert exit_code == 0
    out = capsys.readouterr().out
    assert '<reading anchor="task-issue">' in out

    hook_state_dir = tmp_path / ".spectrack-cache" / "hook-state"
    if hook_state_dir.exists():
        assert not list(hook_state_dir.iterdir())
