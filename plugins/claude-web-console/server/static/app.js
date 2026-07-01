// claude-web-console viewer.
// Accumulates assistant text deltas per message_id and renders Markdown, with a
// fenced-block renderer registry keyed by the block's info-string.
// Libraries are vendored locally under /vendor (self-contained esbuild bundles;
// see dev/vendor.md) so the viewer never depends on a CDN staying reachable.
import markdownit from "/vendor/markdown-it.mjs";
import texmath from "/vendor/texmath.mjs";
import katex from "/vendor/katex/katex.mjs";
import plantumlEncoder from "/vendor/plantuml-encoder.mjs";

let plantumlServer = "http://127.0.0.1:8478/plantuml";
try {
  const cfg = await (await fetch("/config.json")).json();
  if (cfg.plantumlServer) plantumlServer = cfg.plantumlServer;
} catch (_) {
  /* keep default */
}

const md = markdownit({ html: false, linkify: true, breaks: false }).use(texmath, {
  engine: katex,
  delimiters: "dollars",
  katexOptions: { throwOnError: false },
});

// --- Renderer registry: dispatch fenced blocks by info-string ---------------
const escapeHtml = md.utils.escapeHtml;
const originalFence = md.renderer.rules.fence;

function fallbackFence(token) {
  return `<pre class="code"><code>${escapeHtml(token.content)}</code></pre>`;
}

const RENDERERS = {
  plantuml: renderPlantuml,
  puml: renderPlantuml,
  uml: renderPlantuml,
  math: renderMath,
  latex: renderMath,
  tex: renderMath,
};

function renderPlantuml(token) {
  const encoded = plantumlEncoder.encode(token.content);
  const src = `${plantumlServer}/svg/${encoded}`;
  return (
    `<div class="render plantuml"><img alt="PlantUML diagram" src="${src}" ` +
    `onerror="this.replaceWith(Object.assign(document.createElement('div'),` +
    `{className:'render-error',textContent:'PlantUML engine unavailable'}))"/></div>`
  );
}

function renderMath(token) {
  try {
    const html = katex.renderToString(token.content, {
      displayMode: true,
      throwOnError: false,
    });
    return `<div class="render math">${html}</div>`;
  } catch (_) {
    return `<div class="render-error">Math render error</div>`;
  }
}

md.renderer.rules.fence = (tokens, idx, options, env, self) => {
  const token = tokens[idx];
  const info = (token.info || "").trim().split(/\s+/)[0].toLowerCase();
  const renderer = RENDERERS[info];
  if (renderer) return renderer(token);
  if (originalFence) return originalFence(tokens, idx, options, env, self);
  return fallbackFence(token);
};

// --- Live event stream ------------------------------------------------------
const logEl = document.getElementById("log");
const statusEl = document.getElementById("status");
const messages = new Map(); // message_id -> { text, body }

function bubble(kind, roleText) {
  const el = document.createElement("section");
  el.className = `msg ${kind}`;
  const role = document.createElement("div");
  role.className = "role";
  role.textContent = roleText;
  const body = document.createElement("div");
  body.className = "body";
  el.append(role, body);
  logEl.append(el);
  return body;
}

function renderUser(text) {
  bubble("user", "You").textContent = text;
}

function renderAssistantDelta(ev) {
  const id = ev.message_id || "unknown";
  let m = messages.get(id);
  if (!m) {
    m = { text: "", body: bubble("assistant", "Claude") };
    messages.set(id, m);
  }
  m.text += ev.delta || "";
  m.body.innerHTML = md.render(m.text);
  m.body.scrollIntoView({ block: "end" });
}

const source = new EventSource("/events");
source.onopen = () => {
  statusEl.textContent = "live";
  statusEl.className = "status ok";
};
source.onerror = () => {
  statusEl.textContent = "disconnected";
  statusEl.className = "status err";
};
source.onmessage = (e) => {
  let ev;
  try {
    ev = JSON.parse(e.data);
  } catch (_) {
    return;
  }
  if (ev.type === "user") renderUser(ev.text || "");
  else if (ev.type === "assistant_delta") renderAssistantDelta(ev);
  // ev.type === "turn_end": the final delta already rendered the message; no-op.
};
