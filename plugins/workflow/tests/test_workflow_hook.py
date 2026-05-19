"""Tests for workflow SessionStart policy injection."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path
from typing import Any

import pytest

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
_MAIN_CONTEXT_ROOT = _PLUGIN_ROOT / "agents" / "workflow-main-context"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import workflow_hook  # noqa: E402
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_github_issue_cache import GitHubIssueCache  # noqa: E402
from workflow_github import DEFAULT_ISSUE_FIELDS, GitHubRepository  # noqa: E402
from workflow_github_issue_refs import extract_issue_numbers as extract_github_issue_numbers  # noqa: E402
from workflow_jira_issue_refs import jira_issue_keys_from_references  # noqa: E402
from hook_claude import (  # noqa: E402
    ClaudeCommonPayload,
    ClaudePostToolUsePayload,
    ClaudePreToolUsePayload,
)
from hook_claude import ClaudeSessionStartPayload  # noqa: E402
from hook_claude import ClaudeSubagentStartPayload  # noqa: E402
from hook_claude import main as claude_main  # noqa: E402
from hook_claude import parse_claude_event_payload  # noqa: E402
from hook_claude import session_start as claude_session_start  # noqa: E402
from hook_codex import CodexSessionStartPayload  # noqa: E402
from hook_codex import CodexStopPayload, CodexUserPromptSubmitPayload  # noqa: E402
from hook_codex import parse_codex_event_payload  # noqa: E402
from hook_codex import session_start as codex_session_start  # noqa: E402
from hook_codex import stop, user_prompt_submit  # noqa: E402
from workflow_env import codex_env_exports  # noqa: E402
from workflow_session_state import (  # noqa: E402
    legacy_session_env_state_path,
    session_policy_state_path,
    session_state_path,
)


class FakeRunner:
    def __init__(self, responses: dict[tuple[str, ...], CommandResult]):
        self.responses = responses
        self.requests: list[CommandRequest] = []

    def __call__(self, request: CommandRequest) -> CommandResult:
        self.requests.append(request)
        response = self.responses.get(request.args)
        if response is None:
            response = default_github_relationship_response(request)
        if response is None:
            return CommandResult(request=request, returncode=127, stderr="unexpected command")
        return response


def result(args: tuple[str, ...], stdout: str = "", stderr: str = "", returncode: int = 0) -> CommandResult:
    return CommandResult(request=CommandRequest(args=args), returncode=returncode, stdout=stdout, stderr=stderr)


def main_context_fragment(name: str) -> str:
    return (_MAIN_CONTEXT_ROOT / name).read_text(encoding="utf-8").strip()


def expected_session_start_context(
    *,
    runtime: str,
    knowledge_kind: str,
    issue_kind: str = "github",
) -> str:
    text = main_context_fragment("session-policy.md")
    policy_dir = _PLUGIN_ROOT / "agents" / "workflow-main-context" / "policy"
    issue_fetch_block = main_context_fragment(f"snippets/issue-fetch/{issue_kind}.md")
    launcher_block = main_context_fragment(f"snippets/launcher/{runtime}.md")
    if runtime == "codex":
        launcher_block = launcher_block.replace(
            "{{WORKFLOW_PLUGIN_ROOT}}", str(_PLUGIN_ROOT)
        )
    return (
        text
        .replace("{{WORKFLOW_LAUNCHER_BLOCK}}", launcher_block)
        .replace("{{WORKFLOW_ISSUE_FETCH_BLOCK}}", issue_fetch_block)
        .replace("{{WORKFLOW_POLICY_DIR}}", str(policy_dir))
        .replace("{{WORKFLOW_ISSUE_PROVIDER}}", issue_kind)
        .replace("{{WORKFLOW_KNOWLEDGE_PROVIDER}}", knowledge_kind)
    )


def default_github_relationship_response(request: CommandRequest) -> CommandResult | None:
    args = request.args
    if len(args) < 3 or args[:2] != ("gh", "api"):
        return None

    path = args[2]
    prefix = "repos/studykit/studykit-plugins/issues/"
    if not path.startswith(prefix):
        return None

    suffix = path.removeprefix(prefix)
    issue_number = suffix.split("/", 1)[0]
    try:
        issue_id = int(issue_number) * 1000
    except ValueError:
        return None

    if suffix == issue_number:
        return CommandResult(
            request=request,
            returncode=0,
            stdout=json.dumps(
                {
                    "id": issue_id,
                    "number": int(issue_number),
                    "title": f"Issue {issue_number}",
                    "state": "open",
                    "state_reason": None,
                    "updated_at": "2026-05-14T00:00:00Z",
                }
            ),
        )

    if suffix == f"{issue_number}/parent":
        return CommandResult(request=request, returncode=404, stderr="not found")

    if args[3:] == ("--paginate",) and suffix in {
        f"{issue_number}/sub_issues",
        f"{issue_number}/dependencies/blocked_by",
        f"{issue_number}/dependencies/blocking",
    }:
        return CommandResult(request=request, returncode=0, stdout="[]")

    return None


def _json_object(output: str) -> dict[str, Any]:
    parsed = json.loads(output)
    assert isinstance(parsed, dict)
    return parsed


def gh_issue_view_args(issue: int | str) -> tuple[str, ...]:
    return (
        "gh",
        "issue",
        "view",
        str(issue),
        "--repo",
        "studykit/studykit-plugins",
        "--json",
        ",".join(DEFAULT_ISSUE_FIELDS),
    )


def gh_api_args(*args: str) -> tuple[str, ...]:
    return ("gh", "api", *args)


def empty_relationship_read_args(issue: int | str) -> list[tuple[str, ...]]:
    base = f"repos/studykit/studykit-plugins/issues/{issue}"
    return [
        gh_api_args(base),
        gh_api_args(f"{base}/parent"),
        gh_api_args(f"{base}/sub_issues", "--paginate"),
        gh_api_args(f"{base}/dependencies/blocked_by", "--paginate"),
        gh_api_args(f"{base}/dependencies/blocking", "--paginate"),
    ]


def issue_payload(number: int, *, title: str = "Implement workflow hook cache context") -> dict[str, Any]:
    return {
        "number": number,
        "title": title,
        "state": "OPEN",
        "stateReason": None,
        "body": "Issue body.",
        "labels": [{"name": "workflow"}],
        "updatedAt": "2026-05-14T00:00:00Z",
        "comments": [],
    }


def _write_config(project: Path) -> None:
    config_path = project / ".workflow" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: github
    repo: studykit/studykit-plugins
  knowledge:
    kind: github
    path: wiki/workflow
issue_id_format: github
commit_refs:
  enabled: true
  style: provider-native
""".lstrip(),
        encoding="utf-8",
    )


def _write_filesystem_config(project: Path) -> None:
    config_path = project / ".workflow" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: filesystem
    path: workflow/issues
  knowledge:
    kind: filesystem
    path: workflow/knowledge
issue_id_format: number
commit_refs:
  enabled: false
""".lstrip(),
        encoding="utf-8",
    )


def _write_jira_config(project: Path) -> None:
    config_path = project / ".workflow" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: jira
    site: https://jira.example.test
    deployment: data-center
    api_version: 2
    project: TEST
    issue_type: Task
  knowledge:
    kind: github
issue_id_format: jira
commit_refs:
  enabled: true
  style: provider-native
""".lstrip(),
        encoding="utf-8",
    )


def jira_issue_payload(*, title: str = "Support Jira Data Center hooks") -> dict[str, Any]:
    return {
        "id": "10001",
        "key": "TEST-1234",
        "fields": {
            "summary": title,
            "description": "Jira hook body.",
            "labels": ["workflow", "jira"],
            "created": "2026-05-15T09:00:00.000+0900",
            "updated": "2026-05-15T10:00:00.000+0900",
            "status": {"name": "In Progress", "statusCategory": {"key": "indeterminate"}},
            "comment": {"comments": []},
            "issuelinks": [],
        },
    }


def curl_args(url: str) -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)


def jira_issue_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}"


def jira_remote_links_url(issue: str = "TEST-1234") -> str:
    return f"https://jira.example.test/rest/api/2/issue/{issue}/remotelink"


def _run_session_start(
    project: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    runtime: str,
    payload_update: dict[str, Any] | None = None,
) -> str:
    payload = {
        "session_id": f"{runtime}-session",
        "cwd": str(project),
        "hook_event_name": "SessionStart",
        "source": "startup",
    }
    if runtime == "codex":
        payload["turn_id"] = "turn-1"
        monkeypatch.setenv("PLUGIN_ROOT", str(_PLUGIN_ROOT))
        monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
        monkeypatch.delenv("CLAUDE_PLUGIN_ROOT", raising=False)
    else:
        monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(project))
        monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))
        monkeypatch.delenv("PLUGIN_ROOT", raising=False)

    if payload_update:
        payload.update(payload_update)

    captured = io.StringIO()
    if runtime == "codex":
        codex_event = parse_codex_event_payload(payload)
        assert isinstance(codex_event, CodexSessionStartPayload)
        assert codex_session_start(codex_event, stdout=captured) == 0
    else:
        event_payload = parse_claude_event_payload(payload)
        assert isinstance(event_payload, ClaudeSessionStartPayload)
        assert claude_session_start(event_payload, stdout=captured) == 0
    return captured.getvalue()


def _write_subagent_transcript(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "type": "session_meta",
                "payload": {
                    "thread_source": "subagent",
                    "source": {
                        "subagent": {
                            "thread_spawn": {
                                "parent_thread_id": "parent-thread",
                                "agent_role": "default",
                            }
                        }
                    },
                    "agent_role": "default",
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )


@pytest.mark.parametrize("runtime", ["claude", "codex"])
def test_session_start_emits_nothing_without_workflow_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    runtime: str,
) -> None:
    out = _run_session_start(tmp_path, monkeypatch, runtime=runtime)

    assert out == ""


@pytest.mark.parametrize("runtime", ["claude", "codex"])
def test_session_start_injects_policy_once_per_session_except_clear(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    runtime: str,
) -> None:
    _write_config(tmp_path)

    first = _run_session_start(tmp_path, monkeypatch, runtime=runtime)
    second = _run_session_start(tmp_path, monkeypatch, runtime=runtime)
    clear = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime=runtime,
        payload_update={"source": "clear"},
    )
    after_clear = _run_session_start(tmp_path, monkeypatch, runtime=runtime)
    third = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime=runtime,
        payload_update={"session_id": f"{runtime}-session-2", "turn_id": "turn-2"},
    )

    assert first
    assert second == ""
    assert clear
    assert after_clear == ""
    assert third


def test_session_start_policy_state_is_runtime_scoped(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)

    claude_first = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"session_id": "shared-session"},
    )
    codex_first = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"session_id": "shared-session"},
    )
    claude_second = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"session_id": "shared-session"},
    )
    codex_second = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"session_id": "shared-session"},
    )

    assert claude_first
    assert codex_first
    assert claude_second == ""
    assert codex_second == ""


def test_session_start_ignores_claude_compact_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)

    compact = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"source": "compact"},
    )
    startup = _run_session_start(tmp_path, monkeypatch, runtime="claude")

    assert compact == ""
    assert startup


def test_claude_entrypoint_owns_runtime_for_codex_shaped_payload(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))
    monkeypatch.delenv("PLUGIN_ROOT", raising=False)

    captured = io.StringIO()
    event_payload = parse_claude_event_payload(
        {
            "session_id": "claude-session",
            "turn_id": "codex-shaped-turn",
            "cwd": str(tmp_path),
            "hook_event_name": "SessionStart",
            "source": "compact",
        }
    )
    assert isinstance(event_payload, ClaudeSessionStartPayload)
    assert claude_session_start(event_payload, stdout=captured) == 0

    assert captured.getvalue() == ""


def test_claude_main_dispatches_from_payload_event_name(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))
    monkeypatch.delenv("PLUGIN_ROOT", raising=False)

    captured = io.StringIO()
    assert claude_main(
        ["legacy-subcommand-ignored"],
        payload={
            "session_id": "claude-main-dispatch",
            "cwd": str(tmp_path),
            "hook_event_name": "SessionStart",
            "source": "startup",
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    assert payload["hookSpecificOutput"]["hookEventName"] == "SessionStart"


def test_claude_post_read_records_authoring_file_reads_in_session_state(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path, runtime="claude")
    authoring_file = _PLUGIN_ROOT / "authoring" / "common" / "task-authoring.md"
    payload = {
        "session_id": "claude-authoring-read",
        "cwd": str(tmp_path),
        "permission_mode": "default",
        "hook_event_name": "PostToolUse",
        "tool_name": "Read",
        "tool_input": {"file_path": str(authoring_file)},
        "tool_response": {"filePath": str(authoring_file)},
        "tool_use_id": "toolu_read",
        "duration_ms": 12,
    }

    captured = io.StringIO()
    assert claude_main(payload=payload, stdout=captured) == 0
    assert claude_main(payload=payload, stdout=captured) == 0

    assert captured.getvalue() == ""
    state_file = session_state_path(tmp_path, "claude", "claude-authoring-read")
    assert state_file is not None
    state = json.loads(state_file.read_text(encoding="utf-8"))
    assert state["authoring"]["read_files"] == [
        {
            "path": str(authoring_file.resolve()),
            "relative_path": "common/task-authoring.md",
        }
    ]


def test_claude_pre_read_notifies_when_authoring_file_was_already_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path, runtime="claude")
    authoring_file = _PLUGIN_ROOT / "authoring" / "common" / "task-authoring.md"
    post_payload = {
        "session_id": "claude-authoring-reread",
        "cwd": str(tmp_path),
        "hook_event_name": "PostToolUse",
        "tool_name": "Read",
        "tool_input": {"file_path": str(authoring_file)},
        "tool_response": {"filePath": str(authoring_file)},
    }
    pre_payload = {
        **post_payload,
        "hook_event_name": "PreToolUse",
    }

    assert claude_main(payload=post_payload, stdout=io.StringIO()) == 0
    captured = io.StringIO()
    assert claude_main(payload=pre_payload, stdout=captured) == 0

    payload = json.loads(captured.getvalue())
    hook_output = payload["hookSpecificOutput"]
    assert hook_output["hookEventName"] == "PreToolUse"
    assert hook_output["additionalContext"] == (
        "Workflow authoring file already read in this session: "
        "`common/task-authoring.md`."
    )


def test_claude_pre_read_emits_nothing_for_first_authoring_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path, runtime="claude")
    authoring_file = _PLUGIN_ROOT / "authoring" / "common" / "task-authoring.md"

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "claude-authoring-first-read",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Read",
            "tool_input": {"file_path": str(authoring_file)},
        },
        stdout=captured,
    ) == 0

    assert captured.getvalue() == ""


def test_claude_post_read_skips_non_authoring_reads(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path, runtime="claude")
    readme = tmp_path / "README.md"
    readme.write_text("# Project\n", encoding="utf-8")

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "claude-non-authoring-read",
            "cwd": str(tmp_path),
            "hook_event_name": "PostToolUse",
            "tool_name": "Read",
            "tool_input": {"file_path": str(readme)},
        },
        stdout=captured,
    ) == 0

    assert captured.getvalue() == ""
    state_file = session_state_path(tmp_path, "claude", "claude-non-authoring-read")
    assert state_file is not None
    assert not state_file.exists()


def test_claude_post_read_skips_subagent_authoring_reads(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path, runtime="claude")
    authoring_file = _PLUGIN_ROOT / "authoring" / "common" / "task-authoring.md"

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "claude-subagent-authoring-read",
            "cwd": str(tmp_path),
            "hook_event_name": "PostToolUse",
            "agent_type": "workflow-operator",
            "tool_name": "Read",
            "tool_input": {"file_path": str(authoring_file)},
        },
        stdout=captured,
    ) == 0

    assert captured.getvalue() == ""
    state_file = session_state_path(tmp_path, "claude", "claude-subagent-authoring-read")
    assert state_file is not None
    assert not state_file.exists()


def test_parse_claude_event_payload_builds_event_structures(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    session_event = parse_claude_event_payload(
        {
            "session_id": "s1",
            "cwd": str(tmp_path),
            "hook_event_name": "SessionStart",
            "source": "startup",
            "model": "claude-sonnet-4-6",
        }
    )
    assert isinstance(session_event, ClaudeSessionStartPayload)
    assert isinstance(session_event, ClaudeCommonPayload)
    assert session_event.session_id == "s1"
    assert session_event.cwd == str(tmp_path)
    assert session_event.hook_event_name == "SessionStart"
    assert session_event.agent_type is None
    assert not hasattr(session_event, "permission_mode")
    assert not hasattr(session_event, "effort")
    assert not hasattr(session_event, "agent_id")
    assert session_event.source == "startup"
    assert session_event.model == "claude-sonnet-4-6"

    subagent_event = parse_claude_event_payload(
        {
            "session_id": "s1",
            "transcript_path": "/tmp/transcript.jsonl",
            "cwd": str(tmp_path),
            "hook_event_name": "SubagentStart",
            "agent_id": "agent-123",
            "agent_type": "workflow-operator",
        }
    )
    assert isinstance(subagent_event, ClaudeSubagentStartPayload)
    assert subagent_event.hook_event_name == "SubagentStart"
    assert subagent_event.agent_id == "agent-123"
    assert subagent_event.agent_type == "workflow-operator"
    assert not hasattr(subagent_event, "model")

    tool_event = parse_claude_event_payload(
        {
            "session_id": "s1",
            "cwd": str(tmp_path),
            "permission_mode": "default",
            "effort": {"level": "medium"},
            "hook_event_name": "PreToolUse",
            "tool_name": "Write",
            "tool_input": {"file_path": "workflow/task.md", "content": "body"},
            "tool_use_id": "toolu_123",
        }
    )
    assert isinstance(tool_event, ClaudePreToolUsePayload)
    assert tool_event.hook_event_name == "PreToolUse"
    assert tool_event.permission_mode == "default"
    assert tool_event.effort == {"level": "medium"}
    assert tool_event.tool_name == "Write"
    assert tool_event.tool_input == {"file_path": "workflow/task.md", "content": "body"}
    assert tool_event.tool_use_id == "toolu_123"
    assert not hasattr(tool_event, "edit_targets")

    post_tool_event = parse_claude_event_payload(
        {
            "session_id": "s1",
            "cwd": str(tmp_path),
            "permission_mode": "default",
            "effort": {"level": "medium"},
            "hook_event_name": "PostToolUse",
            "tool_name": "Read",
            "tool_input": {
                "file_path": "plugins/workflow/authoring/common/task-authoring.md"
            },
            "tool_response": {
                "filePath": "plugins/workflow/authoring/common/task-authoring.md"
            },
            "tool_use_id": "toolu_456",
            "duration_ms": 9,
        }
    )
    assert isinstance(post_tool_event, ClaudePostToolUsePayload)
    assert post_tool_event.hook_event_name == "PostToolUse"
    assert post_tool_event.permission_mode == "default"
    assert post_tool_event.effort == {"level": "medium"}
    assert post_tool_event.tool_name == "Read"
    assert post_tool_event.tool_input == {
        "file_path": "plugins/workflow/authoring/common/task-authoring.md"
    }
    assert post_tool_event.tool_response == {
        "filePath": "plugins/workflow/authoring/common/task-authoring.md"
    }
    assert post_tool_event.tool_use_id == "toolu_456"
    assert post_tool_event.duration_ms == 9


def test_session_start_clear_uses_documented_source_only(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)

    first = _run_session_start(tmp_path, monkeypatch, runtime="codex")
    alias_clear = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"source": "", "matcher": "clear", "session_start_source": "clear"},
    )
    source_clear = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"source": "clear"},
    )

    assert first
    assert alias_clear == ""
    assert source_clear


@pytest.mark.parametrize(
    "payload_update",
    [
        {"source": "agent"},
        {"subagent_type": "workflow-operator"},
        {"parent_session_id": "parent-session"},
    ],
)
def test_codex_session_start_emits_nothing_for_agent_sessions(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    payload_update: dict[str, Any],
) -> None:
    _write_config(tmp_path)

    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update=payload_update,
    )

    assert out == ""


@pytest.mark.parametrize(
    "payload_update",
    [
        {"agent_type": "workflow-operator"},
    ],
)
def test_claude_session_start_emits_nothing_for_agent_sessions(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    payload_update: dict[str, Any],
) -> None:
    _write_config(tmp_path)

    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update=payload_update,
    )

    assert out == ""


def test_session_start_emits_nothing_for_codex_subagent_transcript(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    transcript_path = tmp_path / "subagent-rollout.jsonl"
    _write_subagent_transcript(transcript_path)

    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"source": "startup", "transcript_path": str(transcript_path)},
    )

    assert out == ""


def test_session_start_transcript_agent_metadata_is_codex_only(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    transcript_path = tmp_path / "subagent-rollout.jsonl"
    _write_subagent_transcript(transcript_path)

    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"transcript_path": str(transcript_path)},
    )

    assert out != ""


def test_extract_issue_numbers_respects_issue_id_format() -> None:
    repo = GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")
    text = (
        "Review #45, issue 47, studykit/studykit-plugins#48, "
        "other/repo#49, https://github.com/studykit/studykit-plugins/issues/50, "
        "and Jira keys test-1234 plus TEST-1235."
    )

    assert extract_github_issue_numbers(text, repo=repo) == ["45", "48", "50"]
    assert jira_issue_keys_from_references([text]) == ["TEST-1234", "TEST-1235"]


def _hook_env(
    monkeypatch: pytest.MonkeyPatch,
    project: Path,
    *,
    runtime: str = "codex",
) -> None:
    if runtime == "codex":
        monkeypatch.setenv("PLUGIN_ROOT", str(_PLUGIN_ROOT))
        monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
        monkeypatch.delenv("CLAUDE_PLUGIN_ROOT", raising=False)
    else:
        monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(project))
        monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))
        monkeypatch.delenv("PLUGIN_ROOT", raising=False)


@pytest.mark.parametrize("runtime", ["claude", "codex"])
def test_session_start_injects_policy_for_configured_project(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    runtime: str,
) -> None:
    _write_config(tmp_path)

    out = _run_session_start(tmp_path, monkeypatch, runtime=runtime)

    payload = json.loads(out)
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert payload["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert context == expected_session_start_context(
        runtime=runtime, knowledge_kind="github", issue_kind="github"
    )
    policy_dir = _PLUGIN_ROOT / "agents" / "workflow-main-context" / "policy"
    assert "## workflow policy" in context
    if runtime == "claude":
        assert "\"$WORKFLOW\" <script>.py" in context
    else:
        assert f"\"{_PLUGIN_ROOT}/scripts/workflow\" <script>.py" in context
        assert "{{WORKFLOW_PLUGIN_ROOT}}" not in context
    assert "read-only" in context
    assert str(policy_dir / "authoring.md") in context
    assert str(policy_dir / "provider-writes" / "github.md") in context
    assert str(policy_dir / "knowledge" / "github.md") in context
    assert "{{WORKFLOW_POLICY_DIR}}" not in context
    assert "{{WORKFLOW_LAUNCHER_BLOCK}}" not in context
    assert "{{WORKFLOW_ISSUE_FETCH_BLOCK}}" not in context
    assert "{{WORKFLOW_ISSUE_PROVIDER}}" not in context
    assert "{{WORKFLOW_KNOWLEDGE_PROVIDER}}" not in context
    assert "provider-writes/jira.md" not in context
    assert "provider-writes/filesystem.md" not in context
    assert "workflow-operator" not in context
    assert "Delegate workflow operations" not in context
    assert "codex-operator-reuse" not in context
    assert "from_cache" not in context
    assert "comments-pending" not in context


def test_claude_session_start_appends_workflow_env_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    env_file = tmp_path / "claude.env"
    monkeypatch.setenv("CLAUDE_ENV_FILE", str(env_file))

    _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"session_id": "claude-shell-session"},
    )

    content = env_file.read_text(encoding="utf-8")
    assert f"export WORKFLOW={_PLUGIN_ROOT / 'scripts' / 'workflow'}" in content
    assert f"export WORKFLOW_PLUGIN_ROOT={_PLUGIN_ROOT}" in content
    assert f"export WORKFLOW_PROJECT_DIR={tmp_path}" in content
    assert "export WORKFLOW_SESSION_ID=claude-shell-session" in content
    assert "AUTHORING_RESOLVER" not in content


def test_codex_session_start_writes_session_export_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)

    _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"session_id": "codex-shell-session"},
    )

    content = codex_env_exports(tmp_path, "codex-shell-session")
    assert f"export WORKFLOW={_PLUGIN_ROOT / 'scripts' / 'workflow'}" in content
    assert f"export WORKFLOW_PLUGIN_ROOT={_PLUGIN_ROOT}" in content
    assert f"export WORKFLOW_PROJECT_DIR={tmp_path}" in content
    assert "export WORKFLOW_SESSION_ID=codex-shell-session" in content
    assert "AUTHORING_RESOLVER" not in content


def test_codex_hook_state_uses_single_file_per_session(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    session_id = "codex-clean-session"

    _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"session_id": session_id},
    )
    event_payload = parse_codex_event_payload(
        {
            "session_id": session_id,
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "커밋 전에 #45 확인",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(
        event_payload,
        stdout=io.StringIO(),
        runner=FakeRunner(
            {
                gh_issue_view_args(45): result(
                    gh_issue_view_args(45),
                    stdout=json.dumps(issue_payload(45)),
                )
            }
        ),
    ) == 0

    state_file = session_state_path(tmp_path, "codex", session_id)
    assert state_file is not None
    session_files = sorted(path.name for path in state_file.parent.glob(f"*{session_id}*"))
    assert session_files == [state_file.name]

    state = json.loads(state_file.read_text(encoding="utf-8"))
    assert state["env"]["WORKFLOW_SESSION_ID"] == session_id
    assert state["flags"]["session_policy"] is True
    assert state["flags"]["commit_prefix"] is True
    assert state["issues"]["announced"] == ["45"]


def test_codex_session_start_migrates_legacy_split_state(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    session_id = "codex-legacy-session"
    legacy_env = legacy_session_env_state_path(tmp_path, "codex", session_id)
    legacy_policy = session_policy_state_path(tmp_path, "codex", session_id)
    assert legacy_env is not None
    assert legacy_policy is not None
    legacy_env.parent.mkdir(parents=True)
    legacy_env.write_text("export WORKFLOW_SESSION_ID=old-session\n", encoding="utf-8")
    legacy_policy.write_text("announced\n", encoding="utf-8")

    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"session_id": session_id},
    )

    assert out == ""
    assert not legacy_env.exists()
    assert not legacy_policy.exists()
    state_file = session_state_path(tmp_path, "codex", session_id)
    assert state_file is not None
    assert sorted(path.name for path in state_file.parent.glob(f"*{session_id}*")) == [state_file.name]

    state = json.loads(state_file.read_text(encoding="utf-8"))
    assert state["env"]["WORKFLOW_SESSION_ID"] == session_id
    assert state["flags"]["session_policy"] is True


@pytest.mark.parametrize("runtime", ["claude", "codex"])
def test_session_start_uses_filesystem_issue_policy_for_local_artifacts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    runtime: str,
) -> None:
    _write_filesystem_config(tmp_path)

    out = _run_session_start(tmp_path, monkeypatch, runtime=runtime)

    payload = json.loads(out)
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert context == expected_session_start_context(
        runtime=runtime, knowledge_kind="filesystem", issue_kind="filesystem"
    )
    policy_dir = _PLUGIN_ROOT / "agents" / "workflow-main-context" / "policy"
    assert str(policy_dir / "provider-writes" / "filesystem.md") in context
    assert str(policy_dir / "knowledge" / "filesystem.md") in context
    assert "provider-writes/github.md" not in context
    assert "provider-writes/jira.md" not in context
    assert "knowledge/github.md" not in context


def test_session_start_discovers_config_from_nested_project_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    nested = tmp_path / "src" / "feature"
    nested.mkdir(parents=True)

    out = _run_session_start(nested, monkeypatch, runtime="codex")

    payload = json.loads(out)
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert "## workflow policy" in context
    assert f"\"{_PLUGIN_ROOT}/scripts/workflow\" <script>.py" in context


def test_non_empty_hook_stdout_is_json_only(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)

    codex_session = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"session_id": "codex-json-session"},
    )
    claude_session = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"session_id": "claude-json-session"},
    )

    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner(
        {
            gh_issue_view_args(45): result(
                gh_issue_view_args(45),
                stdout=json.dumps(issue_payload(45)),
            )
        }
    )
    user_prompt_output = io.StringIO()
    user_prompt_event = parse_codex_event_payload(
        {
            "session_id": "codex-json-prompt",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "Inspect #45.",
        },
    )
    assert isinstance(user_prompt_event, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(
        user_prompt_event,
        stdout=user_prompt_output,
        runner=runner,
    ) == 0

    outputs = [
        codex_session,
        claude_session,
        user_prompt_output.getvalue(),
    ]
    for output in outputs:
        assert output
        _json_object(output)


def test_session_start_records_codex_subagent_identity_and_emits_nothing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    transcript = tmp_path / "subagent-rollout.jsonl"
    _write_subagent_transcript(transcript)

    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="codex",
        payload_update={"source": "startup", "transcript_path": str(transcript)},
    )

    assert out == ""
    parent_state = session_state_path(tmp_path, "codex", "parent-thread")
    assert parent_state is not None
    parent_state_payload = json.loads(parent_state.read_text(encoding="utf-8"))
    assert parent_state_payload["subagents"]["started"] == [
        {"agent_id": "codex-session", "agent_type": "default"}
    ]
    subagent_state = session_state_path(tmp_path, "codex", "codex-session")
    assert subagent_state is not None
    assert not subagent_state.exists()


def test_session_start_uses_jira_provider_writes_pointer_for_jira_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_jira_config(tmp_path)

    out = _run_session_start(tmp_path, monkeypatch, runtime="codex")

    payload = json.loads(out)
    context = payload["hookSpecificOutput"]["additionalContext"]
    policy_dir = _PLUGIN_ROOT / "agents" / "workflow-main-context" / "policy"
    assert str(policy_dir / "provider-writes" / "jira.md") in context
    assert "provider-writes/github.md" not in context
    assert "provider-writes/filesystem.md" not in context


def test_session_start_skips_claude_subagent_payload(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Claude subagent SessionStart persists env but injects no policy."""

    _write_config(tmp_path)
    env_file = tmp_path / "claude.env"
    monkeypatch.setenv("CLAUDE_ENV_FILE", str(env_file))
    out = _run_session_start(
        tmp_path,
        monkeypatch,
        runtime="claude",
        payload_update={"agent_type": "general-purpose", "session_id": "claude-subagent-session"},
    )

    assert out == ""
    content = env_file.read_text(encoding="utf-8")
    assert f"export WORKFLOW={_PLUGIN_ROOT / 'scripts' / 'workflow'}" in content
    assert "export WORKFLOW_SESSION_ID=claude-subagent-session" in content
    assert "AUTHORING_RESOLVER" not in content


def test_claude_subagent_start_records_subagent_identity_and_emits_nothing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "claude-session",
            "transcript_path": "/tmp/transcript.jsonl",
            "cwd": str(tmp_path),
            "hook_event_name": "SubagentStart",
            "agent_id": "agent-123",
            "agent_type": "general-purpose",
        },
        stdout=captured,
    ) == 0

    assert captured.getvalue() == ""
    state_file = session_state_path(tmp_path, "claude", "claude-session")
    assert state_file is not None
    state = json.loads(state_file.read_text(encoding="utf-8"))
    assert state["subagents"]["started"] == [
        {"agent_id": "agent-123", "agent_type": "general-purpose"}
    ]


def test_claude_subagent_start_deduplicates_agent_identity_records(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    payload = {
        "session_id": "claude-session",
        "transcript_path": "/tmp/transcript.jsonl",
        "cwd": str(tmp_path),
        "hook_event_name": "SubagentStart",
        "agent_id": "agent-123",
        "agent_type": "general-purpose",
    }

    assert claude_main(payload=payload, stdout=io.StringIO()) == 0
    assert claude_main(payload=payload, stdout=io.StringIO()) == 0
    assert claude_main(
        payload={**payload, "agent_id": "agent-456", "agent_type": "Plan"},
        stdout=io.StringIO(),
    ) == 0

    state_file = session_state_path(tmp_path, "claude", "claude-session")
    assert state_file is not None
    state = json.loads(state_file.read_text(encoding="utf-8"))
    assert state["subagents"]["started"] == [
        {"agent_id": "agent-123", "agent_type": "general-purpose"},
        {"agent_id": "agent-456", "agent_type": "Plan"},
    ]


def test_static_claude_manifest_registers_global_subagent_start_hook() -> None:
    manifest = json.loads((_PLUGIN_ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8"))

    assert "SubagentStart" in manifest["hooks"]
    assert "matcher" not in manifest["hooks"]["SubagentStart"][0]
    assert manifest["hooks"]["SubagentStart"][0]["hooks"][0]["command"] == (
        'uv run --script "${CLAUDE_PLUGIN_ROOT}/scripts/hook_claude.py"'
    )


def test_static_claude_manifest_does_not_register_stop_hook() -> None:
    manifest = json.loads((_PLUGIN_ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8"))

    assert "Stop" not in manifest["hooks"]
    assert "Stop" not in manifest["description"]


def test_static_codex_manifest_does_not_register_stop_hook() -> None:
    manifest = json.loads(
        (_PLUGIN_ROOT / "hooks" / "hooks.codex.json").read_text(encoding="utf-8")
    )

    assert {"SessionStart", "UserPromptSubmit"}.issubset(manifest["hooks"])
    assert "Stop" not in manifest["hooks"]
    assert "Stop" not in manifest["description"]


def test_user_prompt_caches_issue_and_injects_project_relative_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner(
        {
            gh_issue_view_args(45): result(
                gh_issue_view_args(45),
                stdout=json.dumps(issue_payload(45, title="Write-back freshness checks")),
            )
        }
    )

    captured = io.StringIO()
    event_payload = parse_codex_event_payload(
        {
            "session_id": "s1",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "#45 작업 내용 확인",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=runner) == 0

    payload = json.loads(captured.getvalue())
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert payload["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
    assert "- #45 → `.workflow-cache/issues/45/issue.md` (refreshed)" in context
    assert "open" not in context
    assert "Write-back freshness checks" not in context
    assert (
        tmp_path
        / ".workflow-cache"
        / "issues"
        / "45"
        / "issue.md"
    ).is_file()


def test_user_prompt_injects_github_commit_prefix_hint_without_issue_fetch(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner({})

    raw_payload = {
        "session_id": "commit-s1",
        "turn_id": "turn-1",
        "cwd": str(tmp_path),
        "hook_event_name": "UserPromptSubmit",
        "prompt": "Please commit the staged workflow changes.",
    }
    captured = io.StringIO()
    event_payload = parse_codex_event_payload(raw_payload)
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=runner) == 0

    payload = json.loads(captured.getvalue())
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert context == main_context_fragment("commit-prefix.md")

    repeated = io.StringIO()
    repeated_event = parse_codex_event_payload(raw_payload)
    assert isinstance(repeated_event, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(repeated_event, stdout=repeated, runner=runner) == 0

    assert repeated.getvalue() == ""
    assert runner.requests == []


def test_user_prompt_emits_nothing_for_codex_subagent_payload_marker(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner(
        {
            gh_issue_view_args(45): result(
                gh_issue_view_args(45),
                stdout=json.dumps(issue_payload(45)),
            )
        }
    )

    captured = io.StringIO()
    event_payload = parse_codex_event_payload(
        {
            "session_id": "subagent-prompt-s1",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "parent_session_id": "parent-session",
            "prompt": "Please inspect #45 and commit.",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=runner) == 0

    assert captured.getvalue() == ""
    assert runner.requests == []


def test_user_prompt_emits_nothing_for_codex_subagent_transcript(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    transcript_path = tmp_path / "subagent-rollout.jsonl"
    _write_subagent_transcript(transcript_path)
    runner = FakeRunner(
        {
            gh_issue_view_args(45): result(
                gh_issue_view_args(45),
                stdout=json.dumps(issue_payload(45)),
            )
        }
    )

    captured = io.StringIO()
    event_payload = parse_codex_event_payload(
        {
            "session_id": "subagent-prompt-s2",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "transcript_path": str(transcript_path),
            "prompt": "Please inspect #45 and commit.",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=runner) == 0

    assert captured.getvalue() == ""
    assert runner.requests == []


def test_user_prompt_caches_jira_issue_and_injects_snapshot_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_jira_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner(
        {
            curl_args(jira_issue_url()): result(
                curl_args(jira_issue_url()),
                stdout=json.dumps(jira_issue_payload(title="Jira hook cache context")),
            ),
            curl_args(jira_remote_links_url()): result(
                curl_args(jira_remote_links_url()),
                stdout="[]",
            ),
        }
    )

    captured = io.StringIO()
    event_payload = parse_codex_event_payload(
        {
            "session_id": "jira-s1",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "TEST-1234 작업 내용 확인",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=runner) == 0

    payload = json.loads(captured.getvalue())
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert payload["hookSpecificOutput"]["hookEventName"] == "UserPromptSubmit"
    assert "- TEST-1234 → `.workflow-cache/jira/jira.example.test/issues/TEST-1234/snapshot.md` (refreshed)" in context
    assert "#TEST-1234" not in context
    assert "Jira hook cache context" not in context
    assert [request.args for request in runner.requests] == [
        curl_args(jira_issue_url()),
        curl_args(jira_remote_links_url()),
    ]
    assert (
        tmp_path
        / ".workflow-cache"
        / "jira"
        / "jira.example.test"
        / "issues"
        / "TEST-1234"
        / "snapshot.md"
    ).is_file()


def test_user_prompt_injects_jira_commit_prefix_hint_without_issue_fetch(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_jira_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner({})

    captured = io.StringIO()
    event_payload = parse_codex_event_payload(
        {
            "session_id": "jira-commit-s1",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "커밋 준비",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=runner) == 0

    payload = json.loads(captured.getvalue())
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert context == main_context_fragment("commit-prefix.md")
    assert runner.requests == []


def test_user_prompt_dedupes_announced_issue_paths_within_session(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner(
        {
            gh_issue_view_args(45): result(
                gh_issue_view_args(45),
                stdout=json.dumps(issue_payload(45)),
            )
        }
    )
    raw_payload = {
        "session_id": "s1",
        "turn_id": "turn-1",
        "cwd": str(tmp_path),
        "hook_event_name": "UserPromptSubmit",
        "prompt": "Please inspect #45.",
    }

    first_event = parse_codex_event_payload(raw_payload)
    assert isinstance(first_event, CodexUserPromptSubmitPayload)
    first = io.StringIO()
    assert user_prompt_submit(first_event, stdout=first, runner=runner) == 0
    second_event = parse_codex_event_payload(raw_payload)
    assert isinstance(second_event, CodexUserPromptSubmitPayload)
    second = io.StringIO()
    assert user_prompt_submit(second_event, stdout=second, runner=runner) == 0

    assert first.getvalue()
    assert second.getvalue() == ""


def test_user_prompt_lists_issue_path_when_frontmatter_has_relationships(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    repo = GitHubRepository(host="github.com", owner="studykit", name="studykit-plugins")
    cache = GitHubIssueCache.for_project(tmp_path, configured_repo=repo)
    cache.write_issue_bundle(repo, issue_payload(39, title="Requested issue"))
    cache.write_relationships_projection(
        repo,
        39,
        {
            "updatedAt": "2026-05-14T00:00:00Z",
            "parent": {"number": 28},
            "children": [{"number": 41}],
            "dependencies": {
                "blocked_by": [{"number": 33}],
                "blocking": [{"number": 45}],
            },
        },
        fetched_at="2026-05-14T00:00:00Z",
    )

    captured = io.StringIO()
    event_payload = parse_codex_event_payload(
        {
            "session_id": "s1",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "#39 작업 내용 확인",
        },
    )
    assert isinstance(event_payload, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(event_payload, stdout=captured, runner=FakeRunner({})) == 0

    payload = json.loads(captured.getvalue())
    context = payload["hookSpecificOutput"]["additionalContext"]
    assert context == "## Workflow issue cache\n\n- #39 → `.workflow-cache/issues/39/issue.md`"


def test_stop_does_not_carry_issue_refs_to_next_user_prompt(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    _hook_env(monkeypatch, tmp_path)
    runner = FakeRunner(
        {
            gh_issue_view_args(46): result(
                gh_issue_view_args(46),
                stdout=json.dumps(issue_payload(46, title="Stop hook cache finalization")),
            )
        }
    )

    captured = io.StringIO()
    stop_event = parse_codex_event_payload(
        {
            "session_id": "s2",
            "turn_id": "turn-1",
            "cwd": str(tmp_path),
            "hook_event_name": "Stop",
            "last_assistant_message": "The assistant referenced #46 during the turn.",
        },
    )
    assert isinstance(stop_event, CodexStopPayload)
    assert stop(stop_event, stdout=captured, runner=runner) == 0

    assert captured.getvalue() == ""
    assert runner.requests == []
    state_file = session_state_path(tmp_path, "codex", "s2")
    assert state_file is not None
    assert not state_file.exists()
    issue_file = (
        tmp_path
        / ".workflow-cache"
        / "issues"
        / "46"
        / "issue.md"
    )
    assert not issue_file.exists()

    prompt_context = io.StringIO()
    follow_event = parse_codex_event_payload(
        {
            "session_id": "s2",
            "turn_id": "turn-2",
            "cwd": str(tmp_path),
            "hook_event_name": "UserPromptSubmit",
            "prompt": "Continue.",
        },
    )
    assert isinstance(follow_event, CodexUserPromptSubmitPayload)
    assert user_prompt_submit(follow_event, stdout=prompt_context, runner=runner) == 0

    assert not issue_file.exists()
    assert not state_file.exists()
    assert prompt_context.getvalue() == ""


def test_claude_pre_write_blocks_github_cache_issue_body_update(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    issue_file = tmp_path / ".workflow-cache" / "issues" / "39" / "issue.md"
    issue_file.parent.mkdir(parents=True)
    current_issue_text = """---
schema_version: 1
title: Cached issue
state: open
labels:
  - task
  - workflow
source_updated_at: 2026-05-14T00:00:00Z
---

Current body.
"""
    issue_file.write_text(current_issue_text, encoding="utf-8")
    next_issue_text = current_issue_text.replace("Current body.", "Updated body.")

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "cache-issue-protection",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Write",
            "tool_input": {
                "file_path": str(issue_file),
                "content": next_issue_text,
            },
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    reason = payload["reason"]
    assert payload["decision"] == "block"
    assert "projection is read-only" in reason
    assert "body-file flow" in reason
    assert f"Target: {issue_file}" in reason


def test_claude_pre_write_blocks_github_cache_comment_body_edit(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    comment_file = (
        tmp_path
        / ".workflow-cache"
        / "issues"
        / "39"
        / "comment-2026-05-14T00-01-00Z-IC_kw.md"
    )
    comment_file.parent.mkdir(parents=True)
    comment_file.write_text(
        """---
id: IC_kw
author: studykit
updated_at: 2026-05-14T00:01:00Z
---

Existing comment body.
""",
        encoding="utf-8",
    )

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "cache-comment-protection",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Edit",
            "tool_input": {
                "file_path": str(comment_file),
                "old_string": "Existing comment body.",
                "new_string": "Edited comment body.",
            },
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    reason = payload["reason"]
    assert payload["decision"] == "block"
    assert "projection is read-only" in reason
    assert "body-file flow" in reason
    assert f"Target: {comment_file}" in reason


def test_claude_pre_write_blocks_creating_github_cache_issue_body(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    issue_file = tmp_path / ".workflow-cache" / "issues" / "40" / "issue.md"
    issue_text = """---
title: New issue
labels:
  - task
---

Updated body.
"""

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "cache-issue-protection",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Write",
            "tool_input": {
                "file_path": str(issue_file),
                "content": issue_text,
            },
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    reason = payload["reason"]
    assert payload["decision"] == "block"
    assert "projection has not been prepared yet" in reason
    assert f"Target: {issue_file}" in reason
    assert "$WORKFLOW github_issue_fetch.py" in reason


def test_provider_issue_cache_body_recognition_dispatches_to_provider_module(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    config = workflow_hook.workflow_config_for_project(tmp_path)
    assert config is not None
    calls: list[tuple[Path, Path]] = []

    def fake_github_recognizer(path: Path, project: Path) -> bool:
        calls.append((path, project))
        return True

    def unexpected_jira_recognizer(path: Path, project: Path) -> bool:
        raise AssertionError("Jira recognizer should not run for GitHub issue config")

    monkeypatch.setattr(workflow_hook, "is_github_issue_cache_body_path", fake_github_recognizer)
    monkeypatch.setattr(workflow_hook, "is_jira_issue_cache_body_path", unexpected_jira_recognizer)

    target = tmp_path / "provider-owned-layout-is-not-parsed-here.md"

    assert workflow_hook.is_provider_issue_cache_body(target, config)
    assert calls == [(target, tmp_path)]


def test_claude_pre_write_blocks_github_cache_issue_frontmatter_changes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    issue_file = tmp_path / ".workflow-cache" / "issues" / "39" / "issue.md"
    issue_file.parent.mkdir(parents=True)
    issue_file.write_text(
        """---
schema_version: 1
title: Cached issue
state: open
labels:
  - task
  - workflow
source_updated_at: 2026-05-14T00:00:00Z
---

Current body.
""",
        encoding="utf-8",
    )

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "cache-frontmatter-protection",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Edit",
            "tool_input": {
                "file_path": str(issue_file),
                "old_string": "title: Cached issue",
                "new_string": "title: Changed issue",
            },
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    reason = payload["reason"]
    assert payload["decision"] == "block"
    assert "projection is read-only" in reason
    assert "body-file flow" in reason


def test_claude_pre_write_blocks_jira_cache_snapshot_edits(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_jira_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    snapshot = (
        tmp_path
        / ".workflow-cache"
        / "jira"
        / "jira.example.test"
        / "issues"
        / "TEST-1234"
        / "snapshot.md"
    )
    snapshot.parent.mkdir(parents=True)
    snapshot.write_text(
        "# TEST-1234: Cached Jira issue\n\nCached body.\n",
        encoding="utf-8",
    )

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "jira-projection-protection",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Edit",
            "tool_input": {
                "file_path": str(snapshot),
                "old_string": "Cached body.",
                "new_string": "Edited body.",
            },
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    reason = payload["reason"]
    assert payload["decision"] == "block"
    assert "projection is read-only" in reason
    assert "body-file flow" in reason


def test_claude_pre_write_blocks_github_cache_comment_create_when_no_projection(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_config(tmp_path)
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(_PLUGIN_ROOT))

    comment_file = (
        tmp_path
        / ".workflow-cache"
        / "issues"
        / "39"
        / "comment-2026-05-14T000000Z-7700001.md"
    )

    captured = io.StringIO()
    assert claude_main(
        payload={
            "session_id": "comment-creation-protection",
            "cwd": str(tmp_path),
            "hook_event_name": "PreToolUse",
            "tool_name": "Write",
            "tool_input": {
                "file_path": str(comment_file),
                "content": "---\nauthor: me\n---\n\nLocal comment body.\n",
            },
        },
        stdout=captured,
    ) == 0

    payload = json.loads(captured.getvalue())
    reason = payload["reason"]
    assert payload["decision"] == "block"
    assert "projection has not been prepared" in reason


def test_session_start_emits_nothing_for_invalid_config(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config_path = tmp_path / ".workflow" / "config.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        """
version: 1
providers:
  issues:
    kind: confluence
  knowledge:
    kind: github
""".lstrip(),
        encoding="utf-8",
    )

    out = _run_session_start(tmp_path, monkeypatch, runtime="claude")

    assert out == ""
