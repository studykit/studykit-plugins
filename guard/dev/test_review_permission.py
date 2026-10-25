#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Consent-bound Claude permission adapter; native delivery is checked in Herdr."""

import json
import unittest

import test_stop_review as fixtures


class ReviewPermissionTests(unittest.TestCase):
    setUp = fixtures.StopReviewTests.setUp
    configure = fixtures.StopReviewTests.configure
    write = fixtures.StopReviewTests.write
    run_script = fixtures.StopReviewTests.run_script
    record = fixtures.StopReviewTests.record
    event = fixtures.StopReviewTests.event
    invoke = fixtures.StopReviewTests.invoke
    approve = fixtures.StopReviewTests.approve
    token = fixtures.StopReviewTests.token
    checkpoint = fixtures.StopReviewTests.checkpoint
    cli = fixtures.StopReviewTests.cli

    def fixture(self):
        self.configure("claude", [fixtures.ask_rule("main.py", "reviewer")])
        self.record("claude", self.write("main.py"))
        question = self.invoke("claude", "prepare")
        self.token(self.approve("claude", question["request_id"]))
        review_id = next((self.project / "plugin-data/reviews").glob("*.json")).stem
        self.env["CLAUDE_PLUGIN_DATA"] = str(self.project / "plugin-data")
        return {"hook_event_name": "PermissionRequest", "session_id": "session",
            "tool_name": "mcp__plugin_guard_review__get_review_checkpoint",
            "mcp_server": {"name": "plugin:guard:review", "source": "plugin"},
            "tool_input": {"review_id": review_id}}

    def internal_token(self, payload):
        return json.loads((self.project / "plugin-data/reviews" / (payload["tool_input"]["review_id"] + ".json")).read_text())["token"]

    def permission(self, payload):
        return self.run_script("claude", fixtures.PLUGIN / "hooks/scripts/review_permission_claude.py",
                               payload=payload).stdout

    def test_approved_lookup_and_completion_only(self):
        payload = self.fixture()
        for verb in ("get", "complete"):
            payload["tool_name"] = f"mcp__plugin_guard_review__{verb}_review_checkpoint"
            result = json.loads(self.permission(payload))
            self.assertEqual(result, {"hookSpecificOutput": {"hookEventName": "PermissionRequest",
                                    "decision": {"behavior": "allow"}}})
        self.assertIn(self.internal_token(payload),
                      json.loads((self.project / ".claude/guard/state/session.json").read_text())["file_checkpoints"])

    def test_wrong_origin_session_scope_tool_and_extra_arguments_defer_to_host(self):
        payload = self.fixture()
        variants = []
        for key, value in (("hook_event_name", "PreToolUse"), ("tool_name", "Bash"),
                           ("tool_name", []), ("session_id", "other"), ("mcp_server", None),
                           ("mcp_server", {"name": "plugin:guard:review", "source": "user"}),
                           ("mcp_server", {"name": "other", "source": "plugin"})):
            variants.append({**payload, key: value})
        for patch in ({"session_id": "other"}, {"session_id": "../session"}, {"cwd": "/tmp"},
                      {"cwd": "."}, {"review_id": "rv_" + "0" * 32}, {"review_id": []}, {"command": "anything"}):
            variants.append({**payload, "tool_input": {**payload["tool_input"], **patch}})
        for variant in variants:
            with self.subTest(variant=variant):
                self.assertEqual(self.permission(variant), "")

    def test_receipt_retries_keep_permission_scoped_and_reject_corruption(self):
        payload = self.fixture()
        review_id = payload["tool_input"]["review_id"]
        self.invoke("claude", "review_checkpoint", review_id=review_id, complete=True)
        for verb in ("get", "complete"):
            payload["tool_name"] = f"mcp__plugin_guard_review__{verb}_review_checkpoint"
            self.assertEqual(json.loads(self.permission(payload))["hookSpecificOutput"]["decision"]["behavior"], "allow")
        self.assertEqual(self.permission({**payload, "session_id": "other"}), "")
        path = self.project / ".claude/guard/state/session.json"
        original = json.loads(path.read_text())
        for corrupted in ([], {review_id: {}}, {review_id: {"review_id": review_id, "status": "completed", "cleared": True, "remaining": 0}}):
            path.write_text(json.dumps({**original, "file_review_receipts": corrupted}))
            self.assertEqual(self.permission(payload), "")

    def test_manual_corrupt_and_completed_checkpoints_do_not_grant_permission(self):
        payload = self.fixture()
        path = self.project / ".claude/guard/state/session.json"
        original = path.read_text()
        state = json.loads(original)
        del state["file_checkpoints"][self.internal_token(payload)]["approved_stop"]
        path.write_text(json.dumps(state))
        self.assertEqual(self.permission(payload), "")
        path.write_text("{broken")
        self.assertEqual(self.permission(payload), "")
        path.write_text(original)
        self.checkpoint("claude", "complete", self.internal_token(payload))
        self.assertEqual(self.permission(payload), "")


if __name__ == "__main__":
    unittest.main()
