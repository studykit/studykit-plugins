#!/usr/bin/env python3
"""Jira Data Center native issue provider."""

from __future__ import annotations

import hashlib
from collections.abc import Mapping
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from issue.cache import (
    FreshnessMetadata,
    PendingIssueRelationshipOperation,
    WorkflowCacheError,
    WorkflowFreshnessConflict,
    relationship_operations_from_intent,
    require_provider_freshness,
)
from issue.jira.cache import JiraDataCenterIssueCache, jira_target_fingerprint
from issue.jira.refs import JiraProviderError, normalize_jira_issue_key
from issue.jira.relationships import (
    filter_jira_payload,
    normalize_jira_data_center_issue,
    normalize_jira_remote_links,
)
from workflow_command import CommandRunner
from workflow_config import WorkflowConfigError, load_workflow_config
from issue.jira.client import (
    jira_download_attachment,
    jira_upload_attachments,
    jira_data_center_comments_path,
    jira_data_center_issue_path,
    jira_data_center_issue_link_path,
    jira_data_center_issue_links_path,
    jira_data_center_remote_link_global_id_path,
    jira_data_center_remote_link_path,
    jira_data_center_remote_links_path,
    jira_data_center_transitions_path,
    jira_delete,
    jira_get_json,
    jira_send_json,
    resolve_jira_data_center_site,
)
from issue.providers import (
    CACHE_POLICY_BYPASS,
    CACHE_POLICY_DEFAULT,
    TRANSPORT_NATIVE,
    IssueProvider,
    ProviderFreshnessError,
    ProviderOperationError,
    ProviderRequest,
)


JIRA_REVIEW_ISSUE_TYPE = "Task"
JIRA_REVIEW_TITLE_PREFIX = "[Review] "
JIRA_RESEARCH_TITLE_PREFIX = "[Research] "
JIRA_SPIKE_ISSUE_TYPE = "Task"
JIRA_SPIKE_TITLE_PREFIX = "[Spike] "
JIRA_ARTIFACT_ISSUE_TYPES = {
    "bug": "Bug",
    "epic": "Epic",
    "research": "Task",
    "review": JIRA_REVIEW_ISSUE_TYPE,
    "task": "Task",
    "usecase": "Story",
    "spike": JIRA_SPIKE_ISSUE_TYPE,
}


@dataclass(frozen=True)
class _JiraRelationshipMapping:
    relationship: str
    surface: str
    link_type: str | None = None
    direction: str | None = None
    field: str | None = None
    write_to: str | None = None
    value: str | None = None
    remote_relationship: str | None = None
    application_type: str | None = None
    application_name: str | None = None

    def to_json(self) -> dict[str, str]:
        result = {"relationship": self.relationship, "surface": self.surface}
        for key in (
            "link_type",
            "direction",
            "field",
            "write_to",
            "value",
            "remote_relationship",
            "application_type",
            "application_name",
        ):
            value = getattr(self, key)
            if value is not None:
                result[key] = value
        return result


@dataclass(frozen=True)
class _ResolvedJiraRelationshipOperation:
    action: str
    relationship: str
    target_ref: str
    mapping: _JiraRelationshipMapping
    target_issue: str | None = None
    link_id: str | None = None
    remote_url: str | None = None
    remote_title: str | None = None
    remote_global_id: str | None = None
    field_issue: str | None = None
    field_value: Any = None

    def to_json(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "action": self.action,
            "relationship": self.relationship,
            "target_ref": self.target_ref,
            "mapping": self.mapping.to_json(),
        }
        for key in (
            "target_issue",
            "link_id",
            "remote_url",
            "remote_title",
            "remote_global_id",
            "field_issue",
        ):
            value = getattr(self, key)
            if value is not None:
                result[key] = value
        if self.field_value is not None:
            result["field_value"] = self.field_value
        return result


class JiraDataCenterIssueNativeProvider(IssueProvider):
    """Native Jira Data Center issue provider backed by REST API v2 by default."""

    def __init__(self, *, runner: CommandRunner | None = None):
        super().__init__(kind="jira", transport=TRANSPORT_NATIVE)
        self.runner = runner

    def get(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue_key = normalize_jira_issue_key(_required_payload_value(request, "issue"))
        include_body = bool(request.payload.get("include_body", True))
        include_comments = bool(request.payload.get("include_comments", True))
        include_relationships = bool(request.payload.get("include_relationships", True))
        include_remote_links = bool(request.payload.get("include_remote_links", True))

        try:
            site = resolve_jira_data_center_site(request.context.project)
            cache = JiraDataCenterIssueCache.for_project(request.context.project)
            settings = _jira_issue_provider_settings(request.context.project)
            mappings = _relationship_mappings(settings)
            if request.context.cache_policy == CACHE_POLICY_DEFAULT:
                try:
                    return cache.read_issue(
                        site,
                        issue_key,
                        include_body=include_body,
                        include_comments=include_comments,
                        include_relationships=include_relationships,
                        relationship_mappings=mappings,
                    )
                except WorkflowCacheError:
                    pass

            raw_issue = get_issue(site, issue_key, runner=self.runner)
            remote_links = get_remote_links(site, issue_key, runner=self.runner) if include_remote_links else []
            payload = normalize_jira_data_center_issue(
                raw_issue,
                site=site,
                remote_links=remote_links,
                relationship_mappings=mappings,
            )

            if request.context.cache_policy != CACHE_POLICY_BYPASS:
                cache.write_issue_bundle(
                    site,
                    raw_issue,
                    remote_links=remote_links,
                    hidden_comment_markers=_jira_snapshot_hidden_comment_markers(settings),
                    relationship_mappings=mappings,
                )

            return filter_jira_payload(
                payload,
                include_body=include_body,
                include_comments=include_comments,
                include_relationships=include_relationships,
            )
        except JiraProviderError as exc:
            raise ProviderOperationError(str(exc)) from exc

    def comments(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue = self.get(request)
        return {"comments": issue.get("comments", [])}

    def create(self, request: ProviderRequest) -> Mapping[str, Any]:
        site = resolve_jira_data_center_site(request.context.project)
        cache = JiraDataCenterIssueCache.for_project(request.context.project)

        title = str(_required_payload_value(request, "title"))
        body = str(_required_payload_value(request, "body"))
        labels = tuple(_string_list(request.payload.get("labels")))

        settings = _jira_issue_provider_settings(request.context.project)
        title = _jira_issue_title(request, title)
        project_key = (
            _optional_string(request.payload.get("project") or request.payload.get("project_key"))
            or site.project
        )
        explicit_issue_type = _optional_string(
            request.payload.get("jira_issue_type") or request.payload.get("provider_issue_type")
        )
        issue_type = (
            explicit_issue_type
            or _jira_artifact_issue_type(request, settings=settings)
            or _optional_string(request.payload.get("issue_type") or request.payload.get("issuetype"))
            or site.issue_type
        )
        if not project_key:
            raise ProviderOperationError("Jira issue create requires provider project or payload.project")
        if not issue_type:
            raise ProviderOperationError("Jira issue create requires provider issue_type or payload.issue_type")
        subtask_parent_key = _jira_create_subtask_parent_key(request)
        if subtask_parent_key and not _is_jira_subtask_issue_type(issue_type):
            raise ProviderOperationError("Jira subtask_parent can only be used when issue_type is Sub-task")
        epic_name, epic_name_field = _jira_create_epic_name(
            request,
            settings=settings,
            issue_type=issue_type,
            title=title,
        )
        assignee = _optional_string(request.payload.get("assignee"))
        if assignee is not None and assignee.lower() == "me":
            assignee = get_jira_myself(site, runner=self.runner)

        created = create_issue(
            site,
            project_key=project_key,
            issue_type=issue_type,
            title=title,
            body=body,
            labels=labels,
            subtask_parent_key=subtask_parent_key,
            epic_name=epic_name,
            epic_name_field=epic_name_field,
            assignee=assignee,
            runner=self.runner,
        )
        issue_key = normalize_jira_issue_key(created.get("key") or created.get("issue") or "")
        write_result = self._refresh_cache(request.context.project, site, cache, issue_key)
        parent_write_result = (
            self._refresh_cache(request.context.project, site, cache, subtask_parent_key)
            if subtask_parent_key
            else None
        )
        payload: dict[str, Any] = {
            "operation": "create_issue",
            "issue": issue_key,
            "key": issue_key,
            "verified": True,
            "cache_refreshed": True,
            "cache": write_result,
        }
        if subtask_parent_key:
            payload["subtask_parent"] = subtask_parent_key
            payload["parent_cache_refreshed"] = True
            payload["parent_cache"] = parent_write_result
        return payload

    def update(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue_key = normalize_jira_issue_key(_required_payload_value(request, "issue"))
        state = _optional_string(request.payload.get("state"))
        normalized_state = state.lower() if state is not None else None

        label_set = request.payload.get("label_set")
        if label_set is None:
            label_set = request.payload.get("labels")
        label_add = request.payload.get("label_add")
        label_remove = request.payload.get("label_remove")
        if label_set is not None and (label_add or label_remove):
            raise ProviderOperationError(
                "Jira issue update cannot combine label_set with label_add or label_remove"
            )
        assignee = _optional_string(request.payload.get("assignee"))
        unassign = bool(request.payload.get("unassign"))
        if assignee is not None and unassign:
            raise ProviderOperationError(
                "Jira issue update cannot combine assignee with unassign"
            )
        issuetype = _optional_string(request.payload.get("issuetype"))

        fields: dict[str, Any] = {}
        if request.payload.get("title") is not None:
            title = str(request.payload["title"])
            fields["summary"] = _jira_issue_title(request, title)
        if request.payload.get("body") is not None:
            fields["description"] = str(request.payload["body"])
        if label_set is not None:
            fields["labels"] = _string_list(label_set)
        if assignee is not None:
            fields["assignee"] = {"name": assignee}
        elif unassign:
            fields["assignee"] = None
        if issuetype is not None:
            fields["issuetype"] = {"name": issuetype}

        update_payload: dict[str, list[dict[str, Any]]] = {}
        if label_add or label_remove:
            label_ops: list[dict[str, Any]] = []
            for label in _string_list(label_add) if label_add else ():
                if label:
                    label_ops.append({"add": label})
            for label in _string_list(label_remove) if label_remove else ():
                if label:
                    label_ops.append({"remove": label})
            if label_ops:
                update_payload["labels"] = label_ops

        if not fields and not update_payload and normalized_state is None:
            raise ProviderOperationError(
                "Jira issue update requires at least one of body, title, labels, "
                "assignee, issuetype, state"
            )

        site = resolve_jira_data_center_site(request.context.project)
        cache = JiraDataCenterIssueCache.for_project(request.context.project)
        try:
            self._require_write_freshness(request, site, cache, issue_key, target="issue")
        except ProviderFreshnessError as exc:
            return self._conflict_payload(
                site=site,
                cache=cache,
                project=request.context.project,
                issue_key=issue_key,
                operation="update_issue",
                target="issue",
                error=exc,
            )
        if fields or update_payload:
            update_issue(
                site,
                issue_key,
                fields=fields if fields else None,
                update=update_payload if update_payload else None,
                runner=self.runner,
            )

        state_result: Mapping[str, Any] | None = None
        if normalized_state is not None:
            state_result = self._apply_state_transition(request, site, issue_key, normalized_state)

        write_result = self._refresh_cache(request.context.project, site, cache, issue_key)
        return {
            "operation": "update_issue",
            "issue": issue_key,
            "key": issue_key,
            "verified": True,
            "state_changed": state_result is not None,
            "state": dict(state_result) if state_result is not None else None,
            "cache_refreshed": True,
            "cache": write_result,
        }

    def add_comment(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue_key = normalize_jira_issue_key(_required_payload_value(request, "issue"))
        body = str(_required_payload_value(request, "body"))
        state = _optional_string(request.payload.get("state"))
        normalized_state = state.lower() if state is not None else None
        return self._append_comment(request, issue_key, body, state=normalized_state)

    def add_attachment(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue_key = normalize_jira_issue_key(_required_payload_value(request, "issue"))
        raw_files = request.payload.get("files")
        if not isinstance(raw_files, (list, tuple)) or not raw_files:
            raise ProviderOperationError("add_attachment requires a non-empty 'files' payload")
        files = [str(path) for path in raw_files]

        site = resolve_jira_data_center_site(request.context.project)
        cache = JiraDataCenterIssueCache.for_project(request.context.project)
        uploaded = upload_attachments(site, issue_key, files, runner=self.runner)
        # Attachments are additive — they never conflict with a stale body
        # edit — so no freshness gate. Refresh the cache so the projection and
        # per-target fingerprints stay current for the next body-bearing write.
        write_result = self._refresh_cache(request.context.project, site, cache, issue_key)
        return {
            "operation": "add_attachment",
            "issue": issue_key,
            "key": issue_key,
            "attachments": [_attachment_summary(item) for item in uploaded],
            "cache_refreshed": True,
            "cache": write_result,
        }

    def get_attachment(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue_key = normalize_jira_issue_key(_required_payload_value(request, "issue"))
        ids = [str(value) for value in request.payload.get("ids") or []]
        names = [str(value) for value in request.payload.get("names") or []]
        want_all = bool(request.payload.get("all"))
        out_override = _optional_string(request.payload.get("out"))

        site = resolve_jira_data_center_site(request.context.project)
        raw_issue = get_issue(site, issue_key, runner=self.runner)
        fields = raw_issue.get("fields") if isinstance(raw_issue.get("fields"), Mapping) else {}
        attachments = [item for item in (fields.get("attachment") or []) if isinstance(item, Mapping)]
        selected = _select_attachments(attachments, ids=ids, names=names, want_all=want_all)
        if not selected:
            raise ProviderOperationError(
                f"no matching attachment found on Jira issue {issue_key}"
            )

        if out_override:
            out_dir = Path(out_override).expanduser()
        else:
            cache = JiraDataCenterIssueCache.for_project(request.context.project)
            out_dir = cache.issue_dir(site, issue_key) / "attachments"
        out_dir.mkdir(parents=True, exist_ok=True)

        downloaded: list[dict[str, Any]] = []
        for attachment in selected:
            content_url = _optional_string(attachment.get("content"))
            if not content_url:
                continue
            filename = _optional_string(attachment.get("filename")) or f"attachment-{attachment.get('id')}"
            dest = out_dir / filename
            jira_download_attachment(site, content_url, str(dest), runner=self.runner)
            downloaded.append(
                {
                    "id": _optional_string(attachment.get("id")),
                    "filename": filename,
                    "size": attachment.get("size") if isinstance(attachment.get("size"), int) else None,
                    "path": str(dest),
                }
            )

        return {
            "operation": "get_attachment",
            "issue": issue_key,
            "key": issue_key,
            "out_dir": str(out_dir),
            "downloaded": downloaded,
        }

    def apply_relationships(self, request: ProviderRequest) -> Mapping[str, Any]:
        issue_key = normalize_jira_issue_key(_required_payload_value(request, "issue"))
        intent = request.payload.get("relationship_intent") or {}
        if not isinstance(intent, Mapping):
            raise ProviderOperationError("relationship_intent must be a mapping")

        operations = relationship_operations_from_intent(
            intent,
            target_kind="issue",
            target_id=issue_key,
        )
        operations = self._resolve_parent_remove_target(request, issue_key, operations)

        if not operations:
            return {
                "operation": "apply_relationships",
                "issue": issue_key,
                "key": issue_key,
                "applied": 0,
                "operations": [],
                "provider_results": [],
                "cache_refreshed": False,
                "no_changes": True,
            }

        site = resolve_jira_data_center_site(request.context.project)
        cache = JiraDataCenterIssueCache.for_project(request.context.project)
        return self._apply_relationship_operations(request, site, cache, issue_key, operations)

    def _resolve_parent_remove_target(
        self,
        request: ProviderRequest,
        issue_key: str,
        operations: list[PendingIssueRelationshipOperation],
    ) -> list[PendingIssueRelationshipOperation]:
        if not any(
            op.action == "remove" and op.relationship == "parent" and not op.target_ref
            for op in operations
        ):
            return operations
        cache = JiraDataCenterIssueCache.for_project(request.context.project)
        site = resolve_jira_data_center_site(request.context.project)
        current_parent = ""
        try:
            cached = cache.read_issue(site, issue_key, include_body=False, include_comments=False)
        except WorkflowCacheError:
            cached = {}
        parent_value = (
            cached.get("parent")
            or cached.get("parentKey")
            or cached.get("parent_key")
        )
        if isinstance(parent_value, Mapping):
            parent_value = parent_value.get("key") or parent_value.get("ref") or parent_value.get("id")
        if parent_value not in (None, "", 0):
            current_parent = str(parent_value)
        resolved: list[PendingIssueRelationshipOperation] = []
        for op in operations:
            if op.action == "remove" and op.relationship == "parent" and not op.target_ref:
                if not current_parent:
                    continue
                resolved.append(replace(op, target_ref=current_parent))
            else:
                resolved.append(op)
        return resolved

    def _append_comment(
        self,
        request: ProviderRequest,
        issue_key: str,
        body: str,
        *,
        state: str | None = None,
    ) -> Mapping[str, Any]:
        site = resolve_jira_data_center_site(request.context.project)
        cache = JiraDataCenterIssueCache.for_project(request.context.project)
        for target in ("issue", "comments"):
            try:
                self._require_write_freshness(request, site, cache, issue_key, target=target)
            except ProviderFreshnessError as exc:
                return self._conflict_payload(
                    site=site,
                    cache=cache,
                    project=request.context.project,
                    issue_key=issue_key,
                    operation="add_comment",
                    target=target,
                    error=exc,
                )
        created = add_comment(site, issue_key, body=body, runner=self.runner)
        state_result: Mapping[str, Any] | None = None
        if state is not None:
            state_result = self._apply_state_transition(request, site, issue_key, state)
        write_result = self._refresh_cache(request.context.project, site, cache, issue_key)
        return {
            "operation": "add_comment",
            "issue": issue_key,
            "key": issue_key,
            "comment": dict(created) if isinstance(created, Mapping) else {},
            "state_changed": state_result is not None,
            "state": dict(state_result) if state_result is not None else None,
            "cache_refreshed": True,
            "cache": write_result,
        }

    def _apply_state_transition(
        self,
        request: ProviderRequest,
        site: Any,
        issue_key: str,
        verb: str,
    ) -> Mapping[str, Any]:
        settings = _jira_issue_provider_settings(request.context.project)
        transition_name = _jira_state_transition_name(verb, settings)
        if not transition_name:
            raise ProviderOperationError(
                f"Jira verb '{verb}' has no configured transition. "
                f"Run `workflow_setup.py jira-state-transition-inspect --jira-site <url> --issue <KEY>` "
                f"to list the workflow's transitions, then re-run the setup skill so "
                f"providers.issues.state_transitions.{verb} is confirmed into .workflow/config.yml."
            )
        transitions = get_transitions(site, issue_key, runner=self.runner)
        transition_id = _find_transition_id(transitions, transition_name)
        if transition_id is None:
            raise ProviderOperationError(
                f"Jira issue {issue_key} does not expose a '{transition_name}' transition right now. "
                f"If this workflow uses a different name for the '{verb}' verb, run "
                f"`workflow_setup.py jira-state-transition-inspect --jira-site <url> --issue <KEY>` and "
                f"configure providers.issues.state_transitions.{verb} in .workflow/config.yml."
            )
        transition_issue(site, issue_key, transition_id, runner=self.runner)
        return {
            "operation": "transition_issue",
            "verb": verb,
            "transition_name": transition_name,
            "transition_id": transition_id,
        }

    def _apply_relationship_operations(
        self,
        request: ProviderRequest,
        site: Any,
        cache: JiraDataCenterIssueCache,
        issue_key: str,
        operations: list[PendingIssueRelationshipOperation],
    ) -> Mapping[str, Any]:
        if not operations:
            raise ProviderOperationError(f"no Jira relationship operations found for issue {issue_key}")

        settings = _jira_issue_provider_settings(request.context.project)
        resolved = [
            _resolve_jira_relationship_operation(issue_key, operation, settings=settings)
            for operation in operations
        ]
        provider_current = self._require_write_freshness(request, site, cache, issue_key, target="relationships")
        prepared = self._prepare_relationship_removals(site, issue_key, provider_current, resolved)

        applied: list[Mapping[str, Any]] = []
        for operation in prepared:
            applied.append(self._dispatch_relationship_operation(site, operation))

        write_result = self._refresh_cache(request.context.project, site, cache, issue_key)
        return {
            "operation": "apply_relationships",
            "issue": issue_key,
            "key": issue_key,
            "applied": len(applied),
            "operations": [operation.to_json() for operation in prepared],
            "provider_results": [dict(item) for item in applied],
            "cache_refreshed": True,
            "cache": dict(write_result),
        }

    def _prepare_relationship_removals(
        self,
        site: Any,
        issue_key: str,
        provider_current: Mapping[str, Any] | None,
        operations: list[_ResolvedJiraRelationshipOperation],
    ) -> list[_ResolvedJiraRelationshipOperation]:
        needs_issue = any(operation.action == "remove" and operation.mapping.surface == "issue_link" for operation in operations)
        current_issue = provider_current if provider_current is not None else None
        if needs_issue and current_issue is None:
            current_issue = get_issue(site, issue_key, runner=self.runner)

        needs_remote_links = any(
            operation.action == "remove" and operation.mapping.surface == "remote_link" for operation in operations
        )
        current_remote_links = get_remote_links(site, issue_key, runner=self.runner) if needs_remote_links else []

        prepared: list[_ResolvedJiraRelationshipOperation] = []
        for operation in operations:
            if operation.action == "remove" and operation.mapping.surface == "issue_link":
                assert current_issue is not None
                link_id = _find_issue_link_id(current_issue, operation)
                if link_id is None:
                    raise ProviderOperationError(
                        f"Jira issue link not found for {operation.relationship} {operation.target_ref}"
                    )
                operation = replace(operation, link_id=link_id)
            elif operation.action == "remove" and operation.mapping.surface == "remote_link":
                if not any(link.get("global_id") == operation.remote_global_id for link in current_remote_links):
                    raise ProviderOperationError(
                        f"Jira remote link not found for {operation.relationship} {operation.target_ref}"
                    )
            prepared.append(operation)
        return prepared

    def _dispatch_relationship_operation(
        self,
        site: Any,
        operation: _ResolvedJiraRelationshipOperation,
    ) -> Mapping[str, Any]:
        if operation.mapping.surface == "issue_link":
            if operation.action == "add":
                assert operation.target_issue is not None
                return create_issue_link(
                    site,
                    source_issue=operation.field_issue or "",
                    target_issue=operation.target_issue,
                    link_type=operation.mapping.link_type or "",
                    direction=operation.mapping.direction or "",
                    runner=self.runner,
                )
            assert operation.link_id is not None
            return delete_issue_link(site, operation.link_id, runner=self.runner)

        if operation.mapping.surface == "remote_link":
            assert operation.remote_url is not None
            assert operation.remote_title is not None
            assert operation.remote_global_id is not None
            if operation.action == "add":
                return create_remote_link(
                    site,
                    issue_key=operation.field_issue or "",
                    url=operation.remote_url,
                    title=operation.remote_title,
                    global_id=operation.remote_global_id,
                    relationship=operation.mapping.remote_relationship or operation.relationship.replace("_", " "),
                    application_type=operation.mapping.application_type,
                    application_name=operation.mapping.application_name,
                    runner=self.runner,
                )
            return delete_remote_link_by_global_id(
                site,
                issue_key=operation.field_issue or "",
                global_id=operation.remote_global_id,
                runner=self.runner,
            )

        if operation.mapping.surface == "field":
            assert operation.mapping.field is not None
            assert operation.field_issue is not None
            value = operation.field_value if operation.action == "add" else None
            return update_issue(site, operation.field_issue, fields={operation.mapping.field: value}, runner=self.runner)

        raise ProviderOperationError(f"unsupported Jira relationship surface: {operation.mapping.surface}")

    def _require_write_freshness(
        self,
        request: ProviderRequest,
        site: Any,
        cache: JiraDataCenterIssueCache,
        issue_key: str,
        *,
        target: str,
    ) -> Mapping[str, Any] | None:
        if _truthy(request.payload.get("overwrite")):
            return get_issue(site, issue_key, runner=self.runner)
        freshness_flag = request.payload.get("freshness_check")
        if freshness_flag is None:
            freshness_flag = request.payload.get("check_freshness")
        if freshness_flag is not None and not _truthy(freshness_flag):
            return None
        artifact = f"Jira issue {issue_key} {target}"
        try:
            metadata = cache.read_freshness_metadata(site, issue_key, target=target)
        except WorkflowCacheError:
            metadata = FreshnessMetadata(
                fingerprint=None,
                path=cache.meta_file(site, issue_key),
                target=target,
            )
        provider_current = get_issue(site, issue_key, runner=self.runner)
        provider_fingerprint = self._provider_fingerprint(
            request, site, provider_current, target=target
        )
        try:
            require_provider_freshness(
                metadata, provider_fingerprint=provider_fingerprint, artifact=artifact
            )
        except WorkflowFreshnessConflict as exc:
            raise ProviderFreshnessError(str(exc), result=exc.result) from exc
        return provider_current

    def _provider_fingerprint(
        self,
        request: ProviderRequest,
        site: Any,
        provider_current: Mapping[str, Any],
        *,
        target: str,
    ) -> str | None:
        """Recompute the provider's current fingerprint for one freshness target.

        Normalizes the freshly-fetched issue the same way the cache does at write
        time, so an unchanged artifact yields an identical fingerprint. Remote
        links are irrelevant to every fingerprint target, so they are skipped.
        """

        settings = _jira_issue_provider_settings(request.context.project)
        normalized = normalize_jira_data_center_issue(
            provider_current,
            site=site,
            remote_links=[],
            relationship_mappings=_relationship_mappings(settings),
        )
        return jira_target_fingerprint(
            normalized,
            target,
            hidden_comment_markers=_jira_snapshot_hidden_comment_markers(settings),
        )

    def _refresh_cache(
        self,
        project: Any,
        site: Any,
        cache: JiraDataCenterIssueCache,
        issue_key: str,
    ) -> Mapping[str, str]:
        raw_issue = get_issue(site, issue_key, runner=self.runner)
        remote_links = get_remote_links(site, issue_key, runner=self.runner)
        settings = _jira_issue_provider_settings(project)
        return cache.write_issue_bundle(
            site,
            raw_issue,
            remote_links=remote_links,
            hidden_comment_markers=_jira_snapshot_hidden_comment_markers(settings),
            relationship_mappings=_relationship_mappings(settings),
        )

    def _conflict_payload(
        self,
        *,
        site: Any,
        cache: JiraDataCenterIssueCache,
        project: Any,
        issue_key: str,
        operation: str,
        target: str,
        error: ProviderFreshnessError,
        pending_files: list[str] | None = None,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "operation": operation,
            "issue": issue_key,
            "key": issue_key,
            "status": "conflict",
            "reason": "provider_changed",
            "message": (
                f"{operation} stopped: Jira issue {issue_key} {target} changed on the provider "
                "since it was last fetched. The cache was refreshed — reread the listed paths and "
                "reapply your change, or retry with --overwrite to replace the provider copy."
            ),
            "target": target,
            "conflict": error.to_json(),
            "reread_required": True,
            "reread_paths": self._reread_paths(cache, site, issue_key),
            "overwrite_hint": "--overwrite",
        }
        if pending_files is not None:
            payload["pending_files"] = pending_files
        try:
            write_result = self._refresh_cache(project, site, cache, issue_key)
        except Exception as refresh_exc:  # pragma: no cover - defensive reporting path
            payload["cache_refreshed"] = False
            payload["refresh_error"] = str(refresh_exc)
        else:
            payload["cache_refreshed"] = True
            payload["cache"] = dict(write_result)
        return payload

    def _reread_paths(
        self,
        cache: JiraDataCenterIssueCache,
        site: Any,
        issue_key: str,
    ) -> list[str]:
        paths = [str(cache.issue_file(site, issue_key))]
        paths.extend(str(path) for path in cache.comment_files(site, issue_key))
        return paths


def get_issue(
    site: Any,
    issue_key: str,
    *,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    """Read one Jira Data Center issue REST object."""

    raw_issue = jira_get_json(site, jira_data_center_issue_path(site, issue_key), runner=runner)
    if not isinstance(raw_issue, Mapping):
        raise JiraProviderError(f"Jira Data Center issue response was not an object: {issue_key}")
    return raw_issue


def get_remote_links(
    site: Any,
    issue_key: str,
    *,
    runner: CommandRunner | None = None,
) -> list[dict[str, Any]]:
    """Read Jira Data Center remote links for one issue."""

    raw_links = jira_get_json(site, jira_data_center_remote_links_path(site, issue_key), runner=runner)
    return normalize_jira_remote_links(raw_links)


def create_issue(
    site: Any,
    *,
    project_key: str,
    issue_type: str,
    title: str,
    body: str,
    labels: tuple[str, ...] = (),
    subtask_parent_key: str | None = None,
    epic_name: str | None = None,
    epic_name_field: str | None = None,
    assignee: str | None = None,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    payload: dict[str, Any] = {
        "fields": {
            "project": {"key": project_key},
            "summary": title,
            "description": body,
            "issuetype": {"name": issue_type},
        }
    }
    if labels:
        payload["fields"]["labels"] = list(labels)
    if subtask_parent_key:
        payload["fields"]["parent"] = {"key": subtask_parent_key}
    if epic_name is not None and epic_name_field is not None:
        payload["fields"][epic_name_field] = epic_name
    if assignee:
        payload["fields"]["assignee"] = {"name": assignee}
    result = jira_send_json(site, "POST", f"/rest/api/{site.api_version}/issue", payload, runner=runner)
    if not isinstance(result, Mapping):
        raise JiraProviderError("Jira create issue response was not an object")
    return result


def update_issue(
    site: Any,
    issue_key: str,
    *,
    fields: Mapping[str, Any] | None = None,
    update: Mapping[str, Any] | None = None,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    payload: dict[str, Any] = {}
    if fields:
        payload["fields"] = dict(fields)
    if update:
        payload["update"] = dict(update)
    if not payload:
        return {}
    result = jira_send_json(
        site,
        "PUT",
        jira_data_center_issue_path(site, issue_key),
        payload,
        runner=runner,
    )
    if not isinstance(result, Mapping):
        return {}
    return result


def get_jira_myself(
    site: Any,
    *,
    runner: CommandRunner | None = None,
) -> str:
    """Return the authenticated Jira user's name via ``/rest/api/<v>/myself``."""

    path = f"/rest/api/{site.api_version}/myself"
    result = jira_get_json(site, path, runner=runner)
    if isinstance(result, Mapping):
        name = result.get("name")
        if isinstance(name, str) and name.strip():
            return name.strip()
    raise ProviderOperationError("could not resolve Jira authenticated user (missing 'name')")


def create_issue_link(
    site: Any,
    *,
    source_issue: str,
    target_issue: str,
    link_type: str,
    direction: str,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    """Create one Jira issue link from source issue relationship intent."""

    source_key = normalize_jira_issue_key(source_issue)
    target_key = normalize_jira_issue_key(target_issue)
    if direction == "outward":
        outward_issue = source_key
        inward_issue = target_key
    elif direction == "inward":
        outward_issue = target_key
        inward_issue = source_key
    else:
        raise JiraProviderError(f"unsupported Jira issue link direction: {direction}")
    result = jira_send_json(
        site,
        "POST",
        jira_data_center_issue_links_path(site),
        {
            "type": {"name": link_type},
            "inwardIssue": {"key": inward_issue},
            "outwardIssue": {"key": outward_issue},
        },
        runner=runner,
    )
    if not isinstance(result, Mapping):
        return {}
    return result


def delete_issue_link(
    site: Any,
    link_id: str,
    *,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    result = jira_delete(site, jira_data_center_issue_link_path(site, link_id), runner=runner)
    if not isinstance(result, Mapping):
        return {}
    return result


def create_remote_link(
    site: Any,
    *,
    issue_key: str,
    url: str,
    title: str,
    global_id: str,
    relationship: str,
    application_type: str | None = None,
    application_name: str | None = None,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    payload: dict[str, Any] = {
        "globalId": global_id,
        "relationship": relationship,
        "object": {"url": url, "title": title},
    }
    if application_type or application_name:
        payload["application"] = {
            "type": application_type or "studykit.workflow",
            "name": application_name or "Workflow",
        }
    result = jira_send_json(site, "POST", jira_data_center_remote_links_path(site, issue_key), payload, runner=runner)
    if not isinstance(result, Mapping):
        return {}
    return result


def delete_remote_link_by_global_id(
    site: Any,
    *,
    issue_key: str,
    global_id: str,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    result = jira_delete(site, jira_data_center_remote_link_global_id_path(site, issue_key, global_id), runner=runner)
    if not isinstance(result, Mapping):
        return {}
    return result


def delete_remote_link(
    site: Any,
    *,
    issue_key: str,
    link_id: str,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    result = jira_delete(site, jira_data_center_remote_link_path(site, issue_key, link_id), runner=runner)
    if not isinstance(result, Mapping):
        return {}
    return result


def add_comment(
    site: Any,
    issue_key: str,
    *,
    body: str,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    result = jira_send_json(
        site,
        "POST",
        jira_data_center_comments_path(site, issue_key),
        {"body": body},
        runner=runner,
    )
    if not isinstance(result, Mapping):
        return {}
    return result


def upload_attachments(
    site: Any,
    issue_key: str,
    file_paths: list[str],
    *,
    runner: CommandRunner | None = None,
) -> list[Mapping[str, Any]]:
    """Upload local files to a Jira issue and return the created attachments."""

    raw = jira_upload_attachments(site, issue_key, file_paths, runner=runner)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, Mapping)]


def _select_attachments(
    attachments: list[Mapping[str, Any]],
    *,
    ids: list[str],
    names: list[str],
    want_all: bool,
) -> list[Mapping[str, Any]]:
    """Filter raw Jira attachment objects by id / filename, or take all."""

    if want_all:
        return list(attachments)
    id_set = {value for value in ids if value}
    name_set = {value for value in names if value}
    selected: list[Mapping[str, Any]] = []
    for item in attachments:
        item_id = str(item.get("id")) if item.get("id") is not None else None
        item_name = item.get("filename")
        if (item_id is not None and item_id in id_set) or (item_name in name_set):
            selected.append(item)
    return selected


def _attachment_summary(item: Mapping[str, Any]) -> dict[str, Any]:
    """Project the consumer-facing fields of one Jira attachment object."""

    return {
        "id": item.get("id"),
        "filename": item.get("filename"),
        "size": item.get("size"),
        "mime_type": item.get("mimeType"),
        "content": item.get("content"),
        "created": item.get("created"),
    }


def get_transitions(
    site: Any,
    issue_key: str,
    *,
    runner: CommandRunner | None = None,
) -> list[Mapping[str, Any]]:
    """Read available transitions for one Jira issue."""

    raw = jira_get_json(site, jira_data_center_transitions_path(site, issue_key), runner=runner)
    if isinstance(raw, Mapping):
        value = raw.get("transitions")
    else:
        value = raw
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]


def transition_issue(
    site: Any,
    issue_key: str,
    transition_id: str,
    *,
    runner: CommandRunner | None = None,
) -> Mapping[str, Any]:
    """POST a Jira transition to change issue state."""

    result = jira_send_json(
        site,
        "POST",
        jira_data_center_transitions_path(site, issue_key),
        {"transition": {"id": str(transition_id)}},
        runner=runner,
    )
    if not isinstance(result, Mapping):
        return {}
    return result


def _find_transition_id(
    transitions: list[Mapping[str, Any]],
    transition_name: str,
) -> str | None:
    target = transition_name.strip().lower()
    for transition in transitions:
        name = str(transition.get("name") or "").strip().lower()
        if name == target and transition.get("id") is not None:
            return str(transition["id"])
    return None


def _jira_state_transition_name(verb: str, settings: Mapping[str, Any]) -> str | None:
    raw = settings.get("state_transitions") or settings.get("stateTransitions")
    if isinstance(raw, Mapping):
        value = raw.get(verb)
        if value is not None:
            text = str(value).strip()
            if text:
                return text
    return None


def _required_payload_value(request: ProviderRequest, key: str) -> Any:
    value = request.payload.get(key)
    if value is None or value == "":
        raise ProviderOperationError(f"{request.operation} requires payload.{key}")
    return value


def _is_review_request(request: ProviderRequest) -> bool:
    return request.context.artifact_type.strip().lower() == "review"


def _is_research_request(request: ProviderRequest) -> bool:
    return request.context.artifact_type.strip().lower() == "research"


def _is_spike_request(request: ProviderRequest) -> bool:
    return request.context.artifact_type.strip().lower() == "spike"


def _jira_artifact_issue_type(request: ProviderRequest, *, settings: Mapping[str, Any]) -> str | None:
    artifact = request.context.artifact_type.strip().lower()
    configured = _jira_configured_artifact_issue_types(settings).get(artifact)
    return configured or JIRA_ARTIFACT_ISSUE_TYPES.get(artifact)


def _jira_configured_artifact_issue_types(settings: Mapping[str, Any]) -> Mapping[str, str]:
    raw = (
        settings.get("artifact_issue_types")
        or settings.get("artifactIssueTypes")
        or settings.get("issue_types")
        or settings.get("issueTypes")
    )
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        raise ProviderOperationError("providers.issues.artifact_issue_types must be a mapping")
    result: dict[str, str] = {}
    for key, value in raw.items():
        artifact = str(key).strip().lower()
        issue_type = _optional_string(value)
        if artifact and issue_type:
            result[artifact] = issue_type
    return result


def _jira_create_epic_name(
    request: ProviderRequest,
    *,
    settings: Mapping[str, Any],
    issue_type: str,
    title: str,
) -> tuple[str | None, str | None]:
    """Resolve Epic Name payload for create requests.

    Returns ``(epic_name, epic_name_field)`` when the request targets the
    configured Epic issue type; ``(None, None)`` otherwise. Raises when
    ``epic_name`` is set for a non-Epic create (typo guard) or when the
    Epic issue type is selected without ``epic_fields.name`` configured.
    """

    raw_epic_name = _optional_string(
        request.payload.get("epic_name") or request.payload.get("epicName")
    )
    epic_type_name = _jira_epic_issue_type_name(settings)
    if not _is_jira_epic_issue_type(issue_type, epic_type_name=epic_type_name):
        if raw_epic_name is not None:
            raise ProviderOperationError(
                "Jira epic_name is only valid when issue_type matches the configured Epic"
            )
        return None, None
    epic_name_field = _jira_epic_field_id(settings, "name")
    if not epic_name_field:
        raise ProviderOperationError(
            "Jira Epic create requires providers.issues.epic_fields.name; "
            f"got mapped issue_type={issue_type} but the field is unconfigured"
        )
    return raw_epic_name or title, epic_name_field


def _jira_epic_issue_type_name(settings: Mapping[str, Any]) -> str:
    configured = _jira_configured_artifact_issue_types(settings).get("epic")
    return configured or JIRA_ARTIFACT_ISSUE_TYPES["epic"]


def _is_jira_epic_issue_type(issue_type: str, *, epic_type_name: str) -> bool:
    return issue_type.strip().lower() == epic_type_name.strip().lower()


def _jira_epic_fields(settings: Mapping[str, Any]) -> Mapping[str, Any]:
    raw = settings.get("epic_fields") or settings.get("epicFields")
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        raise ProviderOperationError("providers.issues.epic_fields must be a mapping")
    return raw


def _jira_epic_field_id(settings: Mapping[str, Any], kind: str) -> str | None:
    raw = _jira_epic_fields(settings).get(kind)
    return _optional_string(raw)


def _jira_create_subtask_parent_key(request: ProviderRequest) -> str | None:
    raw_parent: str | None = None
    for key in ("subtask_parent", "subtask_parent_key", "subtaskParent", "subtaskParentKey"):
        if request.payload.get(key) is not None:
            raw_parent = str(request.payload[key])
            break
    parent = _optional_string(raw_parent)
    if parent is None:
        return None
    try:
        return normalize_jira_issue_key(parent)
    except JiraProviderError as exc:
        raise ProviderOperationError(f"invalid Jira subtask_parent: {exc}") from exc


def _is_jira_subtask_issue_type(issue_type: str) -> bool:
    normalized = issue_type.strip().lower().replace("-", "").replace("_", "").replace(" ", "")
    return normalized in {"subtask", "subissue"}


def _jira_issue_title(request: ProviderRequest, title: str) -> str:
    if _is_review_request(request):
        return _jira_prefixed_title(title, JIRA_REVIEW_TITLE_PREFIX)
    if _is_research_request(request):
        return _jira_prefixed_title(title, JIRA_RESEARCH_TITLE_PREFIX)
    if _is_spike_request(request):
        return _jira_prefixed_title(title, JIRA_SPIKE_TITLE_PREFIX)
    return title


def _jira_review_title(title: str) -> str:
    return _jira_prefixed_title(title, JIRA_REVIEW_TITLE_PREFIX)


def _jira_prefixed_title(title: str, prefix: str) -> str:
    if title.startswith(prefix):
        return title
    marker = prefix.strip()
    if title.lower().startswith(marker.lower()):
        return f"{prefix}{title[len(marker):].lstrip()}"
    return f"{prefix}{title}"


def _optional_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, Mapping):
        name = value.get("name")
        return [str(name)] if name else []
    if isinstance(value, list | tuple | set):
        labels: list[str] = []
        for item in value:
            if isinstance(item, Mapping):
                name = item.get("name")
                if name:
                    labels.append(str(name))
            elif item is not None:
                labels.append(str(item))
        return labels
    return [str(value)]


def _truthy(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip().lower() not in {"", "0", "false", "no", "off"}
    return bool(value)


def _jira_issue_provider_settings(project: Any) -> Mapping[str, Any]:
    try:
        config = load_workflow_config(project, require=True)
    except (WorkflowConfigError, JiraProviderError) as exc:
        raise ProviderOperationError(str(exc)) from exc
    if config is None or config.issues.kind != "jira":
        raise ProviderOperationError("workflow issue provider is not configured as Jira")
    return config.issues.settings


def _jira_snapshot_hidden_comment_markers(settings: Mapping[str, Any]) -> tuple[str, ...]:
    snapshot = settings.get("snapshot")
    raw = None
    if isinstance(snapshot, Mapping):
        raw = (
            snapshot.get("hidden_comment_markers")
            or snapshot.get("hiddenCommentMarkers")
            or snapshot.get("hide_comment_markers")
            or snapshot.get("comment_hide_markers")
            or snapshot.get("comment_exclude_markers")
        )
    if raw is None:
        raw = settings.get("snapshot_hidden_comment_markers") or settings.get("snapshotHiddenCommentMarkers")
    return _string_tuple(raw, setting="providers.issues.snapshot.hidden_comment_markers")


def _string_tuple(value: Any, *, setting: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    if isinstance(value, list | tuple | set):
        return tuple(str(item).strip() for item in value if str(item).strip())
    raise ProviderOperationError(f"{setting} must be a string or a list of strings")


def _resolve_jira_relationship_operation(
    source_issue: str,
    operation: PendingIssueRelationshipOperation,
    *,
    settings: Mapping[str, Any],
) -> _ResolvedJiraRelationshipOperation:
    mapping = _relationship_mapping(settings, operation.relationship)
    action = operation.action
    if action not in {"add", "remove"}:
        raise ProviderOperationError(f"unsupported Jira relationship action: {action}")

    if mapping.surface == "issue_link":
        target_issue = _jira_relationship_target_issue(operation)
        return _ResolvedJiraRelationshipOperation(
            action=action,
            relationship=operation.relationship,
            target_ref=operation.target_ref,
            target_issue=target_issue,
            field_issue=source_issue,
            mapping=mapping,
        )

    if mapping.surface == "remote_link":
        remote = _remote_link_target(operation.target_ref)
        return _ResolvedJiraRelationshipOperation(
            action=action,
            relationship=operation.relationship,
            target_ref=operation.target_ref,
            field_issue=source_issue,
            remote_url=remote["url"],
            remote_title=remote["title"],
            remote_global_id=_remote_global_id(remote["url"]),
            mapping=mapping,
        )

    if mapping.surface == "field":
        target_issue = _jira_relationship_target_issue(operation)
        field_issue = source_issue
        field_value_target = target_issue
        if mapping.write_to == "target":
            field_issue = target_issue
            field_value_target = source_issue
        field_value = _jira_field_value(field_value_target, mapping)
        return _ResolvedJiraRelationshipOperation(
            action=action,
            relationship=operation.relationship,
            target_ref=operation.target_ref,
            target_issue=target_issue,
            field_issue=field_issue,
            field_value=field_value,
            mapping=mapping,
        )

    raise ProviderOperationError(f"unsupported Jira relationship surface: {mapping.surface}")


def validate_relationship_intent_mappings(
    project: Any, intent: Mapping[str, Any]
) -> None:
    """Raise ``ProviderOperationError`` if any relationship in ``intent`` lacks a
    configured ``providers.issues.relationship_mappings`` entry. Lets callers
    fail fast before issuing a remote write that would later be rejected by
    ``apply_relationships``.
    """

    if not intent:
        return
    settings = _jira_issue_provider_settings(project)
    operations = relationship_operations_from_intent(
        intent, target_kind="issue", target_id="__pre_create__"
    )
    seen: set[str] = set()
    for operation in operations:
        name = operation.relationship
        if name in seen:
            continue
        seen.add(name)
        _relationship_mapping(settings, name)


def _relationship_mapping(settings: Mapping[str, Any], relationship: str) -> _JiraRelationshipMapping:
    raw_mappings = _relationship_mappings(settings)
    aliases = _relationship_aliases(relationship)
    raw_mapping = None
    matched_name = relationship
    for alias in aliases:
        if alias in raw_mappings:
            raw_mapping = raw_mappings[alias]
            matched_name = alias
            break
    if raw_mapping is None:
        raise ProviderOperationError(
            f"Jira relationship '{relationship}' is not configured; add providers.issues.relationship_mappings.{relationship}"
        )
    if not isinstance(raw_mapping, Mapping):
        raise ProviderOperationError(f"Jira relationship mapping for '{matched_name}' must be a mapping")

    surface = _optional_string(raw_mapping.get("surface") or raw_mapping.get("kind"))
    link_type = _optional_string(raw_mapping.get("link_type") or raw_mapping.get("linkType") or raw_mapping.get("name"))
    field = _optional_string(raw_mapping.get("field") or raw_mapping.get("field_id") or raw_mapping.get("fieldId"))
    if surface is None:
        if link_type:
            surface = "issue_link"
        elif field:
            surface = "field"
        elif _truthy(raw_mapping.get("remote_link") or raw_mapping.get("remoteLink")):
            surface = "remote_link"
    surface = _normalize_surface(surface)

    if surface == "issue_link":
        if not link_type:
            raise ProviderOperationError(f"Jira issue-link mapping for '{matched_name}' requires link_type")
        direction = _normalize_direction(raw_mapping.get("direction"))
        return _JiraRelationshipMapping(
            relationship=relationship,
            surface=surface,
            link_type=link_type,
            direction=direction,
        )

    if surface == "remote_link":
        remote_relationship = _optional_string(
            raw_mapping.get("relationship_label")
            or raw_mapping.get("relationshipLabel")
            or raw_mapping.get("remote_relationship")
            or raw_mapping.get("remoteRelationship")
            or raw_mapping.get("relationship")
        )
        return _JiraRelationshipMapping(
            relationship=relationship,
            surface=surface,
            remote_relationship=remote_relationship,
            application_type=_optional_string(raw_mapping.get("application_type") or raw_mapping.get("applicationType")),
            application_name=_optional_string(raw_mapping.get("application_name") or raw_mapping.get("applicationName")),
        )

    if surface == "field":
        if not field:
            raise ProviderOperationError(f"Jira field mapping for '{matched_name}' requires field")
        write_to = _normalize_write_to(raw_mapping.get("write_to") or raw_mapping.get("writeTo"))
        value = _normalize_field_value_kind(raw_mapping.get("value") or raw_mapping.get("value_kind") or raw_mapping.get("valueKind"))
        return _JiraRelationshipMapping(
            relationship=relationship,
            surface=surface,
            field=field,
            write_to=write_to,
            value=value,
        )

    raise ProviderOperationError(f"unsupported Jira relationship surface for '{matched_name}': {surface}")


def _relationship_mappings(settings: Mapping[str, Any]) -> Mapping[str, Any]:
    raw = settings.get("relationship_mappings") or settings.get("relationshipMappings")
    if raw is None and isinstance(settings.get("relationships"), Mapping):
        relationships = settings["relationships"]
        assert isinstance(relationships, Mapping)
        raw = relationships.get("mappings") or relationships
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        raise ProviderOperationError("providers.issues.relationship_mappings must be a mapping")
    return raw


def _relationship_aliases(relationship: str) -> tuple[str, ...]:
    normalized = relationship.strip().lower().replace("-", "_")
    aliases = {
        "parent": ("parent",),
        "child": ("child", "children", "subtask", "subtasks"),
        "blocked_by": ("blocked_by", "blockedBy", "depends_on", "dependency"),
        "blocking": ("blocking", "blocks"),
        "related": ("related", "relates_to"),
    }
    return aliases.get(normalized, (normalized,))


def _normalize_surface(value: str | None) -> str:
    if value is None:
        raise ProviderOperationError("Jira relationship mapping requires surface, link_type, field, or remote_link")
    normalized = value.strip().lower().replace("-", "_")
    aliases = {
        "issuelink": "issue_link",
        "link": "issue_link",
        "issue": "issue_link",
        "remote": "remote_link",
        "remotelink": "remote_link",
        "field_update": "field",
        "parent_field": "field",
    }
    return aliases.get(normalized, normalized)


def _normalize_direction(value: Any) -> str:
    raw_direction = _optional_string(value)
    direction = raw_direction.lower().replace("-", "_") if raw_direction else None
    if direction not in {"outward", "inward"}:
        raise ProviderOperationError("Jira issue-link relationship mapping requires direction 'outward' or 'inward'")
    return direction


def _normalize_write_to(value: Any) -> str:
    raw_write_to = _optional_string(value)
    write_to = raw_write_to.lower().replace("-", "_") if raw_write_to else None
    if write_to not in {"source", "target"}:
        raise ProviderOperationError("Jira field relationship mapping requires write_to 'source' or 'target'")
    return write_to


def _normalize_field_value_kind(value: Any) -> str:
    raw_value_kind = _optional_string(value)
    value_kind = raw_value_kind.lower().replace("-", "_") if raw_value_kind else None
    if value_kind not in {"key", "key_object", "string"}:
        raise ProviderOperationError("Jira field relationship mapping requires value 'key', 'key_object', or 'string'")
    return value_kind


def _jira_relationship_target_issue(operation: PendingIssueRelationshipOperation) -> str:
    try:
        return normalize_jira_issue_key(operation.target_ref)
    except JiraProviderError as exc:
        raise ProviderOperationError(
            f"Jira relationship '{operation.relationship}' requires a Jira issue key target: {operation.target_ref}"
        ) from exc


def _remote_link_target(target_ref: str) -> dict[str, str]:
    text = target_ref.strip()
    parsed = urlparse(text)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ProviderOperationError(
            f"Jira remote-link relationship requires an absolute http(s) URL target: {target_ref}"
        )
    title = parsed.path.rstrip("/").rsplit("/", 1)[-1] or parsed.netloc
    return {"url": text, "title": title}


def _remote_global_id(url: str) -> str:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return f"system=studykit-workflow&id={digest}"


def _jira_field_value(issue_key: str, mapping: _JiraRelationshipMapping) -> Any:
    value_kind = mapping.value
    if value_kind == "string":
        return issue_key
    if value_kind == "key":
        return {"key": issue_key}
    if value_kind == "key_object":
        return {"key": issue_key}
    raise ProviderOperationError(f"unsupported Jira field value mapping: {value_kind}")


def _find_issue_link_id(
    issue: Mapping[str, Any],
    operation: _ResolvedJiraRelationshipOperation,
) -> str | None:
    fields = issue.get("fields") if isinstance(issue.get("fields"), Mapping) else {}
    assert isinstance(fields, Mapping)
    for link in _mapping_list(fields.get("issuelinks")):
        raw_type = link.get("type") if isinstance(link.get("type"), Mapping) else {}
        if not isinstance(raw_type, Mapping) or raw_type.get("name") != operation.mapping.link_type:
            continue
        if link.get("id") is None:
            continue
        # Jira populates whichever of outwardIssue/inwardIssue points away from
        # the current issue, so the populated side depends on which end of the
        # link the source lives on — not on operation.mapping.direction.
        for side_field in ("outwardIssue", "inwardIssue"):
            target_issue = link.get(side_field)
            if not isinstance(target_issue, Mapping):
                continue
            try:
                key = normalize_jira_issue_key(target_issue.get("key") or "")
            except JiraProviderError:
                continue
            if key == operation.target_issue:
                return str(link["id"])
    return None


def _mapping_list(value: Any) -> list[Mapping[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, Mapping)]
