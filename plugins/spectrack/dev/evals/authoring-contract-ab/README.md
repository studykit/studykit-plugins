# SpecTrack Authoring Contract A/B Eval

Ad-hoc GitHub-only evaluation for comparing issue body drafts created **with**
and **without** resolver-returned authoring contracts. This is intentionally not
part of the pytest suite because it evaluates authoring judgment and prose
quality.

## What it tests

For each case in `cases.yml`, the harness creates two conditions:

- `with_contract` — prompt includes `spectrack mustread --provider github` output
  and the contents of the returned authoring files.
- `no_contract` — prompt includes only the workflow type/provider/mode and the
  user request.

Both conditions ask Codex to output only a GitHub issue body. No issue is
published.

## Generate prompts only

```bash
uv run --with PyYAML plugins/spectrack/dev/evals/authoring-contract-ab/run_eval.py \
  --prompts-only
```

This writes prompts under `results/<timestamp>/...` without calling Codex.

## Run Codex drafting

```bash
uv run --with PyYAML plugins/spectrack/dev/evals/authoring-contract-ab/run_eval.py \
  --run \
  --model gpt-5.1-codex \
  --repeats 3
```

Omit `--model` to use the Codex CLI default. The harness calls:

```bash
codex exec --sandbox read-only --output-last-message <draft.md> -
```

The prompt also tells Codex not to modify files, run commands, or publish issues.

## Judge existing drafts

```bash
uv run --with PyYAML plugins/spectrack/dev/evals/authoring-contract-ab/run_eval.py \
  --judge results/<timestamp> \
  --model gpt-5.1-codex
```

Judging randomizes A/B order per case and writes `judge.md` files beside the
paired drafts. The judge prompt does not reveal which draft used contracts.

## Reading results

Look for where contracts materially improve or worsen:

- artifact fit
- specificity
- useful custom sections
- avoidance of frozen implementation plans
- verification quality
- concision

Use the final judge recommendation to decide which authoring contract text to
keep, shrink, or remove.
