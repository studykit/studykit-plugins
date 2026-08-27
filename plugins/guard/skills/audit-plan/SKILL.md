---
name: audit-plan
# Extremely short — see `audit-turn-claims` for why. The plan gate names this skill in its
# hook output ("Run the `guard:audit-plan` skill over the plan", `cmd_plan_gate.py`) and the
# user types `/guard:audit-plan`, so the line never has to attract an invocation; its one job
# is keeping the model from choosing it. That job is not optional: the description that
# described the review got twelve agents dispatched over a plan nobody had approved
# (measured), and naming the hook would put the trigger back — a model that just left plan
# mode reads `ExitPlanMode` as its cue. `disable-model-invocation: true` would shut guard out
# too.
description: Invoked by guard only.
# The two read-only guard commands this skill runs on every review, pre-approved so the
# review does not open with a permission prompt for guard's own bundled scripts. Both print
# and exit: one lists the project's configured knowledge directories, the other records that
# the audit finished. `${CLAUDE_PLUGIN_ROOT}` substitutes in `allowed-tools` exactly as it
# does in the body (`wiki/ref/claude-code-skill-substitutions.md`), so these match however
# the plugin is installed. The wrappers on PATH are named too: that is how the body invokes
# them, and a rule for the underlying `uv run` line alone would never match.
allowed-tools: Bash(guard-knowledge-dirs), Bash(guard-plan-audited:*), Bash(uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py knowledge-dirs), Bash(uv run --script ${CLAUDE_PLUGIN_ROOT}/scripts/guard_hook.py plan-audited:*)
---

# Audit a plan

**Check that you were held.** Either guard blocked an approved plan and named this skill, or
the user asked for this review directly. Neither in your context — you just wrote a plan, or
are about to show one — means you invoked it by mistake: say so in one line and stop.

The user has approved a plan and you were held before building it. It gets checked first —
the environment it assumes and its premises settled, then the plan itself read by six
independent critics.

That timing is deliberate at both ends. It is not inside plan mode, because the review takes
minutes and holds the turn: run it while the plan is still being shaped and the user cannot
talk to you about the plan they are shaping. And it is not after the work, because a critique
of something already built is a bug report. Approval ended plan mode; it built nothing, so
everything the review finds can still change the plan.

You are the caller. You run the two stages below, weigh what comes back, and revise the plan
yourself. Nothing dispatched here edits anything.

**A dispatched agent's report is delivered to you. You do not go and get it.** When you send
an `Agent` call, its report arrives in your context when the agent finishes — that delivery
is the mechanism, and it needs nothing from you. So after dispatching, **end your turn**.
Say what you dispatched, stop, and the report will be there when you next speak.

This is the one place this skill is most often got wrong, so it is worth naming the wrong
version: dispatching, then checking whether the agent is still running, then sleeping because
it is, then checking again. Every part of that is wasted — listing your subagents tells you
only what you already know, and no amount of sleeping makes a report arrive sooner. Do not
poll, do not list agents to see if one finished, do not run a timer or a marker file, and do
not run any shell command whose purpose is to let time pass. There is also never another
stage you could usefully start early: the stages below are strictly ordered.

**Everything in this review happens in English** — the premise list, every report, every
dispatch you write. It is read by agents, never by the user. Only your final summary above
the plan is in the user's language.

## Inputs

**The plan file is the one you already wrote** — the plan under review is on disk, at the
path you were given when you composed it. Pass that path to every agent below.

Pass the path, never the text. A plan retyped into a dispatch is a plan you have summarised,
and the critics would be reviewing something the user will never see.

Also gather, once, and pass along where the table below says:

- **the user's request** — what actually led to this plan. A transcript path if you have one;
  otherwise their own words, quoted, not your reading of them.
- **the knowledge directories** — run `guard-knowledge-dirs`. One absolute path per line, in
  the user's configured order, which is precedence. It prints nothing when none are
  configured; that is normal. Stage 1 passes these on.

## Stage 1 — what the plan stands on

The plan rests on things it treats as already true: facts about the code, and facts about the
system it runs in. If one of those is false, the critics in stage 2 will be reviewing a plan
that does not exist. So this stage runs **first**, and its results go into stage 2 with the
plan.

**1a. The environment, first.** Dispatch one `guard:design-environment` with the plan file and
the knowledge directories, in order. Dispatch it even when there are none; it has other
sources, and it will ask the user if a gap blocks its verdict.

Its report goes into every dispatch below, so the rest of the review starts once it is back.
It settles what the deployed system actually does, and the checkers verify premises that
often rest on exactly that — a route, a layer, a limit. A checker that does not know the
environment reports UNVERIFIED where this agent had the answer, and the same question gets
chased twice.

Most plans do not touch the environment and this returns one line almost immediately. That is
the normal case, not a wasted step.

It may have **asked the user a question** while it ran. If its report says so, do not ask it
again, and treat what they said as settled — including by the checkers below.

**1b. Enumerate.** Dispatch one `guard:design-premises-lister` with the plan file. It returns
a numbered list of the plan's factual claims. It checks nothing.

If it returns an empty list, skip to stage 2 — carrying 1a's environment report with you.

**1c. Check, three times over.** Dispatch **three** `guard:design-premises-checker` agents in
ONE message, each with the same premise list, the plan file, the knowledge directories, and
**1a's environment report** — an environment fact already settled is not theirs to re-derive.

**One message means three `Agent` calls in a single reply** — not three replies with one call
each. Sending them one at a time still runs them, so nothing looks wrong; it just serialises
what was meant to be concurrent. Write all three calls before you send anything.

They must be independent: send the three dispatches identically, and do not tell any of them
that the others exist, what another said, or which premises you suspect. Three agents that
looked separately are the point; three that were nudged the same way are one agent run
three times.

**1d. Compare.** For each premise, line up the three verdicts:

- **All three agree** → that is the verdict. Done, no matter which verdict it is: three
  independent UNVERIFIEDs mean the premise genuinely cannot be settled from here.
- **They differ in any way** → dispatch one `guard:design-premises-recheck` for that premise,
  with the premise and all three verdicts including the evidence each cited. Dispatch every
  contested premise in one message.

  **Its answer is final.** There is no second round — a premise the recheck also could not
  settle is reported as unsettled, not resolved by taking the majority.

**Never resolve a split yourself, and never take the majority.** Two agents can reason from
the same wrong assumption independently; that is a common shape, not a rarity. The recheck
goes and reads the file, which is the only thing that settles it.

**What a FALSE premise means.** It is not automatically fatal, and it is not yours to wave
through either. Read what it actually breaks:

- The plan cites a fact loosely and the correction changes nothing → fix the wording, carry on.
- A step depended on it → that step needs rewriting, and you do that before presenting.
- The approach depended on it → the plan needs rethinking, and **that goes to the user**.

An UNVERIFIED premise the plan leans on is not a pass. Say so when you present, or settle it
first.

## Stage 2 — the critics

Dispatch all six with the **Agent** tool, in **ONE message**, so they run concurrently — six
`Agent` calls in a single reply, not six replies with one call each. Each holds one question
and is told the others hold theirs, which is why six short reports beat one agent asked to
think about everything.

| `subagent_type` | Holds |
| --- | --- |
| `guard:design-coherence` | Does the plan hold together as a plan? |
| `guard:design-adversary` | How does it fail at runtime? |
| `guard:design-alternatives` | What else could have been done? |
| `guard:design-feasibility` | Can it be built in this codebase? |
| `guard:design-fit` | Does it solve the user's actual problem? |
| `guard:design-deferrals` | What does it leave for later that it should settle now? |

Every dispatch carries the **plan file path** and **everything stage 1 settled** — the
premise verdicts and the environment report both. The critics must not re-litigate either,
and one reviewing a plan whose false premise or missing layer you already know about wastes
its whole run. Beyond that:

- `design-fit` also gets **the user's request**.

**Send no instructions of your own.** Do not tell an agent what to look for, do not tell it
what you think of the plan, and do not forward one critic's finding to another. You wrote the
plan; an argument from its author is the one thing that can bias all six at once.

## What comes back

Each reports and changes nothing. These are **critiques of a plan**, not defects in shipped
code, and the difference decides what you do with them:

1. **Weigh before acting.** A critic can be wrong about a design in a way a premise check
   cannot be wrong about a fact. A failure mode that does not apply, an alternative that is
   worse, a constraint already accounted for — note it and move on rather than reworking the
   plan around it.
2. **Revise the plan.** Usually it gains what it was missing: the failure mode handled or
   acknowledged, the alternative named and rejected with a reason, the constraint stated. A
   plan that carries a real objection is better than one that hides it.
3. **Settle what `design-deferrals` raises, before presenting.** An open question inside an
   approved plan is a decision the user delegated without being asked. Where the repository
   answers it, go and settle it and fold the answer in. Where it is genuinely the user's
   decision, put that question to them **with** the plan rather than leaving it inside the
   plan to be resolved later.
4. **A finding that changes the approach goes to the user as a choice, not as a decision.**
   If a critic shows the approach will not work — unbuildable, forbidden by the environment,
   solving the wrong problem — do not silently swap in a different plan. Present what was
   found and what it means. Choosing the approach is what the user is about to do; that is
   what approval *is*.
5. **Never silently drop a finding.** One you are not acting on is named when you present the
   plan, in a clause, with why.

## Then go back to the user

**Write the revised plan back to the plan file first**, then record the audit:
`guard-plan-audited <plan file path>`. Run it **last**, after the revisions are written — it
hashes the file as it stands, so a plan edited afterwards is held again, which is the gate
working rather than failing.

Then tell the user, in **a line or two** in their language, what the review changed: what was
raised, what you folded in, what you are leaving, and any premise that came back FALSE or
UNVERIFIED that still matters. A clean review is one line.

**They approved the plan you had, so a plan that now differs needs their word before you
build it.** Where the review only sharpened it — a failure mode handled, a constraint stated —
say so and carry on. Where it changed what will be done, or where `design-deferrals` surfaced
a decision that is genuinely theirs, ask before building. That is the whole reason this runs
before the work rather than after it.

Do not append the reports. They are reading a summary of what changed, not an audit; a plan
buried under its own review is one nobody reads.
