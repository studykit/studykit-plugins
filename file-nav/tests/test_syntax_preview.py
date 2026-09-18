from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from markdown_preview import Span, Style
import syntax_preview
from theme_colors import resolve
from ui import Navigator


def plain(lines):
    return ["".join(span.text for span in line) for line in lines]


class SyntaxTests(unittest.TestCase):
    def test_common_extensions_and_special_filenames(self):
        examples = {
            "app.py": 'def hello():\n    return "world"\n',
            "app.js": 'const answer = 42;\n',
            "app.ts": 'const answer: number = 42;\n',
            "app.tsx": 'const App = () => <div>Hello</div>;\n',
            "App.java": 'class App { int answer = 42; }\n',
            "App.kt": 'val answer = 42\n',
            "main.go": 'package main\nfunc main() { println("hello") }\n',
            "main.rs": 'fn main() { let answer = 42; }\n',
            "main.c": 'int main() { return 0; }\n',
            "query.sql": 'SELECT name FROM users WHERE id = 1;\n',
            "data.json": '{"name": "hello", "count": 42}\n',
            "config.yaml": 'name: hello\ncount: 42\n',
            "config.toml": '[config]\ncount = 42\n',
            "config.ini": '[config]\ncount = 42\n',
            "index.html": '<div class="hello">World</div>\n',
            "config.xml": '<config value="hello"/>\n',
            "style.css": 'body { color: red; }\n',
            "build.sh": '#!/bin/sh\necho "hello"\n',
            "Dockerfile": 'FROM python:3.12\nRUN echo "hello"\n',
            "Makefile": 'all:\n\techo "hello"\n',
        }
        for name, text in examples.items():
            with self.subTest(name=name):
                result = syntax_preview.render(text, name)
                self.assertIsNotNone(result)
                language, lines = result
                self.assertTrue(language)
                self.assertEqual(plain(lines), text.expandtabs(4).splitlines())
                self.assertGreater(len({span.style.foreground for line in lines for span in line}), 1)

    def test_line_numbers_whitespace_unicode_and_long_lines_preserved(self):
        text = '\n\ndef hello():\n\tprint("한글")\n\nvalue = "' + "x" * 400 + '"\n\n'
        _, lines = syntax_preview.render(text, "hello.py")
        self.assertEqual(plain(lines), text.expandtabs(4).splitlines())
        self.assertGreater(len(plain(lines)[-2]), 400)
        _, lines = syntax_preview.render("a = 1", "hello.py")
        self.assertEqual(plain(lines), ["a = 1"])

    def test_unknown_empty_and_plain_text_use_unstyled_fallback(self):
        for name, text in (("README.txt", "hello"), ("file.unrecognized-nav-test", "x = 42"), ("empty.py", "")):
            self.assertIsNone(syntax_preview.render(text, name))

    def test_theme_applies_to_keyword_string_comment_and_numbers(self):
        source = 'def hello():\n    # note\n    return "world", 42\n'
        for name in ("catppuccin", "catppuccin-latte"):
            palette = resolve({"theme": {"name": name}})
            _, lines = syntax_preview.render(source, "hello.py", palette)
            spans = [span for line in lines for span in line]
            for text, token in (("def", "mauve"), ("hello", "blue"), ("world", "green"), ("# note", "subtext0"), ("42", "peach")):
                self.assertTrue(any(text in span.text and span.style.foreground == palette[token] for span in spans))

    def test_control_sequences_removed_and_no_external_command(self):
        with patch("subprocess.run", side_effect=AssertionError("external command")):
            _, lines = syntax_preview.render('x = "\x1b]52;c;hidden\x07hello\x1b[2J"\n', "file.py")
        self.assertEqual(plain(lines), ['x = "hello"'])

    def test_token_limit(self):
        with patch.object(syntax_preview, "MAX_TOKENS", 1):
            with self.assertRaisesRegex(ValueError, "token limit"):
                syntax_preview.render("x = 42", "file.py")


class NavigatorSyntaxTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / "code.py").write_text('def hello():\n    return "world"\n')
        self.nav = Navigator(self.root, "pane", False, "")

    def test_preview_dispatch_and_cache_invalidation(self):
        self.nav.load("code.py")
        with patch("syntax_preview.render", wraps=syntax_preview.render) as render:
            self.nav.prepare_preview(60)
            self.nav.prepare_preview(60)
            render.assert_called_once()
            self.assertEqual(self.nav.language, "Python")
            self.assertIsNone(self.nav.rendered)
            self.assertIsNotNone(self.nav.syntax)
            self.assertEqual(self.nav.content, ['def hello():', '    return "world"'])
            self.nav.theme_config = {"theme": {"name": "catppuccin-latte"}}
            self.nav.update_theme()
            self.nav.prepare_preview(60)
            self.assertEqual(render.call_count, 2)
            (self.root / "code.py").write_text("value = 123\n")
            self.nav.refresh()
            self.nav.prepare_preview(60)
            self.assertEqual(self.nav.content, ["value = 123"])

    def test_failure_falls_back_and_read_errors_do_not_highlight_old_content(self):
        self.nav.load("code.py")
        with patch("syntax_preview.render", side_effect=ImportError("Pygments")) as render:
            self.nav.prepare_preview(60)
            self.nav.prepare_preview(60)
            render.assert_called_once()
        self.assertIsNone(self.nav.syntax)
        self.assertIn("def hello():", self.nav.content)
        self.nav.load("missing.py")
        with patch("syntax_preview.render") as render:
            self.nav.prepare_preview(60)
            render.assert_not_called()
        self.assertFalse(self.nav.previewable)

    def test_markdown_dispatch_does_not_use_source_highlighter(self):
        (self.root / "readme.md").write_text("# Title\n")
        self.nav.refresh()
        self.nav.load("readme.md")
        with patch("syntax_preview.render") as highlight:
            self.nav.prepare_preview(60)
            highlight.assert_not_called()
        self.assertIsNotNone(self.nav.rendered)
        self.assertIsNone(self.nav.syntax)

    def test_code_draw_keeps_line_numbers_and_horizontal_clipping(self):
        self.nav.load("code.py")
        self.nav.prepare_preview(60)
        screen = Mock()
        screen.getmaxyx.return_value = (40, 120)
        with patch.object(self.nav, "span_style", return_value=0):
            self.nav.draw_content(screen, 0, 80, 30)
            self.assertTrue(any("1 │" in call.args[2] for call in screen.addstr.call_args_list))
            screen.reset_mock()
            self.nav.horizontal = 2
            self.nav.draw_styled_line(screen, 8, 8, 8, [Span("한글abc", Style())])
            self.assertEqual(screen.addstr.call_args.args[2], "글abc")
