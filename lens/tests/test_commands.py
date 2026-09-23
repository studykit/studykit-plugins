from pathlib import Path
import curses
import sys
import tempfile
import unittest

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

    def test_open_reveals_the_file_and_goto_jumps(self):
        self.run_line("e src/deep/module.py")
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
        self.run_line("open src/main.py")
        self.run_line("find needle")
        self.assertEqual(self.nav.find_query, "needle")
        self.assertEqual(self.nav.message, "Match 1/1")

    def test_errors_are_reported(self):
        self.run_line("bogus")
        self.assertIn("Unknown command: bogus", self.nav.message)
        self.run_line("open missing.txt")
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
        for char in "op":
            self.nav.key(char, None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "open ")
        for char in "src/d":
            self.nav.key(char, None)
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "open src/deep/")
        self.nav.key("\t", None)
        self.assertEqual(self.nav.command, "open src/deep/module.py")
        self.nav.key("\x15", None)
        self.nav.key("c", None)
        self.nav.key("\t", None)  # cd, changes: shown as candidates.
        self.assertEqual(self.nav.command, "c")
        self.assertIn("changes", self.nav.message)

    def test_history_and_backspace_on_empty_line(self):
        self.run_line("help")
        self.run_line("help open")
        self.assertIn(":open FILE", self.nav.message)
        self.nav.key(":", None)
        self.nav.key(curses.KEY_UP, None)
        self.assertEqual(self.nav.command, "help open")
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

    def test_cd_changes_root_and_completes_directories(self):
        self.assertEqual(command_line.complete("cd s", self.root, [])[0], "cd src/")
        self.run_line("cd src")
        self.assertEqual(self.nav.root, (self.root / "src").resolve())


if __name__ == "__main__":
    unittest.main()
