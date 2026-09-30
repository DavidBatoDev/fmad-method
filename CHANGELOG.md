# Changelog

## 1.0.0

**FMAD is born.** The Foundry Method for Agile AI-Driven Development starts as a rebranded fork of the BMAD-METHOD `6.13.0-next` development tree. The method and workflows are unchanged; the names, distribution, and branding are FMAD's own. See [NOTICE.md](NOTICE.md) for attribution.

### ✨ Features

* Install with the Skills CLI: `npx skills add DavidBatoDev/fmad-method`. Then ask the `fmad` skill to run `fmad setup`.
* Delivery workflows in the `fmod-method` module: `fmad-build`, `fmad-build-auto`, `fmad-spec`, `fmad-prd`, `fmad-ux`, `fmad-architecture`, `fmad-ticket`, `fmad-code-review`, `fmad-walkthrough`, `fmad-correct-course`, `fmad-retrospective`, `fmad-project-context`, `fmad-product-brief`, `fmad-prfaq`, and `fmad-qa-generate-e2e-tests`.
* The `fmad` hub and standalone tools in the `fmod-core-tools` module: `fmad-brainstorming`, `fmad-forge-idea`, `fmad-deep-recon`, `fmad-review`, `fmad-party-mode`, `fmad-advanced-elicitation`, and `fmad-customize`.
* The Foundry crew: Ember (analyst), Flint (product manager), Sienna (UX designer), Ferris (architect), and Cinder (developer), with the same personalities as their upstream counterparts.
* Web bundles for Gemini Gems and ChatGPT Custom GPTs, released as `web-bundles-v1.0.0`.
* A documentation site on GitHub Pages at <https://davidbatodev.github.io/fmad-method/>, in English.

### 🔧 Changes from upstream

* Renamed `bmad-*` skills to `fmad-*`, the `bmad` hub to `fmad`, `bmod-*` module records to `fmod-*` (`fmod.toml`), and the project folders `_bmad/` and `_bmad-output/` to `_fmad/` and `_fmad-output/`.
* Update checks and install sources point at `github:DavidBatoDev/fmad-method/skills`.
* Removed the plugin-marketplace routes, the npm installer references, the upstream ecosystem modules, community channels, sponsorship links, and the upstream v6→v7 migration files.
* Simplified the release flow to a single `main` branch.
