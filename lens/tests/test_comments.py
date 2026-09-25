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
        self.assertEqual(comments.line(comment, self.root), "src/a.py:1-2 why?")
        self.assertEqual(comments.line(comment, self.root / "src"), "a.py:1-2 why?")
        self.assertEqual(comments.reference(self.comment(3, 3), Path("/elsewhere")), f"{self.file}:3")
        self.assertEqual(comments.reference(comment, None), f"{self.file}:1-2")

    def test_changed_lines_are_noticed(self):
        comment = self.comment(2, 2)
        self.assertFalse(comments.changed(comment))
        self.file.write_text("zero\none\ntwo\nthree\n")
        self.assertTrue(comments.changed(comment))
        self.file.write_text("one\n")
        self.assertTrue(comments.changed(comment))

    def test_message_is_the_text_then_each_comment(self):
        buffer = comments.Buffer()
        first = buffer.add(str(self.file), 1, 1, "", "x")
        buffer.add(str(self.file), 2, 3, "two lines\nof note", "y")
        self.assertEqual(comments.compose(buffer, self.root), "src/a.py:1\n\nsrc/a.py:2-3\ntwo lines\nof note")
        buffer.draft = "Please review.\n"
        buffer.set_note(first.id, " look here ")
        self.assertEqual(comments.compose(buffer, self.root),
                         "Please review.\n\nsrc/a.py:1 look here\n\nsrc/a.py:2-3\ntwo lines\nof note")
        buffer.remove(first.id)
        self.assertEqual([comment.start for comment in buffer.comments], [2])

    def test_store_round_trips_buffers_and_targets(self):
        store = comments.Store(self.root / "state")
        target, source = comments.Target("w1:p2", "t2"), comments.Target("w1:p1", "t1")
        buffer = comments.Buffer()
        buffer.add(str(self.file), 1, 2, "note\nmore", "d")
        buffer.draft = "draft"
        store.save(target, buffer)
        loaded = store.load(target)
        self.assertEqual((loaded.comments, loaded.draft), (buffer.comments, "draft"))
        self.assertEqual(store.load(comments.Target("w1:p2", "other")).comments, [])  # A reused pane ID.
        store.save_target(source, target)
        self.assertEqual(store.load_target(source), target)
        store.save_target(source, source)
        self.assertIsNone(store.load_target(source))
        buffer.clear()
        store.save(target, buffer)
        self.assertEqual(list((self.root / "state" / "comments").glob("*.json")), [])

    def test_store_ignores_malformed_entries_and_old_drafts(self):
        payload = {"version": 1, "comments": [
            {"id": 1, "path": "relative.py", "start": 1, "end": 1},
            {"id": 2, "path": "/abs.py", "start": 3, "end": 2},
            {"id": 3, "path": "/abs.py", "start": 1, "end": 2, "note": 5},
            {"id": 4, "path": "/abs.py", "start": 1, "end": 2, "note": "ok", "digest": "d"}],
            "draft": "src/a.py:1 a whole message"}
        buffer = comments.decode_buffer(payload)
        self.assertEqual([comment.id for comment in buffer.comments], [4])
        self.assertIsNone(buffer.draft)  # A free-text message cannot become notes.


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

    def draw(self):
        from unittest.mock import Mock, patch
        screen = Mock()
        screen.getmaxyx.return_value = (40, 140)
        with patch("curses.has_colors", return_value=False):
            self.nav.draw(screen)

    def test_add_writes_a_note_then_sends_the_message(self):
        self.open("src/main.py")
        self.keys("j", "j", "V", "j", "j", "A")  # A adds the comment and opens its note.
        self.assertEqual((self.nav.composer["mode"], self.nav.composer["text"]), ("note", ""))
        self.keys(*"check this", "\n", *"and this", "\x1b")
        self.assertIsNone(self.nav.selection_anchor)
        self.assertEqual(self.nav.comment_buffer.comments[0].note, "check this\nand this")
        self.keys("k", "A", *"ok?", "\x13")  # C-s from a note saves it and shows the message.
        self.assertEqual(self.nav.composer["mode"], "message")
        self.keys(*"Please look.", "\x13")
        self.assertEqual(self.host.sent, [("w1:p1", "Please look.\n\nsrc/main.py:3-5\ncheck this\nand this"
                                                    "\n\nsrc/main.py:4 ok?")])
        self.assertIsNone(self.nav.composer)
        self.assertEqual(self.nav.comment_buffer.comments, [])
        self.assertEqual(self.store.load(comments.Target("w1:p1", "t1")).comments, [])

    def test_notes_and_message_survive_reopening(self):
        self.open("src/main.py")
        self.keys("A", *"first", "\x1b", "S", *"intro", "\x1b")
        self.nav = self.navigator()
        self.assertEqual((self.nav.comment_buffer.comments[0].note, self.nav.comment_buffer.draft), ("first", "intro"))
        self.keys("S")
        self.assertEqual(self.nav.composer["text"], "intro")

    def test_failed_send_keeps_the_editor_open(self):
        self.open("src/main.py")
        self.keys("A", "\x1b", "S")
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
        self.keys("j", "j", "A", "\x1b")
        self.assertEqual(comments.compose(self.nav.comment_buffer, self.root), "notes.md:3")

    def test_tree_comments_name_a_file_or_folder(self):
        self.nav.preview_focus = False
        for name, note in (("src", "layout?"), ("notes.md", ""), (".", "")):
            self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == name)
            self.keys("A", *note, "\x1b")
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "..")
        self.keys("A")
        self.assertIsNone(self.nav.composer)
        self.assertEqual(comments.compose(self.nav.comment_buffer, self.root), "src/ layout?\n\nnotes.md\n\n./")
        self.keys("S")
        self.assertEqual(self.nav.composer["changed"], [])
        self.keys("\x1b")
        (self.root / "notes.md").unlink()
        self.keys("S")
        self.assertEqual(self.nav.composer["changed"], ["notes.md"])

    def test_text_selection_is_copied_into_the_message(self):
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
        self.assertEqual(self.nav.composer["mode"], "message")
        self.assertIn("C-y", self.nav.composer["hint"])
        self.keys(*"why? ", "\x19")
        self.assertEqual(self.nav.composer["text"], "why? if retry and not timeout:\n   ")
        self.assertEqual(self.nav.composer["hint"], "")
        self.keys("\x1b", "k", "0", "w", "v", "b", "A")  # Into a message with text: after a blank line.
        self.assertTrue(self.nav.composer["text"].endswith("   \n\n"))

    def test_clicking_a_reference_shows_it_in_the_preview(self):
        from unittest.mock import patch
        self.open("src/main.py")
        self.keys(*"jjjjjjjjj", "V", "j", "j", "A", *"why?", "\x1b")
        self.nav.preview_focus = False
        self.nav.selected = next(i for i, row in enumerate(self.nav.items) if row.path == "src")
        self.keys("A", "\x1b", "S", *"see notes.md:3 and src/main.py:2:3-4:5, ok")
        self.draw()
        area_top, left, _, rows = self.nav.composer["layout"]
        segment = rows[0][1]
        self.nav.key(terminal.Mouse(left + 1, area_top, "click"), None)  # A word, not a reference.
        self.assertIsNotNone(self.nav.composer)
        self.nav.key(terminal.Mouse(left + segment.index("src/main.py:2") + 2, area_top, "click"), None)
        self.assertIsNone(self.nav.composer)
        self.assertEqual((self.nav.selection_kind, self.nav.preview_cursor, self.nav.preview_column,
                          self.nav.selection_anchor, self.nav.anchor_column), ("char", 1, 2, 3, 4))
        self.assertEqual(self.nav.comment_buffer.draft, "see notes.md:3 and src/main.py:2:3-4:5, ok")
        self.keys("S")
        self.draw()
        listed = self.nav.composer["list"]
        reference = next(y for y, number, kind in listed if kind == "reference")
        self.nav.key(terminal.Mouse(left + 1, reference, "click"), None)  # The first comment's reference.
        self.assertEqual((self.nav.active, self.nav.preview_cursor, self.nav.selection_anchor), ("src/main.py", 9, 11))
        self.keys("S")
        self.draw()
        folder = [y for y, number, kind in self.nav.composer["list"] if kind == "reference"][1]
        self.nav.key(terminal.Mouse(left + 1, folder, "click"), None)
        self.assertEqual((self.nav.items[self.nav.selected].path, self.nav.preview_focus), ("src", False))
        self.keys("S")
        self.draw()
        note = next(y for y, number, kind in self.nav.composer["list"] if kind == "note")
        self.nav.key(terminal.Mouse(left + 1, note, "click"), None)  # A note opens for editing.
        self.assertEqual((self.nav.composer["mode"], self.nav.composer["text"]), ("note", "why?"))
        self.keys("\x13")
        self.draw()
        self.nav.key(terminal.Mouse(left + segment.index("notes.md") + 2, area_top, "click"), None)
        self.assertEqual((self.nav.active, self.nav.diagram_source, self.nav.preview_cursor), ("notes.md", True, 2))

    def test_preview_marks_commented_lines(self):
        self.open("src/main.py")
        self.keys("j", "V", "j", "A", "\x1b", *"jjjj", "A", "\x1b")
        self.assertEqual(self.nav.commented_lines(), {1, 2, 6})
        self.open("notes.md")
        self.assertEqual(self.nav.commented_lines(), set())

    def test_icon_click_shows_edits_and_deletes_the_comment(self):
        self.open("src/main.py")
        self.keys("j", "V", "j", "A", *"first", "\x1b", *"jjjj", "A", *"second", "\x1b")
        self.assertEqual(set(self.nav.comment_starts()), {1, 6})
        self.nav.divider, self.nav.content_top, self.nav.text_left = 30, 2, 39
        self.nav.preview_scroll = 0
        self.nav.handle_mouse(terminal.Mouse(39 - 7, 2 + 1, "click"))
        self.assertEqual(self.nav.comment_view["ids"], [self.nav.comment_buffer.comments[0].id])
        self.nav.key("q", None)  # Any key but Enter and d closes it.
        self.assertIsNone(self.nav.comment_view)
        self.nav.handle_mouse(terminal.Mouse(39 - 6, 2 + 6, "click"))
        self.nav.key("\n", None)  # Enter edits its note.
        self.assertEqual((self.nav.composer["mode"], self.nav.composer["text"]), ("note", "second"))
        self.nav.key("\x1b", None)
        self.nav.handle_mouse(terminal.Mouse(39 - 7, 2 + 1, "click"))
        self.keys("d", "n")
        self.assertEqual(len(self.nav.comment_buffer.comments), 2)
        self.nav.handle_mouse(terminal.Mouse(39 - 7, 2 + 1, "click"))
        self.keys("d", "y")
        self.assertEqual([comment.note for comment in self.nav.comment_buffer.comments], ["second"])
        self.nav.handle_mouse(terminal.Mouse(39 - 7, 2 + 2, "click"))  # Not where a comment starts.
        self.assertIsNone(self.nav.comment_view)
        self.assertEqual(self.nav.preview_cursor, 2)

    def test_keys_reach_the_gutter_comments(self):
        self.open("src/main.py")
        self.keys("j", "V", "j", "j", "A", *"wide", "\x1b", "k", "A", *"inner", "\x1b", *"jjjjj", "A", "\x1b")
        self.keys("g", "m")
        self.assertIsNone(self.nav.comment_view)
        self.assertIn("No comment", self.nav.message)
        self.keys("}")
        self.assertEqual(self.nav.preview_cursor, 1)
        self.keys("}", "m")  # Line 3 is covered by both; the one starting there comes first.
        self.assertEqual(self.nav.preview_cursor, 2)
        notes = lambda: [self.nav.comment_buffer.find(number).note for number in self.nav.comment_view["ids"]]
        self.assertEqual(notes(), ["inner", "wide"])
        self.keys("j", "\n")  # j chooses the next one, Enter edits it.
        self.assertEqual(self.nav.composer["text"], "wide")
        self.keys("\x1b", "}", "}")
        self.assertEqual(self.nav.preview_cursor, 7)
        self.assertIn("No more comments below", self.nav.message)
        self.keys("{", "{", "{")
        self.assertEqual(self.nav.preview_cursor, 1)
        self.keys("m", "d", "y")
        self.assertEqual(sorted(comment.note for comment in self.nav.comment_buffer.comments), ["", "inner"])

    def test_sidebar_lists_folds_and_shows_comments(self):
        self.open("src/main.py")
        self.draw()
        self.assertEqual(self.nav.sidebar_width, 0)  # No comments, no list.
        self.keys("j", "V", "j", "A", *"why?", "\x1b", *"jjjj", "A", "\x1b")
        self.draw()
        self.assertGreater(self.nav.sidebar_width, 20)
        rows = self.nav.sidebar_rows
        self.assertEqual(sorted({comment.start for _, comment, _ in rows}), [2, 7])
        y = next(y for y, comment, kind in rows if comment.start == 7 and kind == "reference")
        self.nav.key("\t", None)  # To the tree, so the click must bring the preview back.
        self.nav.handle_mouse(terminal.Mouse(self.nav.sidebar_x + 3, y, "click"))
        self.assertEqual((self.nav.active, self.nav.preview_cursor, self.nav.preview_focus), ("src/main.py", 6, True))
        y = next(y for y, comment, kind in rows if kind == "note")
        self.nav.handle_mouse(terminal.Mouse(self.nav.sidebar_x + 3, y, "click"))  # A note opens to edit.
        self.assertEqual(self.nav.composer["text"], "why?")
        self.keys("\x1b")
        self.nav.handle_mouse(terminal.Mouse(self.nav.sidebar_x + 3, 1, "click"))  # The title folds it.
        self.assertFalse(self.nav.sidebar_open)
        self.draw()
        self.assertEqual(self.nav.sidebar_width, 4)
        self.keys("C")
        self.assertTrue(self.nav.sidebar_open)
        self.keys("X", "y")
        self.draw()
        self.assertEqual(self.nav.sidebar_width, 0)

    def test_clear_asks_first(self):
        self.open("src/main.py")
        self.keys("A", "\x1b", "X", "n")
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)
        self.keys("X", "y")
        self.assertEqual(self.nav.comment_buffer.comments, [])
        self.keys("X")
        self.assertFalse(self.nav.confirm_clear)  # Nothing to discard, nothing to ask.

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
        self.keys("A", "\x1b", "S")
        self.assertEqual(comments.compose(self.nav.comment_buffer, self.nav.composer["cwd"]), "main.py:1")
        self.keys("\x1b")
        self.nav = self.navigator()  # The chosen agent is remembered for this pane.
        self.assertEqual(self.nav.comment_target, comments.Target("w1:p2", "t2"))
        del self.host.panes["w1:p2"]
        self.nav = self.navigator()  # Back to this pane's agent once that one is gone.
        self.assertEqual(self.nav.comment_target, comments.Target("w1:p1", "t1"))
        self.assertEqual(len(self.nav.comment_buffer.comments), 1)

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

    def test_escape_drops_the_selection_before_leaving_the_preview(self):
        self.open("src/main.py")
        self.keys("V", "\x1b")
        self.assertIsNone(self.nav.selection_anchor)
        self.assertTrue(self.nav.preview_focus)

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
