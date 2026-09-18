#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Turn-review CLI and hook contract regressions, not live host integration tests."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PLUGIN = Path(__file__).resolve().parents[1]
SCRIPT = PLUGIN / "skills/audit-turn/scripts/review.py"
HOOK = PLUGIN / "hooks/scripts/hook_codex.py"
CLI = PLUGIN / "scripts/guard_hook.py"


class TurnReviewTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="guard-turn-review-")
        self.addCleanup(temporary.cleanup)
        self.project = Path(temporary.name).resolve()
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith(("GUARD_", "CLAUDE_", "CODEX_", "HERDR_"))}
        self.env["PYTHONDONTWRITEBYTECODE"] = "1"

    def config(self, host, action, **extra):
        path = self.project / f".{host}/guard.local.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({"turn_review": action, **extra}))

    def state_path(self, host, session="parent-session"):
        return self.project / f".{host}/guard/state/{session}.json"

    def state(self, host, session="parent-session", **values):
        path = self.state_path(host, session)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(values))

    def run_script(self, path, args=(), payload=None, env=None, error=False):
        result = subprocess.run(
            [sys.executable, str(path), *args], cwd=self.project,
            env=env or self.env, input=json.dumps(payload) if payload else "",
            text=True, capture_output=True, timeout=15,
        )
        self.assertEqual(result.returncode, 1 if error else 0, result.stdout + result.stderr)
        return result

    def prepare(self, host, turn=None, session="parent-session", error=False):
        args = ["--host", host, "--project", str(self.project)]
        if session is not None:
            args += ["--session", session]
        if turn is not None:
            args += ["--turn", turn]
        result = self.run_script(SCRIPT, args, error=error)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout)

    def claude_turn(self):
        transcript = self.project / "transcript.jsonl"
        records = [
            {"type": "user", "promptId": "target-1", "message": {"content": "Original request"}},
            {"type": "assistant", "message": {"content": [
                {"type": "tool_use", "name": "Bash", "input": {"command": "check"}},
                {"type": "text", "text": "Original response — 검토"},
            ]}},
            {"type": "user", "message": {"content": [
                {"type": "tool_result", "content": "Evidence"},
            ]}},
            {"type": "user", "promptId": "audit-1", "message": {"content": "/guard:audit-turn"}},
        ]
        transcript.write_text("\n".join(json.dumps(r) for r in records))
        self.state("claude", transcript_path=str(transcript))
        return transcript

    def hook(self, event, turn="target-1", **values):
        payload = {"hook_event_name": event, "cwd": str(self.project),
                   "session_id": "parent-session", "turn_id": turn, **values}
        result = self.run_script(HOOK, payload=payload)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, "", "Turn lifecycle hooks must not dispatch a review")

    def codex_turn(self):
        self.hook("UserPromptSubmit", prompt="Original request")
        self.hook("PostToolUse", tool_name="Read", tool_input={"path": "source.py"},
                  tool_response="Evidence")
        self.hook("Stop", last_assistant_message="Original response — 검토")

    def snapshots(self, host):
        return list((self.project / f".{host}/guard/turns").glob("*/review-*.json"))

    def test_unset_skips_without_evidence_or_writes(self):
        for host in ("claude", "codex"):
            self.assertEqual(self.prepare(host), {"status": "no_reviewer"})
            self.config(host, {})
            self.assertEqual(self.prepare(host), {"status": "no_reviewer"})
            self.assertFalse((self.project / f".{host}/guard").exists())

    def test_exact_reviewer_and_common_evidence_contract_on_both_hosts(self):
        for host in ("claude", "codex"):
            getattr(self, f"{host}_turn")()
            for kind in ("agent", "skill"):
                reviewer = {"kind": kind, "name": f"my-{host}-reviewer"}
                self.config(host, reviewer, **{"claims-auditor": "off", "audit-plan": "off"})
                result = self.prepare(host)
                self.assertEqual(result["reviewer"], reviewer)
                self.assertEqual(result["turn_id"], "target-1")
                evidence = json.loads(Path(result["input_path"]).read_text())
                self.assertEqual(evidence["user"], "Original request")
                self.assertEqual(evidence["assistant"], "Original response — 검토")
                self.assertIn("Evidence", json.dumps(evidence["tools"]))
                self.assertTrue(Path(evidence["source_path"]).is_file())
                self.assertIn(f".{host}/guard", result["input_path"])

    def test_invalid_and_recursive_settings_never_fall_back(self):
        for host in ("claude", "codex"):
            for action in ({"kind": "unknown", "name": "a"}, {"kind": "agent"},
                           {"kind": "skill", "name": "guard:audit-turn"},
                           {"kind": "skill", "name": "audit-turn"}):
                self.config(host, action)
                self.assertEqual(self.prepare(host, error=True)["status"], "error")
                self.assertFalse(self.snapshots(host))

    def test_no_evidence_is_an_error_not_a_clean_verdict(self):
        for host in ("claude", "codex"):
            self.config(host, {"kind": "agent", "name": "reviewer"})
            self.assertEqual(self.prepare(host, error=True)["status"], "error")
            getattr(self, f"{host}_turn")()
            self.assertEqual(self.prepare(host, turn="missing", error=True)["status"], "error")
            self.assertFalse(self.snapshots(host))

    def test_explicit_turn_and_repeat_reviews_preserve_original_evidence(self):
        self.config("codex", {"kind": "agent", "name": "reviewer"})
        self.codex_turn()
        first = self.prepare("codex")
        first_bytes = Path(first["input_path"]).read_bytes()
        state_before = self.state_path("codex").read_bytes()
        second = self.prepare("codex", turn="target-1")
        self.assertNotEqual(first["input_path"], second["input_path"])
        self.assertEqual(Path(second["input_path"]).read_bytes(), first_bytes)
        self.assertEqual(self.state_path("codex").read_bytes(), state_before)

    def test_codex_audit_and_control_replies_do_not_become_the_next_target(self):
        self.config("codex", {"kind": "skill", "name": "user-review"})
        self.codex_turn()
        for number, prompt in enumerate(("$guard:audit-turn", "/guard:audit-turn target-1",
                                         "$guard:audit-plan plan.md", "$guard:audit-files")):
            turn = f"control-{number}"
            self.hook("UserPromptSubmit", turn, prompt=prompt)
            self.hook("Stop", turn, last_assistant_message="Audit report")
            self.assertEqual(self.prepare("codex")["turn_id"], "target-1")
        self.hook("UserPromptSubmit", "later-1", prompt="A new question")
        self.hook("Stop", "later-1", last_assistant_message="A new answer")
        self.assertEqual(self.prepare("codex")["turn_id"], "later-1")

    def test_host_and_session_are_not_taken_from_the_other_host(self):
        self.env.update(GUARD_HOST="claude", GUARD_PROJECT_DIR="/wrong-project",
                        CLAUDE_CODE_SESSION_ID="unrelated", CODEX_THREAD_ID="parent-session")
        self.config("codex", {"kind": "agent", "name": "codex-reviewer"})
        self.config("claude", {"kind": "agent", "name": "wrong-reviewer"})
        self.codex_turn()
        result = self.prepare("codex", session=None)
        self.assertEqual(result["reviewer"]["name"], "codex-reviewer")
        self.assertFalse(self.state_path("claude").exists())
        self.assertEqual(self.prepare("codex", session="other-session", error=True)["status"], "error")

    def test_unsafe_ids_and_empty_responses_are_rejected(self):
        self.config("codex", {"kind": "agent", "name": "reviewer"})
        for sid in (None, "", "../../elsewhere"):
            self.assertEqual(self.prepare("codex", session=sid, error=True)["status"], "error")
        self.hook("UserPromptSubmit", prompt="Original request")
        self.assertEqual(self.prepare("codex", turn="target-1", error=True)["status"], "error")
        self.assertEqual(self.prepare("codex", turn="../elsewhere", error=True)["status"], "error")
        self.assertFalse(self.snapshots("codex"))

    def test_settings_register_clear_and_reject_self_reference(self):
        for host in ("claude", "codex"):
            env = dict(self.env, GUARD_HOST=host, GUARD_PROJECT_DIR=str(self.project),
                       GUARD_SETTINGS_SKILL="1")
            action = {"kind": "skill", "name": "user:review"}
            self.run_script(CLI, ["settings", "set", "turn_review", json.dumps(action)], env=env)
            shown = self.run_script(CLI, ["settings", "show"], env=env).stdout
            self.assertIn("turn_review: skill:user:review", shown)
            bad = {"kind": "skill", "name": "guard:audit-turn"}
            result = self.run_script(CLI, ["settings", "set", "turn_review", json.dumps(bad)], env=env)
            self.assertIn("cannot review itself", result.stderr)
            shown = self.run_script(CLI, ["settings", "show"], env=env).stdout
            self.assertIn("turn_review: skill:user:review", shown)
            self.run_script(CLI, ["settings", "unset", "turn_review"], env=env)
            shown = self.run_script(CLI, ["settings", "show"], env=env).stdout
            self.assertIn("turn_review: (unset)", shown)


if __name__ == "__main__":
    unittest.main()
