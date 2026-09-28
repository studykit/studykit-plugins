"""Top-level command discovery through the installed-style launcher."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

LAUNCHER = Path(__file__).resolve().parent.parent / "scripts" / "spectrack"


def _config(project: Path, kind: str, site: str | None = None) -> None:
    path = project / ".spectrack" / "config.yml"
    path.parent.mkdir()
    provider = f"    site: {site}\n" if kind == "jira" else "    repo: example/repo\n"
    path.write_text(
        f"version: 1\nproviders:\n  issues:\n    kind: {kind}\n{provider}"
        f"  knowledge:\n    kind: github\nissue_id_format: {'jira' if kind == 'jira' else 'github'}\n",
        encoding="utf-8",
    )


def _run(project: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(LAUNCHER), *args], cwd=project, capture_output=True, text=True,
        env={"PATH": os.environ.get("PATH", "")},
    )


@pytest.mark.parametrize("args", [("--help",), ("help",)])
def test_cloud_help_discovers_agile(tmp_path: Path, args: tuple[str, ...]) -> None:
    _config(tmp_path, "jira", "https://acme.atlassian.net")
    result = _run(tmp_path, *args)
    assert result.returncode == 0, result.stderr
    assert "  agile " in result.stdout
    assert "spectrack <command> --help" in result.stdout


@pytest.mark.parametrize("kind,site", [
    ("github", None), ("jira", "https://jira.example.test"),
])
def test_non_cloud_help_omits_agile(tmp_path: Path, kind: str, site: str | None) -> None:
    _config(tmp_path, kind, site)
    result = _run(tmp_path, "--help")
    assert result.returncode == 0, result.stderr
    assert "  issue " in result.stdout
    assert "  agile " not in result.stdout


def test_help_for_command_routes_to_command_help(tmp_path: Path) -> None:
    _config(tmp_path, "jira", "https://acme.atlassian.net")
    result = _run(tmp_path, "help", "agile")
    assert result.returncode == 0, result.stderr
    assert "{board,sprint,backlog,epic,issue}" in result.stdout
