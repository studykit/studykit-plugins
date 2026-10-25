#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Actual-core stdio transport tests; native host hook delivery is tested separately."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
import select
import subprocess
import sys
import tempfile
import time
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
SERVER = PLUGIN / "mcp" / "server.py"


class StopMcpTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="guard-stop-mcp-")
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name).resolve()
        self.path = self.project / "src" / "changed.txt"
        self.path.parent.mkdir()
        self.path.write_text("before\n")
        self.buffer = b""
        self.processes = []
        self.addCleanup(self.close)

    def close(self):
        for process in self.processes:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=3)
            for stream in (process.stdin, process.stdout, process.stderr):
                if stream and not stream.closed:
                    stream.close()

    def start(self, host="claude", *, timeout=5, capability=None, protocol_version="2025-11-25", reset=True):
        folder = self.project / ("." + host)
        folder.mkdir(exist_ok=True)
        if reset:
            (folder / "guard.local.json").write_text(json.dumps({"file_review_rules": [
                {"glob": "src/**", "action": {"kind": "agent", "name": "project-reviewer"}, "on_stop": "ask"}]}))
            state = folder / "guard" / "state"
            state.mkdir(parents=True, exist_ok=True)
            (state / "session.json").write_text(json.dumps({"edited_files": [str(self.path)],
                "edited_provenance": {str(self.path): {"source": "native"}}}))
        env = {key: value for key, value in os.environ.items()
               if not key.startswith(("GUARD_", "CLAUDE_", "CODEX_", "HERDR_"))}
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        if host == "claude":
            env["CLAUDE_PROJECT_DIR"] = str(self.project)
        self.process = subprocess.Popen([sys.executable, str(SERVER), "--host", host,
            "--elicitation-timeout", str(timeout), "--data-dir", str(self.project / "plugin-data")], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, cwd=self.project, env=env)
        self.processes.append(self.process)
        self.buffer = b""
        self.host = host
        self.send({"id": 100, "method": "initialize", "params": {"protocolVersion": protocol_version,
                   "capabilities": {"elicitation": {"form": {}}} if capability is None else capability}})
        self.assertEqual(self.read()["result"]["serverInfo"]["name"], "guard-review-consent")
        self.send({"method": "notifications/initialized"})

    def send(self, value):
        self.process.stdin.write((json.dumps({"jsonrpc": "2.0", **value}) + "\n").encode())
        self.process.stdin.flush()

    def read(self, timeout=5):
        deadline = time.monotonic() + timeout
        while b"\n" not in self.buffer:
            remaining = deadline - time.monotonic()
            if remaining <= 0 or not select.select([self.process.stdout], [], [], max(remaining, 0))[0]:
                raise TimeoutError("No MCP response")
            chunk = os.read(self.process.stdout.fileno(), 65536)
            if not chunk:
                raise AssertionError("MCP server closed: " + self.process.stderr.read().decode())
            self.buffer += chunk
        line, self.buffer = self.buffer.split(b"\n", 1)
        return json.loads(line)

    def call(self, request=1, **extra):
        arguments = {"cwd": str(self.project), "session_id": "session",
                     "stop_hook_active": "false" if self.host == "claude" else False, **extra}
        self.send({"id": request, "method": "tools/call", "params": {
            "name": "confirm_file_review", "arguments": arguments}})
        return self.read()

    def output(self, message):
        return json.loads(message["result"]["content"][0]["text"])

    def state(self):
        return json.loads((self.project / ("." + self.host) / "guard" / "state" / "session.json").read_text())

    def consent(self):
        return json.loads((self.project / ("." + self.host) / "guard" / "stop-consent" / "session.json").read_text())

    def checkpoint_tool(self, name, token, **extra):
        self.send({"id": 70, "method": "tools/call", "params": {"name": name,
            "arguments": {"review_id": token, **extra}}})
        return self.read()

    def approve(self):
        form = self.call()
        self.send({"id": form["id"], "result": {"action": "accept", "content": {"review_action": "review"}}})
        continuation = self.continuation(self.output(self.read()))
        self.assertIn("review approved", continuation)
        self.assertNotIn('"cwd"', continuation)
        self.assertNotIn('"session_id"', continuation)
        self.assertNotIn('"token"', continuation)
        review_id = re.search(r'"review_id": "([A-Za-z0-9]{8})"', continuation).group(1)
        self.assertEqual(len(review_id), 8)
        return review_id

    def continuation(self, output):
        if self.host == "claude":
            self.assertNotIn("decision", output)
            self.assertEqual(output["hookSpecificOutput"]["hookEventName"], "Stop")
            return output["hookSpecificOutput"]["additionalContext"]
        self.assertEqual(output["decision"], "block")
        return output["reason"]

    def test_checkpoint_tools_round_trip_on_both_hosts(self):
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.start(host)
                self.send({"id": 80, "method": "tools/list"})
                tools = {tool["name"]: tool for tool in self.read()["result"]["tools"]}
                self.assertTrue(tools["get_review_checkpoint"]["annotations"]["readOnlyHint"])
                self.assertFalse(tools["complete_review_checkpoint"]["annotations"]["readOnlyHint"])
                self.assertEqual(tools["get_review_checkpoint"]["inputSchema"]["required"], ["review_id"])
                token = self.approve()
                result = self.output(self.checkpoint_tool("get_review_checkpoint", token))
                self.assertNotIn("token", result)
                self.assertEqual(set(result["files"]), {str(self.path)})
                self.assertEqual(result["groups"][0]["name"], "project-reviewer")
                self.assertIn("every named reviewer", result["workflow"])
                self.assertIn(str(self.path), self.state()["edited_files"])
                done = self.output(self.checkpoint_tool("complete_review_checkpoint", token))
                self.assertEqual((done["cleared"], done["remaining"]), (1, 0))
                self.assertIn("not a clean verdict", done["meaning"])
                self.assertEqual(self.output(self.checkpoint_tool("complete_review_checkpoint", token)), done)

    def test_checkpoint_tools_reject_wrong_session_missing_and_manual_tokens(self):
        self.start()
        token = self.approve()
        for name in ("get_review_checkpoint", "complete_review_checkpoint"):
            for candidate, extra in (("0" * 64, {}), ("rv_" + "a" * 32, {}), ("rv_" + "a" * 12, {}),
                                     (token, {"session_id": "other"}),
                                     (token, {"paths": [str(self.path)]}), ([], {})):
                result = self.checkpoint_tool(name, candidate, **extra)
                self.assertTrue(result["result"]["isError"])
                self.assertIn(str(self.path), self.state()["edited_files"])
        state = self.state()
        del state["file_checkpoints"][next(iter(state["file_checkpoints"]))]["approved_stop"]
        (self.project / ".claude/guard/state/session.json").write_text(json.dumps(state))
        for name in ("get_review_checkpoint", "complete_review_checkpoint"):
            self.assertTrue(self.checkpoint_tool(name, token)["result"]["isError"])
        self.assertIn(str(self.path), self.state()["edited_files"])

    def test_checkpoint_tools_preserve_changed_revisions_and_reviewers(self):
        for host, change in (("claude", "file"), ("codex", "reviewer")):
            with self.subTest(host=host, change=change):
                self.start(host)
                token = self.approve()
                if host == "codex":
                    other = self.project / "other-project"
                    other.mkdir()
                    for name in ("get_review_checkpoint", "complete_review_checkpoint"):
                        self.assertTrue(self.checkpoint_tool(name, token, cwd=str(other))["result"]["isError"])
                if change == "file":
                    self.path.write_text("changed during review\n")
                else:
                    config = self.project / ".codex/guard.local.json"
                    config.write_text(config.read_text().replace("project-reviewer", "other-reviewer"))
                result = self.checkpoint_tool("get_review_checkpoint", token)
                self.assertTrue(result["result"]["isError"])
                self.assertIn("fresh consent", self.output(result)["detail"])
                done = self.output(self.checkpoint_tool("complete_review_checkpoint", token))
                self.assertEqual((done["cleared"], done["remaining"]), (0, 1))

    def test_restart_and_retry_preserve_later_edits_and_original_receipt(self):
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.start(host)
                review_id = self.approve()
                self.process.terminate()
                self.process.wait(timeout=3)
                self.start(host, reset=False)
                self.assertEqual(self.output(self.checkpoint_tool("get_review_checkpoint", review_id))["status"], "approved")
                receipt = self.output(self.checkpoint_tool("complete_review_checkpoint", review_id))
                self.path.write_text("later edits " + host)
                state = self.state()
                state["edited_files"] = [str(self.path)]
                (self.project / ("." + host) / "guard/state/session.json").write_text(json.dumps(state))
                self.process.terminate()
                self.process.wait(timeout=3)
                self.start(host, reset=False)
                for name in ("get_review_checkpoint", "complete_review_checkpoint"):
                    self.assertEqual(self.output(self.checkpoint_tool(name, review_id)), receipt)
                    self.assertIn(str(self.path), self.state()["edited_files"])

    def test_distinct_approvals_and_host_binding(self):
        self.start("claude")
        first = self.approve()
        self.path.write_text("second revision")
        second = self.approve()
        self.assertNotEqual(first, second)
        self.assertTrue(self.checkpoint_tool("get_review_checkpoint", first)["result"]["isError"])
        self.assertEqual(self.output(self.checkpoint_tool("get_review_checkpoint", second))["review_id"], second)
        self.start("codex")
        for name in ("get_review_checkpoint", "complete_review_checkpoint"):
            self.assertTrue(self.checkpoint_tool(name, second)["result"]["isError"])
        self.assertIn(str(self.path), self.state()["edited_files"])

    def test_identical_content_in_two_sessions_has_distinct_ids_and_scopes(self):
        self.start()
        first = self.approve()
        state_dir = self.project / ".claude/guard/state"
        (state_dir / "other.json").write_text(json.dumps({"edited_files": [str(self.path)],
            "edited_provenance": {str(self.path): {"source": "native"}}}))
        form = self.call(session_id="other")
        self.send({"id": form["id"], "result": {"action": "accept", "content": {"review_action": "review"}}})
        reason = self.continuation(self.output(self.read()))
        second = re.search(r'"review_id": "([A-Za-z0-9]{8})"', reason).group(1)
        self.assertNotEqual(first, second)
        self.assertEqual(self.output(self.checkpoint_tool("complete_review_checkpoint", second))["cleared"], 1)
        self.assertIn(str(self.path), self.state()["edited_files"])
        self.assertFalse(json.loads((state_dir / "other.json").read_text())["edited_files"])
        self.assertEqual(self.output(self.checkpoint_tool("get_review_checkpoint", first))["review_id"], first)

    def test_completion_write_failure_cannot_claim_success(self):
        self.start()
        review_id = self.approve()
        script = """
import json, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from guard_core import cmd_checkpoint, stop_review
cmd_checkpoint._write_state = lambda *args: None
try:
    stop_review.review_checkpoint(Path(sys.argv[2]), 'claude', sys.argv[3], complete=True)
except ValueError as error:
    print(str(error))
else:
    raise AssertionError('Failed persistence was reported as success')
"""
        result = subprocess.run([sys.executable, "-c", script, str(PLUGIN / "scripts"),
            str(self.project / "plugin-data"), review_id], capture_output=True, text=True,
            env={**os.environ, "GUARD_HOST": "claude"})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("could not be persisted", result.stdout)
        self.assertIn(str(self.path), self.state()["edited_files"])
        self.assertNotIn(review_id, self.state().get("file_review_receipts", {}))
        self.assertEqual(self.output(self.checkpoint_tool("complete_review_checkpoint", review_id))["cleared"], 1)

    def test_form_requires_an_explicit_review_choice(self):
        for content in ({}, {"review_action": "later"}, {"review_action": True}, {"run_review": True}):
            self.start()
            form = self.call()
            field = form["params"]["requestedSchema"]["properties"]["review_action"]
            self.assertNotIn("default", field)
            self.send({"id": form["id"], "result": {"action": "accept", "content": content}})
            self.assertNotIn("decision", self.output(self.read()))
            self.assertFalse(self.state().get("file_checkpoints"))
            self.path.write_text(self.path.read_text() + "new revision\n")

    def test_expired_confirmation_reports_timeout_not_changed_files(self):
        self.start()
        form = self.call()
        consent = self.consent()
        consent["pending"]["created_at"] -= 301
        (self.project / ".claude/guard/stop-consent/session.json").write_text(json.dumps(consent))
        self.send({"id": form["id"], "result": {"action": "accept", "content": {"review_action": "review"}}})
        message = self.output(self.read())["systemMessage"]
        self.assertIn("expired", message)
        self.assertNotIn("rules changed", message)
        self.assertFalse(self.state().get("file_checkpoints"))

    def test_accept_on_both_hosts_uses_frozen_checkpoint_without_clearing_queue(self):
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.start(host)
                form = self.call()
                self.assertEqual(form["method"], "elicitation/create")
                self.assertIn("src/changed.txt", form["params"]["message"])
                self.assertIn("project-reviewer", form["params"]["message"])
                self.send({"id": form["id"], "result": {"action": "accept", "content": {"review_action": "review"}}})
                result = self.read()
                self.assertEqual(result["id"], 1)
                self.assertIn("get_review_checkpoint", self.continuation(self.output(result)))
                state = self.state()
                self.assertIn(str(self.path), state["edited_files"], "consent is not review completion")
                checkpoints = list(state["file_checkpoints"].values())
                self.assertEqual(checkpoints[0]["groups"][0]["name"], "project-reviewer")
                self.assertEqual(self.output(self.call(2)), {}, "same approved revision must not prompt again")
                self.path.write_text("new revision " + host + "\n")
                self.assertEqual(self.call(3)["method"], "elicitation/create")
                self.process.stdin.close()
                self.process.wait(timeout=5)

    def test_decline_and_cancel_keep_queue_and_suppress_same_revision(self):
        for host, action in (("claude", "decline"), ("codex", "cancel")):
            with self.subTest(host=host, action=action):
                self.start(host)
                form = self.call()
                self.send({"id": form["id"], "result": {"action": action}})
                self.assertIn("no review started", self.output(self.read())["systemMessage"])
                self.assertIn(str(self.path), self.state()["edited_files"])
                self.assertEqual(self.output(self.call(2)), {})
                self.process.stdin.close()
                self.process.wait(timeout=5)

    def test_false_or_string_true_is_not_user_approval(self):
        self.start()
        form = self.call()
        self.send({"id": form["id"], "result": {"action": "accept", "content": {"run_review": "true"}}})
        self.assertIn("no review started", self.output(self.read())["systemMessage"])
        self.assertEqual(self.consent()["last_answer"]["outcome"], "declined")

    def test_unavailable_form_capability_does_not_prepare_or_claim_review(self):
        self.start(capability={"elicitation": {"url": {}}})
        self.assertIn("does not support", self.output(self.call())["systemMessage"])
        self.assertEqual(self.output(self.call(2)), {})
        self.assertFalse((self.project / ".claude/guard/stop-consent/session.json").exists())
        self.assertIn(str(self.path), self.state()["edited_files"])

    def test_invalid_arguments_cannot_supply_user_approval(self):
        self.start()
        for arguments in ({"approved": True}, {"session_id": "../outside"},
                          {"stop_hook_active": "${stop_hook_active}"}):
            result = self.call(**arguments)
            self.assertTrue(result["result"]["isError"])
        self.assertFalse((self.project / ".claude/guard/stop-consent/session.json").exists())

    def test_response_ids_are_typed_and_concurrent_calls_do_not_duplicate_forms(self):
        self.start()
        form = self.call(1)
        # JSON-RPC string '1' and number 1 are different calls, even when one is pending.
        self.assertEqual(self.output(self.call("1")), {})
        self.send({"id": 1, "result": {"action": "accept", "content": {"review_action": "review"}}})
        with self.assertRaises(TimeoutError):
            self.read(.05)
        self.send({"id": form["id"], "result": {"action": "cancel"}})
        self.assertEqual(self.read()["id"], 1)

    def test_malformed_elicitation_response_is_error_and_never_approval(self):
        self.start()
        form = self.call()
        self.send({"id": form["id"], "result": {"action": "approve", "content": {"review_action": "review"}}})
        self.assertTrue(self.read()["result"]["isError"])
        self.assertEqual(self.consent()["last_answer"]["outcome"], "failed")
        self.assertIn(str(self.path), self.state()["edited_files"])

    def test_timeout_cancellation_and_eof_release_pending_request(self):
        for index, ending in enumerate(("timeout", "cancel", "eof")):
            with self.subTest(ending=ending):
                host = "codex" if index == 1 else "claude"
                # Each case gets a fresh revision to avoid the prior failed-offer stamp.
                self.path.write_text(ending + "\n")
                self.start(host, timeout=.1)
                self.call()
                if ending == "cancel":
                    self.send({"method": "notifications/cancelled", "params": {"requestId": 1}})
                elif ending == "eof":
                    self.process.stdin.close()
                    self.process.wait(timeout=5)
                if ending != "eof":
                    response = self.read()
                    self.assertTrue(response["result"]["isError"])
                    if ending == "timeout":
                        self.assertIn("timed out", self.output(response)["systemMessage"])
                self.assertEqual(self.consent()["last_answer"]["outcome"], "failed")
                self.assertNotIn("pending", self.consent())
                self.assertIn(str(self.path), self.state()["edited_files"])
                if ending != "eof":
                    self.process.stdin.close()
                    self.process.wait(timeout=5)

    def test_protocol_parsing_is_bounded_and_does_not_crash_on_invalid_version(self):
        self.start(protocol_version=[])
        self.process.stdin.write(b"not-json\n")
        self.process.stdin.flush()
        self.assertEqual(self.read()["error"]["code"], -32700)
        self.send({"id": 9, "method": "ping"})
        self.assertEqual(self.read(), {"jsonrpc": "2.0", "id": 9, "result": {}})
        self.process.stdin.write(b"x" * (1024 * 1024 + 1))
        self.process.stdin.flush()
        self.assertEqual(self.read()["error"]["code"], -32600)
        self.process.wait(timeout=5)

    def test_codex_compatibility_config_launches_without_argument_interpolation(self):
        # Codex's compatibility loader resolves cwd under the plugin but passes args as-is.
        config = json.loads((PLUGIN / "mcp.codex.json").read_text())["mcpServers"]["review"]
        cwd = PLUGIN / config.get("cwd", ".")
        self.process = subprocess.Popen([config["command"], *config.get("args", [])],
            cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        self.processes.append(self.process)
        self.send({"id": 1, "method": "initialize", "params": {
            "protocolVersion": "2025-11-25", "capabilities": {}}})
        self.assertEqual(self.read()["result"]["serverInfo"]["name"], "guard-review-consent")


if __name__ == "__main__":
    unittest.main()
