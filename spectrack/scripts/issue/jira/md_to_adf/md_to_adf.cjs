#!/usr/bin/env node
// Reads Markdown on stdin and writes the equivalent ADF document as JSON on
// stdout, using Atlassian's own editor transformers so the result is what the
// Jira editor itself would produce.
const { MarkdownTransformer } = require('@atlaskit/editor-markdown-transformer');
const { JSONTransformer } = require('@atlaskit/editor-json-transformer');
const { defaultSchema } = require('@atlaskit/adf-schema/schema-default');

const chunks = [];
process.stdin.on('data', (chunk) => chunks.push(chunk));
process.stdin.on('end', () => {
  const markdown = Buffer.concat(chunks).toString('utf8');
  const doc = new MarkdownTransformer(defaultSchema).parse(markdown);
  process.stdout.write(JSON.stringify(new JSONTransformer().encode(doc)));
});
