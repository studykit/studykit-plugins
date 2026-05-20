# Python

- When executing Python scripts, use `uv` instead of `python` directly (e.g., `uv run script.py`)
- Use type hints when writing Python programs. Type hints may be omitted for throwaway/one-off scripts.


# Language

- When responding in Korean, use 존댓말 (formal/polite endings like -습니다, -세요, -요). Do not use
반말.

# Verify Before Answering

**CRITICAL — READ THE ACTUAL CODE OR FILES BEFORE ANSWERING ANY FACTUAL QUESTION. THIS IS EXTREMELY
IMPORTANT.**

When asked how something works, what a file or symbol does, why behavior X happens, what is configured
where, or what state the project is in — open the actual files in the current working tree first. Do
not answer from prior conversation context, intuition, training-data familiarity, or pattern-matching
against similar projects.

- Before stating "X does Y," "X lives at Z," "X is configured as W," or "X flows into Y" — grep, Read,
or otherwise verify against the current tree.
- Before tracing any flow, open every hop. Do not skip hops because they "should" work a certain way.
- For external runtimes (Claude Code, Codex, plugin schemas, third-party APIs), fetch current docs
rather than relying on memory — behavior changes.
- If verification is genuinely impossible, say so explicitly and ask. Do NOT fall back to a
plausible-sounding guess.
- This applies even when you "already saw" the file earlier in the session — re-check if any edit or
external change could have shifted state.

Confident-sounding wrong answers are the worst failure mode. The cost of a 2-second grep is far
smaller than the cost of being wrong.