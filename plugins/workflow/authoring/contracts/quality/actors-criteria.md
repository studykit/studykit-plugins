# Actors Review Criteria

Quality criteria for reviewing the actors page (the project's canonical actor registry). This file defines what to flag during review.

A reviewer applies each criterion below to the registry. Each non-OK verdict becomes one `review` issue targeting the actors page.

## 1. Required field completeness

Every actor entry must carry:

- **Name** — canonical reference name.
- **Type** — `person` or `system`.
- **Description** — one-paragraph identity definition.
- **Privileges** — required only when authorization scope distinguishes what the actor can do; omit otherwise.

Flag entries missing any required field. Suggested fix names the missing field(s).

## 2. Specificity

An actor name is too generic when two different roles in the project could both reasonably claim it. Examples of generic names to flag: `User`, `The Team`, `Operator`, `The System`, `Admin` (when multiple admin roles exist).

Flag entries whose name is generic. Suggested fix proposes a role-scoped rename (e.g., `Study Group Owner` instead of `User`; `Push Notification Service` instead of `The System`).

## 3. Identity vs participation boundary

The actors page carries general identity — who the actor is across every use case they participate in. Per-flow behavior (what the actor does in a specific situation) belongs on the use case that names the actor, not on the registry entry.

Flag entries whose `Description` reads as a use-case action ("creates a study group, invites members, removes inactive members") instead of an identity ("authenticated user who organizes a study group; can manage membership and content settings"). Suggested fix proposes the identity-level rewrite and notes that the per-flow content should move to the relevant use case.

## 4. Duplicate entries

Flag pairs of entries that appear to describe the same actor under different names (`Study Group Owner` vs `Group Admin`). Suggested fix proposes which name is canonical and which to merge or delete, with rationale.

## 5. Role conflation in a single entry

Flag entries that bundle two distinct roles under one identity (e.g., `User / Moderator` as a single entry). Suggested fix proposes a split into two separate entries.

## 6. Architecture surface leakage

System components with no user-visible role in any use case do not belong on the actors page. Flag system entries that do not appear in any use case as actors. Suggested fix proposes removing the entry from the actors page; the user decides whether the entry belongs on a different knowledge surface.

## Out of scope

- **Dead entry detection.** The reviewer does not have a project-wide view of every use case and so cannot reliably decide whether an actor is unused. Do not flag this as a finding; backlog cleanup is out of scope.
- **Renaming impact.** Tracing downstream references after a rename is handled by a separate procedure. The reviewer flags only registry-side concerns (criterion 4 for duplicates, criterion 2 for generic replacements).

## Filing findings

Findings target the actors page. The calling agent's publishing contract determines how the `review` issue is published and labeled.
