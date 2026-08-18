# Obsidian — block identifiers and block links

Source: <https://obsidian.md/help/links> (reached via 301 redirect from
`https://help.obsidian.md/links`). Fetched 2026-08-13.

Saved while guard shipped a per-project Obsidian mark format (removed in v0.28.1).
Kept as an inspectable copy of the syntax for answers read in an Obsidian vault.

## Defining a block identifier

> a blank space followed by a caret (^) and the block identifier at the end of the line

For structured blocks (lists, tables, quotes) the identifier goes on its own line
after the block instead of at the end of a line.

> Block identifiers can only consist of Latin letters, numbers, and dashes.

Example identifier from the docs:

```
^quote-of-the-day
```

## Linking to a block in ANOTHER note

```
[[2023-01-01#^37066d]]
[[2023-01-01#^quote-of-the-day]]
```

## Linking to a block in the SAME note

**Not documented on this page.** The official page gives no filename-omitted example.
Two candidate URLs for a dedicated internal-links page do not exist:

- `https://obsidian.md/help/links/internal-links` → "File links/internal-links.md does not exist."
- `https://obsidian.md/help/links/internal-link` → "Not Found"

The same-note form used by guard is:

```
[[#^abc123]]
```

Authority: **verified by the user in the Obsidian app** (studykit, 2026-08-13), not by
this docs page. The `#` is always present. This is consistent with the cross-note form
— drop the filename, keep `#^id` — but do not cite Obsidian's documentation for it.
