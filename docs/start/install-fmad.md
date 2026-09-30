---
title: 'How to Install FMAD'
description: Install the current FMAD skills, set up the project runtime, and verify or update it.
---

Install FMAD through the Skills CLI, then run `fmad setup` in the project.

## Prerequisites

You need an AI coding tool that supports skills and [uv](https://docs.astral.sh/uv/) for setup and Python scripts. The Skills CLI also needs Node.js, npm, and Git.

## Install the Skills

From your project directory, run:

```bash
npx skills add DavidBatoDev/fmad-method
```

Select your coding tool and skills. Include `fmad` for setup and help, and the module records `fmod-core-tools` and `fmod-method` for the modules you use. To install a small set by name:

```bash
npx skills add DavidBatoDev/fmad-method --skill fmad --skill fmod-core-tools --skill fmod-method --skill fmad-build --skill fmad-ticket
```

Add review, retrospective, or other skills as needed. Keep project and global installation scopes consistent.

## Set Up and Verify

Open the coding tool from the project folder and ask the `fmad` skill to run `fmad setup`. Setup installs the shared runtime and module scripts under `_fmad/`. Ask for `fmad status` to verify the installation and versions. Documents and tickets go to `_fmad-output`, inside the active initiative's folder when one is set; ask `fmad` to create or switch one.

Invoke `fmad-build` with the change you want, or ask `fmad` for guidance. For work spanning repositories, set up at the workspace root so skills can reach both the output folder and code repositories.

## Update an Installation

Ask the `fmad` skill to run `fmad setup` again. It checks each module's version and runs `npx skills update` for you when there is a newer one. Then it asks any new config questions, moves your `_fmad/custom/` files when a skill was renamed, and offers to delete skills a module renamed or removed. Last, it checks whether a migration applies and asks whether to run it.

If you update by hand with `npx skills update`, run `fmad setup` afterwards. Restart your coding tool when its skill catalog needs refreshing.

## What You Get

Your coding tool discovers the installed skills. The project's `_fmad/` holds shared configuration and supporting scripts. Team and personal customizations live under `_fmad/custom/` and survive setup refreshes.
