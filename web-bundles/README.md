# FMAD Web Bundles

Each bundle packages an FMAD skill as a self-contained install for **Google Gemini Gems** and **ChatGPT Custom GPTs**, so you can run the planning work in your web LLM subscription before opening your IDE.

## Install

**Download the bundle ZIPs from the [`web-bundles-v1.0.0` release](https://github.com/DavidBatoDev/fmad-method/releases).**

Each ZIP holds one bundle. Its `INSTRUCTIONS.md` walks you through the Gemini Gem and ChatGPT Custom GPT setup: create the Gem or GPT, upload the knowledge files, paste the instructions block, save. Every shelf update ships as a tagged GitHub Release; the newest tag holds the current bundles.

## Why use them

- **Cost.** Web LLM subscriptions are flat-rate. Run brainstorming, briefs, PRDs, and research there instead of burning IDE tokens.
- **Right tool for the job.** Planning conversations want Canvas, image generation, and Deep Research. Implementation wants the codebase and a terminal. Use each where it's strongest.
- **Persona swapping.** Every bundle ships a default persona and a contrasting swap example. Change voices without touching the protocol.

## The shelf

| Bundle | Purpose |
| --- | --- |
| Brainstorming Coach | Facilitated ideation across 60 techniques. Defaults to **Blaze** (Osborn lineage); swap to **Ember** for analyst rigor. |
| Product Brief Coach | Build a product brief through guided discovery. Create, Update, or Validate modes. |
| PRFAQ Coach | Working Backwards PRFAQ challenge (Bezos lineage) to forge and stress-test product concepts. |
| PRD Coach | Product Requirements Document with built-in validation (Cagan lineage). |
| UX Coach | UX patterns, flows, and design specifications. Pairs with Google Stitch. |
| Market & Industry Research | Market research, customer JTBD, competitive landscape, regulatory and technical lenses. Deep Research mode integrated. |

Requires Gemini Advanced (for Gems) or ChatGPT Plus / Pro / Business / Enterprise (for Custom GPTs). Deep Research has its own plan limits.

## Build your own

Each bundle is an FMAD skill repackaged as a `SKILL.md`, an `INSTRUCTIONS.md`, and any required data files, with the default persona taken from the matching FMAD agent when there is one. To build your own, use an existing bundle directory as the model and add an entry for it in `bundles.json`.

## What's in this folder

This folder is the **source** for the shelf, packaged into ZIPs and attached to GitHub Releases. End users do not install from here. If you are a contributor working on a bundle, the bundle directories and `bundles.json` are the files you edit; the [release packager](../tools/bundle_web_bundles.py) zips them and updates the release.

## Concept docs

[What web bundles are and when to use them](https://davidbatodev.github.io/fmad-method/customize/use-web-bundles/).
