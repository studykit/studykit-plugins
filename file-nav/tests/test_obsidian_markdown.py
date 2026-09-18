from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import markdown_preview as md
from theme_colors import resolve
from ui import Navigator


def plain(source, width=80, colors=None):
    return "\n".join("".join(span.text for span in line).rstrip()
                     for line in md.render(source, width, colors))


def inline(source):
    return [child for token in md.preview_tokens(source) for child in (token.children or [])]


class ObsidianTests(unittest.TestCase):
    def test_wikilinks_aliases_headings_blocks_and_unicode(self):
        source = "[[Docs/Page]] [[Page#Heading|별칭]] [[#Local]] [[Page#^block]]"
        result = plain(source)
        for label in ("Docs/Page", "별칭", "#Local", "Page#^block"):
            self.assertIn(label, result)
        self.assertNotIn("[[", result)
        links = [token for token in inline(source) if token.type == "wikilink"]
        self.assertEqual([token.meta["target"] for token in links],
                         ["Docs/Page", "Page#Heading", "#Local", "Page#^block"])
        self.assertEqual(links[1].content, "별칭")

    def test_aliases_are_literal_not_rich_markup_or_markdown(self):
        self.assertIn("**literal**", plain("[[Page|**literal**]]"))
        self.assertIn("[[unfinished", plain("[[unfinished"))
        self.assertIn("[[]]", plain("[[]]"))

    def test_embeds_are_visible_placeholders_without_external_access(self):
        # Warm lazy imports before forbidding file access in the renderer.
        plain("warmup")
        source = "![[../../private.md#Section]] ![[https://example.org/x.png|200]]"
        with patch("builtins.open", side_effect=AssertionError("unexpected file access")), \
                patch("subprocess.run", side_effect=AssertionError("unexpected process")), \
                patch("socket.create_connection", side_effect=AssertionError("unexpected network")):
            result = plain(source, 160)
        self.assertIn("[Embed: ../../private.md#Section]", result)
        self.assertIn("https://example.org/x.png", result)

    def test_code_and_escaped_syntax_remain_literal(self):
        literal = "[[Page|Alias]] ==highlight== ![[image.png]] [!note]"
        for source in (f"`{literal}`", f"```markdown\n{literal}\n```", f"    {literal}\n"):
            with self.subTest(source=source):
                self.assertIn(literal, plain(source, 120))
        result = plain(r"\[\[Page\]\] \=\=highlight\=\=")
        self.assertIn("[[Page]] ==highlight==", result)

    def test_highlights_can_contain_emphasis_links_and_inline_code(self):
        source = "==plain **bold** *italic* [[Page|link]] `code`=="
        palette = resolve()
        spans = [span for line in md.render(source, 120, palette) for span in line]
        for word in ("plain", "bold", "italic", "link"):
            self.assertTrue(any(word in span.text and span.style.background == palette["surface1"]
                                for span in spans), word)
        self.assertTrue(any("italic" in span.text and span.style.italic for span in spans))
        self.assertTrue(any("link" in span.text and span.style.underline for span in spans))
        self.assertIn("code", plain(source))
        self.assertNotIn("==", plain(source))

    def test_unpaired_highlight_delimiters_and_code_markers(self):
        self.assertIn("==unclosed", plain("==unclosed"))
        self.assertIn("===literal===", plain("===literal==="))
        self.assertIn("a== b", plain("a== b"))
        self.assertIn("inside == code", plain("==start `inside == code` finish=="))

    def test_callouts_nested_fold_markers_and_default_titles(self):
        source = ("> [!WARNING]- **Careful**\n> Body\n>\n"
                  "> > [!tip]+\n> > Nested body\n\nOutside")
        result = plain(source)
        for text in ("WARNING · Careful", "Body", "TIP", "Nested body", "Outside"):
            self.assertIn(text, result)
        self.assertNotIn("[!", result)
        self.assertIn("╭", result)
        self.assertEqual(sum(t.type == "callout_open" for t in md.preview_tokens(source)), 2)

    def test_callout_title_only_custom_type_and_following_blocks(self):
        for marker in ("[!note]", "[!custom-type] A title", "[!tip]+", "[!warning]-"):
            with self.subTest(marker=marker):
                result = plain(f"> {marker}\n\nFollowing paragraph\n\n---\n")
                self.assertNotIn("[!", result)
                self.assertIn("Following paragraph", result)
        source = "> [!note]\n> - one\n> - two\n>\n> ```python\n> x = 1\n> ```"
        self.assertIn("one", plain(source))
        self.assertIn("x = 1", plain(source))

    def test_regular_quotes_and_literal_callout_text_are_unchanged(self):
        source = "> Ordinary quote\n\n[!note] not a quote\n\n> text [!tip] not a callout"
        self.assertFalse(any(t.type == "callout_open" for t in md.preview_tokens(source)))
        self.assertIn("[!note] not a quote", plain(source))
        self.assertIn("text [!tip] not a callout", plain(source))

    def test_tasks_in_nested_and_ordered_lists_only(self):
        source = "- [ ] Pending\n  - [x] Done\n\n1. [X] Ordered\n\n[ ] Ordinary\n\n- \\[x] Escaped"
        result = plain(source)
        for text in ("☐ Pending", "☑ Done", "☑ Ordered", "[ ] Ordinary", "[x] Escaped"):
            self.assertIn(text, result)
        self.assertEqual(sum(t.type == "checkbox" for t in inline(source)), 3)

    def test_frontmatter_visible_and_never_interpreted_as_markdown(self):
        for closing in ("---", "..."):
            source = f"---\ntitle: 한글\nalias: '[[literal]]'\nflag: '==raw=='\n{closing}\n\nBody"
            result = plain(source)
            for value in ("Properties", "title: 한글", "[[literal]]", "==raw==", "Body"):
                self.assertIn(value, result)
            self.assertEqual(md.preview_tokens(source)[0].type, "frontmatter")

    def test_frontmatter_only_at_document_start_and_requires_closing(self):
        for source in ("Paragraph\n\n---\nkey: value\n---", "---\nno closing",
                       "> ---\n> key: value\n> ---", "    ---\n    key: value\n    ---"):
            with self.subTest(source=source):
                self.assertNotIn("frontmatter", [t.type for t in md.preview_tokens(source)])
        self.assertIn("no closing", plain("---\nno closing"))

    def test_tables_keep_escaped_wikilink_pipes_and_html_line_breaks(self):
        source = "| Link | Details |\n| --- | --- |\n| [[Page\\|별칭]] | first<br />second<BR>third |"
        result = plain(source)
        self.assertIn("별칭", result)
        self.assertNotIn("[[", result)
        lines = result.splitlines()
        positions = [next(i for i, line in enumerate(lines) if word in line)
                     for word in ("first", "second", "third")]
        self.assertEqual(len(set(positions)), 3)
        self.assertIn("<br>", plain("`<br>`"))

    def test_light_and_dark_theme_styles(self):
        source = "[[Page]] ==highlight==\n\n> [!warning] Caution\n> Body\n\n- [x] done"
        for name in ("catppuccin", "catppuccin-latte"):
            palette = resolve({"theme": {"name": name}})
            spans = [s for line in md.render(source, 80, palette) for s in line]
            for word, color in (("Page", "accent"), ("WARNING", "yellow"), ("☑", "green")):
                self.assertTrue(any(word in s.text and s.style.foreground == palette[color]
                                    for s in spans), (name, word))
            self.assertTrue(any("highlight" in s.text and s.style.background == palette["surface1"]
                                for s in spans))

    def test_unicode_wrap_never_exceeds_panel_width(self):
        from rich.cells import cell_len

        source = "---\ntitle: 한글 속성\n---\n\n> [!note] 제목\n> " + "한글 설명 " * 12
        source += "\n>\n> > [!tip] Nested\n> > " + "내용 " * 12
        for width in (20, 35, 80, 160):
            lines = md.render(source, width)
            self.assertTrue(all(cell_len("".join(s.text for s in line)) <= width for line in lines))

    def test_terminal_controls_are_not_emitted_through_new_elements(self):
        source = "[[Page|safe\x1b]52;c;hidden\x07]]\n\n> [!note] Title\n> \x1b[2Jbody"
        result = plain(source)
        self.assertNotIn("\x1b", result)
        self.assertNotIn("hidden", result)
        self.assertIn("safe", result)
        self.assertIn("body", result)

    def test_bounded_output_still_applies(self):
        with patch.object(md, "MAX_RENDER_BYTES", 40):
            with self.assertRaisesRegex(ValueError, "preview limit"):
                md.render("> [!note] Title\n> Long body " * 10, 80)

    def test_no_global_rich_parser_mutation(self):
        from rich.markdown import Markdown

        before = dict(Markdown.elements), set(Markdown.inlines)
        plain("==highlight==\n\n> [!note] title")
        self.assertEqual(before, (Markdown.elements, Markdown.inlines))


class ObsidianNavigatorTests(unittest.TestCase):
    def test_preview_resize_theme_refresh_and_source_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = "[[Page|별칭]]\n\n> [!tip] Title\n> " + "Body " * 20
            (root / "note.md").write_text(source)
            nav = Navigator(root, "pane", False, "")
            nav.selected = next(i for i, row in enumerate(nav.items) if row.path == "note.md")
            nav.key(" ", None)
            self.assertFalse(nav.preview_focus)
            nav.prepare_preview(80)
            self.assertIsNotNone(nav.rendered)
            self.assertIn("별칭", "\n".join(nav.content))
            wide_count = len(nav.content)
            nav.prepare_preview(30)
            self.assertGreater(len(nav.content), wide_count)
            nav.theme_config = {"theme": {"name": "catppuccin-latte"}}
            nav.update_theme()
            nav.prepare_preview(30)
            self.assertIsNotNone(nav.rendered)
            with patch("obsidian_markdown.markdown_type", side_effect=ImportError("Rich")):
                nav.prepare_preview(40)
            self.assertEqual(nav.content, source.splitlines())
            self.assertIsNone(nav.rendered)


if __name__ == "__main__":
    unittest.main()
