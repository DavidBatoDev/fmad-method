![FMAD — Foundry Method for Agile AI-Driven Development](banner-fmad-method.png)

[![Version](https://img.shields.io/github/v/tag/DavidBatoDev/fmad-method?filter=v*&color=e8702a&label=version)](https://github.com/DavidBatoDev/fmad-method/tags)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-1f2937)](https://davidbatodev.github.io/fmad-method/)


**FMAD — Foundry Method for Agile AI-Driven Development. Turn an idea or change request into working software without giving up the thinking.**

AI-driven development covers the whole effort, not only the code: what to build, how it holds together, and how it changes as you learn. The Foundry Method is an agile way to do it. Decisions stay explicit, context carries forward, and the process sizes itself to the work. Small changes go straight to build. Complex work gets the depth it needs. The same method covers a hackathon prototype and a system with years of history behind it.

![The FMAD delivery loop: a vague notion starts at Clarify, a big clear idea at Plan, and a small change at Build and verify; Learn and adjust loops back to Plan](docs/images/fmad-delivery-loop.svg)

_Start anywhere. Use FMAD end to end, or carry its briefs, specifications, and architecture into your existing delivery workflow._

## Start Building

You need an AI coding tool that supports skills (Claude Code, Codex, Cursor, and others), [uv](https://docs.astral.sh/uv/) for FMAD setup and Python scripts, and [Node.js and npm](https://nodejs.org) plus Git for the Skills CLI. In your project, run:

```bash
npx skills add DavidBatoDev/fmad-method
```

Select the skills and coding tool you want. Include `fmad` for setup and help, and the module record for each module you pick skills from: `fmod-method` and `fmod-core-tools`. To install by name instead, list them together:

```bash
npx skills add DavidBatoDev/fmad-method --skill fmad --skill fmod-core-tools --skill fmod-method --skill fmad-build
```

Open your coding tool in the project and ask the `fmad` skill to run `fmad setup`. Then invoke `fmad-build` with what you want to change. Ask `fmad` whenever you want guidance on what comes next or what is optional.

**[Build your first project with FMAD →](https://davidbatodev.github.io/fmad-method/start/build-your-first-change/)**

**[Add FMAD to an existing codebase →](https://davidbatodev.github.io/fmad-method/existing-codebases/start-in-an-existing-codebase/)**

Ask for `fmad status` to check versions and see what to run next. Ask for `fmad setup` to install updates: it runs `npx skills update`, then refreshes the project and cleans up renamed and removed skills.

## Use It in Your Projects

Setup is the same everywhere: install the skills, then ask for `fmad setup`. It creates `_fmad/` (config and scripts; commit it), and FMAD writes its documents to `_fmad-output/`. When unsure, ask `/fmad what should I do next?` — it inspects the project and recommends a skill.

### New Projects

Pick the path by how clear the idea is:

| Situation | Path |
| --- | --- |
| Small and clear (a hackathon MVP, a script) | `/fmad-build <what you want>` — it asks questions, shows a plan, builds, and checks its work |
| Clear but needs several sessions | `/fmad-spec` → `/fmad-ticket` (splits it into stories) → `/fmad-build` per story → `/fmad-retrospective` |
| Fuzzy idea | `/fmad-brainstorming` or `/fmad-forge-idea` → `/fmad-product-brief` or `/fmad-prd` → `/fmad-ux` and `/fmad-architecture` if needed → `/fmad-spec` → tickets → builds |
| Need evidence first | `/fmad-deep-recon` for cited market, competitor, or technology research |

- Run `/fmad-project-context` early so your standards (stack, test commands, rules) land in `AGENTS.md` and every session follows them.
- For hackathons, `forge-idea` → `spec` → `build` is the fastest path that still produces something solid.
- Want several perspectives at once? `/fmad-party-mode` puts Ember, Flint, Sienna, Ferris, and Cinder in one discussion.

### Existing Projects Without Documentation

Don't write documentation first. `fmad-build` reads the code, notes the conventions to reuse, and follows them.

1. Run `/fmad-project-context` and say *"set up AGENTS.md"*. It scans your configs, CI, and code, asks what agents tend to get wrong and what is off limits, and shows you a small verified block. Nothing is written until you approve it.
2. Make changes: a small fix or feature goes straight to `/fmad-build <the change>`; multi-session work goes `/fmad-spec` → `/fmad-ticket` → `/fmad-build` per story; design decisions go to `/fmad-architecture`, which works from the existing codebase.
3. When agents repeat a mistake, run `/fmad-project-context` and say *"record: the agent keeps using the wrong test runner"*. Say *"refresh"* after big changes.

If you want a change to break an existing pattern, say so in the request. Otherwise Build matches what is already there.

### Existing Projects With Documentation

1. **Adopt what you have.** Run `/fmad-project-context` and say *"adopt our AGENTS.md"* or *"set up context from our docs"*. It reads your `AGENTS.md`, `CLAUDE.md`, editor rules, and docs folders, keeps and improves what is good, and deletes nothing without asking. You can also point it at handbooks or wiki exports.
2. **Feed docs into planning, not into every build.** Old documents (the original PRD, design notes) add noise and contradictions to small changes, so keep them archived. For a big change, give `/fmad-spec` the relevant docs as sources, condensed to about 40 pages at most. Use `/fmad-prd` with *"update"* or *"validate"* on an existing PRD, and point `/fmad-architecture` at your architecture doc so it builds on your decisions instead of reinventing them.
3. **Pin must-follow docs** (compliance, style rules) so a skill always loads them, for example in `_fmad/custom/fmad-build.toml`:

   ```toml
   [workflow]
   persistent_facts = [
     "file:{project-root}/docs/coding-standards.md",
     "We deploy on Vercel only.",
   ]
   ```

   Commit that file to share it with a team; personal overrides go in `fmad-build.user.toml`, which is git-ignored. `/fmad-customize` can write these files for you.

More detail: [Choose a Planning Path](https://davidbatodev.github.io/fmad-method/plan/choose-a-planning-path/), [Start in an Existing Codebase](https://davidbatodev.github.io/fmad-method/existing-codebases/start-in-an-existing-codebase/), and [Set and Maintain Project Context](https://davidbatodev.github.io/fmad-method/existing-codebases/set-and-maintain-project-context/).

## Cheat Sheet

📄 **[Download the printable cheat sheet (PDF)](docs-site/public/fmad-cheat-sheet.pdf)** · [view it online](https://davidbatodev.github.io/fmad-method/fmad-cheat-sheet.pdf)

Invoke a skill by name (`/fmad-build …` in Claude Code) or just describe what you want; the phrases below trigger the right one. Documents land in `_fmad-output/`, inside the active initiative's folder when one is set.

### Quick Picks

| I want to… | Run |
| --- | --- |
| Make a change | `/fmad-build` |
| Turn an idea into a buildable contract | `/fmad-spec` |
| Split big work into stories | `/fmad-ticket` |
| Review a change | `/fmad-code-review` or `/fmad-walkthrough` |
| Fix a plan that went off course | `/fmad-correct-course` |
| Set up or fix agent instructions | `/fmad-project-context` |
| Know what's next | `/fmad` |

### Hub and Setup

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad` | Your guide. Answers FMAD questions, recommends the next skill, runs setup, status, update, and repair, and manages the active initiative | *"fmad setup"*, *"fmad status"*, *"what should I do next?"* |
| `fmad-project-context` | Writes and maintains a small verified agent-instructions block in `AGENTS.md`: setup, adopt existing files, refresh, record a pitfall, audit | *"set up AGENTS.md"*, *"record: agents keep using npm instead of pnpm"* |
| `fmad-customize` | Writes override files that change how any skill or agent behaves: facts, principles, menus, hooks | *"customize fmad-build to always run pnpm test"* |

### Explore and Research

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-brainstorming` | Facilitated ideation drawing on 100+ creative techniques, with an HTML keepsake of the session | *"help me brainstorm features for a study-group app"* |
| `fmad-forge-idea` | Pressure-tests a half-formed idea while personas probe its weak points, until it hardens or dies cheaply; can write a short brief | *"forge this idea: …"* |
| `fmad-deep-recon` | Cited research for a decision: market, domain, technical, competitive, user voice, academic literature, or choosing between options. Runs the research here, drafts a prompt for ChatGPT, Gemini, or Perplexity, or summarizes a report you bring | *"research the market for X"*, *"help me choose between Supabase and Firebase"* |
| `fmad-party-mode` | A roundtable between the agents or custom personas, including focus-group panels | *"party mode: should we build X?"* |
| `fmad-advanced-elicitation` | Makes the AI critique and improve its last answer with 70+ methods such as Socratic questioning, first principles, pre-mortem, and red team | *"run a pre-mortem on that"* |

### Define

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-product-brief` | Creates, updates, or validates a product brief: the vision on a page or two | *"create a product brief"* |
| `fmad-prfaq` | Amazon's Working Backwards: writes the launch press release first, then answers hard customer and stakeholder questions | *"work backwards on this idea"* |
| `fmad-prd` | Creates, updates, or validates a PRD, with an HTML validation report | *"create a PRD"*, *"validate the PRD"* |
| `fmad-spec` | Condenses any input (idea, brief, PRD, transcript, notes) into a short spec that Build can execute; also updates and validates specs | *"distill this into a spec"* |

### Design

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-ux` | Captures the UX in `DESIGN.md` (how it looks) and `EXPERIENCE.md` (how it behaves) | *"help me plan the UX"* |
| `fmad-architecture` | Records the technical decisions that keep separately built parts consistent. Works from a spec, a raw idea, or an existing codebase; creates, updates, or validates | *"create the architecture"* |

### Plan and Track

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-ticket` | Slices initiatives into epics and epics into stories, writes and refines tickets, and runs the board (publish, ready, move, assign, status) in the repo, GitHub, Jira, Linear, Notion, or Trello | *"break this epic into stories"*, *"what's ready?"* |

### Build

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-build` | The workhorse. Clarifies the request, plans (you approve), implements, reviews with independent reviewers, verifies, and presents the result. Accepts an issue or story link | *"/fmad-build add dark mode"* |
| `fmad-build-auto` | One unattended build iteration for automated loops, where an orchestrator hands each worker one ticket | Invoke by name |
| `fmad-qa-generate-e2e-tests` | Generates API and end-to-end tests for features that already exist | *"create QA automated tests for checkout"* |

### Review and Verify

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-code-review` | Several independent reviewers check a change in parallel; findings are triaged before you see them | *"run code review"* |
| `fmad-review` | Review lenses for code or documents: adversarial, edge cases, verification gaps, structure, prose | *"review this PRD adversarially"* |
| `fmad-walkthrough` | Walks you through reviewing a commit, PR, file, or folder yourself | Invoke by name |

### Adjust and Learn

| Skill | What it can do | Say something like |
| --- | --- | --- |
| `fmad-correct-course` | When a big change lands mid-build, assesses the impact on the PRD, epics, architecture, and UX and proposes the change | *"correct course: the client dropped payments"* |
| `fmad-retrospective` | Evidence-based review of a finished epic: sourced findings, action items, and an acceptance decision | *"let's retro the epic"* |

### Agent Menus

Talk to an agent (*"talk to Ember"* or `/fmad-agent-analyst`), then type a menu code, or just say what you want.

| Agent | Menu codes |
| --- | --- |
| 📊 **Ember**, analyst | `BP` brainstorm · `MR` market · `DR` domain · `TR` technical · `TS` tech selection · `CR` competitors · `UV` user voice · `CB` product brief · `WB` PRFAQ · `PC` project context |
| 📋 **Flint**, product manager | `PRD` create, update, or validate a PRD · `CC` correct course · `TK` tickets |
| 🎨 **Sienna**, UX designer | `CU` create the UX design |
| 🏗️ **Ferris**, architect | `CA` create the architecture · `TK` tickets |
| 💻 **Cinder**, developer | `BD` build · `QA` generate tests · `CR` code review · `ER` epic retrospective · `TK` tickets |

## Why FMAD?

Coding assistants are effective at implementation, but they often turn unstated assumptions into code. FMAD keeps you in control while its agents and workflows make the important decisions explicit and preserve them as context for the work that follows.

- **Right-sized process** — Go directly to implementation for clear changes or add deeper planning for larger initiatives.
- **New or existing code** — Start from nothing, or establish verified context on a codebase you inherited and work from what is actually there.
- **Durable context** — Carry product and technical decisions forward instead of re-explaining them in every chat.
- **Specialized perspectives** — Bring in product, architecture, UX, development, and testing expertise when it helps.
- **Guided collaboration** — Use structured workflows and multiple-agent discussions without handing over judgment.
- **One delivery path** — Move from early thinking through reviewed implementation, correction, and learning.

[See how much planning a change needs →](https://davidbatodev.github.io/fmad-method/plan/choose-a-planning-path/)

## The Foundry Crew

FMAD ships two modules. `fmod-method` holds the delivery workflows and `fmod-core-tools` holds the `fmad` hub and standalone tools. The named agents bring a perspective into any conversation, one at a time or together in `fmad-party-mode`.

| Agent | Skill | Brings |
| --- | --- | --- |
| 📊 **Ember** — Business Analyst | `fmad-agent-analyst` | Market and domain research, evidence-first discovery |
| 📋 **Flint** — Product Manager | `fmad-agent-pm` | Jobs-to-be-done, requirements, sharp "why?" questions |
| 🎨 **Sienna** — UX Designer | `fmad-agent-ux-designer` | User journeys, interaction design, the screen before the code |
| 🏗️ **Ferris** — System Architect | `fmad-agent-architect` | Boring-on-purpose technology, trade-offs, what breaks at scale |
| 💻 **Cinder** — Senior Software Engineer | `fmad-agent-dev` | Test-first implementation with commit-message brevity |

The workflow skills cover the rest of the loop; the [Cheat Sheet](#cheat-sheet) lists every one with what it can do. See also the [skills and agents reference](https://davidbatodev.github.io/fmad-method/reference/skills-and-agents/).

## Plan on the Web

The [web bundles](web-bundles/) package selected FMAD workflows as Google Gemini Gems and ChatGPT Custom GPTs. Use them for planning in your existing web subscription, then bring the resulting artifacts into your AI coding tool for implementation. Zipped bundles are attached to the [releases](https://github.com/DavidBatoDev/fmad-method/releases).

## Documentation

- **[Build Your First Change](https://davidbatodev.github.io/fmad-method/start/build-your-first-change/)** — Install FMAD and build a small project.
- **[Choose a Planning Path](https://davidbatodev.github.io/fmad-method/plan/choose-a-planning-path/)** — Pick how much planning a change needs and see what each planning skill produces.
- **[Start in an Existing Codebase](https://davidbatodev.github.io/fmad-method/existing-codebases/start-in-an-existing-codebase/)** — Add FMAD to an existing codebase.

## Feedback

FMAD is a personal toolkit for my own projects and hackathons, shared in case it helps you too.

- [GitHub Issues](https://github.com/DavidBatoDev/fmad-method/issues) — Report bugs and request features.
- [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions) — Ask questions and share ideas.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Acknowledgements

FMAD is heavily inspired by, and derived from, [BMAD-METHOD™](https://github.com/bmad-code-org/BMAD-METHOD) by BMad Code, LLC, which is released under the MIT License. FMAD renames the skills, modules, and personas and changes the branding, but the method, workflows, and much of the text come from that project. Credit for the underlying ideas belongs to its authors and contributors. See [NOTICE.md](NOTICE.md) for details.

FMAD is an independent project. It is not affiliated with, endorsed by, or sponsored by BMad Code, LLC. BMad™, BMad Method™, and BMAD-METHOD™ are trademarks of BMad Code, LLC.

## License

MIT License. See [LICENSE](LICENSE) for details.
