# Jira Text Formatting Notation (wiki markup)

Source: <https://issues.apache.org/jira/secure/WikiRendererHelpAction.jspa?section=all>
(canonical `WikiRendererHelpAction.jspa` reference page served by every Jira
Server / Data Center instance; `jira.atlassian.com` and the
`confluence.atlassian.com` mirrors of the same page are login-walled)

Fetched: 2026-08-21

Local path: `wiki/ref/jira-wiki-markup-notation.md`

## Headings

`h1.` through `h6.` at the start of a line.

## Text effects

| Notation | Renders as |
|---|---|
| `*strong*` | bold |
| `_emphasis_` | italic |
| `??citation??` | citation |
| `-deleted-` | strikethrough |
| `+inserted+` | inserted (underline) |
| `^superscript^` | superscript |
| `~subscript~` | subscript |
| `{{monospaced}}` | monospaced |
| `bq. text` | block quote (single paragraph) |
| `{quote}...{quote}` | block quote (multi-paragraph) |
| `{color:red}...{color}` | colored text |

## Text breaks

- Empty line — paragraph break
- `\\` — forced line break
- `----` — horizontal rule
- `---` — em dash, `--` — en dash

## Links

- `[URL]`, `[text|URL]` — external link
- `[#anchor]` — link to an anchor on the same page
- `{anchor:name}` — define an anchor
- `[^attachment.ext]` — attachment link
- `[mailto:someone@example.com]` — mail link
- `[file:///path/to/file]` — file link
- `[~username]` — user profile link

## Lists

- `* item` — bulleted (nest deeper with `**`, `***`)
- `- item` — alternative bullet
- `# item` — numbered (nest deeper with `##`, `###`)
- Mixed nesting: `#*`, `*#`

## Images and attachments

- `!URL!` / `!filename!` — embed image
- `!image.jpg|thumbnail!` — thumbnail
- `!image.gif|align=right, vspace=4!` — with attributes
- `!file.ext|width=300,height=400!` — embedded media

## Tables

- `||heading||heading||` — header row
- `|cell|cell|` — data row

## Advanced formatting

- `{noformat}...{noformat}` — preformatted, no highlighting
- `{panel}...{panel}` — panel box
- `{panel:title=Name|borderStyle=solid|bgColor=#FFF}...{panel}` — styled panel
- `{code}...{code}` / `{code:java}...{code}` — code block with optional language

## Miscellaneous

- `\X` — escape the character X
- Emoticons: `:)` `:(` `:P` `:D` `;)` `(y)` `(n)` `(i)` `(/)` `(x)` `(!)`
  `(+)` `(-)` `(?)` `(on)` `(off)` `(*)` `(*r)` `(*g)` `(*b)` `(*y)`
  `(flag)` `(flagoff)`
- `(/)` renders as a check mark; `(x)` renders as a cross. (Confirmed against
  the same page; the notation table lists the codes without their glyphs.)

## Notes for SpecTrack

There is **no** wiki-markup notation for:

- Markdown ATX headings (`## Heading`) — renders literally
- Markdown task lists (`- [ ] item`) — renders literally
- Backtick inline code or fenced code blocks (`` `x` ``, ```` ``` ````) —
  render literally
- Markdown links (`[label](url)`) — renders literally

Hazard: `-text-` is strikethrough, so hyphens at the outside edges of a word
(`-max-tries-`, a bare `->`) can strike through unintentionally. `{{...}}` is a
styling span, not a raw block, and does not suppress it — use
`{noformat}`/`{code}` or escape as `\-`.

The page documents `-deleted-` as "Makes text as deleted" and states **no**
whitespace or word-boundary rule for the delimiters, so whether an intra-word
hyphen pair (`retry-loop back-off`) can trigger it is not documented. Verified
by fetching the page 2026-08-21.
