#!/usr/bin/env python3
# /// script
# dependencies = ["PyYAML"]
# ///
"""Bootstrap repository-local workflow configuration.

The setup CLI builds and writes the repository-root ``.workflow/config.yml``
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

from workflow_command import CommandRunner, WorkflowCommandError, run_command  # noqa: E402
from workflow_config import (  # noqa: E402
    COMMIT_REF_STYLES,
    CONFIG_NAME,
    CONFIG_RELATIVE_PATH,
    ISSUE_PROVIDERS,
    KNOWLEDGE_PROVIDERS,
    LOCAL_PROJECTION_MODES,
    PROVIDER_NATIVE_ISSUE_ID_FORMATS,
    ProviderConfig,
    WorkflowConfigError,
    load_workflow_config,
    parse_workflow_config,
    validate_provider_for_role,
)
from workflow_env import workflow_project_dir_from_env  # noqa: E402
from workflow_github import GitHubRepositoryError, parse_github_remote_url  # noqa: E402
from workflow_jira_data_center_client import (  # noqa: E402
    jira_data_center_issue_path,
    jira_data_center_site_from_provider_config,
    jira_get_json,
)
from workflow_jira_issue_refs import JiraProviderError, normalize_jira_issue_key  # noqa: E402


class WorkflowSetupError(ValueError):
    """Raised when workflow setup input cannot produce a safe config."""


RELATIONSHIP_SURFACES = {"issue_link", "remote_link", "field"}
ISSUE_LINK_DIRECTIONS = {"inward", "outward"}
FIELD_WRITE_TARGETS = {"source", "target"}
FIELD_VALUE_KINDS = {"key", "key_object", "string"}
DEFAULT_JIRA_RELATIONSHIP_FIELD_QUERIES = ("parent",)


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
            "Jira relationship writes remain unavailable until explicit relationship mappings are provided"
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

    return {
        "operation": "jira_relationship_inspect",
        "site": site.to_json(),
        "link_types": link_types,
        "fields": fields,
        "sample_issues": sample_issues,
        "warnings": [
            "Inspection reports observed Jira data only; choose relationship mappings explicitly before writing config"
        ],
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
    jira_site: str | None = None,
    jira_deployment: str | None = "data_center",
    jira_api_version: str | None = "2",
    jira_project: str | None = None,
    jira_issue_type: str | None = None,
    jira_relationship_mappings: Mapping[str, Any] | None = None,
    confluence_site: str | None = None,
    confluence_deployment: str | None = "data_center",
    confluence_space: str | None = None,
    confluence_space_id: str | None = None,
    confluence_parent_page_id: str | None = None,
    filesystem_issues_path: str | None = None,
    filesystem_knowledge_path: str | None = None,
    local_projection_mode: str = "none",
    local_projection_path: str | None = None,
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

    if local_projection_mode not in LOCAL_PROJECTION_MODES:
        choices = ", ".join(sorted(LOCAL_PROJECTION_MODES))
        raise WorkflowSetupError(f"invalid local projection mode: {local_projection_mode}. Use one of: {choices}")
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

    issues = _issue_provider_config(
        issue_provider,
        github_repo=github_repo or probed_repo,
        github_host=issue_github_host,
        jira_site=jira_site,
        jira_deployment=jira_deployment,
        jira_api_version=jira_api_version,
        jira_project=jira_project,
        jira_issue_type=jira_issue_type,
        jira_relationship_mappings=jira_relationship_mappings,
        filesystem_path=filesystem_issues_path,
    )
    knowledge = _knowledge_provider_config(
        knowledge_provider,
        github_repo=github_wiki_repo or github_repo or probed_repo,
        github_host=knowledge_github_host,
        github_path=github_wiki_path,
        confluence_site=confluence_site,
        confluence_deployment=confluence_deployment,
        confluence_space=confluence_space,
        confluence_space_id=confluence_space_id,
        confluence_parent_page_id=confluence_parent_page_id,
        filesystem_path=filesystem_knowledge_path,
    )

    if issue_provider == "jira":
        _reject_cloud_provider("Jira", issues)
        _validate_relationship_mappings(jira_relationship_mappings)
    if knowledge_provider == "confluence":
        _reject_cloud_provider("Confluence", knowledge)

    effective_commit_style = "disabled" if not commit_refs_enabled else commit_ref_style
    raw: dict[str, Any] = {
        "version": 1,
        "mode": mode,
        "providers": {
            "issues": issues,
            "knowledge": knowledge,
        },
        "issue_id_format": PROVIDER_NATIVE_ISSUE_ID_FORMATS[issue_provider],
        "local_projection": _local_projection_config(local_projection_mode, local_projection_path),
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


def write_config(
    project: Path,
    raw: Mapping[str, Any],
    *,
    force: bool = False,
) -> dict[str, Any]:
    """Atomically write ``.workflow/config.yml`` and verify it with the loader."""

    project = project.expanduser().resolve()
    target = project / CONFIG_RELATIVE_PATH
    parse_workflow_config(raw, path=target)

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

    return {
        "operation": "write",
        "path": str(target),
        "verified": True,
        "verification": {
            "command": "workflow_config.py --require --json",
            "config": verified.to_json(),
        },
    }


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
            "local_projection": config.local_projection.mode,
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

    for key in ("jira_deployment", "confluence_deployment"):
        value = defaults.get(key)
        if isinstance(value, str) and _is_cloud_deployment(value):
            product = "Jira" if key.startswith("jira") else "Confluence"
            warnings.append(f"{product} Cloud was found in provider profile defaults, but only Data Center or Server is supported")

    for key in ("jira_site", "confluence_site"):
        value = defaults.get(key)
        if isinstance(value, str) and _is_atlassian_cloud_site(value):
            product = "Jira" if key.startswith("jira") else "Confluence"
            warnings.append(f"{product} atlassian.net site was found in provider profile defaults, but Cloud is unsupported")

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
    probe.add_argument("--json", action="store_true", help="emit JSON")

    profile = subparsers.add_parser("profile-from-docs", help="extract setup defaults from provider profile docs")
    profile.add_argument("paths", nargs="*", type=Path, help="profile document paths")
    profile.add_argument("--stdin", action="store_true", help="read an additional provider profile from stdin")
    profile.add_argument("--json", action="store_true", help="emit JSON")

    capabilities = subparsers.add_parser("capabilities", help="show provider capabilities and setup warnings")
    capabilities.add_argument("--issue-provider", required=True, choices=sorted(ISSUE_PROVIDERS))
    capabilities.add_argument("--knowledge-provider", required=True, choices=sorted(KNOWLEDGE_PROVIDERS))
    capabilities.add_argument("--jira-relationship-mappings-json")
    capabilities.add_argument("--jira-relationship-mappings-file", type=Path)
    capabilities.add_argument("--jira-relationship-mapping", action="append", default=[])
    capabilities.add_argument("--json", action="store_true", help="emit JSON")

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
    jira_inspect.add_argument("--json", action="store_true", help="emit JSON")

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
    jira_mappings.add_argument("--json", action="store_true", help="emit JSON")

    build = subparsers.add_parser("build-config", help=f"build and validate {CONFIG_NAME} YAML")
    _add_config_build_args(build)
    build.add_argument("--json", action="store_true", help="emit JSON with YAML and warnings")

    write = subparsers.add_parser("write", help=f"write {CONFIG_NAME} atomically")
    _add_config_build_args(write)
    write.add_argument("--config", type=Path, help="YAML config to write; use '-' for stdin")
    write.add_argument("--force", action="store_true", help="overwrite an existing config after explicit confirmation")
    write.add_argument("--json", action="store_true", help="emit JSON")

    return parser


def main(argv: list[str] | None = None, *, stdout: Any = sys.stdout, stderr: Any = sys.stderr) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        payload = _dispatch(args)
    except (WorkflowSetupError, WorkflowConfigError, JiraProviderError) as exc:
        print(f"workflow setup error: {exc}", file=stderr)
        return 2

    if args.command == "probe-git-remote" and args.require and not payload.get("detected"):
        _emit_payload(payload, json_output=args.json, stdout=stdout)
        return 1

    _emit_payload(payload, json_output=getattr(args, "json", False), stdout=stdout)
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
    raise WorkflowSetupError(f"unsupported command: {args.command}")


def _add_config_build_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--mode", default="remote-native", help="workflow mode")
    parser.add_argument("--issue-provider", required=False, choices=sorted(ISSUE_PROVIDERS), default="github")
    parser.add_argument("--knowledge-provider", required=False, choices=sorted(KNOWLEDGE_PROVIDERS), default="github")
    parser.add_argument("--probe-git-remote", action="store_true", help="seed GitHub repo settings from a git remote")
    parser.add_argument("--remote", default="origin", help="git remote name used with --probe-git-remote")
    parser.add_argument("--github-repo", help="GitHub issue repository slug, e.g. owner/repo")
    parser.add_argument("--github-host", help="shared GitHub host fallback when issue and wiki hosts are the same")
    parser.add_argument("--github-issue-host", help="GitHub issue provider host when it differs from the wiki host")
    parser.add_argument("--github-wiki-repo", help="GitHub knowledge repository slug when different from issue repo")
    parser.add_argument("--github-wiki-host", help="GitHub knowledge/wiki repository host when it differs from the issue host")
    parser.add_argument("--github-wiki-path", default="wiki/workflow", help="GitHub repository wiki directory path")
    parser.add_argument("--jira-site", help="Jira Data Center or Server base URL")
    parser.add_argument("--jira-deployment", default="data_center", help="Jira deployment; Cloud is unsupported")
    parser.add_argument("--jira-api-version", default="2", help="Jira REST API version")
    parser.add_argument("--jira-project", help="Jira project key")
    parser.add_argument("--jira-issue-type", help="Jira issue type")
    parser.add_argument("--jira-relationship-mappings-json", help="YAML/JSON mapping for Jira relationship writes")
    parser.add_argument("--jira-relationship-mappings-file", type=Path, help="file containing Jira relationship mappings")
    parser.add_argument(
        "--jira-relationship-mapping",
        action="append",
        default=[],
        help="repeatable mapping, e.g. blocked_by:surface=issue_link,link_type=Blocks,direction=inward",
    )
    parser.add_argument("--confluence-site", help="Confluence Data Center or Server base URL")
    parser.add_argument("--confluence-deployment", default="data_center", help="Confluence deployment; Cloud is unsupported")
    parser.add_argument("--confluence-space", help="Confluence space key")
    parser.add_argument("--confluence-space-id", help="Confluence space id")
    parser.add_argument("--confluence-parent-page-id", help="Confluence parent page id")
    parser.add_argument("--filesystem-issues-path", default="workflow/issues", help="filesystem issue provider path")
    parser.add_argument("--filesystem-knowledge-path", default="workflow/knowledge", help="filesystem knowledge provider path")
    parser.add_argument("--local-projection-mode", choices=sorted(LOCAL_PROJECTION_MODES), default="none")
    parser.add_argument("--local-projection-path", help="local projection path when mode is ephemeral or persistent")
    parser.add_argument("--commit-ref-style", choices=sorted(COMMIT_REF_STYLES), default="provider-native")
    parser.add_argument("--disable-commit-refs", action="store_true", help="disable commit references")


def _config_from_args(args: argparse.Namespace) -> dict[str, Any]:
    return build_config(
        project=args.project,
        issue_provider=args.issue_provider,
        knowledge_provider=args.knowledge_provider,
        github_repo=args.github_repo,
        github_host=args.github_host,
        github_issue_host=args.github_issue_host,
        github_wiki_repo=args.github_wiki_repo,
        github_wiki_host=args.github_wiki_host,
        github_wiki_path=args.github_wiki_path,
        jira_site=args.jira_site,
        jira_deployment=args.jira_deployment,
        jira_api_version=args.jira_api_version,
        jira_project=args.jira_project,
        jira_issue_type=args.jira_issue_type,
        jira_relationship_mappings=_relationship_mappings_from_args(args),
        confluence_site=args.confluence_site,
        confluence_deployment=args.confluence_deployment,
        confluence_space=args.confluence_space,
        confluence_space_id=args.confluence_space_id,
        confluence_parent_page_id=args.confluence_parent_page_id,
        filesystem_issues_path=args.filesystem_issues_path,
        filesystem_knowledge_path=args.filesystem_knowledge_path,
        local_projection_mode=args.local_projection_mode,
        local_projection_path=args.local_projection_path,
        commit_ref_style=args.commit_ref_style,
        commit_refs_enabled=not args.disable_commit_refs,
        mode=args.mode,
        probe_remote=args.probe_git_remote,
        remote=args.remote,
    )


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


def _emit_payload(payload: Mapping[str, Any], *, json_output: bool, stdout: Any) -> None:
    if json_output:
        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        return
    operation = payload.get("operation")
    if operation == "build_config":
        print(payload["yaml"], end="", file=stdout)
        return
    if operation == "jira_relationship_mappings":
        print(payload["yaml"], end="", file=stdout)
        return
    if operation == "capabilities":
        for warning in payload.get("warnings", []):
            print(f"- {warning}", file=stdout)
        return
    if operation == "profile_from_docs":
        print(yaml.safe_dump(payload.get("defaults", {}), sort_keys=False), end="", file=stdout)
        return
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
    jira_relationship_mappings: Mapping[str, Any] | None,
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
        if jira_relationship_mappings:
            settings["relationship_mappings"] = dict(jira_relationship_mappings)
    elif provider == "filesystem":
        _set_if_text(settings, "path", filesystem_path or "workflow/issues")
    return settings


def _knowledge_provider_config(
    provider: str,
    *,
    github_repo: str | None,
    github_host: str | None,
    github_path: str | None,
    confluence_site: str | None,
    confluence_deployment: str | None,
    confluence_space: str | None,
    confluence_space_id: str | None,
    confluence_parent_page_id: str | None,
    filesystem_path: str | None,
) -> dict[str, Any]:
    settings: dict[str, Any] = {"kind": provider}
    if provider == "github":
        _set_if_text(settings, "repo", github_repo)
        _set_if_text(settings, "host", github_host)
        _set_if_text(settings, "path", github_path or "wiki/workflow")
    elif provider == "confluence":
        _set_if_text(settings, "site", confluence_site)
        _set_if_text(settings, "deployment", confluence_deployment or "data_center")
        _set_if_text(settings, "space", confluence_space.upper() if confluence_space else None)
        _set_if_text(settings, "space_id", confluence_space_id)
        _set_if_text(settings, "parent_page_id", confluence_parent_page_id)
    elif provider == "filesystem":
        _set_if_text(settings, "path", filesystem_path or "workflow/knowledge")
    return settings


def _local_projection_config(mode: str, path: str | None) -> dict[str, Any]:
    result: dict[str, Any] = {"mode": mode}
    if mode != "none" and path:
        result["path"] = path
    return result


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
                "Jira relationship writes remain unavailable until providers.issues.relationship_mappings is configured explicitly"
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
    if provider == "confluence":
        return {
            "provider": provider,
            "native_transport": True,
            "reads": True,
            "writes": True,
            "metadata_writes": False,
            "limitations": [
                "Confluence Cloud is unsupported; use Data Center or Server",
                "set_metadata, link, and add_comment knowledge operations are not implemented",
            ],
            "warnings": ["Confluence setup targets Data Center or Server only"],
        }
    if provider == "github":
        return {
            "provider": provider,
            "native_transport": False,
            "reads": "config-only",
            "writes": False,
            "metadata_writes": False,
            "limitations": ["GitHub repository wiki knowledge provider commands are not registered yet"],
            "warnings": ["GitHub knowledge writes are not implemented by the native provider registry yet"],
        }
    return {
        "provider": provider,
        "native_transport": False,
        "reads": "config-only",
        "writes": False,
        "metadata_writes": False,
        "limitations": ["filesystem knowledge provider commands are not registered yet"],
        "warnings": ["filesystem knowledge writes are not implemented by the native provider registry yet"],
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
        ".workflow/config.yml",
        "workflow provider",
        "issue provider",
        "knowledge provider",
        "jira",
        "confluence",
        "github issue",
        "github issues",
        "wiki/",
        "provider profile",
    )
    if not any(marker in normalized for marker in provider_markers):
        return False
    unrelated_git = ("git log", "commit history", "merge commit", "git remote")
    if any(marker in normalized for marker in unrelated_git) and not any(
        marker in normalized for marker in ("jira", "confluence", "github issue", "workflow provider", ".workflow/config.yml")
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
        _set_default(defaults, "confluence_site", _text(knowledge.get("site") or knowledge.get("base_url") or knowledge.get("url")))
        _set_default(defaults, "confluence_deployment", _text(knowledge.get("deployment") or knowledge.get("type") or knowledge.get("edition")))
        _set_default(defaults, "confluence_space", _text(knowledge.get("space") or knowledge.get("space_key")))
        _set_default(defaults, "confluence_space_id", _text(knowledge.get("space_id") or knowledge.get("spaceId")))
        _set_default(defaults, "confluence_parent_page_id", _text(knowledge.get("parent_page_id") or knowledge.get("parentPageId")))

    _set_default(defaults, "local_projection_mode", _dig_text(mapping, ("local_projection", "mode")))
    _set_default(defaults, "local_projection_path", _dig_text(mapping, ("local_projection", "path")))
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
    confluence_site = _first_url_matching(text, "confluence")
    if confluence_site:
        defaults["confluence_site"] = confluence_site
        defaults.setdefault("knowledge_provider", "confluence")
    for key, pattern in {
        "jira_project": r"(?im)^\s*(?:jira[-_ ]*)?project(?: key)?\s*[:=]\s*(?P<value>[A-Za-z][A-Za-z0-9_]+)\s*$",
        "jira_issue_type": r"(?im)^\s*(?:jira[-_ ]*)?issue type\s*[:=]\s*(?P<value>[A-Za-z][A-Za-z0-9 _-]+)\s*$",
        "confluence_space": r"(?im)^\s*(?:confluence[-_ ]*)?space(?: key)?\s*[:=]\s*(?P<value>[A-Za-z][A-Za-z0-9_]+)\s*$",
        "github_wiki_path": r"(?im)^\s*(?:github[-_ ]*)?(?:wiki|knowledge) path\s*[:=]\s*(?P<value>[A-Za-z0-9_./-]+)\s*$",
    }.items():
        match = re.search(pattern, text)
        if match:
            defaults[key] = match.group("value").strip()
    if re.search(r"(?i)\bdata\s*center\b|\bdatacenter\b|\bserver\b", text):
        defaults.setdefault("jira_deployment", "data_center")
        defaults.setdefault("confluence_deployment", "data_center")
    if re.search(r"(?i)\bcloud\b|atlassian\.net", text):
        defaults.setdefault("jira_deployment", "cloud")
        defaults.setdefault("confluence_deployment", "cloud")
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
    return normalized in {"cloud", "jira_cloud", "confluence_cloud", "atlassian_cloud"}


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
