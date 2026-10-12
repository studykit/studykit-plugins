"""Shared Jira Cloud test data: the site and a stand-in Markdown<->ADF codec."""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

SITE = "https://example.atlassian.net"
EMAIL = "user@example.test"
API_TOKEN = "test-token"


def adf_doc(text: str) -> dict[str, Any]:
    """Wrap ``text`` in a one-paragraph ADF document (empty text, no content)."""

    content = [{"type": "paragraph", "content": [{"type": "text", "text": text}]}] if text else []
    return {"type": "doc", "version": 1, "content": content}


def adf_text(document: Mapping[str, Any]) -> str:
    """Invert :func:`adf_doc`, standing in for the site's ADF-to-Markdown converter."""

    return "".join(
        str(node.get("text", ""))
        for paragraph in document.get("content") or []
        for node in paragraph.get("content") or []
    )


def markdown_bodies(issue: Mapping[str, Any]) -> dict[str, Any]:
    """Return ``issue`` as the provider caches it: ADF bodies rendered to text.

    A test that seeds the cache directly must hand it this shape, since the
    provider converts bodies before anything is written.
    """

    fields = dict(issue.get("fields") or {})
    if isinstance(fields.get("description"), Mapping):
        fields["description"] = adf_text(fields["description"])
    comment_block = fields.get("comment")
    if isinstance(comment_block, Mapping):
        comments = [
            {**comment, "body": adf_text(comment["body"])} if isinstance(comment.get("body"), Mapping) else comment
            for comment in comment_block.get("comments") or []
        ]
        fields["comment"] = {**comment_block, "comments": comments}
    return {**issue, "fields": fields}


def sent_json(curl_config: str) -> Any:
    """Decode the JSON body a curl ``--config`` text sends as ``data-binary``."""

    for line in curl_config.splitlines():
        if line.startswith("data-binary = "):
            return json.loads(json.loads(line[len("data-binary = ") :]))
    raise AssertionError("no data-binary line in curl config")
