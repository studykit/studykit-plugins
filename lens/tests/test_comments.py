import curses
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import command_line
import comments
import settings
import terminal_input as terminal
from ui import Navigator


class FakeHost:
    def __init__(self, root):
        self.panes = {
            "w1:p1": {"pane_id": "w1:p1", "terminal_id": "t1", "tab_id": "w1:t1", "workspace_id": "w1",
                      "agent": "claude", "foreground_cwd": str(root)},
            "w1:p2": {"pane_id": "w1:p2", "terminal_id": "t2", "tab_id": "w1:t2", "workspace_id": "w1",
                      "agent": "codex", "foreground_cwd": str(root / "src")},
            "w2:p1": {"pane_id": "w2:p1", "terminal_id": "t3", "tab_id": "w2:t1", "workspace_id": "w2",
                      "agent": "claude", "foreground_cwd": "/elsewhere"},
        }
        self.sent = []
        self.failure = None

    def pane(self, pane_id):
        if pane_id not in self.panes:
            raise RuntimeError("pane_not_found: gone")
        return self.panes[pane_id]

    def agents(self):
        return [dict(pane, place="ws") for pane in self.panes.values() if pane.get("agent")]

    def send(self, pane_id, text):
        if self.failure:
            raise RuntimeError(self.failure)
        self.sent.append((pane_id, text))


class CommentModelTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        (self.root / "src").mkdir()
        self.file = self.root / "src" / "a.py"
        self.file.write_text("one\ntwo\nthree\n")

    def comment(self, start, end, note=""):
        lines = comments.read_lines(self.file)
        return comments.Buffer().add(str(self.file), start, end, note, comments.lines_digest(lines[start - 1:end]))

    def test_reference_is_relative_to_the_target_directory(self):
        comment = self.comment(1, 2, "why?")
        self.assertEqual(comments.line(comment, self.root), "src/a.py:1-2 — why?")
        self.assertEqual(comments.line(comment, self.root / "src"), "a.py:1-2 — why?")
        self.assertEqual(comments.reference(self.comment(3, 3), Path("/elsewhere")), f"{self.file}:3")
        self.assertEqual(comments.reference(comment, None), f"{self.file}:1-2")

    def test_changed_lines_are_noticed(self):
        comment = self.comment(2, 2)
        self.assertFalse(comments.changed(comment))
        self.file.write_text("zero\none\ntwo\nthree\n")
        self.assertTrue(comments.changed(comment))
        self.file.write_text("one\n")
        self.assertTrue(comments.changed(comment))

    def test_draft_keeps_edits_and_appends_later_comments(self):
        buffer = comments.Buffer()
        buffer.add(str(self.file), 1, 1, "", "x")
        self.assertEqual(comments.compose(buffer, self.root), "src/a.py:1")
        buffer.draft, buffer.drafted = "src/a.py:1 look here\n", {1}
        buffer.add(str(self.file), 2, 3, "and here", "y")
        self.assertEqual(comments.compose(buffer, self.root), "src/a.py:1 look here\n\nsrc/a.py:2-3 — and here")

    def test_store_round_trips_buffers_and_targets(self):
        store = comments.Store(self.root / "state")
        target, source = comments.Target("w1:p2", "t2"), comments.Target("w1:p1", "t1")
        buffer = comments.Buffer()
        buffer.add(str(self.file), 1, 2, "note", "d")
        buffer.draft, buffer.drafted = "draft", {1}
        store.save(target, buffer)
        loaded = store.load(target)
        self.assertEqual((loaded.comments, loaded.draft, loaded.drafted), (buffer.comments, "draft", {1}))
        self.assertEqual(store.load(comments.Target("w1:p2", "other")).comments, [])  # A reused pane ID.
        store.save_target(source, target)
        self.assertEqual(store.load_target(source), target)
        store.save_target(source, source)
        self.assertIsNone(store.load_target(source))
        buffer.clear()
        store.save(target, buffer)
        self.assertEqual(list((self.root / "state" / "comments").glob("*.json")), [])

    def test_store_ignores_malformed_entries(self):
        payload = {"version": 1, "comments": [
            {"id": 1, "path": "relative.py", "start": 1, "end": 1},
            {"id": 2, "path": "/abs.py", "start": 3, "end": 2},
            {"id": 3, "path": "/abs.py", "start": 1, "end": 2, "note": 5},
            {"id": 4, "path": "/abs.py", "start": 1, "end": 2, "note": "ok", "digest": "d"}], "draft": 3}
        buffer = comments.decode_buffer(payload)
        self.assertEqual([comment.id for comment in buffer.comments], [4])
        self.assertIsNone(buffer.draft)


class MultiLineEditTests(unittest.TestCase):
    def edit(self, text, cursor, *keys, killed=""):
        for key in keys:
            text, cursor, killed = command_line.edit_text(text, cursor, key, killed)
        return text, cursor, killed

    def test_enter_and_line_joins(self):
        self.assertEqual(self.edit("ab", 1, "\n")[:2], ("a\nb", 2))
        self.assertEqual(self.edit("a\nb", 2, "\x7f")[:2], ("ab", 1))  # Backspace at a line start.
        self.assertEqual(self.edit("a\nb", 1, "\x04")[:2], ("ab", 1))  # C-d at a line end.
        self.assertEqual(self.edit("a\nb", 1, "\x0b"), ("ab", 1, "\n"))  # C-k at a line end.

    def test_line_keys_act_on_the_current_line(self):
        self.assertEqual(self.edit("one\ntwo", 5, "\x01")[1], 4)  # C-a goes to this line's start.
        self.assertEqual(self.edit("one\ntwo", 5, "\x05")[1], 7)
        self.assertEqual(self.edit("one\ntwo\nsix", 5, "\x0b")[:2], ("one\nt\nsix", 5))
        self.assertEqual(self.edit("one\ntwo", 7, "\x15")[:2], ("one\n", 4))

    def test_vertical_and_crossing_moves(self):
        self.assertEqual(self.edit("long line\nab", 7, "\x0e")[1], 12)  # Down clamps to the shorter line.
        self.assertEqual(self.edit("long line\nab", 11, curses.KEY_UP)[1], 1)
        self.assertEqual(self.edit("a\nb", 2, "\x02")[1], 1)  # C-b at a line start.
        self.assertEqual(self.edit("a\nb", 1, curses.KEY_RIGHT)[1], 2)


class NavigatorCommentTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        (self.root / "src").mkdir()
        (self.root / "src" / "main.py").write_text("\n".join(f"line {i}" for i in range(1, 41)) + "\n")
        (self.root / "notes.md").write_text("# Title\n\nSome **text**\n")
        self.host = FakeHost(self.root)
        self.store = comments.Store(self.root / ".state")
        self.nav = self.navigator()

    def navigator(self):
        nav = Navigator(self.root, "w1:p1", False, "", comment_store=self.store, agent_host=self.host,
                        source_terminal="t1")
        nav.body = 10
        return nav

    def keys(self, *keys):
        for key in keys:
            self.nav.key(key, None)

    def open(self, name):
        self.nav.open_file(name)

    def test_select_add_and_send(self):
        self.open("src/main.py")
        self.keys("j", "j", "V", "j", "j", "A")  # A adds the comment and opens the message on it.
        self.assertEqual(self.nav.composer["text"], "src/main.py:3-5 ")  # A space after a line reference.
        self.keys(*"check this", "\x1b")
        self.assertIsNone(self.nav.selection_anchor)
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)
        self.keys("k", "A")  # A without a selection comments on the cursor line.
        self.assertEqual(self.nav.composer["text"], "src/main.py:3-5 check this\n\nsrc/main.py:4 ")
        self.assertEqual(self.nav.composer["cursor"], len(self.nav.composer["text"]))
        self.keys(*"ok?", "\x13")
        self.assertEqual(self.host.sent, [("w1:p1", "src/main.py:3-5 check this\n\nsrc/main.py:4 ok?")])
        self.assertIsNone(self.nav.composer)
        self.assertEqual(self.nav.comment_buffer.comments, [])
        self.assertEqual(self.store.load(comments.Target("w1:p1", "t1")).comments, [])

    def test_escape_keeps_a_draft_that_survives_reopening(self):
        self.open("src/main.py")
        self.keys("A", *"first", "\x1b")
        self.assertIsNone(self.nav.composer)
        self.nav = self.navigator()
        self.open("src/main.py")
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)
        self.keys("G", "A")
        self.assertEqual(self.nav.composer["text"], "src/main.py:1 first\n\nsrc/main.py:40 ")

    def test_emptied_message_discards_the_comments(self):
        self.open("src/main.py")
        self.keys("A", "\x15", "\x1b")
        self.assertEqual(self.nav.comment_buffer.comments, [])

    def test_failed_send_keeps_the_editor_open(self):
        self.open("src/main.py")
        self.keys("A")
        self.host.failure = "agent_blocked: waiting for approval"
        self.keys("\x13")
        self.assertIn("agent_blocked", self.nav.composer["error"])
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)
        del self.host.panes["w1:p1"]
        self.keys("\x13")
        self.assertIn("gone", self.nav.composer["error"])

    def test_rendered_markdown_needs_the_source_view(self):
        self.open("notes.md")
        self.keys("V")
        self.assertIsNone(self.nav.selection_anchor)
        self.assertIn("press s", self.nav.message)
        self.keys("s")
        self.nav.prepare_preview(60)
        self.assertIsNone(self.nav.rendered)
        self.assertEqual(self.nav.content[0], "# Title")
        self.keys("j", "j", "A")
        self.assertEqual(self.nav.composer["text"], "notes.md:3 ")

    def test_tree_comments_name_a_file_or_folder(self):
        self.nav.preview_focus = False
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "src")
        self.keys("A", *" layout?", "\x1b")
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "notes.md")
        self.keys("A", "\x1b")
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == ".")
        self.keys("A", "\x1b")
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "..")
        self.keys("A")
        self.assertIsNone(self.nav.composer)
        self.keys("S")
        self.assertEqual(self.nav.composer["text"], "src/ layout?\n\nnotes.md\n\n./")
        self.assertEqual(self.nav.composer["changed"], [])
        self.keys("\x1b")
        (self.root / "notes.md").unlink()
        self.keys("S")
        self.assertEqual(self.nav.composer["changed"], ["notes.md"])

    def test_text_selection_sends_the_characters(self):
        (self.root / "code.py").write_text("def run(job):\n    if retry and not timeout:\n        wait()\n")
        self.nav.refresh()
        self.open("code.py")
        self.keys("j", "w", "v")  # The cursor moves along the line before a selection starts.
        self.assertEqual((self.nav.selection_kind, self.nav.anchor_column), ("char", 4))
        self.keys("w", "w", "$")
        self.assertEqual(self.nav.preview_column, 28)
        self.keys("j", "^")
        self.assertEqual(self.nav.preview_column, 8)
        self.keys("0", "l", "l", "A")  # Selected text is copied, not added, and the message opens.
        self.assertIsNone(self.nav.selection_anchor)
        self.assertEqual(self.nav.comment_buffer.comments, [])
        self.assertEqual(self.nav.command_killed, "if retry and not timeout:\n   ")
        self.assertIn("C-y", self.nav.composer["hint"])
        self.keys(*"why? ", "\x19")
        self.assertEqual(self.nav.composer["text"], "why? if retry and not timeout:\n   ")
        self.assertEqual(self.nav.composer["hint"], "")
        self.keys("\x1b")
        self.nav.open_file("code.py")
        self.keys("V", "A")  # A line selection is still a comment, after the kept draft.
        self.assertEqual(self.nav.composer["text"], "why? if retry and not timeout:\n   \n\ncode.py:1 ")
        self.keys("\x1b", "v", "A")  # A copy into a message that has text starts after a blank line.
        self.assertEqual(self.nav.composer["text"][-len("code.py:1 \n\n"):], "code.py:1 \n\n")
        self.assertEqual(self.nav.composer["cursor"], len(self.nav.composer["text"]))

    def test_v_and_V_switch_or_end_the_selection(self):
        self.open("src/main.py")
        self.keys("V", "v")
        self.assertEqual((self.nav.selection_kind, self.nav.selection_anchor), ("char", 0))
        self.keys("V")
        self.assertEqual(self.nav.selection_kind, "line")
        self.keys("V")
        self.assertIsNone(self.nav.selection_anchor)
        self.keys("l", "l", "$", "h")  # The cursor moves along the line outside a selection too.
        self.assertEqual(self.nav.preview_column, 4)  # "line 1" ends at column 5.
        self.keys(*("j" * 9), "j", "k")  # j and k return to the wanted column on long enough lines.
        self.assertEqual((self.nav.preview_cursor, self.nav.preview_column), (9, 4))
        self.keys("b")  # b is still page up outside a text selection.
        self.assertEqual(self.nav.preview_cursor, 0)

    def test_click_puts_the_cursor_on_a_character(self):
        (self.root / "tabs.txt").write_text("\tab cd\n")
        self.nav.refresh()
        self.open("tabs.txt")
        self.nav.divider, self.nav.content_top, self.nav.text_left = 30, 2, 39
        self.nav.handle_mouse(terminal.Mouse(39 + 5, 2, "click"))  # The tab takes four cells, then "ab".
        self.assertEqual(self.nav.preview_column, 2)
        self.nav.handle_mouse(terminal.Mouse(39 + 2, 2, "click"))
        self.assertEqual(self.nav.preview_column, 0)
        self.nav.handle_mouse(terminal.Mouse(39 + 40, 2, "click"))
        self.assertEqual(self.nav.preview_column, 5)

    def test_excerpt_fence_outlasts_backticks_inside(self):
        buffer = comments.Buffer()
        comment = buffer.add("/a.md", 1, 1, "", "d", (1, 5), "``` x")
        self.assertEqual(comments.line(comment, None), "/a.md:1:1-1:5\n````\n``` x\n````")
        self.assertEqual(comments.decode_buffer(comments.encode_buffer(comments.Target("p", "t"), buffer)).comments,
                         [comment])

    def test_clear_asks_first(self):
        self.open("src/main.py")
        self.keys("A", "\x1b", "X", "n")
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)
        self.keys("X", "y")
        self.assertEqual(self.nav.comment_buffer.comments, [])
        self.keys("X")
        self.assertFalse(self.nav.confirm_clear)  # Nothing to discard, nothing to ask.

    def test_escape_drops_the_selection_before_leaving_the_preview(self):
        self.open("src/main.py")
        self.keys("V", "\x1b")
        self.assertIsNone(self.nav.selection_anchor)
        self.assertTrue(self.nav.preview_focus)

    def test_picker_scopes_and_target_buffers(self):
        self.open("src/main.py")
        self.keys("A", "\x1b")
        self.nav.run_command("comment.target", None)
        labels = lambda: [agent["pane_id"] for agent in self.nav.agent_choices()]
        self.assertEqual(labels(), ["w1:p1"])
        self.keys("\t")
        self.assertEqual(labels(), ["w1:p1", "w1:p2"])
        self.keys("\t")
        self.assertEqual(labels(), ["w1:p1", "w1:p2", "w2:p1"])
        self.keys(*"codex")
        self.assertEqual(labels(), ["w1:p2"])
        self.keys("\n")
        self.assertEqual(self.nav.comment_target, comments.Target("w1:p2", "t2"))
        self.assertEqual(self.nav.comment_buffer.comments, [])  # Each agent has its own buffer.
        self.keys("A")
        self.assertEqual(self.nav.composer["text"], "main.py:1 ")  # Relative to that agent's directory.
        self.keys("\x1b")
        self.nav = self.navigator()  # The chosen agent is remembered for this pane.
        self.assertEqual(self.nav.comment_target, comments.Target("w1:p2", "t2"))
        del self.host.panes["w1:p2"]
        self.nav = self.navigator()  # Back to this pane's agent once that one is gone.
        self.assertEqual(self.nav.comment_target, comments.Target("w1:p1", "t1"))
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)

    def test_submit_key_is_configurable(self):
        path = self.root / "config.toml"
        path.write_text('[comment]\nsubmit = "alt+enter"\n')
        self.assertTrue(settings.load(path).errors)
        path.write_text('[comment]\nsubmit = "alt+s"\n')
        loaded = settings.load(path)
        self.assertEqual((loaded.submit, loaded.errors), ("\x1bs", []))
        path.write_text('[comment]\nsubmit = "s"\n')
        self.assertTrue(settings.load(path).errors)


if __name__ == "__main__":
    unittest.main()
