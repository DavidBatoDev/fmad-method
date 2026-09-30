# Working in an organization

Use this when the work belongs to a team or enterprise: a PRD already exists, a tracker such as Jira is the record, people must approve, several engineers build in parallel, or requirements change mid-flight.

## When the full path is warranted

A single builder, or a small team that already agrees, goes straight to `fmad-spec` and needs no PRD. Recommend the full path (PRD, architecture, one spec per epic, tracking) only when one of these is true:

- People who did not do the thinking must approve what the product is.
- Several epics, teams, or agents build against the same decisions and must not diverge.
- A regulator, steering committee, or company process requires named documents.

Before any of this, a product manager, designer, or analyst can prototype the idea (`help/prototyping.md`).

## An existing PRD is input

- Point `fmad-prd` at the existing PRD. Validate gives a findings report and changes nothing. Create rewrites the same requirements in the shape later skills read, with `[ASSUMPTION]` tags on what it filled in.
- When the source PRD changes, run `fmad-prd` update. Tell the user never to hand-edit `prd-<slug>.md`.
- `fmad-ux` and `fmad-architecture` start from the existing design system, architecture document, or codebase.

## One owner per document

Each document has one skill that writes it, so give it one owner. One person can hold several roles.

| Role | Runs | Owns |
|---|---|---|
| Product manager | `fmad-prd` | `prd-<slug>.md` and its updates |
| Designer | `fmad-ux` | `DESIGN.md`, `EXPERIENCE.md` |
| Tech lead | `fmad-architecture` | The architecture spine |
| One engineer per epic | `fmad-spec`, `fmad-build`, `fmad-retrospective` | That epic's spec, stories, verdict |
| Whoever tracks the whole | `fmad-ticket` | the ticket tree |

Several engineers can each take an epic at once. An epic-level spine inherits the parent spine's decisions as binding.

## Where sign-off happens

Each moment produces a written result an approval can attach to. Advise placing existing approvals here.

| Moment | What it holds back |
|---|---|
| `fmad-prfaq` verdict | Writing the PRD |
| `fmad-prd` validate | Design and architecture work |
| Architecture spine review | Writing epic specs |
| `fmad-ticket` planning approval | Accepting the breakdown and its dependencies |
| `fmad-retrospective` verdict | Starting the next epic |

`fmad-prfaq` and `fmad-retrospective` accept `-H` to run without a conversation.

## When requirements change

Reviewers ask for changes in whichever document they are reading. Apply the change to the document that owns it, then re-run the later skills.

1. `fmad-prd` update. It surfaces conflicts with earlier decisions before applying anything.
2. `fmad-architecture` update when a decision shared across epics changes.
3. `fmad-spec` for each affected epic. Capability ids stay stable, and it says which stories no longer match.
4. Story breakdown or `fmad-ticket` again. Existing plans retain status.

For a change that threatens the plan itself, run `fmad-correct-course` first. It needs a PRD or a spec.

## Tracker integration

- Nothing syncs with Jira or any tracker automatically, in either direction.
- Repo-store status lives in each joined plan. Builds stop at `built`; the user or orchestrator marks `done`.
- `fmad-ticket` can publish tickets to Jira, Linear, or GitHub. When the skill runs, the tracker's status is read into the leaf file as `tracker_status`. The build's own `status` stays in its separate joined plan; tracker status never drives the build (`help/ticketing-and-epics.md`).
