"""Tests for workflow shell environment helpers."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from workflow_env import (  # noqa: E402
    append_claude_env_file,
    codex_env_file_path,
    codex_env_exports,
    detect_shell_runtime,
    render_path_prepend,
    render_shell_exports,
    write_codex_env_file,
    workflow_project_dir_from_env,
    workflow_session_id_from_env,
)


def test_render_shell_exports_quotes_values() -> None:
    rendered = render_shell_exports(
        {
            "WORKFLOW": "/tmp/plugin root/scripts/workflow",
            "WORKFLOW_PLUGIN_ROOT": "/tmp/plugin root",
            "WORKFLOW_PROJECT_DIR": "/tmp/project",
            "WORKFLOW_SESSION_ID": "session-1",
        }
    )

    assert "export WORKFLOW='/tmp/plugin root/scripts/workflow'" in rendered
    assert "export WORKFLOW_PLUGIN_ROOT='/tmp/plugin root'" in rendered
    assert "export WORKFLOW_PROJECT_DIR=/tmp/project" in rendered
    assert "export WORKFLOW_SESSION_ID=session-1" in rendered


def test_render_path_prepend_quotes_directory_and_is_idempotent(tmp_path: Path) -> None:
    scripts_dir = tmp_path / "plugin with space" / "scripts"
    snippet = render_path_prepend(scripts_dir)

    assert f"__workflow_scripts_dir='{scripts_dir}'" in snippet
    assert "export PATH" in snippet

    probe = (
        f"PATH=/usr/bin\n"
        f"{snippet}"
        f"{snippet}"
        f"printf '%s' \"$PATH\"\n"
    )
    proc = subprocess.run(
        ["sh", "-c", probe],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert proc.stdout == f"{scripts_dir}:/usr/bin"


def test_append_claude_env_file_prepends_scripts_dir_to_path(tmp_path: Path) -> None:
    env_file = tmp_path / "claude.env"

    assert append_claude_env_file(
        env_file=str(env_file),
        project_dir=tmp_path,
        plugin_root=_PLUGIN_ROOT,
        session_id="claude-session-1",
    )

    content = env_file.read_text(encoding="utf-8")
    assert f"export WORKFLOW={_SCRIPTS_DIR / 'workflow'}" in content
    assert f"__workflow_scripts_dir={_SCRIPTS_DIR}" in content

    probe = (
        f"PATH=/usr/bin\n"
        f". {env_file}\n"
        f"printf '%s' \"$PATH\"\n"
    )
    proc = subprocess.run(
        ["sh", "-c", probe],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert proc.stdout == f"{_SCRIPTS_DIR}:/usr/bin"


def test_detect_shell_runtime_uses_exact_session_markers() -> None:
    assert detect_shell_runtime(environ={"CLAUDE_CODE_SHELL": "zsh"}).name == ""
    assert detect_shell_runtime(environ={"CODEX_THREAD_ID": "codex-1"}).name == "codex"
    assert detect_shell_runtime(environ={"CODEX_THREAD_ID": "codex-1"}).session_id == "codex-1"
    assert detect_shell_runtime(environ={"CLAUDE_CODE_SESSION_ID": "claude-1"}).name == "claude"
    assert detect_shell_runtime(environ={"CLAUDE_CODE_SESSION_ID": "claude-1"}).session_id == "claude-1"


def test_detect_shell_runtime_prefers_claude_when_both_markers_exist() -> None:
    runtime = detect_shell_runtime(
        environ={
            "CODEX_THREAD_ID": "codex-1",
            "CLAUDE_CODE_SESSION_ID": "claude-1",
        }
    )

    assert runtime.name == "claude"
    assert runtime.session_id == "claude-1"


def test_workflow_project_and_session_defaults_from_env(tmp_path: Path) -> None:
    assert workflow_project_dir_from_env(environ={"WORKFLOW_PROJECT_DIR": str(tmp_path)}) == tmp_path.resolve()
    assert workflow_session_id_from_env(environ={"WORKFLOW_SESSION_ID": "workflow-1"}) == "workflow-1"


def test_codex_env_file_path_uses_workflow_hook_state(tmp_path: Path) -> None:
    path = codex_env_file_path(tmp_path, "session/with spaces")

    assert path.parent == tmp_path / ".workflow-cache" / "hook-state"
    assert path.name.startswith("workflow-session-codex-session_with_spaces")
    assert path.suffix == ".json"


def test_codex_env_exports_reads_session_state(tmp_path: Path) -> None:
    assert write_codex_env_file(
        project_dir=tmp_path,
        plugin_root=_PLUGIN_ROOT,
        codex_session_id="codex-shell",
        workflow_session_id="parent-shell",
    )

    rendered = codex_env_exports(tmp_path, "codex-shell")

    assert f"export WORKFLOW={_SCRIPTS_DIR / 'workflow'}" in rendered
    assert f"export WORKFLOW_PLUGIN_ROOT={_PLUGIN_ROOT}" in rendered
    assert f"export WORKFLOW_PROJECT_DIR={tmp_path}" in rendered
    assert "export WORKFLOW_SESSION_ID=parent-shell" in rendered
    assert "AUTHORING_RESOLVER" not in rendered


def test_workflow_wrapper_sources_codex_env_file(tmp_path: Path) -> None:
    script = tmp_path / "print_workflow_env.py"
    script.write_text(
        "import json, os\n"
        "print(json.dumps({key: os.environ.get(key) for key in "
        "('WORKFLOW', 'WORKFLOW_PLUGIN_ROOT', 'WORKFLOW_PROJECT_DIR', 'WORKFLOW_SESSION_ID', 'AUTHORING_RESOLVER')}))\n",  # AUTHORING_RESOLVER probed to confirm absence

        encoding="utf-8",
    )
    assert write_codex_env_file(
        project_dir=tmp_path,
        plugin_root=_PLUGIN_ROOT,
        codex_session_id="codex-shell",
        workflow_session_id="parent-shell",
    )

    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), str(script)],
        check=True,
        cwd=tmp_path,
        env={
            "CODEX_THREAD_ID": "codex-shell",
            "PATH": os.environ.get("PATH", ""),
        },
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    payload = json.loads(proc.stdout)
    assert payload["WORKFLOW"] == str(_SCRIPTS_DIR / "workflow")
    assert payload["WORKFLOW_PLUGIN_ROOT"] == str(_PLUGIN_ROOT)
    assert payload["WORKFLOW_PROJECT_DIR"] == str(tmp_path)
    assert payload["WORKFLOW_SESSION_ID"] == "parent-shell"
    assert payload["AUTHORING_RESOLVER"] is None


def test_workflow_wrapper_does_not_use_codex_thread_id_as_session_fallback(tmp_path: Path) -> None:
    script = tmp_path / "print_workflow_session.py"
    script.write_text(
        "import os\n"
        "print(os.environ.get('WORKFLOW_SESSION_ID', '<missing>'))\n",
        encoding="utf-8",
    )

    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), str(script)],
        check=True,
        cwd=tmp_path,
        env={
            "CODEX_THREAD_ID": "codex-subagent-thread",
            "PATH": os.environ.get("PATH", ""),
        },
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert proc.stdout.strip() == "<missing>"


def test_workflow_wrapper_claude_path_does_not_export_session_from_claude_code_session_id(tmp_path: Path) -> None:
    script = tmp_path / "print_workflow_session.py"
    script.write_text(
        "import os\n"
        "print(os.environ.get('WORKFLOW_SESSION_ID', '<missing>'))\n",
        encoding="utf-8",
    )

    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), str(script)],
        check=True,
        cwd=tmp_path,
        env={
            "CLAUDE_CODE_SESSION_ID": "claude-shell-session",
            "PATH": os.environ.get("PATH", ""),
        },
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert proc.stdout.strip() == "<missing>"


def test_workflow_wrapper_prefers_claude_when_both_runtime_markers_exist(tmp_path: Path) -> None:
    script = tmp_path / "print_workflow_session.py"
    script.write_text(
        "import os\n"
        "print(os.environ.get('WORKFLOW_SESSION_ID', '<missing>'))\n",
        encoding="utf-8",
    )
    assert write_codex_env_file(
        project_dir=tmp_path,
        plugin_root=_PLUGIN_ROOT,
        codex_session_id="codex-shell",
        workflow_session_id="codex-parent",
    )

    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), str(script)],
        check=True,
        cwd=tmp_path,
        env={
            "CODEX_THREAD_ID": "codex-shell",
            "CLAUDE_CODE_SESSION_ID": "claude-shell",
            "PATH": os.environ.get("PATH", ""),
        },
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert proc.stdout.strip() == "<missing>"


def test_workflow_wrapper_uses_terminal_defaults_without_runtime_marker(tmp_path: Path) -> None:
    script = tmp_path / "print_terminal_defaults.py"
    script.write_text(
        "import json, os\n"
        "print(json.dumps({key: os.environ.get(key) for key in "
        "('WORKFLOW', 'WORKFLOW_PLUGIN_ROOT', 'WORKFLOW_PROJECT_DIR', 'WORKFLOW_SESSION_ID')}))\n",
        encoding="utf-8",
    )

    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), str(script)],
        check=True,
        cwd=tmp_path,
        env={"PATH": os.environ.get("PATH", "")},
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    payload = json.loads(proc.stdout)
    assert payload["WORKFLOW"] == str(_SCRIPTS_DIR / "workflow")
    assert payload["WORKFLOW_PLUGIN_ROOT"] == str(_PLUGIN_ROOT)
    assert payload["WORKFLOW_PROJECT_DIR"] == str(tmp_path)
    assert payload["WORKFLOW_SESSION_ID"] is None


def test_workflow_wrapper_resolves_bare_name_to_py_script(tmp_path: Path) -> None:
    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), "issue", "--help"],
        check=True,
        cwd=tmp_path,
        env={"PATH": os.environ.get("PATH", "")},
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    assert "usage: issue.py <verb>" in proc.stdout


def test_workflow_wrapper_terminal_defaults_use_launcher_plugin_root(tmp_path: Path) -> None:
    script = tmp_path / "print_terminal_defaults.py"
    script.write_text(
        "import json, os\n"
        "print(json.dumps({key: os.environ.get(key) for key in "
        "('WORKFLOW', 'WORKFLOW_PLUGIN_ROOT', 'WORKFLOW_PROJECT_DIR')}))\n",
        encoding="utf-8",
    )

    proc = subprocess.run(
        [str(_SCRIPTS_DIR / "workflow"), str(script)],
        check=True,
        cwd=tmp_path,
        env={
            "PATH": os.environ.get("PATH", ""),
            "WORKFLOW": "/tmp/stale/workflow",
            "WORKFLOW_PLUGIN_ROOT": "/tmp/stale/plugin",
            "WORKFLOW_PROJECT_DIR": str(tmp_path / "project-from-env"),
        },
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    payload = json.loads(proc.stdout)
    assert payload["WORKFLOW"] == str(_SCRIPTS_DIR / "workflow")
    assert payload["WORKFLOW_PLUGIN_ROOT"] == str(_PLUGIN_ROOT)
    assert payload["WORKFLOW_PROJECT_DIR"] == str(tmp_path / "project-from-env")
