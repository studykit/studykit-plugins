from pathlib import Path
import curses
import sys
import tempfile
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import command_line
from ui import Navigator


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "src" / "deep").mkdir(parents=True)
        (self.root / "src" / "deep" / "module.py").write_text("\n".join(f"line {i}" for i in range(100)))
        (self.root / "src" / "main.py").write_text("print('needle')\n")
        (self.root / "notes.txt").write_text("hello\n")
        self.nav = Navigator(self.root, "pane", False, "")
        self.nav.body = 10

    def run_line(self, text, opener=":"):
        self.nav.key(opener, None)
        for char in text:
            self.nav.key(char, None)
        return self.nav.key("\n", None)

    def test_preview_reveals_the_file_and_goto_jumps(self):
        self.run_line("preview src/deep/module.py")
        self.assertEqual(self.nav.active, "src/deep/module.py")
        self.assertTrue(self.nav.preview_focus)
        self.assertEqual(self.nav.items[self.nav.selected].path, "src/deep/module.py")
        self.run_line("42")
        self.assertEqual(self.nav.preview_scroll, 41)
        self.assertEqual(self.nav.message, "Line 42/100")
        self.run_line("goto 1000")
        self.assertEqual(self.nav.preview_scroll, 90)
        self.run_line("top")
        self.assertEqual(self.nav.preview_scroll, 0)

    def test_alt_x_opens_the_same_prompt_and_quit_closes(self):
        self.nav.key("\x1bx", None)
        self.assertEqual(self.nav.command, "")
        self.nav.key("\x1b", None)
        self.assertIsNone(self.nav.command)
        self.assertFalse(self.run_line("q", opener="\x1bx"))

    def test_find_command_uses_preview_search(self):
        self.run_line("preview src/main.py")
        self.run_line("find needle")
        self.assertEqual(self.nav.find_query, "needle")
        self.assertEqual(self.nav.message, "Match 1/1")

    def test_errors_are_reported(self):
        self.run_line("bogus")
        self.assertIn("Unknown command: bogus", self.nav.message)
        self.run_line("preview missing.txt")
        self.assertIn("No such file", self.nav.message)
        self.run_line("goto 3")
        self.assertEqual(self.nav.message, "Open a file first")
        self.run_line("zoom in")
        self.assertEqual(self.nav.message, "No diagram in this preview")

    def test_icons_command_switches_and_saves(self):
        saved = []
        self.nav.on_icons = saved.append
        self.run_line("icons n")
        self.assertEqual((self.nav.icons, saved), ("nerd", ["nerd"]))
        self.run_line("icons bogus")
        self.assertEqual(self.nav.icons, "nerd")

    def test_fixed_arguments_accept_prefixes(self):
        self.run_line("ignored of")
        self.assertFalse(self.nav.include_ignored)
        self.run_line("ig on")
        self.assertTrue(self.nav.include_ignored)

    def test_tab_completes_commands_and_paths(self):
        self.nav.key(":", None)
        for char in "prev":
            self.nav.key(char, None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "preview ")
        for char in "src/d":
            self.nav.key(char, None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "preview src/deep/")
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "preview src/deep/module.py")
        self.nav.key("\x15", None)
        self.nav.key("c", None)
        self.nav.key("\t", None)  # cd, changes, config: listed in the completion menu.
        self.assertEqual(self.nav.command, "c")
        self.assertIsNotNone(self.nav.command_menu)

    def test_completion_menu_picks_narrows_and_inserts(self):
        self.nav.key(":", None)
        self.nav.key("c", None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command_choices()[1], ["cd", "changes", "config"])
        self.nav.key(curses.KEY_DOWN, None)
        self.nav.key("\t", None)  # Tab also moves on.
        self.assertEqual(self.nav.command_menu["selected"], 2)
        self.nav.key("h", None)  # Typing narrows the list and goes back to its top.
        self.assertEqual(self.nav.command_choices()[1], ["changes"])
        self.nav.key("\n", None)  # Enter inserts the choice without running it.
        self.assertEqual(self.nav.command, "changes ")
        self.assertIsNone(self.nav.command_menu)
        self.nav.key("\x15", None)
        for char in "preview s":
            self.nav.key(char, None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "preview src/")
        self.nav.key("\t", None)
        self.assertIsNotNone(self.nav.command_menu)
        self.nav.key("\x1b", None)  # Esc closes the list, not the command line.
        self.assertIsNone(self.nav.command_menu)
        self.assertEqual(self.nav.command, "preview src/")

    def test_emacs_keys_edit_the_command_line(self):
        self.nav.key(":", None)
        for char in "preview src/main.py":
            self.nav.key(char, None)
        self.nav.key("\x01", None)  # C-a
        self.assertEqual(self.nav.command_cursor, 0)
        self.nav.key("\x1bf", None)  # M-f
        self.assertEqual(self.nav.command_cursor, 7)
        self.nav.key("\x0b", None)  # C-k
        self.assertEqual(self.nav.command, "preview")
        self.nav.key("\x19", None)  # C-y
        self.assertEqual(self.nav.command, "preview src/main.py")
        self.nav.key("\x05", None)  # C-e
        self.nav.key("\x1b\x7f", None)  # M-DEL
        self.assertEqual(self.nav.command, "preview src/main.")
        self.nav.key("\x17", None)  # C-w kills the whole path.
        self.assertEqual(self.nav.command, "preview ")
        self.nav.key("\x02", None)  # C-b, then typing inserts at point.
        self.nav.key("x", None)
        self.assertEqual((self.nav.command, self.nav.command_cursor), ("previewx ", 8))
        self.nav.key("\x1bb", None)  # M-b
        self.nav.key("\x04", None)  # C-d
        self.assertEqual(self.nav.command, "reviewx ")
        self.nav.key("\x05", None)
        self.nav.key("\x02", None)
        self.nav.key("\x15", None)  # C-u kills to the start only.
        self.assertEqual((self.nav.command, self.nav.command_cursor), (" ", 0))
        self.nav.key("\x07", None)  # C-g cancels.
        self.assertIsNone(self.nav.command)

    def test_ctrl_g_cancels_but_never_closes(self):
        for key in "/py":
            self.nav.key(key, None)
        self.nav.key("\x07", None)  # Leaves the filter like Escape.
        self.assertEqual((self.nav.searching, self.nav.query), (False, ""))
        self.nav.preview_focus = True
        self.assertTrue(self.nav.key("\x07", None))
        self.assertFalse(self.nav.preview_focus)
        self.assertTrue(self.nav.key("\x07", None))  # Nothing left to cancel: stays open.
        self.assertFalse(self.nav.changes)
        self.nav.key("c", None)
        self.assertTrue(self.nav.changes)

    def test_emacs_keys_edit_the_filter_and_find(self):
        for key in ("/", *"main.py", "\x01", "\x0b"):  # C-a C-k
            self.nav.key(key, None)
        self.assertEqual((self.nav.query, self.nav.query_cursor), ("", 0))
        self.nav.key("\x19", None)  # C-y
        self.nav.key("\x1bb", None)  # M-b
        self.nav.key("x", None)
        self.assertEqual(self.nav.query, "main.xpy")
        self.nav.key("\x02", None)  # C-b
        self.nav.key("\x04", None)  # C-d
        self.assertEqual(self.nav.query, "main.py")
        self.assertEqual(self.nav.items[0].path, "src/main.py")
        self.nav.key("\n", None)
        self.run_line("preview notes.txt")
        for key in ("/", *"helo", "\x02", "l"):
            self.nav.key(key, None)
        self.assertEqual((self.nav.find_query, self.nav.message), ("hello", "Match 1/1"))

    def test_emacs_keys_edit_the_application_picker(self):
        self.nav.app_picker = {"target": "", "query": "", "cursor": 0, "selected": 0, "scroll": 0,
                               "apps": ["Finder", "Safari"]}
        for key in (*"Safar", "\x01", "\x0b", "\x19", "\x02", "\x04"):
            self.nav.key(key, None)
        self.assertEqual((self.nav.app_picker["query"], self.nav.app_picker["cursor"]), ("Safa", 4))

    def test_completion_keeps_text_after_the_cursor(self):
        self.nav.key(":", None)
        for char in "prev src/main.py":
            self.nav.key(char, None)
        for _ in "src/main.py":
            self.nav.key("\x02", None)
        self.nav.key("\x02", None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "preview  src/main.py")
        self.assertEqual(self.nav.command_cursor, 8)

    def test_mode_line_sits_above_the_command_line(self):
        screen = Mock()
        screen.getmaxyx.return_value = (30, 120)
        self.nav.load("notes.txt")
        self.nav.key(":", None)
        self.nav.draw(screen)
        rows = {}
        for call in screen.addstr.call_args_list:
            rows.setdefault(call.args[0], []).append(call.args[2])
        self.assertIn(" COMMAND ", rows[28])
        self.assertIn("notes.txt", rows[28])
        self.assertIn("6", rows[28])  # The file size.
        self.assertTrue(any(text.startswith(":") for text in rows[29]))

    def test_question_mark_lists_keys_until_any_key(self):
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        self.nav.key("?", None)
        self.nav.draw(screen)
        texts = [call.args[2] for call in screen.addstr.call_args_list]
        self.assertIn("COMMAND LINE", texts)
        self.nav.key("j", None)  # Closes the list without moving.
        self.assertFalse(self.nav.key_help)
        self.assertEqual(self.nav.selected, 0)

    def test_completion_menu_draws_like_the_application_picker(self):
        screen = Mock()
        screen.getmaxyx.return_value = (30, 120)
        self.nav.key(":", None)
        self.nav.key("c", None)
        self.nav.key("\t", None)
        self.nav.draw(screen)
        texts = [call.args[2] for call in screen.addstr.call_args_list]
        self.assertTrue(any("COMPLETE" in text for text in texts))
        self.assertTrue(any("Change the navigation root" in text for text in texts))

    def test_history_and_backspace_on_empty_line(self):
        self.run_line("help")
        self.run_line("help preview")
        self.assertIn(":preview FILE", self.nav.message)
        self.nav.key(":", None)
        self.nav.key(curses.KEY_UP, None)
        self.assertEqual(self.nav.command, "help preview")
        self.nav.key(curses.KEY_UP, None)
        self.assertEqual(self.nav.command, "help")
        self.nav.key("\x15", None)
        self.nav.key("\x7f", None)
        self.assertIsNone(self.nav.command)

    def test_colon_is_text_while_filtering_filenames(self):
        self.nav.key("/", None)
        self.nav.key(":", None)
        self.assertIsNone(self.nav.command)
        self.assertEqual(self.nav.query, ":")

    def test_arrows_pick_filter_results_while_typing(self):
        for key in "/py":
            self.nav.key(key, None)
        paths = [row.path for row in self.nav.items]
        self.nav.key(curses.KEY_DOWN, None)
        self.assertTrue(self.nav.searching)
        self.assertEqual(self.nav.items[self.nav.selected].path, paths[1])
        self.nav.key(curses.KEY_UP, None)
        self.nav.key(curses.KEY_UP, None)  # Stops at the first match.
        self.assertEqual(self.nav.selected, 0)
        self.nav.key("\x0e", None)
        self.nav.key("\n", None)
        self.assertFalse(self.nav.searching)
        self.assertEqual(self.nav.items[self.nav.selected].path, paths[1])

    def test_cd_changes_root_and_completes_directories(self):
        self.assertEqual(command_line.complete("cd s", self.root, [])[0], "cd src/")
        self.run_line("cd src")
        self.assertEqual(self.nav.root, (self.root / "src").resolve())

    def test_git_root_reports_a_root_outside_git(self):
        self.run_line("git-root")
        self.assertEqual(self.nav.message, "The current root is not inside a Git repository")


if __name__ == "__main__":
    unittest.main()
