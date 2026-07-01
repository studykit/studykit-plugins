# Vendoring the viewer's frontend libraries

The viewer (`server/static/app.js`, `index.html`) renders Markdown, math, and
PlantUML entirely in the browser. Those libraries are **vendored** under
`server/static/vendor/` instead of loaded from a CDN, so a page load makes no
external network requests. This file documents how the vendored files are
produced and how to refresh them.

Why vendored, not CDN: esm.sh / jsdelivr are single points of failure loaded via
top-level `await import`. If any one fails, the whole `app.js` module aborts
before it creates the `EventSource`, and the viewer silently hangs at
`connecting…`. (A real esm.sh packaging break — `plantuml-encoder@1`'s stub
importing an unversioned `/pako/lib/deflate` that 404s — caused exactly this.)

## What is vendored

Under `server/static/vendor/`:

- `markdown-it.mjs`, `texmath.mjs`, `plantuml-encoder.mjs` — self-contained
  ESM bundles produced with esbuild (`--bundle`), i.e. every transitive
  dependency inlined into one file. Verified self-contained: no `import … from
  "http…"` and no `import … from "/…"` remain in the output.
- `katex/katex.mjs`, `katex/katex.min.css`, `katex/fonts/*.woff2` — copied
  verbatim from the official `katex` npm dist. KaTeX's `katex.mjs` is already a
  self-contained browser ESM, and its CSS references fonts by relative
  `url(fonts/…)`, so the `fonts/` subdir must sit next to the CSS. Only `.woff2`
  is shipped; modern browsers pick it first from the CSS `src` list, so the
  absent `.woff`/`.ttf` variants are never requested (no 404s).

## Source versions (last refresh)

| package | version |
| --- | --- |
| markdown-it | 14.2.0 |
| markdown-it-texmath | 1.0.0 |
| katex | 0.16.47 |
| plantuml-encoder | 1.4.0 |
| esbuild (build tool) | 0.28.1 |

esbuild and npm are **dev-time only** — nothing about the running plugin needs
Node. The server is Python stdlib; the vendored files are plain static assets.

## Rebuild / version-bump procedure

Run in a throwaway directory (not in the repo — no `package.json`/`node_modules`
should be committed):

```bash
mkdir vbuild && cd vbuild
npm init -y
npm install markdown-it@14 markdown-it-texmath@1 katex@0.16 plantuml-encoder@1.4.0 esbuild

# Entry stubs that re-export each package's default:
mkdir -p src out
printf "export { default } from 'markdown-it';\n"          > src/markdown-it.mjs
printf "export { default } from 'markdown-it-texmath';\n"   > src/texmath.mjs
printf "export { default } from 'plantuml-encoder';\n"      > src/plantuml-encoder.mjs

ESB=node_modules/.bin/esbuild
$ESB src/markdown-it.mjs      --bundle --format=esm --minify --outfile=out/markdown-it.mjs
# texmath uses only the runtime `engine` option (app.js passes `engine: katex`),
# so it does not statically import katex; --external:katex keeps it out anyway.
$ESB src/texmath.mjs          --bundle --format=esm --minify --external:katex --outfile=out/texmath.mjs
$ESB src/plantuml-encoder.mjs --bundle --format=esm --minify --outfile=out/plantuml-encoder.mjs

# Sanity check: each bundle must be self-contained (this should print nothing).
grep -oE '(import|export)[^;]*from *"[^"]*"' out/*.mjs | grep -E '"(https?:|/)' && echo "NOT self-contained!" || echo "ok: self-contained"
```

Then copy into the plugin:

```bash
V=<plugin>/server/static/vendor
rm -rf "$V" && mkdir -p "$V/katex/fonts"
cp out/markdown-it.mjs out/texmath.mjs out/plantuml-encoder.mjs "$V/"
cp node_modules/katex/dist/katex.mjs         "$V/katex/katex.mjs"
cp node_modules/katex/dist/katex.min.css     "$V/katex/katex.min.css"
cp node_modules/katex/dist/fonts/*.woff2     "$V/katex/fonts/"
```

Update the version table above whenever you bump a package.

## Gotchas

- **MIME types.** `server.py`'s `CONTENT_TYPES` must map `.mjs` →
  `text/javascript` and `.woff2` → `font/woff2`. A browser refuses to execute an
  ES module served as `application/octet-stream`, which fails as
  `Failed to fetch dynamically imported module` and hangs the viewer. Changing
  `server.py` requires a server restart (unlike static files, which are read
  from disk per request).
- **Import paths.** `app.js` imports the three bundles by local path and KaTeX
  from `/vendor/katex/katex.mjs`; `index.html` links `/vendor/katex/katex.min.css`.
  If you add a renderer/library, vendor it the same way rather than reintroducing
  a CDN URL.
- **Verify after a refresh.** Load the viewer and confirm
  `performance.getEntriesByType("resource")` contains no non-`127.0.0.1` URLs,
  and that Markdown, a `$$…$$` block, and a ```` ```plantuml ```` block all
  render.
