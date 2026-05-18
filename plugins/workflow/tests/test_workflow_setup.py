"""Tests for workflow setup config generation and writes."""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "setup"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import workflow_setup  # noqa: E402
from workflow_command import CommandRequest, CommandResult  # noqa: E402
from workflow_config import WorkflowConfigError, parse_workflow_config  # noqa: E402
from workflow_setup import (  # noqa: E402
    WorkflowSetupError,
    build_config,
    build_config_payload,
    build_jira_relationship_mappings,
    format_config_yaml,
    inspect_jira_relationships,
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
        github_wiki_path="wiki/workflow",
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
        "github-confluence.yml",
        "jira-confluence.yml",
        "filesystem-filesystem.yml",
    ],
)
def test_setup_fixtures_round_trip_through_workflow_config(fixture: str, tmp_path: Path) -> None:
    raw = _fixture(fixture)

    config = parse_workflow_config(raw, path=tmp_path / ".workflow" / "config.yml")

    assert config.version == 1
    assert config.path == (tmp_path / ".workflow" / "config.yml").resolve()


def test_build_config_generates_github_github_fixture(tmp_path: Path) -> None:
    raw = _github_github_config(tmp_path)

    assert raw == _fixture("github-github.yml")
    config = parse_workflow_config(raw, path=tmp_path / ".workflow" / "config.yml")
    assert config.issue_id_format == "github"
    assert config.local_projection.mode == "none"


def test_build_config_records_projection_and_commit_refs(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="filesystem",
        knowledge_provider="filesystem",
        local_projection_mode="persistent",
        local_projection_path="workflow",
        commit_ref_style="provider-native",
        commit_refs_enabled=False,
    )

    assert raw == _fixture("filesystem-filesystem.yml")
    assert raw["commit_refs"] == {"enabled": False, "style": "disabled"}


def test_build_config_defaults_issue_id_format_to_provider_native(tmp_path: Path) -> None:
    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="confluence",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=_jira_relationship_mappings(),
        confluence_site="https://confluence.example.test",
    )

    assert raw["issue_id_format"] == "jira"


def test_build_config_requires_jira_relationship_mappings(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="relationship_mappings"):
        build_config(
            project=tmp_path,
            issue_provider="jira",
            knowledge_provider="confluence",
            jira_site="https://jira.example.test",
            confluence_site="https://confluence.example.test",
        )


def test_build_config_rejects_invalid_provider_for_role(tmp_path: Path) -> None:
    with pytest.raises(WorkflowConfigError, match="not valid for role"):
        build_config(
            project=tmp_path,
            issue_provider="confluence",
            knowledge_provider="github",
        )


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        (
            {
                "issue_provider": "jira",
                "knowledge_provider": "github",
                "jira_site": "https://acme.atlassian.net",
            },
            "Jira Cloud",
        ),
        (
            {
                "issue_provider": "github",
                "knowledge_provider": "confluence",
                "confluence_deployment": "cloud",
                "confluence_site": "https://confluence.example.test",
            },
            "Confluence Cloud",
        ),
    ],
)
def test_build_config_rejects_cloud_deployments(
    tmp_path: Path,
    kwargs: dict[str, Any],
    message: str,
) -> None:
    with pytest.raises(WorkflowSetupError, match=message):
        build_config(project=tmp_path, **kwargs)


def test_capabilities_mark_jira_setup_incomplete_when_relationship_mappings_are_missing() -> None:
    payload = provider_capabilities(issue_provider="jira", knowledge_provider="confluence")

    assert payload["issues"]["relationship_writes"] is False
    assert any("setup is incomplete" in item for item in payload["warnings"])
    assert any("jira-relationship-inspect" in item for item in payload["warnings"])
    assert not any("remain unavailable" in item for item in payload["warnings"])


def test_build_config_accepts_explicit_jira_relationship_mappings(tmp_path: Path) -> None:
    mappings = _jira_relationship_mappings()

    raw = build_config(
        project=tmp_path,
        issue_provider="jira",
        knowledge_provider="confluence",
        jira_site="https://jira.example.test",
        jira_relationship_mappings=mappings,
        confluence_site="https://confluence.example.test",
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


def test_jira_relationship_mappings_require_explicit_surface(tmp_path: Path) -> None:
    with pytest.raises(WorkflowSetupError, match="requires explicit surface"):
        build_config(
            project=tmp_path,
            issue_provider="jira",
            knowledge_provider="confluence",
            jira_site="https://jira.example.test",
            confluence_site="https://confluence.example.test",
            jira_relationship_mappings={"blocked_by": {"link_type": "Blocks", "direction": "inward"}},
        )


def test_write_refuses_overwrite_and_force_rewrites(tmp_path: Path) -> None:
    first = _github_github_config(tmp_path)
    second = build_config(
        project=tmp_path,
        issue_provider="filesystem",
        knowledge_provider="filesystem",
        local_projection_mode="persistent",
        local_projection_path="workflow",
        commit_refs_enabled=False,
    )

    write_config(tmp_path, first)
    with pytest.raises(WorkflowSetupError, match="already exists"):
        write_config(tmp_path, second)

    result = write_config(tmp_path, second, force=True)
    written = yaml.safe_load((tmp_path / ".workflow" / "config.yml").read_text(encoding="utf-8"))
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
                "kind": "confluence",
                "site": "https://confluence.example.test",
                "deployment": "data_center",
            },
        },
        "issue_id_format": "jira",
        "local_projection": {"mode": "none"},
        "commit_refs": {"enabled": True, "style": "provider-native"},
    }

    with pytest.raises(WorkflowSetupError, match="relationship_mappings"):
        write_config(tmp_path, raw)

    assert not (tmp_path / ".workflow" / "config.yml").exists()


def test_write_is_atomic_when_replace_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    raw = _github_github_config(tmp_path)

    def fail_replace(src: Path, dst: Path) -> None:
        raise OSError("replace failed")

    monkeypatch.setattr(workflow_setup.os, "replace", fail_replace)

    with pytest.raises(OSError, match="replace failed"):
        write_config(tmp_path, raw)

    config_dir = tmp_path / ".workflow"
    assert not (config_dir / "config.yml").exists()
    assert not list(config_dir.glob("*.tmp"))


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
        "path": "wiki/workflow",
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
    assert payload["defaults"]["knowledge_provider"] == "confluence"
    assert payload["defaults"]["jira_project"] == "PROJ"
    assert payload["defaults"]["confluence_space"] == "ENG"
    assert payload["defaults"]["local_projection_mode"] == "persistent"
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
    path: wiki/workflow
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
Confluence site: https://acme.atlassian.net/wiki
""".strip(),
    )

    assert any("Cloud" in item for item in payload["warnings"])


def test_main_build_config_outputs_yaml(tmp_path: Path) -> None:
    stdout = io.StringIO()

    code = workflow_setup.main(
        [
            "build-config",
            "--project",
            str(tmp_path),
            "--issue-provider",
            "github",
            "--knowledge-provider",
            "github",
            "--github-repo",
            "studykit/studykit-plugins",
        ],
        stdout=stdout,
    )

    assert code == 0
    assert yaml.safe_load(stdout.getvalue())["providers"]["issues"]["kind"] == "github"


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

    code = workflow_setup.main(
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

    code = workflow_setup.main(
        ["write", "--project", str(tmp_path), "--config", str(config_file), "--json"],
        stdout=stdout,
    )

    payload = json.loads(stdout.getvalue())
    assert code == 0
    assert payload["verified"] is True
    assert payload["path"].endswith(".workflow/config.yml")
    assert not (tmp_path / "workflow.config.yml").exists()


def test_workflow_manifests_register_codex_skills_and_keep_versions_aligned() -> None:
    repo_root = _PLUGIN_ROOT.parent.parent
    codex = json.loads((_PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    claude = json.loads((_PLUGIN_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    codex_marketplace = json.loads((repo_root / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
    claude_marketplace = json.loads((repo_root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))

    assert codex["skills"] == "./skills/"
    assert codex["version"] == claude["version"]
    assert _marketplace_entry(codex_marketplace, "workflow").get("version") is None
    assert _marketplace_entry(claude_marketplace, "workflow").get("version") is None


def test_setup_skill_uses_short_install_name() -> None:
    skill = _PLUGIN_ROOT / "skills" / "setup" / "SKILL.md"
    skill_dirs = sorted(path.parent.name for path in (_PLUGIN_ROOT / "skills").glob("*/SKILL.md"))

    assert skill.exists()
    assert (_PLUGIN_ROOT / "skills" / "setup" / "agents" / "openai.yaml").exists()
    assert skill_dirs == ["setup"]
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
