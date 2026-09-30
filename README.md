![FMAD — Foundry Method for Agile AI-Driven Development](banner-fmad-method.png)

[![Version](https://img.shields.io/github/v/tag/DavidBatoDev/fmad-method?color=e8702a&label=version)](https://github.com/DavidBatoDev/fmad-method/tags)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-1f2937)](https://davidbatodev.github.io/fmad-method/)

English | [简体中文](README_CN.md) | [Tiếng Việt](README_VN.md) | [한국어](README_KR.md)

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
