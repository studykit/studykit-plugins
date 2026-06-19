#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["PyYAML"]
# ///
"""Bootstrap repository-local workflow configuration.

The setup CLI builds and writes the repository-root ``.spectrack/config.yml``
used by the workflow plugin. It keeps provider choices explicit so setup does
not infer organization-specific Jira link types, custom fields, or cloud
deployment details from prose.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

_SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from command import CommandRunner, WorkflowCommandError, run_command  # noqa: E402
from config import (  # noqa: E402
    COMMIT_REF_STYLES,
    CONFIG_NAME,
    CONFIG_RELATIVE_PATH,
    ISSUE_PROVIDERS,
    KNOWLEDGE_PROVIDERS,
    PROVIDER_NATIVE_ISSUE_ID_FORMATS,
    ProviderConfig,
    WorkflowConfig,
    WorkflowConfigError,
    load_workflow_config,
    parse_workflow_config,
    validate_provider_for_role,
)
from env import workflow_project_dir_from_env  # noqa: E402
from issue.github.gh import GitHubRepositoryError, parse_github_remote_url  # noqa: E402
from prd_path import PrdPathError, normalize_prd_path  # noqa: E402
from issue.jira.client import (  # noqa: E402
    jira_data_center_createmeta_path,
    jira_data_center_issue_path,
    jira_data_center_site_from_provider_config,
    jira_data_center_transitions_path,
    jira_get_json,
)
from issue.jira.refs import JiraProviderError, normalize_jira_issue_key  # noqa: E402


class WorkflowSetupError(ValueError):
    """Raised when workflow setup input cannot produce a safe config."""


RELATIONSHIP_SURFACES = {"issue_link", "remote_link", "field"}
ISSUE_LINK_DIRECTIONS = {"inward", "outward"}
FIELD_WRITE_TARGETS = {"source", "target"}
FIELD_VALUE_KINDS = {"key", "key_object", "string"}
DEFAULT_JIRA_RELATIONSHIP_FIELD_QUERIES = ("parent",)

EPIC_FIELD_SCHEMA_CUSTOM_IDS: Mapping[str, str] = {
    "name": "com.pyxis.greenhopper.jira:gh-epic-label",
    "link": "com.pyxis.greenhopper.jira:gh-epic-link",
    "status": "com.pyxis.greenhopper.jira:gh-epic-status",
}
EPIC_FIELD_NAME_HINTS: Mapping[str, tuple[str, ...]] = {
    "name": ("epic name",),
    "link": ("epic link",),
    "status": ("epic status",),
}
EPIC_ISSUE_TYPE_NAME = "epic"


def probe_git_remote(
    project: Path,
    *,
    remote: str = "origin",
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Probe a Git remote and return a GitHub repository seed when possible."""

    try:
        result = run_command(
            ("git", "remote", "get-url", remote),
            cwd=project,
            runner=runner,
        )
        remote_url = result.stdout.strip()
        repo = parse_github_remote_url(remote_url)
    except (WorkflowCommandError, GitHubRepositoryError) as exc:
        return {
            "operation": "probe_git_remote",
            "detected": False,
            "remote": remote,
            "message": str(exc),
        }

    return {
        "operation": "probe_git_remote",
        "detected": True,
        "remote": remote,
        "remote_url": remote_url,
        "host": repo.host,
        "owner": repo.owner,
        "repo": repo.name,
        "slug": repo.slug,
    }


def provider_capabilities(
    *,
    issue_provider: str,
    knowledge_provider: str,
    jira_relationship_mappings: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Return setup-time capabilities and limitations for selected providers."""

    validate_provider_for_role("issue", issue_provider)
    validate_provider_for_role("knowledge", knowledge_provider)

    issues = _issue_capabilities(issue_provider, bool(jira_relationship_mappings))
    knowledge = _knowledge_capabilities(knowledge_provider)
    warnings = [*issues["warnings"], *knowledge["warnings"]]
    return {
        "operation": "capabilities",
        "issues": issues,
        "knowledge": knowledge,
        "warnings": warnings,
    }


def build_jira_relationship_mappings(
    *,
    issue_links: Sequence[str] = (),
    fields: Sequence[str] = (),
    remote_links: Sequence[str] = (),
    base_mappings: Mapping[str, Any] | None = None,
    remote_application_type: str | None = None,
    remote_application_name: str | None = None,
) -> dict[str, Any]:
    """Build explicit Jira relationship mappings from compact setup specs."""

    mappings: dict[str, Any] = dict(base_mappings or {})
    for spec in issue_links:
        relationship, link_type, direction = _parse_issue_link_mapping_spec(spec)
        mappings[relationship] = {
            "surface": "issue_link",
            "link_type": link_type,
            "direction": direction,
        }
    for spec in fields:
        relationship, field, write_to, value = _parse_field_mapping_spec(spec)
        mappings[relationship] = {
            "surface": "field",
            "field": field,
            "write_to": write_to,
            "value": value,
        }
    for spec in remote_links:
        relationship, relationship_label = _parse_remote_link_mapping_spec(spec)
        mapping = {
            "surface": "remote_link",
            "relationship_label": relationship_label,
        }
        _set_if_text(mapping, "application_type", remote_application_type)
        _set_if_text(mapping, "application_name", remote_application_name)
        mappings[relationship] = mapping

    _validate_relationship_mappings(mappings)
    warnings: list[str] = []
    if not mappings:
        warnings.append(
            "No Jira relationship mappings were provided; collect sample Jira issues, run jira-relationship-inspect, and confirm exact mappings before building Jira config"
        )
    return {
        "operation": "jira_relationship_mappings",
        "relationship_mappings": mappings,
        "yaml": _format_relationship_mappings_yaml(mappings),
        "warnings": warnings,
    }


def inspect_jira_relationships(
    *,
    jira_site: str,
    jira_deployment: str | None = "data_center",
    jira_api_version: str | None = "2",
    jira_project: str | None = None,
    issues: Sequence[str] = (),
    field_queries: Sequence[str] = (),
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Inspect Jira relationship surfaces without inferring config mappings."""

    settings: dict[str, Any] = {
        "site": jira_site,
        "deployment": jira_deployment or "data_center",
        "api_version": jira_api_version or "2",
    }
    _set_if_text(settings, "project", jira_project.upper() if jira_project else None)
    _reject_cloud_provider("Jira", settings)
    site = jira_data_center_site_from_provider_config(
        ProviderConfig(role="issue", kind="jira", settings=settings)
    )

    raw_link_types = jira_get_json(
        site,
        f"/rest/api/{site.api_version}/issueLinkType",
        runner=runner,
    )
    raw_fields = jira_get_json(site, f"/rest/api/{site.api_version}/field", runner=runner)

    link_types = _normalize_jira_link_types(raw_link_types)
    fields = _matching_jira_fields(
        raw_fields,
        field_queries or DEFAULT_JIRA_RELATIONSHIP_FIELD_QUERIES,
    )
    field_ids = tuple(field["id"] for field in fields if field.get("id"))
    sample_issues = [
        _inspect_jira_issue(site, issue, field_ids=field_ids, runner=runner)
        for issue in issues
    ]
    epic = _discover_jira_epic_metadata(
        site,
        raw_fields=raw_fields,
        project_key=site.project,
        runner=runner,
    )

    return {
        "operation": "jira_relationship_inspect",
        "site": site.to_json(),
        "link_types": link_types,
        "fields": fields,
        "epic": epic,
        "sample_issues": sample_issues,
        "warnings": [
            "Inspection reports observed Jira data only; choose relationship mappings explicitly before writing config"
        ],
    }


def inspect_jira_state_transitions(
    *,
    jira_site: str,
    jira_deployment: str | None = "data_center",
    jira_api_version: str | None = "2",
    issues: Sequence[str],
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Inspect Jira workflow transitions reachable from one or more sample issues."""

    if not issues:
        raise WorkflowSetupError("jira-state-transition-inspect requires at least one --issue")

    settings: dict[str, Any] = {
        "site": jira_site,
        "deployment": jira_deployment or "data_center",
        "api_version": jira_api_version or "2",
    }
    _reject_cloud_provider("Jira", settings)
    site = jira_data_center_site_from_provider_config(
        ProviderConfig(role="issue", kind="jira", settings=settings)
    )

    sample_issues: list[dict[str, Any]] = []
    observed_names: list[str] = []
    seen_names: set[str] = set()
    seen_signatures: set[tuple[tuple[str, str], ...]] = set()
    warnings: list[str] = []

    for issue_key in issues:
        normalized_key = normalize_jira_issue_key(issue_key)
        raw = jira_get_json(
            site,
            jira_data_center_transitions_path(site, normalized_key),
            runner=runner,
        )
        if isinstance(raw, Mapping):
            raw_transitions = raw.get("transitions")
        else:
            raw_transitions = raw
        normalized_transitions = _normalize_jira_transitions(raw_transitions)
        signature = tuple(
            sorted(
                (t.get("name", ""), t.get("to_status_name", ""))
                for t in normalized_transitions
            )
        )
        seen_signatures.add(signature)
        for transition in normalized_transitions:
            name = transition.get("name") or ""
            if name and name not in seen_names:
                seen_names.add(name)
                observed_names.append(name)
        sample_issues.append({"issue": normalized_key, "transitions": normalized_transitions})

    if len(seen_signatures) > 1:
        warnings.append(
            "Sample issues exposed different transition sets; confirm each verb against the matching workflow"
        )

    verb_owners: dict[str, list[str]] = {}
    for name in observed_names:
        verb = derive_state_transition_verb(name)
        if not verb:
            warnings.append(
                f"Transition {name!r} derives to an empty verb; specify it explicitly with --jira-state-transition"
            )
            continue
        if verb in RESERVED_STATE_TRANSITION_VERBS:
            warnings.append(
                f"Transition {name!r} derives to reserved verb {verb!r}; "
                "specify a different verb explicitly with --jira-state-transition"
            )
            continue
        verb_owners.setdefault(verb, []).append(name)
    auto_verbs: dict[str, str] = {}
    for verb, owners in verb_owners.items():
        if len(owners) == 1:
            auto_verbs[verb] = owners[0]
            continue
        joined = ", ".join(repr(name) for name in owners)
        warnings.append(
            f"Transitions {joined} all derive to verb {verb!r}; specify each explicitly with --jira-state-transition"
        )

    return {
        "operation": "jira_state_transition_inspect",
        "site": site.to_json(),
        "sample_issues": sample_issues,
        "observed_transition_names": observed_names,
        "auto_verbs": auto_verbs,
        "warnings": warnings,
    }


def build_config(
    *,
    project: Path,
    issue_provider: str,
    knowledge_provider: str,
    github_repo: str | None = None,
    github_host: str | None = None,
    github_issue_host: str | None = None,
    github_wiki_repo: str | None = None,
    github_wiki_host: str | None = None,
    github_wiki_path: str | None = None,
    github_wiki_prd_path: str | None = None,
    jira_site: str | None = None,
    jira_deployment: str | None = "data_center",
    jira_api_version: str | None = "2",
    jira_project: str | None = None,
    jira_issue_type: str | None = None,
    jira_epic_fields: Mapping[str, str] | None = None,
    jira_epic_issue_type: str | None = None,
    jira_relationship_mappings: Mapping[str, Any] | None = None,
    jira_state_transitions: Mapping[str, str] | None = None,
    jira_snapshot_hidden_comment_markers: Sequence[str] | None = None,
    filesystem_issues_path: str | None = None,
    commit_ref_style: str = "provider-native",
    commit_refs_enabled: bool = True,
    mode: str = "remote-native",
    probe_remote: bool = False,
    remote: str = "origin",
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Build a validated workflow config mapping."""

    validate_provider_for_role("issue", issue_provider)
    validate_provider_for_role("knowledge", knowledge_provider)

    if commit_ref_style not in COMMIT_REF_STYLES:
        choices = ", ".join(sorted(COMMIT_REF_STYLES))
        raise WorkflowSetupError(f"invalid commit reference style: {commit_ref_style}. Use one of: {choices}")

    probed_repo: str | None = None
    probed_host: str | None = None
    if probe_remote and (issue_provider == "github" or knowledge_provider == "github"):
        probe = probe_git_remote(project, remote=remote, runner=runner)
        if probe.get("detected"):
            probed_repo = str(probe["slug"])
            probed_host = str(probe["host"])

    probed_non_default_host = _non_default_github_host(probed_host)
    issue_github_host = github_issue_host or github_host or probed_non_default_host
    knowledge_github_host = github_wiki_host or github_host or probed_non_default_host

    normalized_epic_fields = _normalize_epic_fields(jira_epic_fields)
    normalized_epic_issue_type = _text(jira_epic_issue_type)
    effective_relationship_mappings = _augment_jira_relationship_mappings_with_epic(
        jira_relationship_mappings,
        epic_fields=normalized_epic_fields,
    )
    issues = _issue_provider_config(
        issue_provider,
        github_repo=github_repo or probed_repo,
        github_host=issue_github_host,
        jira_site=jira_site,
        jira_deployment=jira_deployment,
        jira_api_version=jira_api_version,
        jira_project=jira_project,
        jira_issue_type=jira_issue_type,
        jira_epic_fields=normalized_epic_fields,
        jira_epic_issue_type=normalized_epic_issue_type,
        jira_relationship_mappings=effective_relationship_mappings,
        jira_state_transitions=jira_state_transitions,
        jira_snapshot_hidden_comment_markers=jira_snapshot_hidden_comment_markers,
        filesystem_path=filesystem_issues_path,
    )
    try:
        normalized_prd_path = normalize_prd_path(github_wiki_prd_path)
    except PrdPathError as exc:
        raise WorkflowSetupError(str(exc)) from exc
    knowledge = _knowledge_provider_config(
        knowledge_provider,
        github_repo=github_wiki_repo or github_repo or probed_repo,
        github_host=knowledge_github_host,
        github_path=github_wiki_path,
        github_prd_path=normalized_prd_path or None,
    )

    if issue_provider == "jira":
        _reject_cloud_provider("Jira", issues)
        _require_jira_relationship_mappings(jira_relationship_mappings)
        _validate_relationship_mappings(jira_relationship_mappings)

    effective_commit_style = "disabled" if not commit_refs_enabled else commit_ref_style
    raw: dict[str, Any] = {
        "version": 1,
        "mode": mode,
        "providers": {
            "issues": issues,
            "knowledge": knowledge,
        },
        "issue_id_format": PROVIDER_NATIVE_ISSUE_ID_FORMATS[issue_provider],
        "commit_refs": {
            "enabled": commit_refs_enabled,
            "style": effective_commit_style,
        },
    }

    parse_workflow_config(raw, path=project / CONFIG_RELATIVE_PATH)
    return raw


def build_config_payload(raw: Mapping[str, Any], *, project: Path) -> dict[str, Any]:
    """Return the agent-facing payload for generated setup YAML."""

    config = parse_workflow_config(raw, path=project / CONFIG_RELATIVE_PATH)
    capabilities = provider_capabilities(
        issue_provider=config.issues.kind,
        knowledge_provider=config.knowledge.kind,
        jira_relationship_mappings=_mapping_or_none(config.issues.settings.get("relationship_mappings")),
    )
    return {
        "operation": "build_config",
        "path": str(project / CONFIG_RELATIVE_PATH),
        "yaml": format_config_yaml(raw),
        "config": config.to_json(),
        "capabilities": capabilities,
        "warnings": capabilities["warnings"],
    }


AGENTS_FILENAME = "AGENTS.md"
CLAUDE_FILENAME = "CLAUDE.md"
AGENTS_KNOWLEDGE_HEADING = "## Workflow Knowledge Root"
CLAUDE_AGENTS_SHIM = "@AGENTS.md\n"
CODEX_DIRNAME = ".codex"
CODEX_CONFIG_FILENAME = "config.toml"
CODEX_CONFIG_RELATIVE_PATH = f"{CODEX_DIRNAME}/{CODEX_CONFIG_FILENAME}"
CODEX_SPECTRACK_AGENT_DIR = f"{CODEX_DIRNAME}/spectrack/agents"
CODEX_AGENT_INSTALL_MARKER_BEGIN = "# BEGIN spectrack custom agents"
CODEX_AGENT_INSTALL_MARKER_END = "# END spectrack custom agents"
SPECTRACK_CODEX_AGENT_ROLES: Mapping[str, str] = {
    "implementation-auditor": "SpecTrack auditor that verifies an issue-implementer report against the issue, branch, commits, and Resume comment.",
    "issue-implementer": "SpecTrack implementer for an approved task, bug, or spike approach; implements, verifies Acceptance Criteria, commits, and refreshes Resume.",
    "mock-html-generator": "SpecTrack mock generator for throwaway HTML/CSS screen mockups grounded in selected usecase issues.",
    "resolution-auditor": "SpecTrack auditor that validates a recorded root cause and approach or fix against real code and git history.",
    "task-size-auditor": "SpecTrack auditor that checks whether a task body is correctly sized or should be split, promoted, or decomposed.",
    "usecase-explorer": "SpecTrack explorer that finds candidate use cases missed by an existing set of workflow usecase issues.",
    "usecase-reviewer": "SpecTrack reviewer that publishes review issues for quality findings in workflow usecase issues.",
}


def _knowledge_root_section(repo_relative: str, absolute: str) -> str:
    return (
        f"{AGENTS_KNOWLEDGE_HEADING}\n\n"
        f"Workflow knowledge pages live at `{repo_relative}` "
        f"(resolved: `{absolute}`).\n"
    )


def ensure_agents_knowledge_root(
    project: Path, config: WorkflowConfig
) -> dict[str, Any] | None:
    """Append the workflow knowledge-root section to ``AGENTS.md`` when applicable.

    The section is appended only when it is not already present. ``CLAUDE.md`` is
    auto-created as a sibling shim (``@AGENTS.md``) when missing, matching the
    project convention. Returns ``None`` when there is no configured knowledge
    path to surface.
    """

    if config.knowledge.kind != "github":
        return None
    raw_path = config.knowledge.settings.get("path")
    if not isinstance(raw_path, str) or not raw_path.strip():
        return None

    project = project.expanduser().resolve()
    repo_relative = raw_path.strip()
    absolute = str((project / repo_relative).resolve())
    section = _knowledge_root_section(repo_relative, absolute)

    agents_path = project / AGENTS_FILENAME
    if agents_path.exists():
        existing = agents_path.read_text(encoding="utf-8")
        if AGENTS_KNOWLEDGE_HEADING in existing:
            agents_action = "skip"
        else:
            separator = "" if existing.endswith("\n") else "\n"
            _atomic_write_text(agents_path, existing + separator + "\n" + section)
            agents_action = "append"
    else:
        _atomic_write_text(agents_path, section)
        agents_action = "create"

    claude_path = project / CLAUDE_FILENAME
    if claude_path.exists():
        claude_action = "skip"
    else:
        _atomic_write_text(claude_path, CLAUDE_AGENTS_SHIM)
        claude_action = "create"

    return {
        "agents_path": str(agents_path),
        "agents_action": agents_action,
        "claude_path": str(claude_path),
        "claude_action": claude_action,
        "knowledge_root": {
            "repo_relative": repo_relative,
            "absolute": absolute,
        },
    }


def install_codex_agents(project: Path) -> dict[str, Any]:
    """Install SpecTrack agents as project-local Codex custom agent roles."""

    project = project.expanduser().resolve()
    codex_dir = project / CODEX_DIRNAME
    role_dir = project / CODEX_SPECTRACK_AGENT_DIR
    codex_dir.mkdir(parents=True, exist_ok=True)
    role_dir.mkdir(parents=True, exist_ok=True)

    installed_roles: list[dict[str, str]] = []
    for agent_name in sorted(SPECTRACK_CODEX_AGENT_ROLES):
        source_path = Path(__file__).resolve().parent.parent / "agents" / f"{agent_name}.md"
        body = _load_agent_instruction_body(source_path)
        role_path = role_dir / f"{agent_name}.toml"
        role_text = _codex_agent_role_config(agent_name, body)
        role_action = _write_text_if_changed(role_path, role_text)
        installed_roles.append(
            {
                "name": f"spectrack:{agent_name}",
                "config_path": str(role_path),
                "source_path": str(source_path),
                "action": role_action,
            }
        )

    config_path = codex_dir / CODEX_CONFIG_FILENAME
    existing_config = config_path.read_text(encoding="utf-8") if config_path.exists() else ""
    role_block = _codex_agent_config_block()
    updated_config, config_action = _upsert_managed_block(
        existing_config,
        role_block,
        existed=config_path.exists(),
    )
    if config_action != "skip":
        _atomic_write_text(config_path, updated_config)

    return {
        "operation": "install_codex_agents",
        "config_path": str(config_path),
        "config_action": config_action,
        "agent_dir": str(role_dir),
        "agents": installed_roles,
        "restart_required": True,
    }


def _load_agent_instruction_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return text.strip() + "\n"
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise WorkflowSetupError(f"invalid agent frontmatter in {path}")
    return parts[2].lstrip()


def _codex_agent_role_config(agent_name: str, body: str) -> str:
    instructions = (
        f"You are running as the SpecTrack `spectrack:{agent_name}` custom agent in Codex.\n\n"
        "Follow the role instructions below. If the role text names Claude-style "
        "tool labels, use the equivalent Codex tools available in this session. "
        "SpecTrack hooks inject launcher, provider, and per-agent policy context "
        "at SubagentStart; prefer that injected runtime context for command usage.\n\n"
        f"{body.strip()}\n"
    )
    return (
        "# Generated by `spectrack setup.py install-codex-agents`.\n"
        "# Re-run setup to refresh this role from the installed SpecTrack plugin.\n"
        f"developer_instructions = {_toml_literal_multiline_string(instructions)}\n\n"
        "[features]\n"
        "apps = false\n\n"
        "[apps._default]\n"
        "enabled = false\n"
    )


def _codex_agent_config_block() -> str:
    lines = [
        CODEX_AGENT_INSTALL_MARKER_BEGIN,
        "# Generated by SpecTrack setup. Re-run `spectrack setup.py install-codex-agents` to refresh.",
    ]
    for agent_name in sorted(SPECTRACK_CODEX_AGENT_ROLES):
        role_name = f"spectrack:{agent_name}"
        lines.extend(
            [
                "",
                f"[agents.{_toml_quoted_key(role_name)}]",
                f"description = {_toml_basic_string(SPECTRACK_CODEX_AGENT_ROLES[agent_name])}",
                f"config_file = {_toml_basic_string(f'spectrack/agents/{agent_name}.toml')}",
            ]
        )
    lines.append(CODEX_AGENT_INSTALL_MARKER_END)
    return "\n".join(lines).rstrip() + "\n"


def _upsert_managed_block(
    existing: str,
    block: str,
    *,
    existed: bool,
) -> tuple[str, str]:
    if not existing.strip():
        return block, "create"

    pattern = re.compile(
        rf"{re.escape(CODEX_AGENT_INSTALL_MARKER_BEGIN)}.*?{re.escape(CODEX_AGENT_INSTALL_MARKER_END)}\n?",
        re.DOTALL,
    )
    replacement = block if block.endswith("\n") else block + "\n"
    if pattern.search(existing):
        updated = pattern.sub(replacement, existing, count=1)
        action = "skip" if updated == existing else "update"
        return updated, action

    separator = "\n" if existing.endswith("\n") else "\n\n"
    return existing + separator + replacement, "append" if existed else "create"


def _write_text_if_changed(path: Path, text: str) -> str:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return "skip"
    action = "update" if path.exists() else "create"
    _atomic_write_text(path, text)
    return action


def _toml_quoted_key(value: str) -> str:
    return json.dumps(value, ensure_ascii=True)


def _toml_basic_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=True)


def _toml_literal_multiline_string(value: str) -> str:
    if "'''" in value:
        raise WorkflowSetupError("generated Codex agent instructions cannot contain triple single quotes")
    return "'''\n" + value.rstrip() + "\n'''"


def write_config(
    project: Path,
    raw: Mapping[str, Any],
    *,
    force: bool = False,
) -> dict[str, Any]:
    """Atomically write ``.spectrack/config.yml`` and verify it with the loader."""

    project = project.expanduser().resolve()
    target = project / CONFIG_RELATIVE_PATH
    config = parse_workflow_config(raw, path=target)
    if config.issues.kind == "jira":
        mappings = _mapping_or_none(config.issues.settings.get("relationship_mappings"))
        _require_jira_relationship_mappings(mappings)
        _validate_relationship_mappings(mappings)

    if target.exists() and not force:
        raise WorkflowSetupError(
            f"{CONFIG_NAME} already exists; pass --force only after explicit overwrite confirmation. "
            f"Existing summary: {json.dumps(existing_config_summary(project), sort_keys=True)}"
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write_text(target, format_config_yaml(raw))
    verified = load_workflow_config(project, require=True)
    if verified is None:
        raise WorkflowSetupError(f"{CONFIG_NAME} was written but could not be verified")

    result: dict[str, Any] = {
        "operation": "write",
        "path": str(target),
        "verified": True,
        "verification": {
            "command": "config.py --require",
            "config": verified.to_json(),
        },
    }
    agents_update = ensure_agents_knowledge_root(project, verified)
    if agents_update is not None:
        result["agents_md"] = agents_update
    result["codex_agents"] = install_codex_agents(project)
    return result


def existing_config_summary(project: Path) -> dict[str, Any]:
    """Return a compact summary of the existing config, even if invalid."""

    path = project.expanduser().resolve() / CONFIG_RELATIVE_PATH
    summary: dict[str, Any] = {"path": str(path), "exists": path.exists()}
    if not path.exists():
        return summary
    try:
        config = load_workflow_config(project, require=True)
    except WorkflowConfigError as exc:
        summary.update({"valid": False, "error": str(exc)})
        return summary
    assert config is not None
    summary.update(
        {
            "valid": True,
            "issues": config.issues.kind,
            "knowledge": config.knowledge.kind,
            "commit_refs": config.commit_refs.style,
        }
    )
    return summary


def profile_from_docs(paths: Sequence[Path], *, stdin_text: str | None = None) -> dict[str, Any]:
    """Extract setup defaults from explicit provider profile documents."""

    defaults: dict[str, Any] = {}
    sources: dict[str, str] = {}
    ignored: list[dict[str, str]] = []
    warnings: list[str] = []

    documents: list[tuple[str, str]] = []
    for path in paths:
        try:
            documents.append((str(path), path.read_text(encoding="utf-8")))
        except OSError as exc:
            ignored.append({"source": str(path), "reason": str(exc)})
    if stdin_text is not None:
        documents.append(("<stdin>", stdin_text))

    for source, text in documents:
        if not _looks_like_provider_profile(text):
            ignored.append({"source": source, "reason": "not a workflow provider profile"})
            continue
        extracted = _extract_profile_defaults(text)
        if not extracted:
            ignored.append({"source": source, "reason": "no setup defaults found"})
            continue
        for key, value in extracted.items():
            if key not in defaults and value not in (None, ""):
                defaults[key] = value
                sources[key] = source

    jira_deployment = defaults.get("jira_deployment")
    if isinstance(jira_deployment, str) and _is_cloud_deployment(jira_deployment):
        warnings.append("Jira Cloud was found in provider profile defaults, but only Data Center or Server is supported")

    jira_site = defaults.get("jira_site")
    if isinstance(jira_site, str) and _is_atlassian_cloud_site(jira_site):
        warnings.append("Jira atlassian.net site was found in provider profile defaults, but Cloud is unsupported")

    return {
        "operation": "profile_from_docs",
        "defaults": defaults,
        "sources": sources,
        "ignored": ignored,
        "warnings": warnings,
    }


def format_config_yaml(raw: Mapping[str, Any]) -> str:
    """Format setup YAML with stable key order."""

    return yaml.safe_dump(dict(raw), sort_keys=False, allow_unicode=False)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    probe = subparsers.add_parser("probe-git-remote", help="probe a GitHub repository from a git remote")
    probe.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    probe.add_argument("--remote", default="origin", help="git remote name")
    probe.add_argument("--require", action="store_true", help="fail when no GitHub remote can be detected")

    profile = subparsers.add_parser("profile-from-docs", help="extract setup defaults from provider profile docs")
    profile.add_argument("paths", nargs="*", type=Path, help="profile document paths")
    profile.add_argument("--stdin", action="store_true", help="read an additional provider profile from stdin")

    capabilities = subparsers.add_parser("capabilities", help="show provider capabilities and setup warnings")
    capabilities.add_argument("--issue-provider", required=True, choices=sorted(ISSUE_PROVIDERS))
    capabilities.add_argument("--knowledge-provider", required=True, choices=sorted(KNOWLEDGE_PROVIDERS))
    capabilities.add_argument("--jira-relationship-mappings-json")
    capabilities.add_argument("--jira-relationship-mappings-file", type=Path)
    capabilities.add_argument("--jira-relationship-mapping", action="append", default=[])

    jira_inspect = subparsers.add_parser(
        "jira-relationship-inspect",
        help="inspect Jira link types, relationship fields, and sample issue relationship data",
    )
    jira_inspect.add_argument("--jira-site", required=True, help="Jira Data Center or Server base URL")
    jira_inspect.add_argument("--jira-deployment", default="data_center", help="Jira deployment; Cloud is unsupported")
    jira_inspect.add_argument("--jira-api-version", default="2", help="Jira REST API version")
    jira_inspect.add_argument("--jira-project", help="Jira project key")
    jira_inspect.add_argument("--issue", action="append", default=[], help="sample Jira issue key to inspect")
    jira_inspect.add_argument(
        "--field-query",
        action="append",
        default=[],
        help="field name/id text to include, e.g. parent or customfield_12345",
    )

    jira_state_inspect = subparsers.add_parser(
        "jira-state-transition-inspect",
        help="inspect Jira workflow transitions reachable from sample issues",
    )
    jira_state_inspect.add_argument("--jira-site", required=True, help="Jira Data Center or Server base URL")
    jira_state_inspect.add_argument("--jira-deployment", default="data_center", help="Jira deployment; Cloud is unsupported")
    jira_state_inspect.add_argument("--jira-api-version", default="2", help="Jira REST API version")
    jira_state_inspect.add_argument(
        "--issue",
        action="append",
        default=[],
        required=True,
        help="sample Jira issue key to inspect; supply open- and closed-side keys to see both directions",
    )

    jira_mappings = subparsers.add_parser(
        "jira-relationship-mappings",
        help="build explicit Jira relationship mapping YAML from compact specs",
    )
    jira_mappings.add_argument(
        "--issue-link",
        action="append",
        default=[],
        help="relationship=link_type:direction, e.g. blocked_by=Blocks:inward",
    )
    jira_mappings.add_argument(
        "--field",
        action="append",
        default=[],
        help="relationship=field:write_to:value, e.g. custom_relation=customfield_12345:source:string or child=parent:target:key",
    )
    jira_mappings.add_argument(
        "--remote-link",
        action="append",
        default=[],
        help="relationship=relationship_label, e.g. related='relates to'",
    )
    jira_mappings.add_argument("--remote-application-type")
    jira_mappings.add_argument("--remote-application-name")
    jira_mappings.add_argument("--jira-relationship-mappings-json")
    jira_mappings.add_argument("--jira-relationship-mappings-file", type=Path)
    jira_mappings.add_argument("--jira-relationship-mapping", action="append", default=[])

    build = subparsers.add_parser("build-config", help=f"build and validate {CONFIG_NAME} YAML")
    _add_config_build_args(build)

    write = subparsers.add_parser("write", help=f"write {CONFIG_NAME} atomically")
    _add_config_build_args(write)
    write.add_argument("--config", type=Path, help="YAML config to write; use '-' for stdin")
    write.add_argument("--force", action="store_true", help="overwrite an existing config after explicit confirmation")
    codex_agents = subparsers.add_parser(
        "install-codex-agents",
        help="install SpecTrack custom agent roles into the project .codex/config.toml",
    )
    codex_agents.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")

    return parser


def main(argv: list[str] | None = None, *, stdout: Any = sys.stdout, stderr: Any = sys.stderr) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        payload = _dispatch(args)
    except (WorkflowSetupError, WorkflowConfigError, JiraProviderError) as exc:
        print(f"workflow setup error: {exc}", file=stderr)
        return 2

    _emit_payload(payload, stdout=stdout)
    if args.command == "probe-git-remote" and args.require and not payload.get("detected"):
        return 1
    return 0


def _dispatch(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "probe-git-remote":
        return probe_git_remote(args.project, remote=args.remote)
    if args.command == "profile-from-docs":
        stdin_text = sys.stdin.read() if args.stdin else None
        return profile_from_docs(args.paths, stdin_text=stdin_text)
    if args.command == "capabilities":
        mappings = _relationship_mappings_from_args(args)
        if mappings is not None:
            _validate_relationship_mappings(mappings)
        return provider_capabilities(
            issue_provider=args.issue_provider,
            knowledge_provider=args.knowledge_provider,
            jira_relationship_mappings=mappings,
        )
    if args.command == "jira-relationship-inspect":
        return inspect_jira_relationships(
            jira_site=args.jira_site,
            jira_deployment=args.jira_deployment,
            jira_api_version=args.jira_api_version,
            jira_project=args.jira_project,
            issues=args.issue,
            field_queries=args.field_query,
        )
    if args.command == "jira-state-transition-inspect":
        return inspect_jira_state_transitions(
            jira_site=args.jira_site,
            jira_deployment=args.jira_deployment,
            jira_api_version=args.jira_api_version,
            issues=args.issue,
        )
    if args.command == "jira-relationship-mappings":
        return build_jira_relationship_mappings(
            issue_links=args.issue_link,
            fields=args.field,
            remote_links=args.remote_link,
            base_mappings=_relationship_mappings_from_args(args),
            remote_application_type=args.remote_application_type,
            remote_application_name=args.remote_application_name,
        )
    if args.command == "build-config":
        raw = _config_from_args(args)
        return build_config_payload(raw, project=args.project)
    if args.command == "write":
        raw = _raw_config_for_write(args)
        return write_config(args.project, raw, force=args.force)
    if args.command == "install-codex-agents":
        return install_codex_agents(args.project)
    raise WorkflowSetupError(f"unsupported command: {args.command}")


def _add_config_build_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--mode", default="remote-native", help="workflow mode")
    parser.add_argument("--issue-provider", choices=sorted(ISSUE_PROVIDERS), help="explicit issue provider")
    parser.add_argument("--knowledge-provider", choices=sorted(KNOWLEDGE_PROVIDERS), help="explicit knowledge provider")
    parser.add_argument("--probe-git-remote", action="store_true", help="seed GitHub repo settings from a git remote")
    parser.add_argument("--remote", default="origin", help="git remote name used with --probe-git-remote")
    parser.add_argument("--github-repo", help="GitHub issue repository slug, e.g. owner/repo")
    parser.add_argument("--github-host", help="shared GitHub host fallback when issue and wiki hosts are the same")
    parser.add_argument("--github-issue-host", help="GitHub issue provider host when it differs from the wiki host")
    parser.add_argument("--github-wiki-repo", help="GitHub knowledge repository slug when different from issue repo")
    parser.add_argument("--github-wiki-host", help="GitHub knowledge/wiki repository host when it differs from the issue host")
    parser.add_argument("--github-wiki-path", help="GitHub knowledge repository directory path (required for the github knowledge provider; no default is assumed)")
    parser.add_argument(
        "--github-wiki-prd-path",
        help=(
            "GitHub knowledge PRD subdirectory, relative to --github-wiki-path. "
            "Optional; when omitted, PRD pages sit at the knowledge folder root. "
            "Must not be absolute and must not contain '..'."
        ),
    )
    parser.add_argument("--jira-site", help="Jira Data Center or Server base URL")
    parser.add_argument("--jira-deployment", default="data_center", help="Jira deployment; Cloud is unsupported")
    parser.add_argument("--jira-api-version", default="2", help="Jira REST API version")
    parser.add_argument("--jira-project", help="Jira project key")
    parser.add_argument("--jira-issue-type", help="Jira issue type")
    parser.add_argument(
        "--jira-epic-issue-type",
        help="Jira Epic issue type name when it differs from the built-in default 'Epic'",
    )
    parser.add_argument(
        "--jira-epic-field-name",
        help="Jira Epic Name customfield id (writes providers.issues.epic_fields.name)",
    )
    parser.add_argument(
        "--jira-epic-field-link",
        help="Jira Epic Link customfield id (writes providers.issues.epic_fields.link)",
    )
    parser.add_argument(
        "--jira-epic-field-status",
        help="Jira Epic Status customfield id (writes providers.issues.epic_fields.status)",
    )
    parser.add_argument(
        "--jira-state-transition",
        action="append",
        default=[],
        help="repeatable verb to transition-name mapping, e.g. close=Closed or in-progress='In Progress' (writes providers.issues.state_transitions.<verb>; overrides auto-derived verbs from jira-state-transition-inspect)",
    )
    parser.add_argument(
        "--jira-snapshot-hidden-comment-marker",
        action="append",
        default=[],
        help="repeatable comment body marker excluded from cached Jira comment-*.md files, e.g. !git-event",
    )
    parser.add_argument("--jira-relationship-mappings-json", help="YAML/JSON mapping for Jira relationship writes")
    parser.add_argument("--jira-relationship-mappings-file", type=Path, help="file containing Jira relationship mappings")
    parser.add_argument(
        "--jira-relationship-mapping",
        action="append",
        default=[],
        help="repeatable mapping, e.g. blocked_by:surface=issue_link,link_type=Blocks,direction=inward",
    )
    parser.add_argument("--filesystem-issues-path", default="workflow/issues", help="filesystem issue provider path")
    parser.add_argument("--commit-ref-style", choices=sorted(COMMIT_REF_STYLES), default="provider-native")
    parser.add_argument("--disable-commit-refs", action="store_true", help="disable commit references")


def _config_from_args(args: argparse.Namespace) -> dict[str, Any]:
    issue_provider = _explicit_provider_arg(args, "issue_provider", role="issue")
    knowledge_provider = _explicit_provider_arg(args, "knowledge_provider", role="knowledge")
    return build_config(
        project=args.project,
        issue_provider=issue_provider,
        knowledge_provider=knowledge_provider,
        github_repo=args.github_repo,
        github_host=args.github_host,
        github_issue_host=args.github_issue_host,
        github_wiki_repo=args.github_wiki_repo,
        github_wiki_host=args.github_wiki_host,
        github_wiki_path=args.github_wiki_path,
        github_wiki_prd_path=args.github_wiki_prd_path,
        jira_site=args.jira_site,
        jira_deployment=args.jira_deployment,
        jira_api_version=args.jira_api_version,
        jira_project=args.jira_project,
        jira_issue_type=args.jira_issue_type,
        jira_epic_issue_type=args.jira_epic_issue_type,
        jira_epic_fields=_jira_epic_fields_from_args(args),
        jira_relationship_mappings=_relationship_mappings_from_args(args),
        jira_state_transitions=_jira_state_transitions_from_args(args),
        jira_snapshot_hidden_comment_markers=_jira_snapshot_hidden_comment_markers_from_args(args),
        filesystem_issues_path=args.filesystem_issues_path,
        commit_ref_style=args.commit_ref_style,
        commit_refs_enabled=not args.disable_commit_refs,
        mode=args.mode,
        probe_remote=args.probe_git_remote,
        remote=args.remote,
    )


def _explicit_provider_arg(args: argparse.Namespace, name: str, *, role: str) -> str:
    value = getattr(args, name, None)
    if value:
        return value
    flag = f"--{name.replace('_', '-')}"
    raise WorkflowSetupError(f"{flag} is required; collect the {role} provider explicitly before building config")


def _raw_config_for_write(args: argparse.Namespace) -> Mapping[str, Any]:
    if args.config is None:
        return _config_from_args(args)
    if str(args.config) == "-":
        text = sys.stdin.read()
    else:
        text = args.config.read_text(encoding="utf-8")
    raw = yaml.safe_load(text)
    if not isinstance(raw, Mapping):
        raise WorkflowSetupError("config input must be a YAML mapping")
    parse_workflow_config(raw, path=args.project / CONFIG_RELATIVE_PATH)
    return raw


def _emit_payload(payload: Mapping[str, Any], *, stdout: Any) -> None:
    print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)


def _issue_provider_config(
    provider: str,
    *,
    github_repo: str | None,
    github_host: str | None,
    jira_site: str | None,
    jira_deployment: str | None,
    jira_api_version: str | None,
    jira_project: str | None,
    jira_issue_type: str | None,
    jira_epic_fields: Mapping[str, str] | None,
    jira_epic_issue_type: str | None,
    jira_relationship_mappings: Mapping[str, Any] | None,
    jira_state_transitions: Mapping[str, str] | None,
    jira_snapshot_hidden_comment_markers: Sequence[str] | None,
    filesystem_path: str | None,
) -> dict[str, Any]:
    settings: dict[str, Any] = {"kind": provider}
    if provider == "github":
        _set_if_text(settings, "repo", github_repo)
        _set_if_text(settings, "host", github_host)
    elif provider == "jira":
        _set_if_text(settings, "site", jira_site)
        _set_if_text(settings, "deployment", jira_deployment or "data_center")
        _set_if_text(settings, "api_version", jira_api_version or "2")
        _set_if_text(settings, "project", jira_project.upper() if jira_project else None)
        _set_if_text(settings, "issue_type", jira_issue_type)
        if jira_epic_issue_type and jira_epic_issue_type != "Epic":
            settings["artifact_issue_types"] = {"epic": jira_epic_issue_type}
        if jira_epic_fields:
            settings["epic_fields"] = dict(jira_epic_fields)
        hidden_markers = _normalized_string_tuple(jira_snapshot_hidden_comment_markers)
        if hidden_markers:
            settings["snapshot"] = {"hidden_comment_markers": list(hidden_markers)}
        if jira_relationship_mappings:
            settings["relationship_mappings"] = dict(jira_relationship_mappings)
        if jira_state_transitions:
            settings["state_transitions"] = dict(jira_state_transitions)
    elif provider == "filesystem":
        _set_if_text(settings, "path", filesystem_path or "workflow/issues")
    return settings


def _knowledge_provider_config(
    provider: str,
    *,
    github_repo: str | None,
    github_host: str | None,
    github_path: str | None,
    github_prd_path: str | None = None,
) -> dict[str, Any]:
    settings: dict[str, Any] = {"kind": provider}
    if provider == "github":
        _set_if_text(settings, "repo", github_repo)
        _set_if_text(settings, "host", github_host)
        _set_if_text(settings, "path", github_path)
        _set_if_text(settings, "prd_path", github_prd_path)
    return settings


def _issue_capabilities(provider: str, has_jira_mappings: bool) -> dict[str, Any]:
    if provider == "github":
        limitations = ["requires GitHub CLI authentication and a resolvable repository"]
        warnings: list[str] = []
        return {
            "provider": provider,
            "native_transport": True,
            "reads": True,
            "writes": True,
            "relationship_writes": True,
            "limitations": limitations,
            "warnings": warnings,
        }
    if provider == "jira":
        limitations = [
            "Jira Cloud is unsupported; use Data Center or Server",
            "metadata writes require explicit workflow metadata mappings",
        ]
        warnings = ["Jira setup targets Data Center or Server only"]
        if not has_jira_mappings:
            warnings.append(
                "Jira issue provider setup is incomplete until providers.issues.relationship_mappings is filled from inspected site data; run jira-relationship-inspect, confirm exact mappings, and pass them to build-config"
            )
        return {
            "provider": provider,
            "native_transport": True,
            "reads": True,
            "writes": True,
            "relationship_writes": has_jira_mappings,
            "limitations": limitations,
            "warnings": warnings,
        }
    return {
        "provider": provider,
        "native_transport": False,
        "reads": "config-only",
        "writes": "config-only",
        "relationship_writes": False,
        "limitations": ["filesystem issue provider config is accepted, but native issue provider commands are not registered yet"],
        "warnings": ["filesystem issue provider operations are limited to local configuration/projection until provider commands are registered"],
    }


def _knowledge_capabilities(provider: str) -> dict[str, Any]:
    return {
        "provider": provider,
        "native_transport": False,
        "reads": "config-only",
        "writes": False,
        "metadata_writes": False,
        "limitations": ["GitHub repository wiki knowledge provider commands are not registered yet"],
        "warnings": ["GitHub knowledge writes are not implemented by the native provider registry yet"],
    }


def _format_relationship_mappings_yaml(mappings: Mapping[str, Any]) -> str:
    return yaml.safe_dump(dict(mappings), sort_keys=False, allow_unicode=False)


def _parse_issue_link_mapping_spec(value: str) -> tuple[str, str, str]:
    relationship, raw = _split_relationship_assignment(value, "issue-link")
    parts = [part.strip() for part in raw.split(":")]
    if len(parts) != 2 or not all(parts):
        raise WorkflowSetupError("issue-link mapping must be relationship=link_type:direction")
    direction = _normalize_token(parts[1])
    if direction not in ISSUE_LINK_DIRECTIONS:
        raise WorkflowSetupError("issue-link mapping direction must be inward or outward")
    return relationship, parts[0], direction


def _parse_field_mapping_spec(value: str) -> tuple[str, str, str, str]:
    relationship, raw = _split_relationship_assignment(value, "field")
    parts = [part.strip() for part in raw.split(":")]
    if len(parts) != 3 or not all(parts):
        raise WorkflowSetupError("field mapping must be relationship=field:write_to:value")
    write_to = _normalize_token(parts[1])
    if write_to not in FIELD_WRITE_TARGETS:
        raise WorkflowSetupError("field mapping write_to must be source or target")
    value_kind = _normalize_token(parts[2])
    if value_kind not in FIELD_VALUE_KINDS:
        raise WorkflowSetupError("field mapping value must be key, key_object, or string")
    return relationship, parts[0], write_to, value_kind


def _parse_remote_link_mapping_spec(value: str) -> tuple[str, str]:
    relationship, relationship_label = _split_relationship_assignment(value, "remote-link")
    if not relationship_label:
        raise WorkflowSetupError("remote-link mapping requires a relationship label")
    return relationship, relationship_label


def _split_relationship_assignment(value: str, kind: str) -> tuple[str, str]:
    text = value.strip()
    if "=" in text:
        relationship, raw = text.split("=", 1)
    elif ":" in text:
        relationship, raw = text.split(":", 1)
    else:
        raise WorkflowSetupError(f"{kind} mapping must start with relationship=")
    relationship = relationship.strip().lower().replace("-", "_")
    if not relationship:
        raise WorkflowSetupError(f"{kind} mapping requires a relationship name")
    raw = raw.strip()
    if not raw:
        raise WorkflowSetupError(f"{kind} mapping requires a value")
    return relationship, raw


def _normalize_jira_transitions(raw_transitions: Any) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    if not isinstance(raw_transitions, list):
        return result
    for item in raw_transitions:
        if not isinstance(item, Mapping):
            continue
        entry: dict[str, str] = {}
        _set_if_text(entry, "id", _text(item.get("id")))
        _set_if_text(entry, "name", _text(item.get("name")))
        to_block = item.get("to")
        if isinstance(to_block, Mapping):
            _set_if_text(entry, "to_status_name", _text(to_block.get("name")))
            _set_if_text(entry, "to_status_id", _text(to_block.get("id")))
            category = to_block.get("statusCategory")
            if isinstance(category, Mapping):
                _set_if_text(entry, "to_status_category", _text(category.get("key")))
        if entry:
            result.append(entry)
    return result


def _normalize_jira_link_types(raw_link_types: Any) -> list[dict[str, str]]:
    if isinstance(raw_link_types, Mapping):
        items = raw_link_types.get("issueLinkTypes")
    else:
        items = raw_link_types
    result: list[dict[str, str]] = []
    if not isinstance(items, list):
        return result
    for item in items:
        if not isinstance(item, Mapping):
            continue
        entry: dict[str, str] = {}
        _set_if_text(entry, "name", _text(item.get("name")))
        _set_if_text(entry, "inward", _text(item.get("inward")))
        _set_if_text(entry, "outward", _text(item.get("outward")))
        if entry:
            result.append(entry)
    return result


def _discover_jira_epic_metadata(
    site: Any,
    *,
    raw_fields: Any,
    project_key: str | None,
    runner: CommandRunner | None,
) -> dict[str, Any]:
    """Discover Jira Software Epic field ids and issue-type Epic Link support."""

    fields = _discover_epic_field_ids(raw_fields)
    field_warnings: list[str] = []
    for kind in EPIC_FIELD_SCHEMA_CUSTOM_IDS:
        if fields.get(kind) is None:
            field_warnings.append(
                f"Epic {kind} customfield was not discovered; the site may not have Jira Software installed or uses non-default field schema"
            )

    issue_types: list[dict[str, str]] = []
    issue_type_epic_link_support: list[dict[str, Any]] = []
    createmeta_warnings: list[str] = []
    if not project_key:
        createmeta_warnings.append(
            "Epic issue-type discovery skipped; supply --jira-project to fetch createmeta"
        )
    else:
        try:
            raw_createmeta = jira_get_json(
                site,
                jira_data_center_createmeta_path(
                    site, project_key=project_key, expand_fields=True
                ),
                runner=runner,
            )
        except (JiraProviderError, WorkflowCommandError) as exc:
            createmeta_warnings.append(f"createmeta fetch failed: {exc}")
        else:
            link_field_id = fields["link"]["id"] if fields.get("link") else None
            issue_types, issue_type_epic_link_support = _parse_jira_createmeta_epic_support(
                raw_createmeta,
                project_key=project_key,
                epic_link_field_id=link_field_id,
            )
            if not issue_types:
                createmeta_warnings.append(
                    "No candidate Epic issue type found in createmeta; pass --jira-epic-issue-type to override"
                )

    return {
        "fields": fields,
        "issue_types": issue_types,
        "issue_type_epic_link_support": issue_type_epic_link_support,
        "warnings": [*field_warnings, *createmeta_warnings],
    }


def _discover_epic_field_ids(raw_fields: Any) -> dict[str, dict[str, str] | None]:
    """Locate Epic Name / Link / Status field ids by Greenhopper schema or name."""

    items = raw_fields if isinstance(raw_fields, list) else []
    schema_matches: dict[str, dict[str, str]] = {}
    name_matches: dict[str, dict[str, str]] = {}
    for item in items:
        if not isinstance(item, Mapping):
            continue
        field_id = _text(item.get("id"))
        name = _text(item.get("name"))
        if not field_id:
            continue
        schema_custom = _text(_dig_text_path(item, ("schema", "custom")))
        for kind, schema_id in EPIC_FIELD_SCHEMA_CUSTOM_IDS.items():
            if schema_custom and schema_custom == schema_id and kind not in schema_matches:
                schema_matches[kind] = {
                    "id": field_id,
                    "name": name or "",
                    "matched_by": "schema",
                }
        if name:
            normalized_name = name.strip().lower()
            for kind, hints in EPIC_FIELD_NAME_HINTS.items():
                if kind in schema_matches or kind in name_matches:
                    continue
                if normalized_name in hints:
                    name_matches[kind] = {
                        "id": field_id,
                        "name": name,
                        "matched_by": "name",
                    }

    discovered: dict[str, dict[str, str] | None] = {}
    for kind in EPIC_FIELD_SCHEMA_CUSTOM_IDS:
        match = schema_matches.get(kind) or name_matches.get(kind)
        discovered[kind] = {key: value for key, value in match.items() if value} if match else None
    return discovered


def _parse_jira_createmeta_epic_support(
    raw_createmeta: Any,
    *,
    project_key: str,
    epic_link_field_id: str | None,
) -> tuple[list[dict[str, str]], list[dict[str, Any]]]:
    if not isinstance(raw_createmeta, Mapping):
        return [], []
    projects = raw_createmeta.get("projects")
    if not isinstance(projects, list):
        return [], []
    normalized_key = project_key.strip().upper()
    selected: Mapping[str, Any] | None = None
    for entry in projects:
        if not isinstance(entry, Mapping):
            continue
        key = _text(entry.get("key"))
        if key and key.upper() == normalized_key:
            selected = entry
            break
    if selected is None and projects:
        first = projects[0]
        if isinstance(first, Mapping):
            selected = first
    if selected is None:
        return [], []

    issue_types_raw = selected.get("issuetypes")
    if not isinstance(issue_types_raw, list):
        return [], []

    epic_issue_types: list[dict[str, str]] = []
    epic_link_support: list[dict[str, Any]] = []
    for entry in issue_types_raw:
        if not isinstance(entry, Mapping):
            continue
        type_id = _text(entry.get("id"))
        type_name = _text(entry.get("name"))
        if not type_name:
            continue
        normalized = type_name.lower()
        record: dict[str, str] = {"name": type_name}
        if type_id:
            record["id"] = type_id
        if normalized == EPIC_ISSUE_TYPE_NAME:
            epic_issue_types.append(record)
        supports = _issue_type_supports_epic_link(entry, epic_link_field_id)
        if supports is not None:
            epic_link_support.append({**record, "supports_epic_link": supports})
    return epic_issue_types, epic_link_support


def _issue_type_supports_epic_link(
    issue_type_entry: Mapping[str, Any],
    epic_link_field_id: str | None,
) -> bool | None:
    fields = issue_type_entry.get("fields")
    if not isinstance(fields, Mapping):
        return None
    if not epic_link_field_id:
        return None
    return epic_link_field_id in fields


def _dig_text_path(mapping: Mapping[str, Any], path: Sequence[str]) -> Any:
    current: Any = mapping
    for key in path:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _matching_jira_fields(raw_fields: Any, queries: Sequence[str]) -> list[dict[str, str]]:
    if not isinstance(raw_fields, list):
        return []
    normalized_queries = tuple(query.strip().lower() for query in queries if query.strip())
    result: list[dict[str, str]] = []
    for item in raw_fields:
        if not isinstance(item, Mapping):
            continue
        field_id = _text(item.get("id"))
        name = _text(item.get("name"))
        searchable = " ".join(part for part in (field_id, name) if part).lower()
        if normalized_queries and not any(query in searchable for query in normalized_queries):
            continue
        entry: dict[str, str] = {}
        _set_if_text(entry, "id", field_id)
        _set_if_text(entry, "name", name)
        if entry:
            result.append(entry)
    return result


def _inspect_jira_issue(
    site: Any,
    issue: str,
    *,
    field_ids: Sequence[str],
    runner: CommandRunner | None,
) -> dict[str, Any]:
    issue_key = normalize_jira_issue_key(issue)
    fields = ("summary", "issuetype", "parent", "subtasks", "issuelinks", *field_ids)
    unique_fields = ",".join(dict.fromkeys(fields))
    raw_issue = jira_get_json(
        site,
        f"{jira_data_center_issue_path(site, issue_key)}?fields={unique_fields}",
        runner=runner,
    )
    return _summarize_jira_issue_relationships(raw_issue, field_ids=field_ids)


def _summarize_jira_issue_relationships(raw_issue: Any, *, field_ids: Sequence[str]) -> dict[str, Any]:
    if not isinstance(raw_issue, Mapping):
        raise WorkflowSetupError("Jira issue response was not an object")
    fields = raw_issue.get("fields") if isinstance(raw_issue.get("fields"), Mapping) else {}
    assert isinstance(fields, Mapping)
    result: dict[str, Any] = {
        "key": _text(raw_issue.get("key")),
        "summary": _text(fields.get("summary")),
    }
    issue_type = fields.get("issuetype") if isinstance(fields.get("issuetype"), Mapping) else {}
    if isinstance(issue_type, Mapping):
        _set_if_text(result, "issue_type", _text(issue_type.get("name")))

    parent = _issue_stub(fields.get("parent"))
    if parent:
        result["parent"] = parent

    subtasks = [_issue_stub(item) for item in _mapping_list(fields.get("subtasks"))]
    subtasks = [item for item in subtasks if item]
    if subtasks:
        result["subtasks"] = subtasks

    issue_links = [_issue_link_summary(item) for item in _mapping_list(fields.get("issuelinks"))]
    issue_links = [item for item in issue_links if item]
    if issue_links:
        result["issue_links"] = issue_links

    custom_fields = {
        field_id: _relationship_field_value(fields.get(field_id))
        for field_id in field_ids
        if fields.get(field_id) is not None
    }
    if custom_fields:
        result["custom_fields"] = custom_fields
    return {key: value for key, value in result.items() if value not in (None, "", [], {})}


def _relationship_field_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        issue = _issue_stub(value)
        if issue:
            return issue
        return {str(key): item for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_relationship_field_value(item) for item in value]
    return value


def _issue_link_summary(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    raw_type = value.get("type") if isinstance(value.get("type"), Mapping) else {}
    assert isinstance(raw_type, Mapping)
    result: dict[str, Any] = {}
    _set_if_text(result, "id", _text(value.get("id")))
    _set_if_text(result, "type", _text(raw_type.get("name")))
    _set_if_text(result, "inward", _text(raw_type.get("inward")))
    _set_if_text(result, "outward", _text(raw_type.get("outward")))
    inward = _issue_stub(value.get("inwardIssue"))
    outward = _issue_stub(value.get("outwardIssue"))
    if inward:
        result["inward_issue"] = inward
    if outward:
        result["outward_issue"] = outward
    return result


def _issue_stub(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    result: dict[str, Any] = {}
    _set_if_text(result, "key", _text(value.get("key")))
    fields = value.get("fields") if isinstance(value.get("fields"), Mapping) else {}
    if isinstance(fields, Mapping):
        _set_if_text(result, "summary", _text(fields.get("summary")))
        issue_type = fields.get("issuetype") if isinstance(fields.get("issuetype"), Mapping) else {}
        if isinstance(issue_type, Mapping):
            _set_if_text(result, "issue_type", _text(issue_type.get("name")))
    return result


def _mapping_list(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def _relationship_mappings_from_args(args: argparse.Namespace) -> dict[str, Any] | None:
    mappings: dict[str, Any] = {}
    if getattr(args, "jira_relationship_mappings_file", None):
        loaded = _load_relationship_mappings(args.jira_relationship_mappings_file.read_text(encoding="utf-8"))
        mappings.update(loaded)
    if getattr(args, "jira_relationship_mappings_json", None):
        loaded = _load_relationship_mappings(args.jira_relationship_mappings_json)
        mappings.update(loaded)
    for item in getattr(args, "jira_relationship_mapping", []) or []:
        name, mapping = _parse_inline_relationship_mapping(item)
        mappings[name] = mapping
    return mappings or None


RESERVED_STATE_TRANSITION_VERBS: frozenset[str] = frozenset({"assign", "unassign", "set-type"})

_VERB_INVALID_CHARS = re.compile(r"[^a-z0-9]+")


def derive_state_transition_verb(transition_name: str) -> str:
    """Derive a CLI-friendly verb from a Jira transition name.

    Lowercase, then collapse non-alphanumeric runs to a single hyphen.
    """

    text = (transition_name or "").strip().lower()
    if not text:
        return ""
    return _VERB_INVALID_CHARS.sub("-", text).strip("-")


def _jira_state_transitions_from_args(args: argparse.Namespace) -> dict[str, str] | None:
    transitions: dict[str, str] = {}
    for item in getattr(args, "jira_state_transition", []) or []:
        if not isinstance(item, str) or "=" not in item:
            raise WorkflowSetupError(
                f"--jira-state-transition must be <verb>=<transition name>, got {item!r}"
            )
        verb, _, transition_name = item.partition("=")
        verb = verb.strip().lower()
        transition_name = transition_name.strip()
        if not verb:
            raise WorkflowSetupError(
                f"--jira-state-transition must be <verb>=<transition name>, got {item!r}"
            )
        if verb in RESERVED_STATE_TRANSITION_VERBS:
            reserved = ", ".join(sorted(RESERVED_STATE_TRANSITION_VERBS))
            raise WorkflowSetupError(
                f"--jira-state-transition verb {verb!r} collides with a reserved issue_fields verb ({reserved})"
            )
        if not transition_name:
            raise WorkflowSetupError(
                f"--jira-state-transition for {verb!r} must include a non-empty transition name"
            )
        if verb in transitions:
            raise WorkflowSetupError(
                f"--jira-state-transition specified more than once for verb {verb!r}"
            )
        transitions[verb] = transition_name
    return transitions or None


def _jira_epic_fields_from_args(args: argparse.Namespace) -> dict[str, str] | None:
    fields: dict[str, str] = {}
    for kind, attr in (
        ("name", "jira_epic_field_name"),
        ("link", "jira_epic_field_link"),
        ("status", "jira_epic_field_status"),
    ):
        text = _text(getattr(args, attr, None))
        if text:
            fields[kind] = text
    return fields or None


def _jira_snapshot_hidden_comment_markers_from_args(args: argparse.Namespace) -> tuple[str, ...]:
    return _normalized_string_tuple(getattr(args, "jira_snapshot_hidden_comment_marker", None))


def _normalized_string_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    if isinstance(value, Sequence):
        result: list[str] = []
        for item in value:
            if item is None:
                continue
            if isinstance(item, str):
                result.extend(part.strip() for part in item.split(",") if part.strip())
            else:
                text = str(item).strip()
                if text:
                    result.append(text)
        return tuple(result)
    text = str(value).strip()
    return (text,) if text else ()


def _load_relationship_mappings(text: str) -> dict[str, Any]:
    data = yaml.safe_load(text)
    if not isinstance(data, Mapping):
        raise WorkflowSetupError("Jira relationship mappings must be a mapping")
    if isinstance(data.get("providers"), Mapping):
        providers = data["providers"]
        assert isinstance(providers, Mapping)
        issues = providers.get("issues")
        if isinstance(issues, Mapping) and isinstance(issues.get("relationship_mappings"), Mapping):
            return dict(issues["relationship_mappings"])
    if isinstance(data.get("relationship_mappings"), Mapping):
        return dict(data["relationship_mappings"])
    return dict(data)


def _parse_inline_relationship_mapping(value: str) -> tuple[str, dict[str, str]]:
    if ":" not in value:
        raise WorkflowSetupError("inline Jira relationship mapping must start with '<relationship>:'")
    name, raw_items = value.split(":", 1)
    relationship = name.strip()
    if not relationship:
        raise WorkflowSetupError("inline Jira relationship mapping requires a relationship name")
    mapping: dict[str, str] = {}
    for item in raw_items.split(","):
        if not item.strip():
            continue
        if "=" not in item:
            raise WorkflowSetupError(f"invalid Jira relationship mapping item: {item}")
        key, raw_value = item.split("=", 1)
        mapping[key.strip()] = raw_value.strip()
    return relationship, mapping


def _validate_relationship_mappings(mappings: Mapping[str, Any] | None) -> None:
    if mappings is None:
        return
    if not isinstance(mappings, Mapping):
        raise WorkflowSetupError("providers.issues.relationship_mappings must be a mapping")
    for name, raw_mapping in mappings.items():
        if not isinstance(raw_mapping, Mapping):
            raise WorkflowSetupError(f"Jira relationship mapping for '{name}' must be a mapping")
        surface = _normalize_surface(raw_mapping.get("surface"))
        if surface is None:
            raise WorkflowSetupError(
                f"Jira relationship mapping for '{name}' requires explicit surface; setup will not infer from link_type, field, or prose"
            )
        if surface not in RELATIONSHIP_SURFACES:
            raise WorkflowSetupError(f"Jira relationship mapping for '{name}' has unsupported surface: {surface}")
        if surface == "issue_link":
            if not _text(raw_mapping.get("link_type") or raw_mapping.get("linkType") or raw_mapping.get("name")):
                raise WorkflowSetupError(f"Jira issue-link relationship mapping for '{name}' requires link_type")
            direction = _normalize_token(raw_mapping.get("direction"))
            if direction not in ISSUE_LINK_DIRECTIONS:
                raise WorkflowSetupError(f"Jira issue-link relationship mapping for '{name}' requires direction inward or outward")
        elif surface == "field":
            if not _text(raw_mapping.get("field") or raw_mapping.get("field_id") or raw_mapping.get("fieldId")):
                raise WorkflowSetupError(f"Jira field relationship mapping for '{name}' requires field")
            write_to = _normalize_token(raw_mapping.get("write_to") or raw_mapping.get("writeTo"))
            if write_to not in FIELD_WRITE_TARGETS:
                raise WorkflowSetupError(f"Jira field relationship mapping for '{name}' requires write_to source or target")
            value = _normalize_token(raw_mapping.get("value") or raw_mapping.get("value_kind") or raw_mapping.get("valueKind"))
            if value not in FIELD_VALUE_KINDS:
                raise WorkflowSetupError(f"Jira field relationship mapping for '{name}' requires value key, key_object, or string")


def _normalize_epic_fields(value: Mapping[str, Any] | None) -> dict[str, str] | None:
    """Coerce epic_fields input into the canonical {name/link/status: id} shape."""

    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise WorkflowSetupError("Jira epic_fields must be a mapping of {name, link, status} to field ids")
    allowed = set(EPIC_FIELD_SCHEMA_CUSTOM_IDS)
    normalized: dict[str, str] = {}
    for raw_kind, raw_id in value.items():
        kind = str(raw_kind).strip().lower()
        if kind not in allowed:
            raise WorkflowSetupError(
                f"unknown Jira epic_fields entry '{raw_kind}'; expected one of: {sorted(allowed)}"
            )
        text = _text(raw_id)
        if text:
            normalized[kind] = text
    return normalized or None


def _augment_jira_relationship_mappings_with_epic(
    mappings: Mapping[str, Any] | None,
    *,
    epic_fields: Mapping[str, str] | None,
) -> Mapping[str, Any] | None:
    """Auto-add the standard ``epic`` field mapping when the Epic Link id is known."""

    if not epic_fields or "link" not in epic_fields:
        return mappings
    if mappings and "epic" in mappings:
        return mappings
    augmented = dict(mappings or {})
    augmented["epic"] = {
        "surface": "field",
        "field": epic_fields["link"],
        "write_to": "source",
        "value": "string",
    }
    return augmented


def _require_jira_relationship_mappings(mappings: Mapping[str, Any] | None) -> None:
    if mappings:
        return
    raise WorkflowSetupError(
        "Jira issue provider setup requires providers.issues.relationship_mappings; "
        "run jira-relationship-inspect with sample issues, confirm exact mappings, "
        "and pass --jira-relationship-mappings-file or --jira-relationship-mappings-json before building config"
    )


def _reject_cloud_provider(product: str, settings: Mapping[str, Any]) -> None:
    deployment = _text(settings.get("deployment") or settings.get("type") or settings.get("edition"))
    if deployment and _is_cloud_deployment(deployment):
        raise WorkflowSetupError(f"{product} Cloud is unsupported; use Data Center or Server settings")
    site = _text(settings.get("site") or settings.get("base_url") or settings.get("url") or settings.get("host") or settings.get("hostname"))
    if site and _is_atlassian_cloud_site(site):
        raise WorkflowSetupError(f"{product} Cloud atlassian.net sites are unsupported; use Data Center or Server settings")


def _looks_like_provider_profile(text: str) -> bool:
    normalized = text.lower()
    provider_markers = (
        ".spectrack/config.yml",
        "workflow provider",
        "issue provider",
        "knowledge provider",
        "jira",
        "github issue",
        "github issues",
        "wiki/",
        "provider profile",
    )
    if not any(marker in normalized for marker in provider_markers):
        return False
    unrelated_git = ("git log", "commit history", "merge commit", "git remote")
    if any(marker in normalized for marker in unrelated_git) and not any(
        marker in normalized for marker in ("jira", "github issue", "workflow provider", ".spectrack/config.yml")
    ):
        return False
    return True


def _extract_profile_defaults(text: str) -> dict[str, Any]:
    defaults: dict[str, Any] = {}
    for mapping in _yaml_mappings_from_text(text):
        _merge_profile_mapping(defaults, mapping)
    _merge_if_absent(defaults, _extract_profile_regex_defaults(text))
    return defaults


def _yaml_mappings_from_text(text: str) -> list[Mapping[str, Any]]:
    mappings: list[Mapping[str, Any]] = []
    candidates = [text]
    candidates.extend(match.group("body") for match in re.finditer(r"```(?:ya?ml|json)?\s*\n(?P<body>.*?)```", text, re.DOTALL | re.IGNORECASE))
    for candidate in candidates:
        try:
            data = yaml.safe_load(candidate)
        except yaml.YAMLError:
            continue
        if isinstance(data, Mapping):
            mappings.append(data)
    return mappings


def _merge_profile_mapping(defaults: dict[str, Any], mapping: Mapping[str, Any]) -> None:
    providers = mapping.get("providers") if isinstance(mapping.get("providers"), Mapping) else {}
    assert isinstance(providers, Mapping)
    issues = providers.get("issues") if isinstance(providers.get("issues"), Mapping) else mapping.get("issues")
    knowledge = providers.get("knowledge") if isinstance(providers.get("knowledge"), Mapping) else mapping.get("knowledge")

    if isinstance(issues, Mapping):
        issue_kind = _text(issues.get("kind") or issues.get("provider"))
        _set_default(defaults, "issue_provider", issue_kind)
        _set_default(defaults, "github_repo", _text(issues.get("repo") or issues.get("repository") or issues.get("slug")))
        _set_default(defaults, "github_issue_host", _text(issues.get("host") or issues.get("hostname")))
        _set_default(defaults, "jira_site", _text(issues.get("site") or issues.get("base_url") or issues.get("url")))
        _set_default(defaults, "jira_deployment", _text(issues.get("deployment") or issues.get("type") or issues.get("edition")))
        _set_default(defaults, "jira_project", _text(issues.get("project") or issues.get("project_key")))
        _set_default(defaults, "jira_issue_type", _text(issues.get("issue_type") or issues.get("issueType")))
        if isinstance(issues.get("relationship_mappings"), Mapping):
            defaults.setdefault("jira_relationship_mappings", dict(issues["relationship_mappings"]))

    if isinstance(knowledge, Mapping):
        knowledge_kind = _text(knowledge.get("kind") or knowledge.get("provider"))
        _set_default(defaults, "knowledge_provider", knowledge_kind)
        _set_default(defaults, "github_wiki_repo", _text(knowledge.get("repo") or knowledge.get("repository") or knowledge.get("slug")))
        _set_default(defaults, "github_wiki_host", _text(knowledge.get("host") or knowledge.get("hostname")))
        _set_default(defaults, "github_wiki_path", _text(knowledge.get("path")))
        _set_default(defaults, "github_wiki_prd_path", _text(knowledge.get("prd_path")))

    _set_default(defaults, "commit_ref_style", _dig_text(mapping, ("commit_refs", "style")))


def _extract_profile_regex_defaults(text: str) -> dict[str, Any]:
    defaults: dict[str, Any] = {}
    github_url = re.search(r"https?://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)(?:\.git)?", text)
    if github_url:
        defaults["github_repo"] = f"{github_url.group('owner')}/{github_url.group('repo').removesuffix('.git')}"
    repo_line = re.search(r"(?im)^\s*(?:github[-_ ]*)?repo(?:sitory)?\s*[:=]\s*(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\s*$", text)
    if repo_line:
        defaults["github_repo"] = repo_line.group("repo")
    jira_site = _first_url_matching(text, "jira")
    if jira_site:
        defaults["jira_site"] = jira_site
        defaults.setdefault("issue_provider", "jira")
    for key, pattern in {
        "jira_project": r"(?im)^\s*(?:jira[-_ ]*)?project(?: key)?\s*[:=]\s*(?P<value>[A-Za-z][A-Za-z0-9_]+)\s*$",
        "jira_issue_type": r"(?im)^\s*(?:jira[-_ ]*)?issue type\s*[:=]\s*(?P<value>[A-Za-z][A-Za-z0-9 _-]+)\s*$",
        "github_wiki_path": r"(?im)^\s*(?:github[-_ ]*)?(?:wiki|knowledge) path\s*[:=]\s*(?P<value>[A-Za-z0-9_./-]+)\s*$",
    }.items():
        match = re.search(pattern, text)
        if match:
            defaults[key] = match.group("value").strip()
    if re.search(r"(?i)\bdata\s*center\b|\bdatacenter\b|\bserver\b", text):
        defaults.setdefault("jira_deployment", "data_center")
    if re.search(r"(?i)\bcloud\b|atlassian\.net", text):
        defaults.setdefault("jira_deployment", "cloud")
    return defaults


def _first_url_matching(text: str, marker: str) -> str | None:
    for match in re.finditer(r"https?://[^\s)>\]\"']+", text):
        value = match.group(0).rstrip(".,")
        if marker in value.lower():
            return value
    return None


def _atomic_write_text(path: Path, text: str) -> None:
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    temp_path = Path(temp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as temp_file:
            temp_file.write(text)
        os.replace(temp_path, path)
    except OSError:
        try:
            temp_path.unlink()
        except OSError:
            pass
        raise


def _set_if_text(settings: dict[str, Any], key: str, value: str | None) -> None:
    if value is not None and str(value).strip():
        settings[key] = str(value).strip()


def _set_default(defaults: dict[str, Any], key: str, value: str | None) -> None:
    if value is not None and value.strip() and key not in defaults:
        defaults[key] = value.strip()


def _merge_if_absent(target: dict[str, Any], source: Mapping[str, Any]) -> None:
    for key, value in source.items():
        if value not in (None, "") and key not in target:
            target[key] = value


def _mapping_or_none(value: Any) -> Mapping[str, Any] | None:
    return value if isinstance(value, Mapping) else None


def _normalize_surface(value: Any) -> str | None:
    raw = _text(value)
    return raw.lower().replace("-", "_") if raw else None


def _normalize_token(value: Any) -> str | None:
    raw = _text(value)
    return raw.lower().replace("-", "_") if raw else None


def _text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _dig_text(mapping: Mapping[str, Any], keys: tuple[str, str]) -> str | None:
    first = mapping.get(keys[0])
    if not isinstance(first, Mapping):
        return None
    return _text(first.get(keys[1]))


def _is_cloud_deployment(value: str) -> bool:
    normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
    return normalized in {"cloud", "jira_cloud", "atlassian_cloud"}


def _is_atlassian_cloud_site(value: str) -> bool:
    raw = value.strip()
    if "://" not in raw:
        raw = f"https://{raw}"
    parsed = urlparse(raw)
    return bool(parsed.hostname and parsed.hostname.lower().endswith(".atlassian.net"))


def _non_default_github_host(host: str | None) -> str | None:
    if host and host != "github.com":
        return host
    return None


if __name__ == "__main__":
    raise SystemExit(main())
