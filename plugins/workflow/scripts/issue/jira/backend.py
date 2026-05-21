#!/usr/bin/env python3
"""Jira issue backend driver.

Ports the per-intent logic from the (now-deleted) ``jira_issue_*.py`` CLI
scripts onto a single :class:`JiraIssueBackend` driver consumed by the
dispatcher scripts under ``scripts/issue_*.py``. The backend keeps the
original argument surface and emitted JSON payload shapes; the only moved
seam is the config-kind guard, which the dispatcher owns.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any, TextIO

import frontmatter as frontmatter_lib

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError
from workflow_jira_data_center_client import resolve_jira_data_center_site
from issue.backend import IssueBackendError
from issue.cli_output import (
    IssueFetchContext,
    cache_refreshed_from_payload,
    display_project_path,
    flatten_provider_envelope,
    format_issue_cache_json,
)
from issue.jira.cache import JiraDataCenterIssueCache
from issue.jira.provider import (
    JIRA_ARTIFACT_ISSUE_TYPES,
    JiraDataCenterIssueNativeProvider,
    _jira_configured_artifact_issue_types,
    _jira_issue_provider_settings,
    get_jira_myself,
    validate_relationship_intent_mappings,
)
from issue.jira.refs import (
    JiraProviderError,
    jira_issue_keys_from_references,
    normalize_jira_issue_key,
)
from workflow_providers import (
    CACHE_POLICY_DEFAULT,
    CACHE_POLICY_REFRESH,
    ProviderContext,
    ProviderOperationError,
    ProviderRequest,
)


_FRONTMATTER_HANDLER = frontmatter_lib.YAMLHandler()

_CACHE_FETCH_POLICIES = (CACHE_POLICY_DEFAULT, CACHE_POLICY_REFRESH)


_RESERVED_FIELDS_VERBS = frozenset({"assign", "unassign", "set-type"})

_LIFECYCLE_NOTE = (
    "Lifecycle verbs come from providers.issues.state_transitions; "
    "configure one with `workflow_setup.py build-config "
    "--jira-state-transition <verb>=<transition>`."
)


class _JiraFieldsParserShim:
    """Mixin-style helper to surface friendly errors for unknown verbs.

    Re-implements the ``_JiraFieldsParser.error`` hook from the legacy
    the legacy Jira fields CLI directly on the dispatcher's top-level parser
    by patching its ``error`` method after the subparsers are wired.
    """


class JiraIssueBackend:
    """Drive Jira-specific issue intents for the unified dispatchers."""

    kind = "jira"

    # ------------------------------------------------------------------
    # fetch
    # ------------------------------------------------------------------

    def add_fetch_args(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--cache-policy",
            choices=_CACHE_FETCH_POLICIES,
            default=CACHE_POLICY_DEFAULT,
            help="provider cache policy",
        )
        parser.add_argument(
            "references",
            nargs="+",
            help="Jira issue keys or text containing configured Jira issue keys",
        )

    def run_fetch(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            site = resolve_jira_data_center_site(config.root)
        except (WorkflowConfigError, JiraProviderError) as exc:
            print(f"Jira issue fetch error: {exc}", file=stderr)
            return 2

        try:
            issue_keys = jira_issue_keys_from_references(list(args.references))
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue fetch error: {exc}", file=stderr)
            return 2
        if not issue_keys:
            print(
                "Jira issue fetch error: no Jira issue references were found",
                file=stderr,
            )
            return 2

        provider = JiraDataCenterIssueNativeProvider(runner=runner)
        cache = JiraDataCenterIssueCache.for_project(config.root)
        contexts: list[IssueFetchContext] = []
        try:
            for issue in issue_keys:
                try:
                    issue_key = normalize_jira_issue_key(issue)
                except JiraProviderError as exc:
                    raise IssueBackendError(str(exc)) from exc
                response = provider.call(
                    ProviderRequest(
                        role="issue",
                        kind="jira",
                        operation="get",
                        context=ProviderContext(
                            project=config.root,
                            artifact_type="task",
                            cache_policy=args.cache_policy,
                        ),
                        payload={
                            "issue": issue_key,
                            "include_body": False,
                            "include_comments": False,
                            "include_relationships": False,
                        },
                    )
                )
                issue_dir = cache.issue_dir(site, issue_key)
                comment_paths = tuple(
                    display_project_path(path, config.root)
                    for path in cache.comment_files(site, issue_key)
                )
                contexts.append(
                    IssueFetchContext(
                        number=issue_key,
                        issue_dir=display_project_path(
                            issue_dir, config.root, trailing_slash=True
                        ),
                        title=str(response.payload.get("title") or ""),
                        state=str(response.payload.get("state") or "").upper(),
                        cache_refreshed=cache_refreshed_from_payload(
                            response.payload, default=True
                        ),
                        provider_kind="jira",
                        comments=comment_paths,
                    )
                )
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue fetch error: {exc}", file=stderr)
            return 2

        payload = format_issue_cache_json(contexts)
        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        return 0

    # ------------------------------------------------------------------
    # comments
    # ------------------------------------------------------------------

    def add_comments_args(self, parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest="command", required=True)
        append = subparsers.add_parser(
            "append",
            help="append a comment to one Jira issue from a body file",
        )
        append.add_argument("--type", default="task", help="workflow artifact type")
        append.add_argument("--issue", required=True, help="Jira issue key")
        append.add_argument(
            "--body-file",
            type=Path,
            required=True,
            help="path to the opaque body content file (leading YAML frontmatter is stripped)",
        )
        append.add_argument(
            "--state",
            help="workflow verb keyed in providers.issues.state_transitions (free-form)",
        )
        append.add_argument(
            "--state-reason",
            choices=["completed", "not_planned", "reopened"],
        )

    def run_comments(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            if args.command == "append":
                payload = self._append_comment(
                    config=config,
                    artifact_type=args.type,
                    issue=args.issue,
                    body_file=args.body_file,
                    state=args.state,
                    state_reason=args.state_reason,
                    runner=runner,
                )
            else:
                raise IssueBackendError(f"unsupported command: {args.command}")
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue comment append error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        if payload.get("status") == "blocked":
            return 3
        return 0

    def _append_comment(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        issue: str,
        body_file: Path,
        state: str | None,
        state_reason: str | None,
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        artifact_type = _required_text(artifact_type, "artifact type")
        try:
            issue_key = normalize_jira_issue_key(issue)
        except JiraProviderError as exc:
            raise IssueBackendError(str(exc)) from exc

        body_path = body_file.expanduser()
        if not body_path.is_file():
            raise IssueBackendError(f"body file does not exist: {body_path}")
        body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

        payload: dict[str, object] = {
            "issue": issue_key,
            "body": body,
            "freshness_check": True,
        }
        if state:
            payload["state"] = state.strip().lower()
        if state_reason:
            payload["state_reason"] = state_reason.strip()

        provider = JiraDataCenterIssueNativeProvider(runner=runner)
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="add_comment",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload=payload,
            )
        )

        provider_payload = dict(response.payload)
        if provider_payload.get("status") == "blocked":
            provider_payload["body_file"] = str(body_path)
            provider_payload["body_file_removed"] = False
            return provider_payload

        cache_payload = (
            provider_payload.get("cache")
            if isinstance(provider_payload.get("cache"), dict)
            else {}
        )
        issue_file = (
            cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
        )
        body_removed = False
        try:
            body_path.unlink()
        except OSError:
            body_removed = False
        else:
            body_removed = True

        return {
            "operation": "append_comment",
            "kind": "jira",
            "issue": provider_payload.get("issue") or provider_payload.get("key"),
            "key": provider_payload.get("key"),
            "comment": provider_payload.get("comment"),
            "state_changed": bool(provider_payload.get("state_changed")),
            "state": provider_payload.get("state"),
            "issue_file": issue_file,
            "body_file": str(body_path),
            "body_file_removed": body_removed,
            "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        }

    # ------------------------------------------------------------------
    # drafts (publish)
    # ------------------------------------------------------------------

    def add_drafts_args(self, parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest="command", required=True)
        publish = subparsers.add_parser(
            "publish",
            help="publish a new Jira issue from a body file",
        )
        publish.add_argument("--type", required=True, help="workflow artifact type")
        publish.add_argument("--title", required=True)
        publish.add_argument("--label", action="append", default=[])
        publish.add_argument("--issue-type", help="Jira provider issue type")
        publish.add_argument(
            "--subtask-parent",
            help=(
                "create the new issue as a native Jira Sub-task under this parent key. "
                "Sets the create-time parent field and forces issuetype=Sub-task; no "
                "post-create relationship step. Pick this when siblings under the parent "
                "are Sub-tasks. Use --parent instead for a post-create issue-link "
                "relationship that leaves issuetype unchanged."
            ),
        )
        publish.add_argument(
            "--project-key",
            help="override the Jira project key for this create",
        )
        publish.add_argument(
            "--body-file",
            type=Path,
            required=True,
            help="path to the opaque body content file (leading YAML frontmatter is stripped)",
        )
        publish.add_argument(
            "--epic-name",
            help="Epic Name customfield value (epic only; defaults to --title)",
        )
        publish.add_argument(
            "--assignee",
            help='Jira DC username or the literal "me" to resolve via /rest/api/<v>/myself',
        )
        publish.add_argument(
            "--parent",
            help=(
                "add a post-create issue-link parent relationship to this key. "
                "Does not change the new issue's issuetype (use --subtask-parent for a "
                "native Sub-task). Requires providers.issues.relationship_mappings.parent "
                "to be configured; the post-create step fails otherwise."
            ),
        )
        publish.add_argument(
            "--epic",
            help="add Epic Link after publish (rejected when --type epic)",
        )
        publish.add_argument(
            "--blocked-by",
            action="append",
            default=[],
            help="add blocked-by dependency after publish (repeatable)",
        )
        publish.add_argument(
            "--blocking",
            action="append",
            default=[],
            help="add blocking dependency after publish (repeatable)",
        )
        publish.add_argument(
            "--child",
            action="append",
            default=[],
            help="add child after publish (repeatable)",
        )
        publish.add_argument(
            "--related",
            action="append",
            default=[],
            help="add related ref after publish (repeatable)",
        )

    def run_drafts(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            if args.command == "publish":
                payload = self._publish_issue(
                    config=config,
                    artifact_type=args.type,
                    title=args.title,
                    body_file=args.body_file,
                    labels=tuple(args.label),
                    issue_type=args.issue_type,
                    subtask_parent=args.subtask_parent,
                    project_key=args.project_key,
                    epic_name=args.epic_name,
                    assignee=args.assignee,
                    relationship_intent=self._publish_relationship_intent(args),
                    runner=runner,
                )
            else:
                raise IssueBackendError(f"unsupported command: {args.command}")
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue draft error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        relationships = payload.get("relationships") if isinstance(payload, dict) else None
        if isinstance(relationships, dict) and relationships.get("status") == "failed":
            return 1
        return 0

    @staticmethod
    def _publish_relationship_intent(args: argparse.Namespace) -> dict[str, object]:
        intent: dict[str, object] = {}
        if getattr(args, "parent", None):
            intent["parent_add"] = args.parent
        if getattr(args, "epic", None):
            if getattr(args, "type", None) and str(args.type).strip().lower() == "epic":
                raise IssueBackendError(
                    "publish --epic cannot be combined with --type epic"
                )
            intent["epic_add"] = args.epic
        if getattr(args, "blocked_by", None):
            intent["blocked_by_add"] = list(args.blocked_by)
        if getattr(args, "blocking", None):
            intent["blocking_add"] = list(args.blocking)
        if getattr(args, "child", None):
            intent["child_add"] = list(args.child)
        if getattr(args, "related", None):
            intent["related_add"] = list(args.related)
        return intent

    def _publish_issue(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        title: str,
        body_file: Path,
        labels: tuple[str, ...],
        issue_type: str | None,
        subtask_parent: str | None,
        project_key: str | None,
        epic_name: str | None,
        assignee: str | None,
        relationship_intent: dict[str, object],
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        artifact_type = _required_text(artifact_type, "artifact type")
        title = _required_text(title, "title")
        normalized_labels = tuple(label.strip() for label in labels if label.strip())
        normalized_subtask_parent = _jira_issue_key(subtask_parent, "subtask parent")
        normalized_issue_type = _optional_text(issue_type)
        normalized_epic_name = _optional_text(epic_name)

        body_path = body_file.expanduser()
        if not body_path.is_file():
            raise IssueBackendError(f"body file does not exist: {body_path}")

        if relationship_intent:
            try:
                validate_relationship_intent_mappings(config.root, relationship_intent)
            except ProviderOperationError as exc:
                raise IssueBackendError(str(exc)) from exc

        body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

        payload: dict[str, object] = {
            "title": title,
            "body": body,
            "labels": list(normalized_labels),
        }
        if normalized_issue_type:
            payload["jira_issue_type"] = normalized_issue_type
        if normalized_subtask_parent:
            payload["subtask_parent_key"] = normalized_subtask_parent
        normalized_project_key = _optional_text(project_key)
        if normalized_project_key:
            payload["project_key"] = normalized_project_key
        if normalized_epic_name is not None:
            payload["epic_name"] = normalized_epic_name
        normalized_assignee = _optional_text(assignee)
        if normalized_assignee:
            payload["assignee"] = normalized_assignee

        provider = JiraDataCenterIssueNativeProvider(runner=runner)
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="create",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload=payload,
            )
        )

        provider_payload = dict(response.payload)
        cache_payload = (
            provider_payload.get("cache")
            if isinstance(provider_payload.get("cache"), dict)
            else {}
        )
        issue_file = (
            cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
        )

        result: dict[str, object] = {
            "operation": "publish_issue",
            "kind": "jira",
            "issue": provider_payload.get("issue") or provider_payload.get("key"),
            "key": provider_payload.get("key"),
            "verified": bool(provider_payload.get("verified")),
            "issue_file": issue_file,
            "body_file": str(body_path),
            "body_file_removed": False,
            "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
            "subtask_parent": provider_payload.get("subtask_parent"),
        }

        relationship_failed = False
        if relationship_intent:
            new_key = provider_payload.get("key") or provider_payload.get("issue")
            try:
                relationships_response = provider.call(
                    ProviderRequest(
                        role="issue",
                        kind="jira",
                        operation="apply_relationships",
                        context=ProviderContext(
                            project=config.root, artifact_type=artifact_type
                        ),
                        payload={
                            "issue": new_key,
                            "relationship_intent": relationship_intent,
                        },
                    )
                )
                result["relationships"] = dict(relationships_response.payload)
            except Exception as exc:  # noqa: BLE001
                relationship_failed = True
                result["relationships"] = {
                    "operation": "apply_relationships",
                    "status": "failed",
                    "error": str(exc),
                    "intent": dict(relationship_intent),
                }

        if not relationship_failed:
            try:
                body_path.unlink()
            except OSError:
                pass
            else:
                result["body_file_removed"] = True

        return result

    # ------------------------------------------------------------------
    # writeback
    # ------------------------------------------------------------------

    def add_writeback_args(self, parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest="command", required=True)
        update = subparsers.add_parser(
            "update",
            help="update one Jira issue body from a body file",
        )
        update.add_argument("--type", default="task", help="workflow artifact type")
        update.add_argument("--issue", required=True, help="Jira issue key")
        update.add_argument(
            "--body-file",
            type=Path,
            required=True,
            help="path to the opaque body content file (leading YAML frontmatter is stripped)",
        )
        update.add_argument("--title")
        update.add_argument(
            "--add-label",
            dest="add_label",
            action="append",
            default=[],
            help="add a label (repeatable; cannot be combined with --set-labels)",
        )
        update.add_argument(
            "--remove-label",
            dest="remove_label",
            action="append",
            default=[],
            help="remove a label (repeatable; cannot be combined with --set-labels)",
        )
        update.add_argument(
            "--set-labels",
            dest="set_labels",
            help="replace the label set with a comma-separated list",
        )
        update.add_argument(
            "--state",
            help="workflow verb keyed in providers.issues.state_transitions (free-form)",
        )
        update.add_argument(
            "--state-reason",
            choices=["completed", "not_planned", "reopened"],
        )

    def run_writeback(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            if args.command == "update":
                set_labels: tuple[str, ...] | None = None
                if args.set_labels is not None:
                    set_labels = tuple(part for part in args.set_labels.split(","))
                payload = self._update_issue(
                    config=config,
                    artifact_type=args.type,
                    issue=args.issue,
                    body_file=args.body_file,
                    title=args.title,
                    add_labels=tuple(args.add_label),
                    remove_labels=tuple(args.remove_label),
                    set_labels=set_labels,
                    state=args.state,
                    state_reason=args.state_reason,
                    runner=runner,
                )
            else:
                raise IssueBackendError(f"unsupported command: {args.command}")
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue update error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        if payload.get("status") == "blocked":
            return 3
        return 0

    def _update_issue(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        issue: str,
        body_file: Path,
        title: str | None,
        add_labels: tuple[str, ...],
        remove_labels: tuple[str, ...],
        set_labels: tuple[str, ...] | None,
        state: str | None,
        state_reason: str | None,
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        artifact_type = _required_text(artifact_type, "artifact type")
        try:
            issue_key = normalize_jira_issue_key(issue)
        except JiraProviderError as exc:
            raise IssueBackendError(str(exc)) from exc

        body_path = body_file.expanduser()
        if not body_path.is_file():
            raise IssueBackendError(f"body file does not exist: {body_path}")
        body = _strip_body_frontmatter(body_path.read_text(encoding="utf-8"))

        normalized_add = tuple(label.strip() for label in add_labels if label.strip())
        normalized_remove = tuple(label.strip() for label in remove_labels if label.strip())
        normalized_set: tuple[str, ...] | None
        if set_labels is None:
            normalized_set = None
        else:
            normalized_set = tuple(label.strip() for label in set_labels if label.strip())
        if normalized_set is not None and (normalized_add or normalized_remove):
            raise IssueBackendError(
                "--set-labels cannot be combined with --add-label or --remove-label"
            )

        payload: dict[str, object] = {
            "issue": issue_key,
            "body": body,
            "freshness_check": True,
        }
        if title is not None:
            payload["title"] = title
        if normalized_set is not None:
            payload["label_set"] = list(normalized_set)
        if normalized_add:
            payload["label_add"] = list(normalized_add)
        if normalized_remove:
            payload["label_remove"] = list(normalized_remove)
        if state:
            payload["state"] = state.strip().lower()
        if state_reason:
            payload["state_reason"] = state_reason.strip()

        provider = JiraDataCenterIssueNativeProvider(runner=runner)
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="update",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload=payload,
            )
        )

        provider_payload = dict(response.payload)
        if provider_payload.get("status") == "blocked":
            provider_payload["body_file"] = str(body_path)
            provider_payload["body_file_removed"] = False
            return provider_payload

        cache_payload = (
            provider_payload.get("cache")
            if isinstance(provider_payload.get("cache"), dict)
            else {}
        )
        issue_file = (
            cache_payload.get("issue_file") if isinstance(cache_payload, dict) else None
        )
        body_removed = False
        try:
            body_path.unlink()
        except OSError:
            body_removed = False
        else:
            body_removed = True

        return {
            "operation": "update_issue",
            "kind": "jira",
            "issue": provider_payload.get("issue") or provider_payload.get("key"),
            "key": provider_payload.get("key"),
            "verified": bool(provider_payload.get("verified")),
            "state_changed": bool(provider_payload.get("state_changed")),
            "state": provider_payload.get("state"),
            "issue_file": issue_file,
            "body_file": str(body_path),
            "body_file_removed": body_removed,
            "cache_refreshed": bool(provider_payload.get("cache_refreshed")),
        }

    # ------------------------------------------------------------------
    # relationships
    # ------------------------------------------------------------------

    def add_relationships_args(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--type", default="task", help="workflow artifact type")
        parent_group = parser.add_mutually_exclusive_group()
        parent_group.add_argument(
            "--parent", help="add parent (errors if a parent already exists)"
        )
        parent_group.add_argument(
            "--replace-parent",
            dest="replace_parent",
            help="set parent, replacing any existing parent",
        )
        parent_group.add_argument(
            "--remove-parent",
            dest="remove_parent",
            action="store_true",
            help="remove the current parent (no-op when no parent exists)",
        )
        epic_group = parser.add_mutually_exclusive_group()
        epic_group.add_argument(
            "--epic",
            help="add Epic Link (errors if an Epic Link already exists)",
        )
        epic_group.add_argument(
            "--replace-epic",
            dest="replace_epic",
            help="set Epic Link, replacing any existing Epic Link",
        )
        epic_group.add_argument(
            "--remove-epic",
            dest="remove_epic",
            action="store_true",
            help="remove the current Epic Link (no-op when no Epic Link exists)",
        )
        parser.add_argument(
            "--child", action="append", default=[], help="add a child (repeatable)"
        )
        parser.add_argument(
            "--remove-child",
            dest="remove_child",
            action="append",
            default=[],
            help="remove a child (repeatable)",
        )
        parser.add_argument(
            "--blocked-by",
            action="append",
            default=[],
            help="add a blocked-by dependency (repeatable)",
        )
        parser.add_argument(
            "--remove-blocked-by",
            dest="remove_blocked_by",
            action="append",
            default=[],
            help="remove a blocked-by dependency (repeatable)",
        )
        parser.add_argument(
            "--blocking",
            action="append",
            default=[],
            help="add a blocking dependency (repeatable)",
        )
        parser.add_argument(
            "--remove-blocking",
            dest="remove_blocking",
            action="append",
            default=[],
            help="remove a blocking dependency (repeatable)",
        )
        parser.add_argument(
            "--related", action="append", default=[], help="add a related ref (repeatable)"
        )
        parser.add_argument(
            "--remove-related",
            dest="remove_related",
            action="append",
            default=[],
            help="remove a related ref (repeatable)",
        )
        parser.add_argument("issue", help="Jira issue key")

    def run_relationships(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        intent = self._relationships_intent(args)
        try:
            payload = self._apply_relationships(
                config=config,
                issue_ref=args.issue,
                artifact_type=args.type,
                intent=intent,
                runner=runner,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue relationship error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        return 0

    @staticmethod
    def _relationships_intent(args: argparse.Namespace) -> dict[str, object]:
        intent: dict[str, object] = {}
        if args.parent:
            intent["parent_add"] = args.parent
        if args.replace_parent:
            intent["parent_replace"] = args.replace_parent
        if args.remove_parent:
            intent["parent_remove"] = True
        if args.epic:
            intent["epic_add"] = args.epic
        if args.replace_epic:
            intent["epic_replace"] = args.replace_epic
        if args.remove_epic:
            intent["epic_remove"] = True
        if args.blocked_by:
            intent["blocked_by_add"] = list(args.blocked_by)
        if args.remove_blocked_by:
            intent["blocked_by_remove"] = list(args.remove_blocked_by)
        if args.blocking:
            intent["blocking_add"] = list(args.blocking)
        if args.remove_blocking:
            intent["blocking_remove"] = list(args.remove_blocking)
        if args.child:
            intent["child_add"] = list(args.child)
        if args.remove_child:
            intent["child_remove"] = list(args.remove_child)
        if args.related:
            intent["related_add"] = list(args.related)
        if args.remove_related:
            intent["related_remove"] = list(args.remove_related)
        return intent

    def _apply_relationships(
        self,
        *,
        config: WorkflowConfig,
        issue_ref: str,
        artifact_type: str,
        intent: dict[str, object],
        runner: CommandRunner | None,
    ) -> dict[str, object]:
        try:
            site = resolve_jira_data_center_site(config.root)
        except (WorkflowConfigError, JiraProviderError) as exc:
            raise IssueBackendError(str(exc)) from exc
        issue_keys: list[str] = []
        for issue in jira_issue_keys_from_references([issue_ref]):
            try:
                issue_keys.append(normalize_jira_issue_key(issue))
            except JiraProviderError as exc:
                raise IssueBackendError(str(exc)) from exc
        if not issue_keys:
            raise IssueBackendError("no Jira issue references were found")
        if len(issue_keys) != 1:
            raise IssueBackendError(
                "relationship apply requires exactly one issue ref"
            )
        issue_key = issue_keys[0]

        provider = JiraDataCenterIssueNativeProvider(runner=runner)
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="apply_relationships",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": issue_key, "relationship_intent": intent},
            )
        )
        cache = JiraDataCenterIssueCache.for_project(config.root)
        return flatten_provider_envelope(
            response.payload,
            project=config.root,
            issue_file=cache.issue_file(site, issue_key),
        )

    # ------------------------------------------------------------------
    # fields
    # ------------------------------------------------------------------
    #
    # The Jira fields parser depends on the project's configured state
    # transitions (one dynamic subparser per ``providers.issues.state_transitions``
    # key). The dispatcher hands us a freshly built parser; we resolve the
    # state-verb list directly from the loaded ``WorkflowConfig`` ahead of
    # parsing. Argument registration and friendly-error wiring live below.

    def add_fields_args(
        self,
        parser: argparse.ArgumentParser,
        *,
        state_verbs: Iterable[str] = (),
    ) -> None:
        verbs = tuple(state_verbs)
        parser.description = (
            f"{parser.description or ''} {_LIFECYCLE_NOTE}".strip()
        )
        self._patch_parser_for_friendly_verb_errors(parser, verbs)

        parser.add_argument("--type", default="task", help="workflow artifact type")
        subparsers = parser.add_subparsers(dest="verb", required=True)

        p_assign = subparsers.add_parser("assign", help="assign an issue to a user")
        p_assign.add_argument("issue", help="Jira issue key")
        p_assign.add_argument("user", help='Jira DC username or the literal "me"')

        p_unassign = subparsers.add_parser("unassign", help="clear the assignee")
        p_unassign.add_argument("issue", help="Jira issue key")

        p_set_type = subparsers.add_parser(
            "set-type", help="set the Jira issuetype via the artifact mapping"
        )
        p_set_type.add_argument("issue", help="Jira issue key")
        p_set_type.add_argument(
            "new_type",
            metavar="type",
            help="workflow artifact type whose Jira issuetype to apply",
        )

        for verb in verbs:
            sub = subparsers.add_parser(verb, help=f"apply the '{verb}' state transition")
            sub.add_argument("issue", help="Jira issue key")
            sub.add_argument(
                "--comment",
                help="optional comment posted alongside the transition",
            )

    @staticmethod
    def _patch_parser_for_friendly_verb_errors(
        parser: argparse.ArgumentParser,
        verbs: tuple[str, ...],
    ) -> None:
        prog = parser.prog
        original_error = parser.error

        def hint(verb: str) -> str:
            reserved = ", ".join(sorted(_RESERVED_FIELDS_VERBS))
            configured = ", ".join(verbs) if verbs else "(none configured)"
            return (
                f"{prog}: error: unknown verb '{verb}'.\n"
                f"  reserved verbs: {reserved}\n"
                f"  configured lifecycle verbs: {configured}\n"
                f"  to add this verb, configure providers.issues.state_transitions.{verb} "
                f"in .workflow/config.yml (see `workflow_setup.py build-config "
                f"--jira-state-transition {verb}=<transition>`).\n"
            )

        def patched_error(message: str) -> None:
            match = re.match(r"argument verb: invalid choice: '([^']+)'", message)
            if match:
                verb = match.group(1)
                parser.print_usage(sys.stderr)
                parser.exit(2, hint(verb))
            original_error(message)

        parser.error = patched_error  # type: ignore[assignment]

    def discover_state_verbs(self, config: WorkflowConfig) -> list[str]:
        """Return the configured Jira state-transition verbs.

        Used by the ``issue.py`` dispatcher (via the legacy ``issue_fields``
        module) so the parser only knows about the active project's
        transitions.
        """

        try:
            settings = _jira_issue_provider_settings(config.root)
        except Exception:  # noqa: BLE001 — match legacy fallback
            return []
        raw = settings.get("state_transitions") or settings.get("stateTransitions")
        if not isinstance(raw, Mapping):
            return []
        verbs: list[str] = []
        for key, value in raw.items():
            verb = str(key).strip()
            if not verb or verb in _RESERVED_FIELDS_VERBS:
                continue
            text = str(value).strip() if value is not None else ""
            if not text:
                continue
            verbs.append(verb)
        return sorted(set(verbs))

    def run_fields(
        self,
        args: argparse.Namespace,
        *,
        config: WorkflowConfig,
        runner: CommandRunner | None,
        stdout: TextIO,
        stderr: TextIO,
    ) -> int:
        try:
            payload = self._fields_payload(
                config=config,
                artifact_type=args.type,
                verb=args.verb,
                issue=args.issue,
                comment=getattr(args, "comment", None),
                user=getattr(args, "user", None),
                new_type=getattr(args, "new_type", None),
                runner=runner,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"Jira issue fields error: {exc}", file=stderr)
            return 2

        print(json.dumps(payload, indent=2, sort_keys=False), file=stdout)
        if payload.get("status") == "blocked":
            return 3
        return 0

    def _fields_payload(
        self,
        *,
        config: WorkflowConfig,
        artifact_type: str,
        verb: str,
        issue: str,
        comment: str | None,
        user: str | None,
        new_type: str | None,
        runner: CommandRunner | None,
    ) -> dict[str, Any]:
        try:
            site = resolve_jira_data_center_site(config.root)
            issue_key = normalize_jira_issue_key(issue)
        except (WorkflowConfigError, JiraProviderError) as exc:
            raise IssueBackendError(str(exc)) from exc

        provider = JiraDataCenterIssueNativeProvider(runner=runner)
        context = ProviderContext(project=config.root, artifact_type=artifact_type)

        if verb not in _RESERVED_FIELDS_VERBS:
            if comment:
                payload: dict[str, Any] = {
                    "issue": issue_key,
                    "freshness_check": True,
                    "body": comment,
                    "state": verb,
                }
                operation = "add_comment"
            else:
                payload = {"issue": issue_key, "freshness_check": True, "state": verb}
                operation = "update"
            response = provider.call(
                ProviderRequest(
                    role="issue",
                    kind="jira",
                    operation=operation,
                    context=context,
                    payload=payload,
                )
            )
            return flatten_provider_envelope(response.payload, project=config.root)

        if verb == "assign":
            if not user:
                raise IssueBackendError("assign requires a user")
            resolved = user
            if resolved.strip().lower() == "me":
                resolved = get_jira_myself(site, runner=runner)
            payload = {
                "issue": issue_key,
                "freshness_check": True,
                "assignee": resolved,
            }
        elif verb == "unassign":
            payload = {"issue": issue_key, "freshness_check": True, "unassign": True}
        elif verb == "set-type":
            if not new_type or not new_type.strip():
                raise IssueBackendError("set-type requires a non-empty type")
            artifact = new_type.strip().lower()
            try:
                settings = _jira_issue_provider_settings(config.root)
            except Exception as exc:  # noqa: BLE001
                raise IssueBackendError(str(exc)) from exc
            configured = _jira_configured_artifact_issue_types(settings).get(artifact)
            native = configured or JIRA_ARTIFACT_ISSUE_TYPES.get(artifact)
            if not native:
                raise IssueBackendError(
                    f"no Jira issuetype mapping for workflow type '{new_type}'. "
                    f"Configure providers.issues.artifact_issue_types.{artifact} in .workflow/config.yml."
                )
            payload = {
                "issue": issue_key,
                "freshness_check": True,
                "issuetype": native,
            }
        else:
            raise IssueBackendError(f"unsupported verb: {verb}")

        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="update",
                context=context,
                payload=payload,
            )
        )
        return flatten_provider_envelope(response.payload, project=config.root)


def _strip_body_frontmatter(body: str) -> str:
    if not _FRONTMATTER_HANDLER.detect(body):
        return body
    try:
        _frontmatter_text, remainder = _FRONTMATTER_HANDLER.split(body)
    except Exception:  # noqa: BLE001 — defensive
        return body
    return remainder.lstrip("\n")


def _required_text(value: str, name: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise IssueBackendError(f"{name} is required")
    return text


def _optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _jira_issue_key(value: str | None, name: str) -> str | None:
    parent = _optional_text(value)
    if parent is None:
        return None
    try:
        return normalize_jira_issue_key(parent)
    except JiraProviderError as exc:
        raise IssueBackendError(f"invalid {name}: {exc}") from exc


# ---------------------------------------------------------------------------
# Module-level helpers (call-site compatibility with the deleted ``jira_issue_*.py``
# CLIs). These let library tests keep their existing signatures (``project=...``,
# ``runner=...``) without depending on dispatcher plumbing. The dispatcher
# itself does NOT use these helpers — it goes through the backend driver.
# ---------------------------------------------------------------------------


# Error aliases preserved so existing ``pytest.raises(JiraIssueXxxError, ...)``
# assertions continue to work against the unified backend.
JiraIssueFetchError = IssueBackendError
JiraIssueCommentsError = IssueBackendError
JiraIssueDraftError = IssueBackendError
JiraIssueWritebackError = IssueBackendError
JiraIssueRelationshipsError = IssueBackendError
JiraIssueFieldsError = IssueBackendError


def _load_jira_config(project: Path) -> WorkflowConfig:
    from workflow_config import load_workflow_config

    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise IssueBackendError(str(exc)) from exc
    if config is None:
        raise IssueBackendError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise IssueBackendError(
            f"Jira issue dispatcher requires configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


def fetch_cache_payload(
    *,
    project: Path,
    references: list[str],
    cache_policy: str = CACHE_POLICY_DEFAULT,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Fetch configured Jira issue references into the workflow cache."""

    config = _load_jira_config(project)
    try:
        site = resolve_jira_data_center_site(config.root)
    except (WorkflowConfigError, JiraProviderError) as exc:
        raise IssueBackendError(str(exc)) from exc

    issue_keys = jira_issue_keys_from_references(references)
    if not issue_keys:
        raise IssueBackendError("no Jira issue references were found")

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    cache = JiraDataCenterIssueCache.for_project(config.root)
    contexts: list[IssueFetchContext] = []
    for issue in issue_keys:
        try:
            issue_key = normalize_jira_issue_key(issue)
        except JiraProviderError as exc:
            raise IssueBackendError(str(exc)) from exc
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="get",
                context=ProviderContext(
                    project=config.root,
                    artifact_type="task",
                    cache_policy=cache_policy,
                ),
                payload={
                    "issue": issue_key,
                    "include_body": False,
                    "include_comments": False,
                    "include_relationships": False,
                },
            )
        )
        issue_dir = cache.issue_dir(site, issue_key)
        comment_paths = tuple(
            display_project_path(path, config.root)
            for path in cache.comment_files(site, issue_key)
        )
        contexts.append(
            IssueFetchContext(
                number=issue_key,
                issue_dir=display_project_path(
                    issue_dir, config.root, trailing_slash=True
                ),
                title=str(response.payload.get("title") or ""),
                state=str(response.payload.get("state") or "").upper(),
                cache_refreshed=cache_refreshed_from_payload(
                    response.payload, default=True
                ),
                provider_kind="jira",
                comments=comment_paths,
            )
        )

    return format_issue_cache_json(contexts)


def append_comment(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    state: str | None = None,
    state_reason: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Post one comment from an opaque body file to one Jira issue."""

    config = _load_jira_config(project)
    return JiraIssueBackend()._append_comment(
        config=config,
        artifact_type=artifact_type,
        issue=issue,
        body_file=body_file,
        state=state,
        state_reason=state_reason,
        runner=runner,
    )


def publish_issue(
    *,
    project: Path,
    artifact_type: str,
    title: str,
    body_file: Path,
    labels: tuple[str, ...] = (),
    issue_type: str | None = None,
    subtask_parent: str | None = None,
    project_key: str | None = None,
    epic_name: str | None = None,
    assignee: str | None = None,
    relationship_intent: dict[str, object] | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Create a Jira issue from an opaque caller-owned body file."""

    config = _load_jira_config(project)
    return JiraIssueBackend()._publish_issue(
        config=config,
        artifact_type=artifact_type,
        title=title,
        body_file=body_file,
        labels=labels,
        issue_type=issue_type,
        subtask_parent=subtask_parent,
        project_key=project_key,
        epic_name=epic_name,
        assignee=assignee,
        relationship_intent=relationship_intent or {},
        runner=runner,
    )


def update_issue(
    *,
    project: Path,
    artifact_type: str,
    issue: str,
    body_file: Path,
    title: str | None = None,
    add_labels: tuple[str, ...] = (),
    remove_labels: tuple[str, ...] = (),
    set_labels: tuple[str, ...] | None = None,
    state: str | None = None,
    state_reason: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Update one Jira issue body from an opaque caller-owned body file."""

    config = _load_jira_config(project)
    return JiraIssueBackend()._update_issue(
        config=config,
        artifact_type=artifact_type,
        issue=issue,
        body_file=body_file,
        title=title,
        add_labels=add_labels,
        remove_labels=remove_labels,
        set_labels=set_labels,
        state=state,
        state_reason=state_reason,
        runner=runner,
    )


def apply_relationships_payload(
    *,
    project: Path,
    issue_ref: str,
    artifact_type: str,
    intent: dict[str, object],
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Apply a single Jira issue's relationship intent directly."""

    config = _load_jira_config(project)
    return JiraIssueBackend()._apply_relationships(
        config=config,
        issue_ref=issue_ref,
        artifact_type=artifact_type,
        intent=intent,
        runner=runner,
    )


def fields_payload(
    *,
    project: Path,
    artifact_type: str,
    verb: str,
    issue: str,
    comment: str | None = None,
    user: str | None = None,
    new_type: str | None = None,
    runner: CommandRunner | None = None,
) -> dict[str, Any]:
    """Apply a body-less Jira issue field mutation."""

    config = _load_jira_config(project)
    return JiraIssueBackend()._fields_payload(
        config=config,
        artifact_type=artifact_type,
        verb=verb,
        issue=issue,
        comment=comment,
        user=user,
        new_type=new_type,
        runner=runner,
    )
