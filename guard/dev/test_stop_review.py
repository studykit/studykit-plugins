#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Stop consent/checkpoint regressions; no live model or host elicitation calls."""

import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

import test_file_reviews as fixtures


PLUGIN = fixtures.PLUGIN
rule = fixtures.rule


BRIDGE = """
import json, sys
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from guard_core import stop_review
from guard_core.paths import _state_root
data = json.load(sys.stdin)
project = Path(data['project'])
session = data.get('session', 'session')
host = data['host']
try:
    op = data['operation']
    if op == 'prepare':
        result = stop_review.prepare(project, session, host,
            stop_hook_active=data.get('stop_hook_active', False))
    elif op == 'answer':
        if 'id_candidates' in data:
            characters = iter(''.join(data['id_candidates']))
            stop_review.secrets.choice = lambda _: next(characters)
        result = stop_review.answer(project, session, host, data['request_id'],
            data['action'], data.get('content'), data_dir=project / 'plugin-data')
    elif op == 'review_checkpoint':
        result = stop_review.review_checkpoint(project / 'plugin-data', host, data['review_id'],
            complete=data.get('complete', False))
    elif op == 'failure':
        result = stop_review.failure(project, session, data['request_id'])
    elif op == 'consent_path':
        result = str(_state_root(project) / 'stop-consent' / (session + '.json'))
    print(json.dumps({'result': result}))
except Exception as error:
    print(json.dumps({'error': type(error).__name__, 'message': str(error)}))
"""


def ask_rule(pattern, name, kind="agent"):
    return dict(rule(pattern, name, kind), on_stop="ask")


class StopReviewTests(unittest.TestCase):
    # Reuse the native edit/queue fixture without inheriting its test cases.
    setUp = fixtures.FileReviewTests.setUp
    configure = fixtures.FileReviewTests.configure
    write = fixtures.FileReviewTests.write
    run_script = fixtures.FileReviewTests.run_script
    cli = fixtures.FileReviewTests.cli
    event = fixtures.FileReviewTests.event
    record = fixtures.FileReviewTests.record
    checkpoint = fixtures.FileReviewTests.checkpoint

    def invoke(self, host, operation, *, error=None, **arguments):
        result = subprocess.run(
            [sys.executable, "-c", BRIDGE, str(PLUGIN / "scripts")],
            cwd=self.project, env=dict(self.env, GUARD_HOST=host),
            input=json.dumps(dict(arguments, project=str(self.project),
                                  host=host, operation=operation)),
            capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        if error:
            self.assertEqual(payload.get("error"), error, payload)
            return payload
        self.assertNotIn("error", payload, payload)
        return payload["result"]

    def pending(self, host):
        return set(self.checkpoint(host, "show")["files"])

    def approve(self, host, request_id, **extra):
        return self.invoke(host, "answer", request_id=request_id,
                           action="accept", content={"review_action": "review"}, **extra)

    def token(self, response):
        self.assertEqual(response.get("decision"), "block", response)
        match = re.search(r'"review_id": "([A-Za-z0-9]{8})"', response["reason"])
        self.assertIsNotNone(match, response)
        return json.loads((self.project / "plugin-data/reviews" / (match.group(1) + ".json")).read_text())["token"]

    def test_short_id_collision_retries_without_overwriting_existing_approval(self):
        self.configure("claude", [ask_rule("main.py", "reviewer")])
        path = self.write("main.py")
        self.record("claude", path)
        question = self.invoke("claude", "prepare")
        first = self.approve("claude", question["request_id"])
        first_id = re.search(r'"review_id": "([A-Za-z0-9]{8})"', first["reason"]).group(1)
        record_path = self.project / "plugin-data/reviews" / (first_id + ".json")
        original = record_path.read_text()
        self.write("main.py", "next revision")
        question = self.invoke("claude", "prepare")
        second = self.approve("claude", question["request_id"], id_candidates=[first_id, "Z9y8X7w6"])
        self.assertIn('"review_id": "Z9y8X7w6"', second["reason"])
        self.assertEqual(record_path.read_text(), original)
        self.assertTrue((record_path.parent / "Z9y8X7w6.json").is_file())

    def test_default_manual_unmatched_and_excluded_do_not_ask(self):
        for host in ("claude", "codex"):
            with self.subTest(host=host):
                self.configure(host, [rule("default.py", "default-review"),
                                      dict(rule("manual.py", "manual-review"), on_stop="manual"),
                                      ask_rule("excluded.py", "excluded-review")],
                               files_exclude=["excluded.py"])
                for name in ("default.py", "manual.py", "excluded.py", "unmatched.py"):
                    self.record(host, self.write(name))
                self.assertEqual(self.invoke(host, "prepare"), {"status": "empty"})
                self.assertEqual(self.pending(host),
                                 {str(self.project / n) for n in ("default.py", "manual.py")})

    def test_specificity_selects_the_winning_rules_stop_policy(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("**/*.py", "broad-review"),
                                  rule("src/manual.py", "manual-review"),
                                  ask_rule("src/special.py", "exact-review")])
            for name in ("src/manual.py", "src/special.py", "other.py"):
                self.record(host, self.write(name))
            question = self.invoke(host, "prepare")
            self.assertEqual(question["status"], "ask")
            approved = self.checkpoint(host, "show", "--token",
                                       self.token(self.approve(host, question["request_id"])))
            self.assertEqual({g["name"] for g in approved["groups"]},
                             {"broad-review", "exact-review"})
            self.assertNotIn(str(self.project / "src/manual.py"), approved["files"])

    def test_accept_freezes_only_ask_subset_until_checkpoint_completion(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("one.py", "team:Exact-Reviewer"),
                                  ask_rule("two.json", "project-structure", "skill"),
                                  rule("manual.md", "project-docs")])
            names = ("one.py", "two.json", "manual.md")
            for name in names:
                self.record(host, self.write(name))
            question = self.invoke(host, "prepare")
            late = self.write("late.py")
            # An unmatched later edit cannot enlarge the approved checkpoint.
            self.record(host, late)
            token = self.token(self.approve(host, question["request_id"]))
            approved = self.checkpoint(host, "show", "--token", token)
            self.assertEqual(set(approved["files"]),
                             {str(self.project / n) for n in ("one.py", "two.json")})
            self.assertEqual({(g["kind"], g["name"]) for g in approved["groups"]},
                             {("agent", "team:Exact-Reviewer"), ("skill", "project-structure")})
            self.assertEqual(len(self.pending(host)), 3)
            self.assertEqual(self.invoke(host, "prepare"), {"status": "unchanged"})
            completed = self.checkpoint(host, "complete", token)
            self.assertEqual(completed, {"cleared": 2, "remaining": 1})
            self.assertEqual(self.pending(host), {str(self.project / "manual.md")})

    def test_decline_cancel_and_later_keep_queue_and_suppress_revision(self):
        for host in ("claude", "codex"):
            for index, (action, content) in enumerate(
                    (("decline", None), ("cancel", None), ("accept", {"review_action": "later"}))):
                with self.subTest(host=host, action=action):
                    self.configure(host, [ask_rule("**/*.py", "project-review")])
                    self.record(host, self.write("main.py", f"revision {index}\n"))
                    question = self.invoke(host, "prepare")
                    response = self.invoke(host, "answer", request_id=question["request_id"],
                                           action=action, content=content)
                    self.assertIn("no review started", response["systemMessage"])
                    self.assertIn(str(self.project / "main.py"), self.pending(host))
                    self.assertEqual(self.invoke(host, "prepare"), {"status": "unchanged"})

    def test_new_path_offers_only_the_previously_unoffered_revision(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("**/*.py", "project-review")])
            first = self.write("first.py")
            self.record(host, first)
            question = self.invoke(host, "prepare")
            self.invoke(host, "answer", request_id=question["request_id"], action="decline")
            second = self.write("second.py")
            self.record(host, second, turn="turn-2")
            question = self.invoke(host, "prepare")
            self.assertIn("second.py", question["message"])
            self.assertNotIn("first.py", question["message"])
            token = self.token(self.approve(host, question["request_id"]))
            self.assertEqual(set(self.checkpoint(host, "show", "--token", token)["files"]),
                             {str(second)})
            self.assertEqual(self.pending(host), {str(first), str(second)})

    def test_content_and_reviewer_changes_reoffer(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "first-review")])
            path = self.write("main.py", "before\n")
            self.record(host, path)
            first = self.invoke(host, "prepare")
            self.invoke(host, "answer", request_id=first["request_id"], action="decline")
            path.write_text("after\n")
            second = self.invoke(host, "prepare")
            self.assertEqual(second["status"], "ask")
            self.invoke(host, "answer", request_id=second["request_id"], action="decline")
            self.configure(host, [ask_rule("main.py", "second-review", "skill")])
            third = self.invoke(host, "prepare")
            self.assertEqual(third["status"], "ask")
            self.assertIn("skill:second-review", third["message"])
            self.assertEqual(len({first["request_id"], second["request_id"], third["request_id"]}), 3)

    def test_new_eligible_path_during_question_is_not_included_in_approval(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("**/*.py", "project-review")])
            first = self.write("first.py")
            self.record(host, first)
            question = self.invoke(host, "prepare")
            second = self.write("second.py")
            self.record(host, second, turn="turn-2")
            token = self.token(self.approve(host, question["request_id"]))
            self.assertEqual(set(self.checkpoint(host, "show", "--token", token)["files"]),
                             {str(first)})
            self.assertEqual(self.pending(host), {str(first), str(second)})
            offered = self.invoke(host, "prepare")
            self.assertEqual(offered["status"], "ask")
            self.assertIn("second.py", offered["message"])
            self.assertNotIn("first.py", offered["message"])

    def test_changes_while_form_is_open_reject_stale_approval(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "project-review")])
            path = self.write("main.py")
            self.record(host, path)
            question = self.invoke(host, "prepare")
            path.write_text("changed while waiting\n")
            response = self.approve(host, question["request_id"])
            self.assertNotIn("decision", response)
            self.assertIn("remain pending", response["systemMessage"])
            self.assertEqual(self.pending(host), {str(path)})
            self.assertEqual(self.invoke(host, "prepare")["status"], "ask")

    def test_reviewer_change_while_form_is_open_requires_new_consent(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "old-review")])
            path = self.write("main.py")
            self.record(host, path)
            question = self.invoke(host, "prepare")
            self.configure(host, [ask_rule("main.py", "new-review", "skill")])
            response = self.approve(host, question["request_id"])
            self.assertNotIn("decision", response)
            self.assertIn("No review was started", response["systemMessage"])
            self.assertEqual(self.pending(host), {str(path)})
            replacement = self.invoke(host, "prepare")
            self.assertEqual(replacement["status"], "ask")
            self.assertIn("skill:new-review", replacement["message"])

    def test_duplicate_prepare_continuation_and_wrong_id_do_not_dispatch(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "project-review")])
            self.record(host, self.write("main.py"))
            self.assertEqual(self.invoke(host, "prepare", stop_hook_active=True),
                             {"status": "continuation"})
            question = self.invoke(host, "prepare")
            self.assertEqual(self.invoke(host, "prepare"), {"status": "pending"})
            self.assertEqual(self.approve(host, "wrong-request"), {})
            self.assertEqual(self.invoke(host, "prepare"), {"status": "pending"})
            self.assertEqual(self.approve(host, question["request_id"], session="other-session"), {})
            self.assertEqual(self.invoke(host, "prepare", session="other-session"), {"status": "empty"})
            self.token(self.approve(host, question["request_id"]))
            self.assertEqual(self.approve(host, question["request_id"]), {})

    def test_removed_queue_entry_cannot_be_approved(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "project-review")])
            self.record(host, self.write("main.py"))
            question = self.invoke(host, "prepare")
            self.checkpoint(host, "clear")
            response = self.approve(host, question["request_id"])
            self.assertNotIn("decision", response)
            self.assertIn("No review was started", response["systemMessage"])
            self.assertEqual(self.pending(host), set())

    def test_failure_keeps_queue_without_success_or_dispatch(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "project-review")])
            path = self.write("main.py")
            self.record(host, path)
            question = self.invoke(host, "prepare")
            self.assertIsNone(self.invoke(host, "failure", request_id=question["request_id"]))
            self.assertEqual(self.pending(host), {str(path)})
            self.assertEqual(self.approve(host, question["request_id"]), {})
            self.assertEqual(self.invoke(host, "prepare"), {"status": "unchanged"})

    def test_corrupt_consent_state_fails_closed_and_preserves_queue(self):
        for host in ("claude", "codex"):
            self.configure(host, [ask_rule("main.py", "project-review")])
            path = self.write("main.py")
            self.record(host, path)
            question = self.invoke(host, "prepare")
            consent = Path(self.invoke(host, "consent_path"))
            consent.write_text("{broken")
            self.invoke(host, "prepare", error="JSONDecodeError")
            self.approve(host, question["request_id"], error="JSONDecodeError")
            self.assertEqual(self.pending(host), {str(path)})

    def test_approved_token_refuses_changed_revision_or_routing_and_cannot_clear_it(self):
        for host in ("claude", "codex"):
            for change in ("content", "reviewer", "manual", "removed"):
                with self.subTest(host=host, change=change):
                    self.configure(host, [ask_rule("main.py", "approved-review")])
                    path = self.write("main.py", change + " before\n")
                    self.record(host, path)
                    question = self.invoke(host, "prepare")
                    token = self.token(self.approve(host, question["request_id"]))
                    if change == "content":
                        path.write_text("changed after approval\n")
                    elif change == "reviewer":
                        self.configure(host, [ask_rule("main.py", "replacement-review", "skill")])
                    elif change == "manual":
                        self.configure(host, [rule("main.py", "approved-review")])
                    else:
                        self.configure(host, [])
                    result = subprocess.run(
                        [sys.executable, str(fixtures.CLI), "file-checkpoint", "show", "--token", token,
                         "--session", "session", "--host", host],
                        cwd=self.project, env=dict(self.env, GUARD_HOST=host),
                        capture_output=True, text=True, timeout=15)
                    self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertEqual(result.stdout, "")
                    self.assertIn("Request fresh consent", result.stderr)
                    # Do not refresh the queue first: an explicit refresh can reconcile rules
                    # that no longer match. The old approval itself must never clear this path.
                    self.assertEqual(self.checkpoint(host, "complete", token),
                                     {"cleared": 0, "remaining": 1})

    def test_explicit_checkpoints_keep_their_existing_completion_contract(self):
        for host in ("claude", "codex"):
            for on_stop in ("manual", "ask"):
                with self.subTest(host=host, on_stop=on_stop):
                    self.configure(host, [dict(rule("main.py", "original-review"), on_stop=on_stop)])
                    self.record(host, self.write("main.py", on_stop + "\n"))
                    snapshot = self.checkpoint(host, "show")
                    self.configure(host, [rule("main.py", "replacement-review")])
                    existing = self.checkpoint(host, "show", "--token", snapshot["token"])
                    self.assertEqual(existing["groups"], snapshot["groups"])
                    self.assertEqual(existing["groups"][0]["name"], "original-review")
                    self.assertEqual(self.checkpoint(host, "complete", snapshot["token"]),
                                     {"cleared": 1, "remaining": 0})


if __name__ == "__main__":
    unittest.main()
