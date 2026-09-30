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

### Cheat Sheet

| I want to… | Run |
| --- | --- |
| Make a change | `/fmad-build` |
| Turn an idea into a buildable contract | `/fmad-spec` |
| Split big work into stories | `/fmad-ticket` |
| Review a change | `/fmad-code-review` or `/fmad-walkthrough` |
| Fix a plan that went off course | `/fmad-correct-course` |
| Set up or fix agent instructions | `/fmad-project-context` |
| Know what's next | `/fmad` |

More detail: [Choose a Planning Path](https://davidbatodev.github.io/fmad-method/plan/choose-a-planning-path/), [Start in an Existing Codebase](https://davidbatodev.github.io/fmad-method/existing-codebases/start-in-an-existing-codebase/), and [Set and Maintain Project Context](https://davidbatodev.github.io/fmad-method/existing-codebases/set-and-maintain-project-context/).

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

The workflows cover the rest of the loop: `fmad-brainstorming`, `fmad-forge-idea`, `fmad-product-brief`, `fmad-prfaq`, `fmad-deep-recon`, `fmad-prd`, `fmad-ux`, `fmad-architecture`, `fmad-spec`, `fmad-ticket`, `fmad-build`, `fmad-build-auto`, `fmad-code-review`, `fmad-review`, `fmad-walkthrough`, `fmad-qa-generate-e2e-tests`, `fmad-correct-course`, `fmad-retrospective`, `fmad-project-context`, `fmad-customize`, and `fmad-advanced-elicitation`. See the [skills and agents reference](https://davidbatodev.github.io/fmad-method/reference/skills-and-agents/).

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
