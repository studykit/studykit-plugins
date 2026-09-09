# Frontmatter rationale — the user-level agents

Why each field in `global/agents/*.md` is set the way it is. Contributor notes: nothing here is
loaded at runtime, and none of it is installed.

These definitions land in a directory shared by every project on the machine, which is the one
thing that separates them from a plugin's agents. A field set wrongly here is set wrongly for
work that has nothing to do with the project it was set in.

**`memory:` silently grants Write and Edit, and the host does not scope the grant.** An agent
carrying the field can write outside its own memory directory and nothing refuses it, so the
boundary rests on the agent's body. That is measured and written up in
`../../guard/dev/agent-frontmatter-rationale.md`, which is where the finding was made; it is
repeated here because two of the three definitions below carry the field.

`memory: user` rather than `project` for everything here, and not as a default: these agents are
reached from any repository, so a store under `.claude/agent-memory/` would be a store that
exists in whichever project the agent happened to be dispatched from first.

`think-board`'s frontmatter has no write-up yet.

## The Korean pair

Both were guard's until v0.125.0, and the reasoning below was made there — see
`../../guard/dev/design.md` § "The Korean pair leaves the plugin" for why they moved and
`../README.md` for what they do. The tool lists and the models are unchanged by the move; what
changed is the `memory:` field, the input wording in each body, and — for the translator — the
frame. It was written for developer documentation and is now written for any kind of text, on
the maintainer's call: nothing in the method was specific to documentation, and the field-specific
part (a term of art keeps the form its own field uses) is a rule that generalises rather than one
that had to be dropped.

`color:` is deliberately split — `magenta` for the translator, `red` for the corrector. Both
were `red` at first, which is the one thing that does not survive the pair running back to back
on the same text: the transcript is where you tell which of the two produced what you are
looking at.

They are one step in two halves. The translator ends by naming the corrector, so 직역 that
survives the first has a reader downstream — which is the whole reason the pair exists rather
than one agent that translates and then re-reads its own prose.

### `korean-translator`

`tools: Read, Write, SendMessage`

`Read` for the English source, `Write` for the destination. No `Edit`, which shapes the agent
rather than fencing it: it produces a new file rather than revising one, and the surgical change
— a sentence improved in passing while translating — is the one it has no tool for. It is not a
fence, because `Write` takes any path; what makes the source read-only is the body saying so
twice. The reason either way is that the source is what a later translation would be made from,
and an unreviewed edit would be sitting in it.

`SendMessage` for the one thing it may not decide alone. A sentence it cannot render without
choosing what the author meant is a claim, not a phrasing, so it asks the session that dispatched
it, which holds the English.

No `Grep`, `Glob` or `Bash`: it translates prose and verifies nothing the document asserts.
Handing it the repository would invite exactly the failure the body forbids — noticing a defect
in the English and translating a corrected version of it.

`memory: user`, added with the move and reversing the field's absence in the plugin. The
argument against it is worth keeping, because it is the risk the field now carries: a store
fixes a first-turn word choice for every turn after it, including the ones where it was wrong,
and a translation is the one artifact nobody diffs against its predecessor. What is on the other
side is real too — glossary consistency across documents that have no common source, which is
the case a user-level agent is in and a per-turn plugin agent never was. The body is what keeps
the risk in bounds: what may go in the store is a term and where it was seen used that way,
never a ruling that saves the agent from reading the document in front of it. If the Korean
starts carrying a word this document never used, this field is the first place to look.

`model: sonnet`, set by the maintainer's decision rather than by a head-to-head. The argument for
`opus` still stands on paper and is worth knowing: the cheap failure mode of a weak translator is
not a mistranslation but exactly the 직역 this agent was added to remove, which is fluent,
grammatical, and invisible in review. What makes `sonnet` defensible is that this agent is not
the last word — `korean-corrector` reads what it wrote and is dispatched by its own report. If
직역 starts surviving to the reader, this field is the second place to look.

### `korean-corrector`

`tools: Read, Edit, Write, SendMessage`

`Read` and `Edit` for the file it was handed. Its input is text a reader is about to be shown, so
a correction belongs in that file and not in a second one the reader would have to be talked into
opening. `Write` for the one case `Edit` cannot express — a change too large to write as an
edit, which the body allows and discourages in the same sentence. It judges prose, so it needs
no search or shell access.

`memory: user`, on the same reversal as the translator and carrying more of the risk, because
nothing reads this agent afterwards. A stored ruling that some phrasing is fine would stop a
whole class of finding from ever being raised again, and a pass is indistinguishable from a clean
file — so the body allows the store only a term this project deliberately keeps, and forbids
storing a pass.

`model: sonnet`, changed with `korean-translator` by the maintainer's decision and not measured.
This one is the last judgment made on the Korean, so unnatural prose it cannot hear is a pass it
will report. The same note applies — a head-to-head before changing it back, and this field first
if unnatural Korean starts reaching the reader.
