# FMAD Core Tools knowledge

This document covers the skills of the `core-tools` module: what each one is for and when to recommend it.

## How the core tools fit

The core tools belong to no phase and no path. Each stands alone and works with or without any other module. Suggest one whenever it would help: before, during, after, or entirely outside another module's flow. Never present one as a required step. A project may hold only some of these skills: recommend from what is installed.

## Initiatives

An initiative is one body of work of any kind: a product, a feature, a book, a set of art assets. Its folder under `output_folder` holds what every module's skills write for that work. `active_initiative` under `[core]` in `_fmad/custom/config.user.toml` names the folder in use; the file is personal, so each person can work on a different one. With none active, work is written loose to `{output_folder}/`, and some skills first ask whether it belongs to an initiative. The `fmad` skill shows, switches, creates, or clears the active initiative. What goes inside the folder is up to each module: its help says.

## Start here

- No idea yet, or wants more and better ideas on a topic → `fmad-brainstorming`.
- Has an idea and is not sure it holds up → `fmad-forge-idea`.
- Needs facts from outside before deciding (a market, a technology, competitors, what users say), or has a research report to make usable → `fmad-deep-recon`.
- Has a piece of work and wants it better:
  - It was just produced in this conversation and they want it pushed further, or they name a critique method → `fmad-advanced-elicitation`.
  - They ask for a review of a diff, a file, or a document → `fmad-review`.
  - They want several points of view arguing it out, a roundtable, or a focus group of their customers → `fmad-party-mode`.
- FMAD itself needs attention:
  - Something was installed or updated, or a skill reports that FMAD is not set up or an FMAD script was not found → `fmad setup`.
  - "What do I have, and is it current?" → `fmad status`.
  - Which initiative is active, or they want to switch, create, or clear one → `fmad`.
  - They want a skill or an agent to behave differently, or to use the team's template → `fmad-customize`.
  - They ask what an FMAD module is or how to make one → `help/modules.md`.

## The skills

| Skill | For | Good to know | Writes |
|---|---|---|---|
| `fmad-brainstorming` | A coached session that pushes well past the obvious ideas. | The user picks who supplies the ideas: themselves, both, or the skill alone. It does not judge ideas until asked to converge. Sessions resume. | `{output_folder}/{active_initiative}/brainstorm-<topic>/`, or under `{output_folder}/` for loose work, with `brainstorm.html` and, on request, `brainstorm-<topic>.md`: the chosen ideas, ready as input to any installed planning skill. |
| `fmad-forge-idea` | Questions one half-formed idea hard until the user can act on it or drop it. | Any idea, not only products, including a change to an existing project. It ends hardened, killed, or clearer, and all three are good outcomes. Not for generating ideas or for outside facts. | `{output_folder}/{active_initiative}/forge-<slug>/`, or under `{output_folder}/` for loose work, with `forge-report.html` and, when the idea hardens, `forge-<slug>.md`: the surviving decisions, ready as input to any installed planning or build skill. |
| `fmad-deep-recon` | Research that serves a decision, with cited sources found now, never from memory. | It can draft a prompt for the user's own research tool, process a finished report, or run the research here. It can also choose between candidates. | `{output_folder}/{active_initiative}/research-<topic>/`, or under `{output_folder}/` for loose work, with `brief.md` and `research-<topic>.md`, which is input for whatever skill acts on the decision. |
| `fmad-advanced-elicitation` | Pushes the most recent output to be reconsidered and improved. | It offers critique methods such as socratic questioning, first principles, pre-mortem, and red team. Nothing changes unless the user accepts. Other skills call it at their pauses. | Nothing. It improves the work in place. |
| `fmad-review` | Independent review lenses over any diff or document: adversarial, edge cases, verification gaps, structure, prose. | It runs only when the user asks and says "review". Acting on earlier findings is a change, not a review. No severity ranking. | The report in chat, or a file when the project sets a report path. |
| `fmad-party-mode` | A group conversation between agents or personas, with the user in the room. | It works alone or beside any skill. Custom parties, a default party, and memory are all configurable, and a module can ship a cast. It debates and does not verify. | On request, a keepsake `{output_folder}/{active_initiative}/party-<slug>/party-<slug>.html`, or under `{output_folder}/` for loose work. Memory under `{output_folder}/party-mode/memories/`. |
| `fmad-customize` | Changes how an installed skill or agent behaves without editing it: persona, standing facts, templates, output paths, steps on completion. | Team overrides are committed and shared; personal ones are not. It offers only what the target skill exposes. Central config is edited by hand. | `{project-root}/_fmad/custom/{skill-name}.toml` for the team, `{skill-name}.user.toml` for one person. |

## `fmad`: setup, status, and help

- `fmad setup` creates and repairs `{project-root}/_fmad`, including the shared scripts other skills call, and asks each installed module's new configuration questions. Recommend it after anything is installed or updated.
- `fmad status` changes nothing. It reports what is installed, what is missing or out of date, and the one command to run next.
- Either takes a module code, such as `fmad setup core-tools`, to cover that module only.
- FMAD is installed per project. To use it in another repository, run `npx skills add DavidBatoDev/fmad-method` there, then `fmad setup`.

## More detail

This document should be enough to route the user and say what to do next. Each topic file below sits in this folder and goes deeper on one subject. Read one only when the question is about that subject, using the path the knowledge script lists for it. For how one skill behaves in detail, that skill's own files are the last resort.

| Topic file | Read when the user asks about |
|---|---|
| `help/party-mode.md` | What party mode is good for alone or with other skills, custom parties, the default party, memory, parties that come with a module. |
| `help/research.md` | Getting the most from `fmad-deep-recon` and which of its services to use. |
| `help/customization.md` | How overrides work: team or personal file, how they merge, central config, an override that is not applied, resetting. |
| `help/team-adoption.md` | Making a whole team's FMAD follow shared rules, tools, templates, and publishing steps. |
| `help/modules.md` | What an FMAD module is, each file in one, a single-skill module, a module that only ships personas and parties, building one. |

## When this document is not enough

For a `core-tools` question this document, its topic files, and the installed skills cannot answer, fetch the documentation site at `https://davidbatodev.github.io/fmad-method/` and follow the pages relevant to the question. The source repository it links to is the final authority on how anything actually behaves.
