"""Tests for the prd_path script."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from prd_path import (  # noqa: E402
    COMPONENT_PATHS,
    PrdPathError,
    main,
    normalize_prd_path,
    resolve_all_prd_paths,
    resolve_prd_path,
)


def _config_path(project: Path) -> Path:
    config_dir = project / ".workflow"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "config.yml"


def _write_config(
    project: Path,
    *,
    knowledge_path: str | None = "wiki/workflow",
    prd_path: str | None = None,
) -> None:
    lines = [
        "version: 1",
        "providers:",
        "  issues:",
        "    kind: github",
        "    repo: example/repo",
        "  knowledge:",
        "    kind: github",
    ]
    if knowledge_path is not None:
        lines.append(f"    path: {knowledge_path}")
    if prd_path is not None:
        lines.append(f"    prd_path: {prd_path}")
    _config_path(project).write_text("\n".join(lines) + "\n", encoding="utf-8")


@pytest.mark.parametrize(
    ("component", "expected_relative"),
    [
        ("actors", "usecases/actors.md"),
        ("context", "context.md"),
        ("usecase", "usecases/"),
        ("spec", "specs/"),
        ("nfr", "nfr/"),
        ("domain", "domain/"),
    ],
)
def test_resolve_returns_component_path(
    tmp_path: Path, component: str, expected_relative: str
) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")

    resolution = resolve_prd_path(component, project=tmp_path)

    assert resolution.component == component
    assert resolution.relative == expected_relative
    assert resolution.base == (tmp_path / "wiki/workflow").resolve()


def test_directory_components_end_with_slash(tmp_path: Path) -> None:
    _write_config(tmp_path)
    for component in ("usecase", "spec", "nfr", "domain"):
        resolution = resolve_prd_path(component, project=tmp_path)
        assert resolution.relative.endswith("/")


def test_file_components_do_not_end_with_slash(tmp_path: Path) -> None:
    _write_config(tmp_path)
    for component in ("actors", "context"):
        resolution = resolve_prd_path(component, project=tmp_path)
        assert not resolution.relative.endswith("/")
        assert resolution.relative.endswith(".md")


def test_unknown_component_raises(tmp_path: Path) -> None:
    _write_config(tmp_path)
    with pytest.raises(PrdPathError, match="unknown PRD component"):
        resolve_prd_path("nonsense", project=tmp_path)


def test_missing_knowledge_path_raises(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path=None)
    with pytest.raises(PrdPathError, match="providers.knowledge.path"):
        resolve_prd_path("actors", project=tmp_path)


def test_missing_config_raises(tmp_path: Path) -> None:
    with pytest.raises(PrdPathError, match=".workflow/config.yml was not found"):
        resolve_prd_path("actors", project=tmp_path)


def test_to_markdown_output_shape(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")
    resolution = resolve_prd_path("actors", project=tmp_path)

    output = resolution.to_markdown()

    expected_base = (tmp_path / "wiki/workflow").resolve()
    assert output == (
        f'<prd_path component="actors">\n'
        f"Base: {expected_base}\n"
        f"- usecases/actors.md\n"
        f"</prd_path>\n"
    )


def test_component_paths_coverage() -> None:
    assert set(COMPONENT_PATHS) == {
        "actors",
        "context",
        "usecase",
        "spec",
        "nfr",
        "domain",
    }


def test_prd_path_setting_extends_base(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow", prd_path="prd")

    resolution = resolve_prd_path("actors", project=tmp_path)

    assert resolution.base == (tmp_path / "wiki/workflow/prd").resolve()
    assert resolution.relative == "usecases/actors.md"


def test_empty_prd_path_uses_knowledge_path_root(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow", prd_path="")

    resolution = resolve_prd_path("actors", project=tmp_path)

    assert resolution.base == (tmp_path / "wiki/workflow").resolve()


def test_absolute_prd_path_raises(tmp_path: Path) -> None:
    _write_config(tmp_path, prd_path="/etc/passwd")

    with pytest.raises(PrdPathError, match="relative path"):
        resolve_prd_path("actors", project=tmp_path)


def test_prd_path_with_dotdot_raises(tmp_path: Path) -> None:
    _write_config(tmp_path, prd_path="prd/../escape")

    with pytest.raises(PrdPathError, match="escape"):
        resolve_prd_path("actors", project=tmp_path)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (None, ""),
        ("", ""),
        ("   ", ""),
        ("prd", "prd"),
        ("prd/sub", "prd/sub"),
        ("  prd  ", "prd"),
    ],
)
def test_normalize_prd_path_valid(value: str | None, expected: str) -> None:
    assert normalize_prd_path(value) == expected


@pytest.mark.parametrize(
    "value",
    ["/abs", "/abs/path", "../escape", "prd/../leak", "..", "./../leak"],
)
def test_normalize_prd_path_rejects(value: str) -> None:
    with pytest.raises(PrdPathError):
        normalize_prd_path(value)


def test_resolve_all_returns_every_component_sorted(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")

    listing = resolve_all_prd_paths(project=tmp_path)

    assert listing.base == (tmp_path / "wiki/workflow").resolve()
    assert [name for name, _ in listing.entries] == sorted(COMPONENT_PATHS)
    assert dict(listing.entries) == COMPONENT_PATHS


def test_resolve_all_respects_prd_path_setting(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow", prd_path="prd")

    listing = resolve_all_prd_paths(project=tmp_path)

    assert listing.base == (tmp_path / "wiki/workflow/prd").resolve()


def test_resolve_all_missing_config_raises(tmp_path: Path) -> None:
    with pytest.raises(PrdPathError, match=".workflow/config.yml was not found"):
        resolve_all_prd_paths(project=tmp_path)


def test_resolve_all_to_markdown_shape(tmp_path: Path) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")
    listing = resolve_all_prd_paths(project=tmp_path)

    output = listing.to_markdown()

    expected_base = (tmp_path / "wiki/workflow").resolve()
    expected_lines = ["<prd_path>", f"Base: {expected_base}"]
    for name in sorted(COMPONENT_PATHS):
        expected_lines.append(f"- {name}: {COMPONENT_PATHS[name]}")
    expected_lines.append("</prd_path>")
    assert output == "\n".join(expected_lines) + "\n"


def test_main_list_prints_listing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")

    exit_code = main(["--list", "--project", str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.startswith("<prd_path>\n")
    assert "- actors: usecases/actors.md" in captured.out
    assert captured.out.rstrip().endswith("</prd_path>")
    assert captured.err == ""


def test_main_list_with_component_errors(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")

    with pytest.raises(SystemExit) as exc_info:
        main(["--list", "actors", "--project", str(tmp_path)])

    assert exc_info.value.code == 2
    captured = capsys.readouterr()
    assert "--list cannot be combined" in captured.err


def test_main_without_component_or_list_errors(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")

    with pytest.raises(SystemExit) as exc_info:
        main(["--project", str(tmp_path)])

    assert exc_info.value.code == 2
    captured = capsys.readouterr()
    assert "provide a component name or pass --list" in captured.err


def test_main_single_component_prints_resolution(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    _write_config(tmp_path, knowledge_path="wiki/workflow")

    exit_code = main(["actors", "--project", str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.startswith('<prd_path component="actors">\n')
    assert "- usecases/actors.md" in captured.out
