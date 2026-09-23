from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ui import Navigator


class FindTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        lines = [f"line {i}" for i in range(80)]
        lines[5] = "Needle here and needle there"
        lines[60] = "\tlate NEEDLE" + " " * 100 + "needle far right"
        (self.root / "plain.txt").write_text("\n".join(lines))
        (self.root / "code.py").write_text("x = 1\n" * 50 + "value = 'needle'\n")
        self.nav = Navigator(self.root, "pane", False, "")
        self.nav.body, self.nav.text_width = 10, 40

    def open(self, name):
        self.nav.load(name)
        self.nav.preview_focus = True

    def type(self, text):
        for char in text:
            self.nav.key(char, None)

    def test_slash_in_preview_finds_incrementally_and_enter_keeps(self):
        self.open("plain.txt")
        self.type("/need")
        self.assertTrue(self.nav.finding)
        self.assertEqual(self.nav.query, "")  # The filename filter is untouched.
        self.assertEqual(self.nav.matches()[:2], [(5, 0, 4), (5, 16, 20)])
        self.assertEqual(self.nav.find_index, 0)
        self.nav.key("\n", None)
        self.assertFalse(self.nav.finding)
        self.assertEqual(self.nav.message, "Match 1/4")
        self.nav.key("n", None)
        self.nav.key("n", None)
        self.assertEqual(self.nav.find_index, 2)
        self.assertEqual(self.nav.preview_scroll, 60 - self.nav.body // 3)
        self.nav.key("N", None)
        self.assertEqual(self.nav.find_index, 1)
        for _ in range(3):
            self.nav.key("n", None)
        self.assertEqual(self.nav.message, "Match 1/4 (wrapped)")

    def test_smart_case_and_escape_restores_position(self):
        self.open("plain.txt")
        self.nav.preview_scroll = 20
        self.type("/NEEDLE")
        self.assertEqual(self.nav.matches(), [(60, 9, 15)])  # Tab expands to four spaces.
        self.nav.key("\x1b", None)
        self.assertFalse(self.nav.finding)
        self.assertEqual((self.nav.preview_scroll, self.nav.find_query), (20, ""))
        self.assertTrue(self.nav.preview_focus)

    def test_enter_alone_repeats_the_last_search_and_misses_report(self):
        self.open("plain.txt")
        self.type("/needle\n")
        self.type("/\n")
        self.assertEqual(self.nav.find_query, "needle")
        self.type("/zzz\n")
        self.assertEqual(self.nav.message, "Not found: zzz")

    def test_matches_scroll_long_lines_into_view(self):
        self.open("plain.txt")
        self.type("/far right\n")
        self.assertEqual(self.nav.matches()[0][0], 60)
        start = self.nav.matches()[0][1]
        self.assertGreater(self.nav.horizontal, 0)
        self.assertLessEqual(self.nav.horizontal, start)
        self.assertLess(start - self.nav.horizontal, self.nav.text_width)

    def test_draw_highlights_matches_on_screen(self):
        self.open("code.py")
        self.nav.prepare_preview(60)
        self.type("/needle\n")
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        with patch.object(self.nav, "span_style", return_value=0):
            self.nav.draw(screen)
        drawn = [call.args[2] for call in screen.addstr.call_args_list]
        self.assertIn("needle", drawn)
        self.assertTrue(any("Find in preview: needle" in text for text in drawn))

    def test_tree_focus_slash_still_filters_filenames(self):
        self.nav.load("plain.txt")
        self.nav.preview_focus = False
        self.type("/code")
        self.assertTrue(self.nav.searching)
        self.assertFalse(self.nav.finding)
        self.assertEqual(self.nav.query, "code")


if __name__ == "__main__":
    unittest.main()
