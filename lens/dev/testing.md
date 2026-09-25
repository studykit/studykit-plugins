# Development and verification

For startup measurements and the repeatable component benchmark, see
[Startup performance](performance.md).

## Repeated overlay actions

Herdr 0.9.1 creates a new overlay for every `plugin pane open` request; it does
not deduplicate by plugin or entrypoint. Actions therefore serialize overlay
lookup and creation with a file lock keyed by host socket path and tab ID.
The record stores the live pane and terminal IDs. A recorded pane must still
have the same terminal and tab before it can be focused. A missing pane permits
a fresh open; other host errors propagate instead of causing a second open.
Do not replace or unlink the lock file: contenders must lock the same inode.

The adapter can also adopt an already-focused navigator from before instance
tracking was installed, using the host's `plugin pane focus` response to check
its plugin ID and entrypoint. It never sends keystrokes into the source pane.
Refocusing preserves the running navigator's view, including its current
project/changes mode, and re-enables zoom. Closed overlays leave harmless stale
records that are validated on the next invocation. Popup launches keep the
host's existing modal behavior.

Validation for 0.17.2: 211 tests passed. A separate Herdr 0.9.1 session, isolated
XDG directories, and a throwaway project reproduced two navigator panes before
the fix and one afterward. Real keyboard input verified repeated shortcuts,
preserved terminal identity and search text, unzooming without duplication,
refocusing from the source pane, and Overlay → Popup → Overlay. Two bursts of
six concurrent action invocations, including one after closing the navigator,
also produced exactly one navigator. All 15 test action invocations succeeded.

Runtime details were checked against the installed API schema and
[Herdr's plugin pane handlers](https://github.com/herdrdev/herdr/blob/v0.9.1/src/app/api/plugins/mod.rs).
The session socket environment contract is defined in
[Herdr's API module](https://github.com/herdrdev/herdr/blob/v0.9.1/src/api/mod.rs).

## General verification

The plugin targets Herdr's terminal pane and popup APIs. It intentionally has no Claude Code
or Codex manifests: neither agent runtime owns this UI, and the navigator works
with either agent inside Herdr.

Run automated checks from the repository root:

```sh
uv run --no-config --no-project --with rich==15.0.0 python -m unittest discover -s lens/tests -v
```

For local development, register the working tree:

```sh
herdr plugin link /absolute/path/to/lens
```

Use a throwaway project with tracked, staged, unstaged, deleted, and untracked
files. Launch a separate named Herdr test session or a separate test pane so the
source agent is not affected. Invoking the action through Herdr is required to
verify manifest execution and injected context; running the Python entrypoint
with synthetic environment variables only verifies the adapter.

Verify both actions, the root displayed in the header, filename searches into
collapsed directories, click/Enter previews, Ctrl+D vimdiff and `q` return, Ctrl+E editor return,
refresh after edits, scrolling, terminal resize, Escape, and focus restoration.
Repeat from a nested directory and another source pane. Confirm that the original
pane receives no command input, except a comment message the user submits. Test a linked working tree rather than an older
installed checkout.

The adapter talks to Herdr through the socket API (`HERDR_SOCKET_PATH`), one
newline-delimited JSON request per call, instead of spawning the `herdr` CLI.
Herdr 0.9.1's CLI rejected an explicit `--placement popup` override, so popup
launches use the dedicated popup manifest entrypoint. Overlay launches use the
native overlay manifest entrypoint.

Left and right halves cover the whole tab. Herdr splits only single panes, and
`layout.apply` recreates panes without their processes, so a half parks every
pane but the first in a temporary tab, splits the first, and moves the others
back following the `layout.export` tree. Moves fail in a zoomed tab, so zoom is
turned off first. Live-check a tab with nested splits: the ratios must match
before opening and after closing. The overlay placement opens beside the
*focused* pane, so focus the test tab before driving it from another pane.
Popups do not have pane IDs or receive `HERDR_PANE_ID`; the action forwards the
source pane ID explicitly. Direct pane entrypoints use the focused pane in the
plugin context. The source folder remains fixed during a popup invocation.

Pane commands use an executable script relative to the plugin root. Passing a
relative Python filename as an interpreter argument fails when the pane opens
with the project's working directory. Preserve the executable bit when packaging.

## Verified behavior

On Herdr 0.9.1, a separate named session with a temporary Git project verified
both manifest actions, the injected source pane and foreground directory,
filename search followed by Enter, diff opening, an actual mouse click,
editor launch and return, resizing from a single panel to two panels, and Escape
restoring the source shell. Reopening after changing the source shell into a
subdirectory showed only that subdirectory's files. The source shell received
no navigator input. Linux has not been exercised in a live host session.

For 0.2, both configured shortcuts were exercised through the real Herdr client.
The updated popup displayed the focus badge, active panel borders, and headers;
Tab moved focus back to files after a file preview. Ctrl+D opened two Vim diff
windows for a modified file, and Enter from the changes action compared an
untracked file against an empty HEAD buffer. `q` returned to the navigator.
The automated suite also starts the installed Vim in Ex mode and checks that
both windows are vertical, in diff mode, read-only, and non-modifiable.

For 0.3, the real popup was resized from 96% × 92% to 85% × 80% while a searched
file was open. The reopened popup retained the query, file, and content focus.
A subsequent fresh launch loaded 85% × 80%, and the Large preset restored
96% × 92%. Unit coverage also checks scroll restoration, cancellation, bounds,
malformed preferences, modal-release retry, and focus-change cancellation.

## Popup resizing

Herdr 0.9.1 exposes dimensions at popup launch but no popup resize method.
Ctrl+Y prepares a size change; Enter saves a one-use resume record under the
plugin state directory and starts a detached helper before the popup exits.
The helper waits up to five seconds for Herdr to release the old modal, opens
the new popup, and saves `popup-size.json` under the plugin config directory.
The new popup consumes and removes the resume record. Search, expanded folders,
selection, preview position, and focus are restored; scroll positions clamp to
the newly available viewport. Focus moving to a different source pane cancels
the reopen. Helper errors are written to `resize.log` in the plugin state
directory. Resizing does not modify the shared manifest or Herdr keybindings.

For 0.4, a real Herdr 0.9.1 popup verified that ordinary typing leaves the filter
unchanged, Ctrl+S enters search even with a Ctrl+S host prefix, Enter applies the
filter, and Escape cancels edits without closing the popup. A long Markdown
fixture rendered through installed Glow 3.0.0; wheel-down moved its rendered-line
position from 1 to 4 and wheel-up returned it to 1. Arrow scrolling also worked.
Opening vimdiff and returning with `q` preserved both search and mouse handling.

Mouse reports are decoded directly with keypad translation disabled, avoiding
the missing fifth-button constant in older macOS ncurses builds. The UI enables
SGR mouse reporting and raw input so Ctrl+S reaches the application instead of
triggering terminal flow control. It releases these modes for external editors
and reinstates them on return.

Starting in 0.5, Rich replaces the external Glow process. The executable adapter
declares Rich through inline script metadata and runs under uv, with project
configuration disabled. This keeps dependencies independent of the invoking
project and the system Python. The resize helper reuses that environment's
interpreter. Rendering takes bounded source text, removes file-supplied terminal
controls, and captures Rich's styled output in memory with an 8 MiB output limit.
Only sanitized text/style spans reach curses. Render results are cached for the
loaded file and panel width; renderer errors fall back to source text. No renderer
subprocess or remote-document fetch is used.

For 0.5, a separate Herdr 0.9.1 session launched the uv-backed adapter through
`prefix+t`. The content panel reported `MARKDOWN · Rich`, rendered the Markdown
fixture, and scrolled from position 1 to 4 and back with the wheel. Resizing to
85% × 80% and back to 96% × 92% retained the file and rendered it at each width.
The 50-test suite includes real Rich rendering of tables, highlighted code,
Korean text, narrow wrapping, terminal-control filtering, output limits, and
fallback behavior without invoking an external renderer.

## Theme integration and preview keys

Herdr 0.9.1 does not expose its effective palette in the plugin context or socket
schema. The adapter reads the configured `HERDR_CONFIG_PATH`, otherwise
`XDG_CONFIG_HOME/herdr/config.toml` or the usual user config location. Shared UI
code receives a loader and normalized theme data, not host environment variables.
Settings are reread on launch and Ctrl+R. Built-in colors, aliases, custom token
overrides, legacy UI accents, and appearance-specific override precedence follow
Herdr 0.9.1. The popup queries host appearance with CSI ? 996 n; CSI ? 997 replies
select the light/dark palette for auto-switch configurations. Without a reply,
the same dark fallback as Herdr applies. RGB colors map to the nearest xterm-256
color; terminal defaults remain unset. Focus borders still distinguish panels
when the terminal palette has little color contrast.

The palette data in `herdr_palettes.json` is adapted from the Herdr project's
`src/app/state.rs` at tag `v0.9.1`, licensed under Apache-2.0. Its license is
included in `licenses/Herdr-Apache-2.0.txt`. This is an extracted data table, not
an unmodified source file. Reference:
https://github.com/herdrdev/herdr/blob/v0.9.1/src/app/state.rs

Preview-only pager keys are dispatched after search/mouse input and before
ordinary navigation. Resize and search modes take priority; Ctrl+D and Ctrl+E
keep their existing actions. Tests cover line/page/half-page steps, clamping,
rendered Markdown line counts, modal priority, and theme resolution.

For 0.6, separate Herdr sessions verified both the user's Catppuccin setup and a
temporary Catppuccin Latte configuration without changing the user's config.
Captured terminal attributes showed the corresponding dark/light background,
text, accent, and Markdown syntax colors. The long rendered preview responded
to `j`, `d`, `u`, `G`, `g`, Space, and `b` with the expected viewport positions.
The 63-test suite covers all 18 built-in palettes, aliases, custom colors,
auto-switch resolution, default terminal colors, and preview-only pager keys.

For 0.7, the 68-test suite verifies tree-only `h/j/k/l` navigation, selecting the
first child of an expanded folder, moving to the parent, cursor bounds, and
Space preview without invoking vimdiff in either browse mode. It also checks
that search/resize modes retain priority and that Space still pages down once
preview has focus. These additions were verified with automated UI-state tests;
the 0.7 key sequence has not yet been exercised in a live Herdr popup.

## Ignored-file visibility

Version 0.11.0 adds Ctrl+V to include Git-ignored files in the project tree and
search. Git status remains scoped to the current repository, so ignored files
are not classified as changes. Inclusion uses bounded breadth-first filesystem
traversal, preserving sibling source directories before descending deeply into
caches. Metadata directories and worktree `.git` files remain excluded; directory
symlinks are not followed. Explicit directory records keep empty folders visible.

The toggle defaults off, is preserved through root changes, refresh, and resize,
and switches to project mode when enabled. A failed scan leaves the old state
intact; hiding an excluded file clears its preview. The 119-test suite covers
these state transitions, nested repositories, filesystem limits, symlink safety,
modal priority, search, and final header output. Read-only validation on the
reported knowledge base confirmed its previously hidden source directory, nine
immediate subdirectories, and source files are included. That large tree reaches
the 50,000-entry limit; changing roots narrows the scan. No new live Herdr session
was used for this change.

Reference: https://git-scm.com/docs/git-ls-files

## Directory colors from ls

Version 0.10.0 resolves ordinary-directory styling from explicit environment
inputs at the adapter boundary. GNU `LS_COLORS` `di` settings take priority over
the BSD `LSCOLORS` directory pair. Defaults match blue BSD directories and bold
blue GNU directories. The UI retains Herdr selection styling and uses its panel
background unless the directory style specifies a background. Malformed values
fall back to theme text; raw escape sequences are never emitted.

The 108-test suite covers default palettes, BSD pairs, GNU SGR colors and resets,
invalid input, adapter forwarding, and curses color-pair selection. A read-only
check of native macOS `ls -G` output confirmed ANSI foreground 34 for the ordinary
directory fixture. This change was not exercised in a new live Herdr popup.

References:

- https://man.freebsd.org/cgi/man.cgi?query=ls&sektion=1
- https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html

## Preview without focus transfer

Version 0.9.1 keeps tree focus when Space previews a selected file. Enter and
mouse activation still focus content. The regression tests cover repeated Space,
continued tree navigation with `j`, previewing the next file, changes-only mode
without invoking vimdiff, and Tab followed by Space paging through the preview.

Version 0.9.2 adds Nerd Font folder icons alongside expansion arrows, with distinct closed,
open, and parent-folder markers. Drawing tests cover Unicode folder names and
ensure files, including search results containing directory paths, do not gain
folder icons.

Version 0.9.3 preserves private-use Unicode characters in terminal text cleanup.
Python's `isprintable()` excludes category Co, which silently replaced Nerd Font
glyphs with spaces. Regression coverage now checks the final `screen.addstr`
arguments, not just labels passed to drawing helpers, while ensuring escape,
NUL, and bidi controls remain filtered.

## Navigation root changes

Version 0.9 adds a synthetic `..` tree entry, parent navigation, a Ctrl+O path
dialog, and `t` Git-root navigation. Parent entries never participate in file
search, previews, editing, or diff snapshots. A root switch validates and scans
the destination before replacing the current index; failures preserve the old
view. Successful changes clear root-relative view state and reselect the previous
folder when moving up. The source pane and process working directory are unchanged.
Resize state already carries the selected navigation root.

The 97-test suite covers relative, absolute, home-expanded, Unicode, spaced,
symlink, empty, invalid, and unreadable destinations; repository transitions;
modal priority; path editing; parent selection; search exclusion; and resize
restoration. Existing file-selection tests explicitly account for the new parent
row. A throwaway Herdr session verified Enter and mouse activation of `..`, the
root dialog, selected-folder entry, Git-root navigation, previewing a file in a
second root, and cancelling an invalid destination without losing the old view.

## Root-specific saved views

Version 0.14 stores one versioned JSON view per canonical root under the plugin's
runtime state directory. The adapter resolves `HERDR_PLUGIN_STATE_DIR`; shared
storage and UI code receive paths/callbacks, never host environment variables.
SHA-256 filenames isolate roots and avoid embedding project paths in filenames.
Writes use mode-0600 temporary files and atomic replacement. Reads and writes
are bounded at 4 MiB, and schema/path validation rejects malformed views. No
project files or preview contents are stored. Without a state directory, the
navigator remains usable without persistence.

The UI checkpoints changed views before waiting for input, before leaving a
root, and on exit. This retains the last displayed state even when the host
terminates the popup without running exit handlers; identical snapshots do not
cause repeated writes. Save errors are reported without terminating navigation.
Normal launches load only the invoking root's state, while one-shot resize
snapshots take precedence. The explicit changes action overrides saved browse
mode. Deleted/unreadable previews are cleared, stale expanded folders are pruned,
and offsets are clamped after the first render, not against Markdown source-line
counts. Search-entry and unfinished modal state are intentionally transient.

The 164-test suite includes 19 persistence regressions covering atomic/private
writes, root isolation, symlink aliases, bounded/corrupt/schema-invalid snapshots,
write failures, full restoration across panes, filters, deleted/changed files,
rendered Markdown offsets, checkpoint deduplication, root departure, the input
loop, adapter close/reopen, explicit changes, resize precedence, and exceptional
exit. Tests use throwaway directories. Adapter tests stub the host/curses boundary;
they do not claim a fresh live Herdr popup integration test.

Official runtime contract checked:
https://github.com/herdrdev/herdr/blob/master/docs/next/website/src/content/docs/plugins.mdx

## Focus-preserving preview scrolling

Version 0.13 adds Ctrl+N/P (one line) and Ctrl+F/B (one screen) for scrolling the
current preview from either panel without changing keyboard focus, tree position,
or the active file. Search and root/size dialogs retain input priority. Ordinary
tree navigation and content-focused pager keys keep their existing behavior.

Mouse-wheel routing now uses pointer location without assigning keyboard focus
or leaving search mode. In narrow layouts it targets the currently visible panel.
Clicks still transfer focus, and root/size dialogs ignore wheel input.

The 145-test suite passes, including seven new tests for shared scrolling keys,
rendered-line bounds, input modes, pointer routing with either focus, search/dialog
isolation, narrow layouts, and click behavior. The existing raw-mouse regression
now asserts that preview wheel scrolling leaves tree focus unchanged. These are
automated navigator checks; no new live Herdr popup session was run.

## Obsidian-style Markdown previews

Version 0.12 retains Python, Rich, Pygments, and the existing preview interface.
The parser extension works on Markdown tokens, not whole-document substitutions:
wiki links run before ordinary links/images, highlights use delimiter balancing,
and callouts are recognized from blockquote tokens before inline parsing. This
keeps code, escape sequences, tables, and reference definitions independent.
Rich element and inline-style maps are subclassed rather than mutated globally.

Callouts render as theme-colored panels; all foldable bodies stay expanded.
Frontmatter is highlighted as YAML without deserializing it. Embeds retain a
visible target label without resolving files or fetching URLs. (Version 0.22
resolves note and image embeds; see below.) The extension
does not introduce dependencies, change host adapters, or alter keybindings.
The plugin remains Herdr-only, so no Claude/Codex marketplace registration is
added. The root catalog describes the new user-facing preview support.

The 138-test suite includes 19 new parser, renderer, and navigator regressions:
aliases, headings/block links, embed isolation, literal/escaped code, balanced
highlights, nested/custom/title-only callouts, tasks, frontmatter boundaries,
table aliases and line breaks, light/dark themes, Unicode wrapping, control
sequence removal, output limits, no global Rich mutation, and preview cache/
fallback behavior. Existing search, focus, mouse, root navigation, and reference
tests still pass.

A read-only rendering check of the previously reported KB overview confirmed
all 32 reference definitions remain on separate lines at widths 35, 80, 120,
and 160 in both Catppuccin dark and light themes. Text output for a combined
fixture was inspected at widths 35 and 80. These are renderer and navigator
checks, not a new live Herdr popup session.

References checked for this change:

- https://help.obsidian.md/obsidian-flavored-markdown
- https://help.obsidian.md/callouts
- https://help.obsidian.md/links
- https://help.obsidian.md/syntax
- https://markdown-it-py.readthedocs.io/en/latest/architecture.html
- https://rich.readthedocs.io/en/stable/markdown.html

## Obsidian embeds

Version 0.22 reverses the placeholder-only rule for `![[...]]`. An embed alone in its
paragraph is resolved inside the vault — the nearest ancestor holding `.obsidian`,
else the browsed root — by path from the note, then from the vault root, then by
filename anywhere, nearest the root first, as Obsidian's shortest-path links do. A
resolved path must stay inside the vault after symlinks, so `../` cannot read
beyond it. Hidden folders (including `.trash`) are not searched.

Notes are parsed with the same token pipeline and wrapped in `obsidian_note_*`
tokens that Rich draws as a titled panel; a note embedding itself stops at the
repeat, and depth is capped. Heading sections honor fences; `#^id` takes the
paragraph or list item ending in the ID, or the block above an ID on its own
line (which Obsidian separates with a blank line). Block ID markers are hidden
everywhere, as in the reading view.

Images reuse the diagram pipeline as the `image` pseudo-language: the key holds
the path, the `|W` or `|WxH` size and the mtime, so an edited image re-renders.
Only PNG reaches Kitty graphics, so other formats are converted with
`rsvg-convert`, `sips` or ImageMagick. An image inside an embedded note replaces
its panel row, so the panel's side border is missing beside the picture.

Wiki links and relative Markdown links resolve the same way, per note while its
folder is known, and travel to the UI as `lens-file:` span links (Rich emits them
as OSC 8, which parse_ansi keeps instead of forwarding). Following one calls
`open_file`; the `#heading` or `#^block` is located on the next render by
matching rendered lines, so a heading near the end scrolls only as far as the
last page allows.

A live check ran Lens from a separate Herdr 0.9.1 pane on a throwaway vault:
whole notes, heading sections, block and list IDs, a recursive embed, inline and
missing placeholders rendered as expected, and the image embed reserved its rows.

## Footnote reference layout

Version 0.8.1 preserves visible footnote definitions at their source location.
Rich does not render footnotes natively, so the preview parser excludes footnote
labels from ordinary link-definition parsing and converts soft breaks before
definitions into hard breaks. This avoids both merged wiki-link references and
hidden URL-only definitions. Ordinary paragraphs, reference-style links, fenced
and indented code, and inline code retain their existing behavior.

The 83-test suite includes five reference-layout regressions. A read-only check
of the reported document confirmed that all 32 definitions start on separate
rendered lines at widths 35, 80, 120, and 160. This patch was checked through the
preview renderer, not a new live popup session.

Parser API reference: https://markdown-it-py.readthedocs.io/en/latest/using.html

## Source syntax previews

Version 0.8 dispatches Markdown to Rich and other text files to Pygments filename
matching. The highlighter consumes the same already-bounded preview text instead
of reopening a path, preserving the existing symlink/binary/size checks. It never
loads a lexer from project files or executes the source. Tabs expand before
tokenization; control sequences are removed, and styled spans retain source
line boundaries without wrapping. Token styles are shared with Markdown code
blocks and come from the current Herdr palette. Unknown lexers, missing
dependencies, renderer errors, and the 100,000-token limit fall back to source.

The 78-test suite covers 20 common extensions and special filenames, source-line
preservation, Unicode/tab alignment, long lines and horizontal clipping, language
labels, theme changes, stale-content prevention after read errors, and cache
invalidation on refresh.

An isolated Herdr session verified Python and JSON syntax previews with distinct
token colors, source line numbers, Unicode content, and language labels. Switching
between those files, Rich Markdown, and plain text cleared the previous renderer's
state correctly. Ctrl+S search followed by Enter and Space opened each preview and
transferred focus to content. The Python fixture contained a deliberate exception;
it appeared as source without being executed. Version 0.8.0 was linked after this
live check.

References:

- https://pygments.org/docs/api/#pygments.lexers.get_lexer_for_filename
- https://rich.readthedocs.io/en/stable/syntax.html

Official references checked during implementation:

- https://herdr.dev/docs/plugins/
- https://herdr.dev/docs/cli-reference/
- https://herdr.dev/docs/marketplace/
- https://code.claude.com/docs/en/plugins-reference
- https://developers.openai.com/codex/plugins
- https://vimhelp.org/diff.txt.html
- https://vimhelp.org/starting.txt.html
- https://github.com/charmbracelet/glow
- https://rich.readthedocs.io/en/stable/markdown.html
- https://rich.readthedocs.io/en/stable/console.html
- https://docs.astral.sh/uv/guides/scripts/
- https://invisible-island.net/xterm/ctlseqs/ctlseqs.html

The 0.2 UI uses a fixed dark palette, distinct active/inactive panel headers,
double/single borders, and a global focus badge. File activation transfers focus
to content. Mouse release events must not transfer it back to the source row.
Diff rendering belongs to Vim; the navigator prepares disposable byte snapshots
and suspends curses for the lifetime of that child. The bundled Vim configuration
does not depend on a user vimrc and uses broadly supported `diffopt` values.

Herdr discovery uses `herdr-plugin.toml` in the public repository and the
repository's `herdr-plugin` GitHub topic. Publishing or modifying repository
topics is a separate release operation.


## 0.16: popup and overlay modes

Ctrl+W opens a two-mode chooser: 1 Popup, 2 Overlay. Both are native Herdr
surfaces, selected through separate manifest entrypoints. The plugin has no
split mode, pane-zoom controls, or split target/direction overrides. The host
restores the previous focus and zoom state when its native overlay closes.

Mode transitions reuse the one-use resume mechanism used by popup resizing.
Wait for the old Python process and any old overlay pane to disappear before
opening the replacement. Remove `HERDR_PANE_ID` from the helper environment:
it names the navigator that is closing. The focus guard cancels transitions if
the user moves to another source.

Save the last successfully selected mode atomically in the plugin config
`layout.json`. Both actions load it. Missing, invalid, or legacy `split`
preferences fall back to Popup. Popup dimensions remain in `popup-size.json`.
Ctrl+Y opens the popup-size dialog. Slash is the only search-entry shortcut; Ctrl+S is no longer bound. In search
input, slash remains an ordinary path separator.

The ignored-file visibility shortcut is Ctrl+H instead of Ctrl+V; its scan,
filter, and saved-view behavior are unchanged. Ctrl+H is the ASCII Backspace byte,
so normal navigation handles it before parent-root navigation. DEL and
`KEY_BACKSPACE` retain parent-root behavior; search and path input still accept
Ctrl+H for deleting text.

The input loop reconciles curses dimensions with the PTY and uses a short input
timeout so an early resize during initialization can recover without a keystroke.

Automated coverage checks both supported modes, legacy preference fallback,
rejected split requests, snapshots across mode changes, process/pane release
ordering, focus-change cancellation, unchanged preferences after failed opens,
modal input priority, and popup-only sizing.

Official runtime references checked for this change:

- https://herdr.dev/docs/cli-reference/#plugins
- https://github.com/herdrdev/herdr/blob/v0.9.1/src/app/api/plugins/panes.rs
- https://github.com/herdrdev/herdr/blob/v0.9.1/src/cli/pane.rs
- https://code.claude.com/docs/en/plugins
- https://developers.openai.com/codex/plugins

Claude/Codex plugin registration is unchanged: Herdr owns the display surface.

Validation: 184 automated tests passed. A separate Herdr 0.9.1 session on macOS
used isolated XDG directories, a throwaway project, and the linked working tree.
Real client keyboard input verified legacy Split preferences opening Popup,
Popup → Overlay → Popup, both saved modes on fresh launches, unchanged saved
search/preview/scroll state, popup resizing, slash-only search, Ctrl+H visibility,
and restoration of the source layout after overlay closure. Linux was not
exercised in a live host session.

## Comments

Comments reach the target through `agent.prompt` on the socket API, which pastes
the text with the pane's bracketed-paste mode and presses Enter. Live-check a
multi-line message against both Claude Code and Codex: every line must arrive in
one prompt, not as several submissions. Also check that a blocked agent (an
approval prompt showing) makes the send fail and leaves the editor open. Check the
picker's tab, workspace and session scopes with agents in more than one tab.
