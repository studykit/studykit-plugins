"""Tests for workflow setup config generation and writes."""

from __future__ import annotations

import io
import json
import sys
import tomllib
from pathlib import Path
from typing import Any

import pytest
import yaml

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "setup"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import setup  # noqa: E402
from command import CommandRequest, CommandResult  # noqa: E402
from config import WorkflowConfigError, parse_workflow_config  # noqa: E402
from setup import (  # noqa: E402
    AGENTS_FILENAME,
    AGENTS_KNOWLEDGE_HEADING,
    CODEX_AGENT_INSTALL_MARKER_BEGIN,
    CODEX_AGENT_INSTALL_MARKER_END,
    CODEX_CONFIG_RELATIVE_PATH,
    CODEX_SPECTRACK_AGENT_DIR,
    CLAUDE_AGENTS_SHIM,
    CLAUDE_FILENAME,
    SPECTRACK_CODEX_AGENT_ROLES,
    WorkflowSetupError,
    build_config,
    build_config_payload,
    build_jira_relationship_mappings,
    derive_state_transition_verb,
    format_config_yaml,
    install_codex_agents,
    inspect_jira_relationships,
    inspect_jira_state_transitions,
    probe_git_remote,
    profile_from_docs,
    provider_capabilities,
    write_config,
)


def _fixture(name: str) -> dict[str, Any]:
    return yaml.safe_load((_FIXTURES / name).read_text(encoding="utf-8"))


def _github_github_config(project: Path) -> dict[str, Any]:
    return build_config(
        project=project,
        issue_provider="github",
        knowledge_provider="github",
        github_repo="studykit/studykit-plugins",
        github_wiki_path="wiki/spectrack",
    )


def _jira_relationship_mappings() -> dict[str, Any]:
    return {
        "blocked_by": {
            "surface": "issue_link",
            "link_type": "Blocks",
            "direction": "inward",
        }
    }


def _curl_get_args(url: str) -> tuple[str, ...]:
    return ("curl", "--silent", "--show-error", "--fail", "--request", "GET", "--config", "-", url)


@pytest.mark.parametrize(
    "fixture",
    [
        "github-github.yml",
        "filesystem-github.yml",
    ],
)
def test_setup_fixtures_round_trip_through_workflow_config(fixture: str, tmp_path: Path) -> None:
    raw = _fixture(fixture)

    config = parse_workflow_config(raw, path=tmp_path / ".spectrack" / "config.yml")

    assert config.version == 1
    assert config.path == (tmp_path / ".spectrack" / "config.yml").resolve()


def test_build_config_generates_github_github_fixture(tmp_path: Path) -> None:
    raw = _github_github_config(tmp_path)

    assert raw == _fixture("github-github.yml")
    config = parse_workflow_config(raw, path=tmp_path / ".spectrack" / "config.yml")
    assert config.issue_id_format == "github"


def test_build_config_records_commit_refs(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="filesystem",
        knowledge_provider="github",
        commit_ref_style="provider-native",
        commit_refs_enabled=False,
    )

    assert raw == _fixture("filesystem-github.yml")
    assert raw["commit_refs"] == {"enabled": False, "style": "disabled"}


def test_build_config_includes_prd_path_when_provided(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="github",
        knowledge_provider="github",
        github_repo="example/repo",
        github_wiki_path="wiki/spectrack",
        github_wiki_prd_path="prd",
    )

    assert raw["providers"]["knowledge"]["prd_path"] == "prd"


def test_build_config_omits_prd_path_when_not_provided(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="github",
        knowledge_provider="github",
        github_repo="example/repo",
        github_wiki_path="wiki/spectrack",
    )

    assert "prd_path" not in raw["providers"]["knowledge"]


def test_build_config_rejects_absolute_prd_path(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="relative path"):
        build_config(
            project=tmp_path,
            issue_provider="github",
            knowledge_provider="github",
            github_repo="example/repo",
            github_wiki_path="wiki/spectrack",
            github_wiki_prd_path="/etc",
        )


def test_build_config_rejects_prd_path_with_dotdot(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="escape"):
        build_config(
            project=tmp_path,
            issue_provider="github",
            knowledge_provider="github",
            github_repo="example/repo",
            github_wiki_path="wiki/spectrack",
            github_wiki_prd_path="prd/../leak",
        )


def test_build_config_defaults_issue_id_format_to_provider_native(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
    )

    assert raw["issue_id_format"] == "jira"


def test_build_config_records_jira_snapshot_hidden_comment_markers(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
        jira_snapshot_hidden_comment_markers=("!git-event",),
    )

    assert raw["providers"]["issues"]["snapshot"] == {"hidden_comment_markers": ["!git-event"]}


def test_build_config_requires_jira_relationship_mappings(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="relationship_mappings"):
        build_config(
            project=tmp_path,
            issue_provider="jira",
            knowledge_provider="github",
            jira_site="https://jira.example.test",
            )


def test_build_config_rejects_invalid_provider_for_role(tmp_path: Path) -> None:
    with pytest.raises(WorkflowConfigError, match="not valid for role"):
        build_config(
            project=tmp_path,
            issue_provider="wiki",
            knowledge_provider="github",
        )


def test_build_config_rejects_jira_cloud_deployment(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="Jira Cloud"):
        build_config(
            project=tmp_path,
            issue_provider="jira",
            knowledge_provider="github",
            jira_site="https://acme.atlassian.net",
        )


def test_capabilities_mark_jira_setup_incomplete_when_relationship_mappings_are_missing() -> None:
    payload = provider_capabilities(issue_provider="jira", knowledge_provider="github")

    assert payload["issues"]["relationship_writes"] is False
    assert any("setup is incomplete" in item for item in payload["warnings"])
    assert any("jira-relationship-inspect" in item for item in payload["warnings"])
    assert not any("remain unavailable" in item for item in payload["warnings"])


def test_build_config_accepts_explicit_jira_relationship_mappings(tmp_path: Path) -> None:
    mappings = _jira_relationship_mappings()

    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=mappings,
    )
    payload = build_config_payload(raw, project=tmp_path)

    assert raw["providers"]["issues"]["relationship_mappings"] == mappings
    assert payload["capabilities"]["issues"]["relationship_writes"] is True


def test_jira_relationship_mapping_helper_builds_explicit_mapping_yaml() -> None:
    payload = build_jira_relationship_mappings(
        issue_links=(
            "blocked_by=Blocks:inward",
            "blocking=Blocks:outward",
            "related=Relate:outward",
        ),
        fields=(
            "custom_relation=customfield_12345:source:string",
            "child=parent:target:key",
        ),
    )

    mappings = payload["relationship_mappings"]
    assert mappings["blocked_by"] == {
        "surface": "issue_link",
        "link_type": "Blocks",
        "direction": "inward",
    }
    assert mappings["custom_relation"] == {
        "surface": "field",
        "field": "customfield_12345",
        "write_to": "source",
        "value": "string",
    }
    assert mappings["child"] == {
        "surface": "field",
        "field": "parent",
        "write_to": "target",
        "value": "key",
    }
    assert yaml.safe_load(payload["yaml"]) == mappings


def test_jira_relationship_mapping_helper_rejects_incomplete_specs() -> None:
    with pytest.raises(WorkflowSetupError, match="field mapping must"):
        build_jira_relationship_mappings(fields=("custom_relation=customfield_12345:source",))


def test_jira_relationship_inspect_reports_observed_surfaces() -> None:
    def runner(request: CommandRequest) -> CommandResult:
        responses = {
            _curl_get_args("https://jira.example.test/rest/api/2/issueLinkType"): {
                "issueLinkTypes": [
                    {"name": "Blocks", "inward": "is blocked by", "outward": "blocks"},
                    {"name": "Relate", "inward": "is related by", "outward": "relates to"},
                ]
            },
            _curl_get_args("https://jira.example.test/rest/api/2/field"): [
                {"id": "customfield_12345", "name": "Custom Relationship"},
                {"id": "customfield_12287", "name": "Parent Link"},
                {"id": "summary", "name": "Summary"},
            ],
            _curl_get_args(
                "https://jira.example.test/rest/api/2/issue/PROJ-9911"
                "?fields=summary,issuetype,parent,subtasks,issuelinks,customfield_12345,customfield_12287"
            ): {
                "key": "PROJ-9911",
                "fields": {
                    "summary": "Task with site relationship",
                    "issuetype": {"name": "Task"},
                    "parent": {"key": "PROJ-9877", "fields": {"summary": "Parent task", "issuetype": {"name": "Task"}}},
                    "subtasks": [
                        {"key": "PROJ-10062", "fields": {"summary": "Sub task", "issuetype": {"name": "Sub-task"}}}
                    ],
                    "issuelinks": [
                        {
                            "id": "10001",
                            "type": {"name": "Blocks", "inward": "is blocked by", "outward": "blocks"},
                            "outwardIssue": {
                                "key": "PROJ-9912",
                                "fields": {"summary": "Blocked target", "issuetype": {"name": "Task"}},
                            },
                        }
                    ],
                    "customfield_12345": "PROJ-9508",
                    "customfield_12287": None,
                },
            },
        }
        payload = responses.get(request.args)
        if payload is None:
            return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")
        return CommandResult(request=request, returncode=0, stdout=json.dumps(payload))

    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        issues=("PROJ-9911",),
        field_queries=("customfield_12345", "Parent Link"),
        runner=runner,
    )

    assert payload["link_types"][0] == {"name": "Blocks", "inward": "is blocked by", "outward": "blocks"}
    assert [field["id"] for field in payload["fields"]] == ["customfield_12345", "customfield_12287"]
    sample = payload["sample_issues"][0]
    assert sample["key"] == "PROJ-9911"
    assert sample["parent"]["key"] == "PROJ-9877"
    assert sample["subtasks"][0]["key"] == "PROJ-10062"
    assert sample["issue_links"][0]["outward_issue"]["key"] == "PROJ-9912"
    assert sample["custom_fields"]["customfield_12345"] == "PROJ-9508"
    assert any("observed Jira data only" in warning for warning in payload["warnings"])


def _epic_field_response() -> list[dict[str, Any]]:
    return [
        {
            "id": "customfield_12345",
            "name": "Epic Name",
            "schema": {"custom": "com.pyxis.greenhopper.jira:gh-epic-label"},
        },
        {
            "id": "customfield_12346",
            "name": "Epic Link",
            "schema": {"custom": "com.pyxis.greenhopper.jira:gh-epic-link"},
        },
        {
            "id": "customfield_12347",
            "name": "Epic Status",
            "schema": {"custom": "com.pyxis.greenhopper.jira:gh-epic-status"},
        },
        {"id": "summary", "name": "Summary"},
    ]


def _epic_createmeta_response() -> dict[str, Any]:
    return {
        "projects": [
            {
                "key": "TEST",
                "issuetypes": [
                    {
                        "id": "10000",
                        "name": "Task",
                        "fields": {"summary": {}, "customfield_12346": {}},
                    },
                    {
                        "id": "10001",
                        "name": "Story",
                        "fields": {"summary": {}, "customfield_12346": {}},
                    },
                    {
                        "id": "10100",
                        "name": "Epic",
                        "fields": {
                            "summary": {},
                            "customfield_12345": {},
                            "customfield_12347": {},
                        },
                    },
                    {
                        "id": "10200",
                        "name": "Sub-task",
                        "fields": {"summary": {}, "customfield_12346": {}},
                    },
                ],
            }
        ]
    }


def _jira_inspect_runner(
    *,
    fields: list[dict[str, Any]] | None = None,
    createmeta: dict[str, Any] | None = None,
    project: str | None = "TEST",
):
    raw_fields = fields if fields is not None else _epic_field_response()
    raw_createmeta = createmeta if createmeta is not None else _epic_createmeta_response()
    createmeta_url = (
        f"https://jira.example.test/rest/api/2/issue/createmeta?projectKeys={project}"
        "&expand=projects.issuetypes.fields"
    ) if project else None

    def runner(request: CommandRequest) -> CommandResult:
        responses: dict[tuple[str, ...], Any] = {
            _curl_get_args("https://jira.example.test/rest/api/2/issueLinkType"): {"issueLinkTypes": []},
            _curl_get_args("https://jira.example.test/rest/api/2/field"): raw_fields,
        }
        if createmeta_url is not None:
            responses[_curl_get_args(createmeta_url)] = raw_createmeta
        payload = responses.get(request.args)
        if payload is None:
            return CommandResult(request=request, returncode=127, stderr=f"unexpected command: {request.args}")
        return CommandResult(request=request, returncode=0, stdout=json.dumps(payload))

    return runner


def test_jira_relationship_inspect_discovers_epic_fields_by_schema() -> None:
    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        jira_project="TEST",
        runner=_jira_inspect_runner(),
    )

    epic = payload["epic"]
    assert epic["fields"]["name"]["id"] == "customfield_12345"
    assert epic["fields"]["name"]["matched_by"] == "schema"
    assert epic["fields"]["link"]["id"] == "customfield_12346"
    assert epic["fields"]["status"]["id"] == "customfield_12347"


def test_jira_relationship_inspect_falls_back_to_name_match_for_epic_fields() -> None:
    fields = [
        {"id": "customfield_22001", "name": "Epic Name"},
        {"id": "customfield_22002", "name": "Epic Link"},
        {"id": "customfield_22003", "name": "Epic Status"},
    ]
    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        jira_project="TEST",
        runner=_jira_inspect_runner(fields=fields),
    )

    epic = payload["epic"]
    assert epic["fields"]["name"] == {
        "id": "customfield_22001",
        "name": "Epic Name",
        "matched_by": "name",
    }
    assert epic["fields"]["link"]["matched_by"] == "name"


def test_jira_relationship_inspect_warns_when_epic_fields_missing() -> None:
    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        jira_project="TEST",
        runner=_jira_inspect_runner(fields=[{"id": "summary", "name": "Summary"}]),
    )

    epic = payload["epic"]
    assert epic["fields"]["name"] is None
    assert epic["fields"]["link"] is None
    assert any("Epic name customfield" in warning for warning in epic["warnings"])


def test_jira_relationship_inspect_surfaces_epic_issue_type_candidates() -> None:
    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        jira_project="TEST",
        runner=_jira_inspect_runner(),
    )

    epic = payload["epic"]
    assert epic["issue_types"] == [{"id": "10100", "name": "Epic"}]


def test_jira_relationship_inspect_reports_per_issue_type_epic_link_support() -> None:
    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        jira_project="TEST",
        runner=_jira_inspect_runner(),
    )

    support = {
        entry["name"]: entry["supports_epic_link"]
        for entry in payload["epic"]["issue_type_epic_link_support"]
    }
    assert support == {
        "Task": True,
        "Story": True,
        "Epic": False,
        "Sub-task": True,
    }


def test_jira_relationship_inspect_warns_when_project_missing_for_createmeta() -> None:
    payload = inspect_jira_relationships(
        jira_site="https://jira.example.test",
        runner=_jira_inspect_runner(project=None),
    )

    epic = payload["epic"]
    assert epic["issue_types"] == []
    assert epic["issue_type_epic_link_support"] == []
    assert any("supply --jira-project" in warning for warning in epic["warnings"])


def test_build_config_writes_epic_fields_when_provided(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
        jira_epic_fields={
            "name": "customfield_12345",
            "link": "customfield_12346",
            "status": "customfield_12347",
        },
    )

    issues = raw["providers"]["issues"]
    assert issues["epic_fields"] == {
        "name": "customfield_12345",
        "link": "customfield_12346",
        "status": "customfield_12347",
    }
    assert issues["relationship_mappings"]["epic"] == {
        "surface": "field",
        "field": "customfield_12346",
        "write_to": "source",
        "value": "string",
    }


def test_build_config_keeps_explicit_epic_mapping_when_provided(tmp_path: Path) -> None:
    mappings = dict(_jira_relationship_mappings())
    mappings["epic"] = {
        "surface": "field",
        "field": "customfield_99999",
        "write_to": "source",
        "value": "string",
    }
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=mappings,
        jira_epic_fields={"link": "customfield_12346"},
    )

    assert raw["providers"]["issues"]["relationship_mappings"]["epic"]["field"] == "customfield_99999"


def test_build_config_writes_epic_issue_type_only_when_non_default(tmp_path: Path) -> None:
    raw_default = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
        jira_epic_issue_type="Epic",
    )
    raw_override = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
        jira_epic_issue_type="Initiative",
    )

    assert "artifact_issue_types" not in raw_default["providers"]["issues"]
    assert raw_override["providers"]["issues"]["artifact_issue_types"] == {"epic": "Initiative"}


def test_build_config_rejects_unknown_epic_fields_key(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="unknown Jira epic_fields entry"):
        build_config(
            project=tmp_path,
            issue_provider="jira",
            knowledge_provider="github",
            jira_site="https://jira.example.test",
            jira_relationship_mappings=_jira_relationship_mappings(),
            jira_epic_fields={"unknown": "customfield_12345"},
            )


def _jira_state_transition_runner(
    transitions_by_issue: dict[str, list[dict[str, Any]]],
):
    def runner(request: CommandRequest) -> CommandResult:
        for key, transitions in transitions_by_issue.items():
            url = f"https://jira.example.test/rest/api/2/issue/{key}/transitions"
            if request.args == _curl_get_args(url):
                return CommandResult(
                    request=request,
                    returncode=0,
                    stdout=json.dumps({"transitions": transitions}),
                )
        return CommandResult(
            request=request,
            returncode=127,
            stderr=f"unexpected command: {request.args}",
        )

    return runner


def test_jira_state_transition_inspect_reports_per_issue_transitions() -> None:
    runner = _jira_state_transition_runner(
        {
            "PROJ-1": [
                {"id": "31", "name": "Done", "to": {"name": "Closed", "id": "6", "statusCategory": {"key": "done"}}},
            ],
            "PROJ-2": [
                {"id": "41", "name": "Reopen", "to": {"name": "Open", "id": "1", "statusCategory": {"key": "new"}}},
            ],
        }
    )
    payload = inspect_jira_state_transitions(
        jira_site="https://jira.example.test",
        issues=("PROJ-1", "PROJ-2"),
        runner=runner,
    )

    assert payload["operation"] == "jira_state_transition_inspect"
    issue_keys = [sample["issue"] for sample in payload["sample_issues"]]
    assert issue_keys == ["PROJ-1", "PROJ-2"]
    sample_one, sample_two = payload["sample_issues"]
    assert sample_one["transitions"] == [
        {
            "id": "31",
            "name": "Done",
            "to_status_name": "Closed",
            "to_status_id": "6",
            "to_status_category": "done",
        }
    ]
    assert sample_two["transitions"][0]["name"] == "Reopen"
    assert set(payload["observed_transition_names"]) == {"Done", "Reopen"}
    assert payload["auto_verbs"] == {"done": "Done", "reopen": "Reopen"}
    assert payload["warnings"] != []  # transitions differ between issues


def test_jira_state_transition_inspect_silent_when_all_samples_match() -> None:
    transitions = [
        {"id": "31", "name": "Done", "to": {"name": "Closed"}},
    ]
    runner = _jira_state_transition_runner({"PROJ-1": transitions, "PROJ-2": transitions})

    payload = inspect_jira_state_transitions(
        jira_site="https://jira.example.test",
        issues=("PROJ-1", "PROJ-2"),
        runner=runner,
    )

    assert payload["warnings"] == []
    assert payload["observed_transition_names"] == ["Done"]
    assert payload["auto_verbs"] == {"done": "Done"}


@pytest.mark.parametrize(
    "transition_name, expected_verb",
    [
        ("Done", "done"),
        ("Reopen", "reopen"),
        ("In Progress", "in-progress"),
        ("Ready to Review", "ready-to-review"),
        ("Resolve Issue", "resolve-issue"),
        ("  Spaced  ", "spaced"),
        ("Multi   space", "multi-space"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_derive_state_transition_verb(transition_name: str, expected_verb: str) -> None:
    assert derive_state_transition_verb(transition_name) == expected_verb


def test_jira_state_transition_inspect_skips_reserved_auto_verb() -> None:
    runner = _jira_state_transition_runner(
        {
            "PROJ-1": [
                {"id": "31", "name": "Assign", "to": {"name": "Assigned"}},
                {"id": "32", "name": "Done", "to": {"name": "Closed"}},
            ],
        }
    )

    payload = inspect_jira_state_transitions(
        jira_site="https://jira.example.test",
        issues=("PROJ-1",),
        runner=runner,
    )

    assert payload["auto_verbs"] == {"done": "Done"}
    assert any("reserved verb 'assign'" in w for w in payload["warnings"])


def test_jira_state_transition_inspect_skips_colliding_auto_verbs() -> None:
    runner = _jira_state_transition_runner(
        {
            "PROJ-1": [
                {"id": "31", "name": "Resolve", "to": {"name": "Resolved"}},
                {"id": "32", "name": "Resolve!", "to": {"name": "Resolved"}},
                {"id": "33", "name": "Done", "to": {"name": "Closed"}},
            ],
        }
    )

    payload = inspect_jira_state_transitions(
        jira_site="https://jira.example.test",
        issues=("PROJ-1",),
        runner=runner,
    )

    assert payload["auto_verbs"] == {"done": "Done"}
    assert any("derive to verb 'resolve'" in w for w in payload["warnings"])


def test_jira_state_transition_inspect_requires_at_least_one_issue() -> None:
    with pytest.raises(WorkflowSetupError, match="requires at least one --issue"):
        inspect_jira_state_transitions(
            jira_site="https://jira.example.test",
            issues=(),
        )


def test_build_config_writes_state_transitions_when_provided(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
        jira_state_transitions={"close": "Closed", "reopen": "Reopened"},
    )

    assert raw["providers"]["issues"]["state_transitions"] == {
        "close": "Closed",
        "reopen": "Reopened",
    }


def test_build_config_omits_state_transitions_when_not_provided(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="github",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
    )

    assert "state_transitions" not in raw["providers"]["issues"]


def _build_config_cli(args: list[str]) -> int:
    stdout = io.StringIO()
    stderr = io.StringIO()
    return setup.main(args, stdout=stdout, stderr=stderr)


@pytest.mark.parametrize(
    "value, message",
    [
        ("closedDone", "must be <verb>=<transition name>"),
        ("assign=Done", "collides with a reserved issue_fields verb"),
        ("close=", "must include a non-empty transition name"),
    ],
)
def test_build_config_state_transition_flag_rejects_malformed_input(
    tmp_path: Path, value: str, message: str
) -> None:
    args = [
        "build-config",
        "--project",
        str(tmp_path),
        "--issue-provider",
        "jira",
        "--knowledge-provider",
        "github",
        "--jira-site",
        "https://jira.example.test",
        "--jira-relationship-mapping",
        "blocked_by:surface=issue_link,link_type=Blocks,direction=inward",
        "--jira-state-transition",
        value,
    ]
    stdout = io.StringIO()
    stderr = io.StringIO()
    rc = setup.main(args, stdout=stdout, stderr=stderr)
    assert rc == 2
    assert message in stderr.getvalue()


def test_build_config_state_transition_flag_rejects_duplicate_verb(tmp_path: Path) -> None:
    args = [
        "build-config",
        "--project",
        str(tmp_path),
        "--issue-provider",
        "jira",
        "--knowledge-provider",
        "github",
        "--jira-site",
        "https://jira.example.test",
        "--jira-relationship-mapping",
        "blocked_by:surface=issue_link,link_type=Blocks,direction=inward",
        "--jira-state-transition",
        "close=Closed",
        "--jira-state-transition",
        "close=Resolved",
    ]
    stdout = io.StringIO()
    stderr = io.StringIO()
    rc = setup.main(args, stdout=stdout, stderr=stderr)
    assert rc == 2
    assert "specified more than once for verb" in stderr.getvalue()


def test_jira_relationship_mappings_require_explicit_surface(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="requires explicit surface"):
        build_config(
            project=tmp_path,
            issue_provider="jira",
            knowledge_provider="github",
            jira_site="https://jira.example.test",
            jira_relationship_mappings={"blocked_by": {"link_type": "Blocks", "direction": "inward"}},
        )


def test_write_refuses_overwrite_and_force_rewrites(tmp_path: Path) -> None:
    first = _github_github_config(tmp_path)
    second = build_config(
        project=tmp_path,
        issue_provider="filesystem",
        knowledge_provider="github",
        commit_refs_enabled=False,
    )

    write_config(tmp_path, first)
    with pytest.raises(WorkflowSetupError, match="already exists"):
        write_config(tmp_path, second)

    result = write_config(tmp_path, second, force=True)
    written = yaml.safe_load((tmp_path / ".spectrack" / "config.yml").read_text(encoding="utf-8"))
    assert result["verified"] is True
    assert written["providers"]["issues"]["kind"] == "filesystem"


def test_write_rejects_jira_config_without_relationship_mappings(tmp_path: Path) -> None:
    raw = {
        "version": 1,
        "mode": "remote-native",
        "providers": {
            "issues": {
                "kind": "jira",
                "site": "https://jira.example.test",
                "deployment": "data_center",
                "api_version": "2",
            },
            "knowledge": {
                "kind": "github",
                "path": "wiki/spectrack",
            },
        },
        "issue_id_format": "jira",
        "commit_refs": {"enabled": True, "style": "provider-native"},
    }

    with pytest.raises(WorkflowSetupError, match="relationship_mappings"):
        write_config(tmp_path, raw)

    assert not (tmp_path / ".spectrack" / "config.yml").exists()


def test_write_is_atomic_when_replace_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    raw = _github_github_config(tmp_path)

    def fail_replace(src: Path, dst: Path) -> None:
        raise OSError("replace failed")

    monkeypatch.setattr(setup.os, "replace", fail_replace)

    with pytest.raises(OSError, match="replace failed"):
        write_config(tmp_path, raw)

    config_dir = tmp_path / ".spectrack"
    assert not (config_dir / "config.yml").exists()
    assert not list(config_dir.glob("*.tmp"))


def test_write_creates_agents_md_with_knowledge_root(tmp_path: Path) -> None:
    raw = _github_github_config(tmp_path)

    result = write_config(tmp_path, raw)

    agents_path = tmp_path / AGENTS_FILENAME
    claude_path = tmp_path / CLAUDE_FILENAME
    agents_text = agents_path.read_text(encoding="utf-8")
    expected_absolute = str((tmp_path / "wiki" / "spectrack").resolve())

    assert AGENTS_KNOWLEDGE_HEADING in agents_text
    assert "`wiki/spectrack`" in agents_text
    assert expected_absolute in agents_text
    assert claude_path.read_text(encoding="utf-8") == CLAUDE_AGENTS_SHIM
    assert result["agents_md"]["agents_action"] == "create"
    assert result["agents_md"]["claude_action"] == "create"
    assert result["agents_md"]["knowledge_root"] == {
        "repo_relative": "wiki/spectrack",
        "absolute": expected_absolute,
    }
    assert result["codex_agents"]["restart_required"] is True
    assert (tmp_path / CODEX_CONFIG_RELATIVE_PATH).exists()
    assert (tmp_path / CODEX_SPECTRACK_AGENT_DIR / "issue-implementer.toml").exists()


def test_write_appends_knowledge_root_when_agents_md_exists(tmp_path: Path) -> None:
    agents_path = tmp_path / AGENTS_FILENAME
    original = "# Project Agents\n\nExisting prose.\n"
    agents_path.write_text(original, encoding="utf-8")
    claude_path = tmp_path / CLAUDE_FILENAME
    claude_path.write_text("custom CLAUDE shim\n", encoding="utf-8")

    raw = _github_github_config(tmp_path)
    result = write_config(tmp_path, raw)

    agents_text = agents_path.read_text(encoding="utf-8")
    assert agents_text.startswith(original)
    assert AGENTS_KNOWLEDGE_HEADING in agents_text
    assert claude_path.read_text(encoding="utf-8") == "custom CLAUDE shim\n"
    assert result["agents_md"]["agents_action"] == "append"
    assert result["agents_md"]["claude_action"] == "skip"


def test_write_skips_agents_md_when_section_already_present(tmp_path: Path) -> None:
    agents_path = tmp_path / AGENTS_FILENAME
    existing = (
        f"# Project Agents\n\n{AGENTS_KNOWLEDGE_HEADING}\n\nStale entry.\n"
    )
    agents_path.write_text(existing, encoding="utf-8")

    raw = _github_github_config(tmp_path)
    result = write_config(tmp_path, raw)

    assert agents_path.read_text(encoding="utf-8") == existing
    assert result["agents_md"]["agents_action"] == "skip"


def test_write_omits_agents_md_update_when_knowledge_path_absent(
    tmp_path: Path,
) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="filesystem",
        knowledge_provider="github",
        commit_refs_enabled=False,
    )

    result = write_config(tmp_path, raw)

    assert "agents_md" not in result
    assert result["codex_agents"]["operation"] == "install_codex_agents"
    assert not (tmp_path / AGENTS_FILENAME).exists()
    assert not (tmp_path / CLAUDE_FILENAME).exists()
    assert (tmp_path / CODEX_CONFIG_RELATIVE_PATH).exists()


def test_install_codex_agents_creates_project_roles(tmp_path: Path) -> None:
    result = install_codex_agents(tmp_path)

    config_path = tmp_path / CODEX_CONFIG_RELATIVE_PATH
    config_text = config_path.read_text(encoding="utf-8")
    role_path = tmp_path / CODEX_SPECTRACK_AGENT_DIR / "issue-implementer.toml"
    role_text = role_path.read_text(encoding="utf-8")

    tomllib.loads(config_text)
    tomllib.loads(role_text)
    assert result["config_action"] == "create"
    assert len(result["agents"]) == len(SPECTRACK_CODEX_AGENT_ROLES)
    assert CODEX_AGENT_INSTALL_MARKER_BEGIN in config_text
    assert CODEX_AGENT_INSTALL_MARKER_END in config_text
    assert '[agents."spectrack:issue-implementer"]' in config_text
    assert 'config_file = "spectrack/agents/issue-implementer.toml"' in config_text
    assert "developer_instructions = '''" in role_text
    assert "SpecTrack `spectrack:issue-implementer` custom agent in Codex" in role_text
    assert "# Issue Implementer" in role_text
    assert "[apps._default]" in role_text
    assert "enabled = false" in role_text


def test_install_codex_agents_replaces_managed_block_only(tmp_path: Path) -> None:
    codex_dir = tmp_path / ".codex"
    codex_dir.mkdir()
    config_path = codex_dir / "config.toml"
    config_path.write_text(
        "\n".join(
            [
                'sandbox_mode = "workspace-write"',
                "",
                CODEX_AGENT_INSTALL_MARKER_BEGIN,
                "[agents.old]",
                'description = "stale"',
                CODEX_AGENT_INSTALL_MARKER_END,
                "",
                "[features]",
                "hooks = true",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = install_codex_agents(tmp_path)
    text = config_path.read_text(encoding="utf-8")

    assert result["config_action"] == "update"
    assert 'sandbox_mode = "workspace-write"' in text
    assert "[features]\nhooks = true" in text
    assert "[agents.old]" not in text
    assert text.count(CODEX_AGENT_INSTALL_MARKER_BEGIN) == 1
    assert '[agents."spectrack:resolution-auditor"]' in text


def test_install_codex_agents_is_idempotent(tmp_path: Path) -> None:
    install_codex_agents(tmp_path)

    result = install_codex_agents(tmp_path)

    assert result["config_action"] == "skip"
    assert {item["action"] for item in result["agents"]} == {"skip"}


def test_probe_git_remote_detects_github_repository(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        assert request.args == ("git", "remote", "get-url", "origin")
        return CommandResult(
            request=request,
            returncode=0,
            stdout="git@github.com:studykit/studykit-plugins.git\n",
        )

    payload = probe_git_remote(tmp_path, runner=runner)

    assert payload["detected"] is True
    assert payload["slug"] == "studykit/studykit-plugins"


def test_build_config_with_remote_probe_preserves_enterprise_github_host(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        assert request.args == ("git", "remote", "get-url", "origin")
        return CommandResult(
            request=request,
            returncode=0,
            stdout="git@github.example.test:team/source-analyzer.git\n",
        )

    raw = build_config(
        project=tmp_path,
        issue_provider="github",
        knowledge_provider="github",
        probe_remote=True,
        runner=runner,
    )

    assert raw["providers"]["issues"]["repo"] == "team/source-analyzer"
    assert raw["providers"]["issues"]["host"] == "github.example.test"
    assert raw["providers"]["knowledge"]["host"] == "github.example.test"


def test_build_config_supports_distinct_github_issue_and_wiki_hosts(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="github",
        knowledge_provider="github",
        github_repo="public-org/issues",
        github_issue_host="github.com",
        github_wiki_repo="enterprise/wiki",
        github_wiki_host="github.enterprise.test",
    )

    assert raw["providers"]["issues"] == {
        "kind": "github",
        "repo": "public-org/issues",
        "host": "github.com",
    }
    assert raw["providers"]["knowledge"] == {
        "kind": "github",
        "repo": "enterprise/wiki",
        "host": "github.enterprise.test",
    }


def test_probe_git_remote_reports_missing_remote(tmp_path: Path) -> None:
    def runner(request: CommandRequest) -> CommandResult:
        return CommandResult(request=request, returncode=1, stderr="missing remote")

    payload = probe_git_remote(tmp_path, runner=runner)

    assert payload["detected"] is False
    assert "missing remote" in payload["message"]


def test_profile_from_docs_extracts_defaults_and_ignores_unrelated_git_docs() -> None:
    payload = profile_from_docs(
        [
            _FIXTURES / "provider-profile.md",
            _FIXTURES / "unrelated-git-history.md",
        ]
    )

    assert payload["defaults"]["issue_provider"] == "jira"
    assert payload["defaults"]["jira_project"] == "PROJ"
    assert payload["defaults"]["jira_relationship_mappings"]["blocked_by"]["surface"] == "issue_link"
    assert any(item["source"].endswith("unrelated-git-history.md") for item in payload["ignored"])


def test_profile_from_docs_extracts_distinct_github_hosts() -> None:
    payload = profile_from_docs(
        [],
        stdin_text="""
Workflow provider profile:

```yaml
providers:
  issues:
    kind: github
    repo: public-org/issues
    host: github.com
  knowledge:
    kind: github
    repo: enterprise/wiki
    host: github.enterprise.test
    path: wiki/spectrack
```
""".strip(),
    )

    assert payload["defaults"]["github_repo"] == "public-org/issues"
    assert payload["defaults"]["github_issue_host"] == "github.com"
    assert payload["defaults"]["github_wiki_repo"] == "enterprise/wiki"
    assert payload["defaults"]["github_wiki_host"] == "github.enterprise.test"


def test_profile_from_docs_reports_cloud_defaults() -> None:
    payload = profile_from_docs(
        [],
        stdin_text="""
Workflow provider profile:
Jira site: https://acme.atlassian.net
""".strip(),
    )

    assert any("Cloud" in item for item in payload["warnings"])


@pytest.mark.parametrize(
    ("argv", "message"),
    [
        (["build-config"], "--issue-provider is required"),
        (["build-config", "--issue-provider", "github"], "--knowledge-provider is required"),
    ],
)
def test_main_build_config_requires_explicit_providers(
    tmp_path: Path,
    argv: list[str],
    message: str,
) -> None:
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = setup.main(
        [*argv, "--project", str(tmp_path)],
        stdout=stdout,
        stderr=stderr,
    )

    assert code == 2
    assert stdout.getvalue() == ""
    assert message in stderr.getvalue()


def test_main_write_outputs_json(tmp_path: Path) -> None:
    config_file = tmp_path / "candidate.yml"
    config_file.write_text(format_config_yaml(_github_github_config(tmp_path)), encoding="utf-8")
    stdout = io.StringIO()

    code = setup.main(
        ["write", "--project", str(tmp_path), "--config", str(config_file)],
        stdout=stdout,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["verified"] is True
    assert payload["path"].endswith(".spectrack/config.yml")
    assert not (tmp_path / "workflow.config.yml").exists()


def test_manifests_register_codex_skills_and_keep_versions_aligned() -> None:
    repo_root = _PLUGIN_ROOT.parent.parent
    codex = json.loads((_PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    claude = json.loads((_PLUGIN_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    codex_marketplace = json.loads((repo_root / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    claude_marketplace = json.loads((repo_root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))

    assert codex["skills"] == "./skills/"
    assert codex["version"] == claude["version"]
    assert _marketplace_entry(codex_marketplace, "spectrack").get("version") is None
    assert _marketplace_entry(claude_marketplace, "spectrack").get("version") is None


def test_setup_skill_uses_short_install_name() -> None:
    skill = _PLUGIN_ROOT / "skills" / "setup" / "SKILL.md"
    skill_dirs = sorted(path.parent.name for path in (_PLUGIN_ROOT / "skills").glob("*/SKILL.md"))

    assert skill.exists()
    assert (_PLUGIN_ROOT / "skills" / "setup" / "agents" / "openai.yaml").exists()
    assert "setup" in skill_dirs
    assert yaml.safe_load(skill.read_text(encoding="utf-8").split("---", 2)[1])["name"] == "setup"


def test_setup_skill_requires_jira_relationship_profiling_before_config_generation() -> None:
    text = (_PLUGIN_ROOT / "skills" / "setup" / "SKILL.md").read_text(encoding="utf-8")
    normalized = " ".join(text.split())

    assert "This flow is required whenever the issue provider is `jira`" in normalized
    assert "do not offer to defer Jira relationship setup until later" in normalized
    assert "do not build or write a Jira issue config" in normalized
    assert "warn that relationship writes remain unavailable" not in text


def _marketplace_entry(marketplace: dict[str, Any], name: str) -> dict[str, Any]:
    for entry in marketplace["plugins"]:
        if entry["name"] == name:
            return entry
    raise AssertionError(f"missing marketplace entry: {name}")
