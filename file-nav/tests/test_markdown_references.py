from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import markdown_preview as md


class MarkdownReferenceTests(unittest.TestCase):
    def lines(self, source, width=120):
        return ["".join(span.text for span in line).rstrip()
                for line in md.render(source, width)]

    def test_adjacent_wiki_references_start_separate_lines(self):
        source = "## References\n\n" + "\n".join(
            f"[^{i}]: [[Docs/page-{i}]] — reference {i}" for i in range(1, 10))
        for width in (35, 80, 160):
            with self.subTest(width=width):
                lines = self.lines(source, width)
                for i in range(1, 10):
                    self.assertEqual(sum(line.startswith(f"[^{i}]:") for line in lines), 1)
                self.assertTrue(all(line.count("[^") <= 1 for line in lines))

    def test_url_footnotes_stay_visible_and_normal_links_still_resolve(self):
        source = ("A note[^a] and [website][site].\n\n"
                  "[^a]: https://example.org/alpha\n"
                  "[^b]: https://example.org/beta\n\n"
                  "[site]: https://example.org/site\n")
        lines = self.lines(source)
        self.assertIn("[^a]: https://example.org/alpha", lines)
        self.assertIn("[^b]: https://example.org/beta", lines)
        self.assertNotIn("[site]:", "\n".join(lines))
        self.assertIn("website", "\n".join(lines))

    def test_ordinary_softbreaks_and_reference_continuations_still_wrap(self):
        lines = self.lines("ordinary\nparagraph\n\n[^a]: first\n    continuation\n[^b]: second")
        self.assertIn("ordinary paragraph", lines)
        self.assertIn("[^a]: first continuation", lines)
        self.assertIn("[^b]: second", lines)

    def test_code_blocks_and_multiline_inline_code_are_untouched(self):
        source = ("```text\n[^a]: literal\n[^b]: literal\n```\n\n"
                  "    [^c]: indented\n    [^d]: indented\n\n"
                  "`literal\n[^e]: inline`\n")
        tokens = md.preview_tokens(source)
        self.assertEqual(next(t.content for t in tokens if t.type == "fence"),
                         "[^a]: literal\n[^b]: literal\n")
        self.assertEqual(next(t.content for t in tokens if t.type == "code_block"),
                         "[^c]: indented\n[^d]: indented\n")
        children = [c for t in tokens for c in (t.children or [])]
        self.assertEqual(next(c.content for c in children if c.type == "code_inline"),
                         "literal [^e]: inline")
        self.assertFalse(any(c.type == "hardbreak" for c in children))

    def test_reference_body_retains_inline_styling(self):
        lines = md.render("[^a]: **bold** and `code`\n[^b]: *italic*", 80)
        spans = [span for line in lines for span in line]
        self.assertTrue(any("bold" in span.text and span.style.bold for span in spans))
        self.assertTrue(any("italic" in span.text and span.style.italic for span in spans))


if __name__ == "__main__":
    unittest.main()
