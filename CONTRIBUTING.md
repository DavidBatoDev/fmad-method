# Contributing to FMAD

Thanks for your interest. FMAD is a personal toolkit that I use for my own projects and hackathons, so it moves at my pace and follows my priorities. Issues, ideas, and small pull requests are welcome.

> **Before you write a large change, open an issue or a discussion first.**
>
> If your change adds features, restructures code, or touches more than a couple of files, check that it fits before you invest the time. A short conversation can save you hours.

## Philosophy

FMAD is about **human amplification, not replacement**. Specialized agents and guided workflows should bring out better thinking from both the human and the AI. Every contribution should answer: **"Does this make humans and AI better together?"**

**Welcome:**

- Better collaboration patterns and workflows
- Improved agent personas and prompts
- Clearer planning and context continuity
- Fixes to scripts, validators, and docs

**Doesn't fit:**

- Purely automated flows that sideline the human
- Complexity that makes FMAD harder to adopt
- Features that fragment the shared core

## Reporting Issues

Bug reports and feature requests go through [GitHub Issues](https://github.com/DavidBatoDev/fmad-method/issues). Search open and closed issues first. Questions and open-ended ideas fit better in [GitHub Discussions](https://github.com/DavidBatoDev/fmad-method/discussions).

- **Bugs:** use the [bug report template](https://github.com/DavidBatoDev/fmad-method/issues/new?template=bug-report.yaml). Include steps to reproduce, expected and actual behavior, and your environment (model, coding tool, FMAD version from `fmad status`).
- **Features:** use the [feature request template](https://github.com/DavidBatoDev/fmad-method/issues/new?template=feature-request.md) and say what the feature is and why it helps.

## Pull Requests

- Branch from `main` and target `main`.
- Keep a PR to one feature or fix. Aim for 200–400 changed lines and stay under 800, excluding generated files.
- Use [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`), under 72 characters.
- Run the checks before you push: `uv sync --frozen && (cd docs-site && npm ci) && uv run --frozen tools/quality.py`. They mirror `.github/workflows/quality.yaml`.

### AI-Generated Code

Most contributions here involve AI assistance, and that is fine. What matters is **human curation**: understand every line you submit, make deliberate choices about what to include, and be able to explain them. Bulk refactors nobody asked for, or changes that clearly ignore the existing code, will be closed.

### PR Description Template

```markdown
## What
[1-2 sentences describing WHAT changed]

## Why
[1-2 sentences explaining WHY this change is needed]
Fixes #[issue number]

## How
- [2-3 bullets listing HOW you implemented it]

## Testing
[1-2 sentences on how you tested this]
```

## Prompt and Agent Guidelines

- Keep dev agents lean: focus on coding context, not documentation.
- Web and planning agents can be larger and handle more complex tasks.
- Skills and workflows are natural language (markdown). Deterministic helpers are Python scripts run through `uv`.
- Skill rules live in `tools/skill-validator.md`. Validate with `uv run tools/validate_skills.py --strict` and `uv run tools/validate_file_refs.py --strict`.

| File Pattern | Validator | Extraction Function |
| ------------ | --------- | ------------------- |
| `*.yaml`, `*.yml` | `validate_file_refs.py` | `extract_yaml_refs` |
| `*.md`, `*.xml` | `validate_file_refs.py` | `extract_markdown_refs` |

## Code of Conduct

By participating, you agree to abide by the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## License

Contributions are licensed under the same MIT License as the project. See [LICENSE](LICENSE) and [CONTRIBUTORS.md](CONTRIBUTORS.md).
