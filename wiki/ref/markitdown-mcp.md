# markitdown-mcp — the one tool it exposes, and how it is launched

Source: <https://github.com/microsoft/markitdown/blob/main/packages/markitdown-mcp/README.md>
and the registry entry at <https://github.com/mcp/microsoft/markitdown>
Retrieved: 2026-08-23
Local path: `wiki/ref/markitdown-mcp.md`

## The tool surface

> The `markitdown-mcp` package provides a lightweight STDIO, Streamable HTTP, and SSE MCP
> server for calling MarkItDown.
>
> It exposes one tool: `convert_to_markdown(uri)`, where uri can be any `http:`, `https:`,
> `file:`, or `data:` URI.

One tool, one argument. Because it accepts `http:`/`https:` it is a fetch path as well as a
file converter: it retrieves the URI and returns the converted Markdown.

The registry entry describes the scope as "Convert various file formats (PDF, Word, Excel,
images, audio) to Markdown."

## Launch

The registry entry records the distribution, and it is the detail that matters for a plugin:

```json
{"identifier": "markitdown-mcp", "registryType": "pypi", "runtimeHint": "uvx",
 "transport": {"type": "stdio"}, "version": "0.0.1a4"}
```

So `uvx markitdown-mcp` over stdio, from PyPI — no separate install step and no Docker
required. **Version `0.0.1a4` is an alpha**; pin it if anything depends on its behaviour.

The README's own instructions are `pip install markitdown-mcp` then `markitdown-mcp`
(stdio by default), or `markitdown-mcp --http --host 127.0.0.1 --port 3001`. Its Claude Desktop
example uses Docker (`docker run --rm -i markitdown-mcp:latest`) and recommends that image for
that host specifically.

## Security, quoted

> The server does not support authentication, and runs with the privileges of the user running
> it. For this reason, when running in SSE or Streamable HTTP mode, the server binds by default
> to `localhost`. Even still, it is important to recognize that the server can be accessed by
> any process or users on the same local machine, and that the `convert_to_markdown` tool can
> be used to read **any file that the server's user has access to**, or any data from the
> network.

And the package's own framing:

> The MarkItDown-MCP package is meant for **local use**, with local trusted agents.

Two things follow for a design that hands this tool to an agent. `convert_to_markdown` is an
arbitrary-file read that no `tools` allowlist narrows further — an agent granted it can read
anything the user can via a `file:` URI, whatever else its tool list says. And with stdio there
is no listening socket, which is the safer of the two transports for this reason: the HTTP/SSE
modes are reachable by any local process.

## Not covered here

Whether the converted output is truncated or paginated for a very long document, and how it
reports a fetch failure. The README says neither; both would need a live run to establish.
