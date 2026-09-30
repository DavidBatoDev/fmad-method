---
title: 'Add Modules'
description: Know which modules FMAD ships, install a custom module from a Git repository, understand how fmad finds modules, keep them updated, and know where to build your own.
sidebar:
  order: 3
---

FMAD extends through modules. A module is a set of skills that belong
together, plus one `fmod-<code>` folder that tells the `fmad` skill about
them. FMAD ships two official modules. Custom modules come from any Git
repository and install the same way, through the Skills CLI; there is no
separate installer, registry, or build step.

## Official modules

Run `npx skills add DavidBatoDev/fmad-method` and pick the skills you want,
including `fmad` and the module records `fmod-method` and
`fmod-core-tools`. Then ask the `fmad` skill to run `fmad setup`. See
[How to Install FMAD](../start/install-fmad.md) for the full steps.

- **`fmod-method`** (code `method`) -- the delivery skills, from planning through build, review, and retrospective
- **`fmod-core-tools`** (code `core-tools`) -- the `fmad` hub plus standalone tools such as brainstorming, party mode, and customization

There are no official add-on modules. Anything else is a custom module.

## Install from a custom source

A custom module is any module installed from a Git repository other than
FMAD's own. Only install modules from sources you trust: a module's skills
run in your coding tool like any other skill.

:::note[Prerequisites]
The Skills CLI needs [Node.js](https://nodejs.org), npm, and Git, and
`fmad setup` needs [uv](https://docs.astral.sh/uv/). A custom module can be
added in a fresh install or to an existing installation.
:::

### Interactive installation

Run `npx skills add <owner>/<repo>` with the module's repository, select
your coding tool, and pick the skills you want. Include the module's
`fmod-<code>` folder: it is the module record `fmad` reads.

Then ask the `fmad` skill to run `fmad setup`. Setup finds the new module,
asks its config questions, and offers to install skills the module requires
that are missing.

### Non-interactive installation

To install by name, pass each skill with `--skill`, and add `-y` to skip
the confirmation prompts:

```bash
npx skills add <owner>/<repo> \
  --skill fmod-my-module \
  --skill my-skill \
  -y
```

Then run `fmad setup` as above.

## How `fmad` finds modules

`fmad` reads every skills folder your coding tool has active. A folder whose
`fmod.toml` has a `[fmod]` table is a module record; by convention it is
named `fmod-<code>`. It holds:

| File           | Required | What it holds                                                                                                     |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `fmod.toml`    | Yes      | The record under a `[fmod]` table: code, version, update source, member skills, dependencies, and setup questions |
| `SKILL.md`     | Yes      | A stub that marks the folder as a skill so it installs with the others; nobody invokes it                         |
| `help/help.md` | No       | What `fmad` reads to guide users: what each skill is for and what comes next                                      |
| `roster.toml`  | No       | Personas and parties the module offers to `fmad-party-mode`                                                       |

Each member skill carries its own small `fmod.toml` with a `[skill]` table
naming its module folder and source. A standalone skill can be its own
module: one `fmod.toml` holding both `[fmod]` and `[skill]`, with no
separate `fmod-` folder.

## Develop a module locally

While you build a module, keep its folders in your coding tool's skills
directory (see [Where Skills Live](../reference/skills-and-agents.md#where-skills-live)),
and `fmad` finds it on its next run. To check versions against your working
copy instead of a published repository, point `update_source` at a `file:`
path:

```toml
[fmod]
code = "my-module"
version = "0.1.0"
update_source = "file:../my-module-repo/skills"
skills = ["my-skill"]
```

A relative `file:` path resolves from the project root and names the folder
that holds `fmod-my-module/`.

:::caution[Before publishing]
Point `update_source` at the published location, such as
`github:<owner>/<repo>/skills`, before others install the module. A `file:`
path only resolves on your machine.
:::

## What you get

After `fmad setup`, a custom module sits beside the official ones:

```
your-project/
├── .claude/skills/        # Your coding tool's skills directory
│   ├── fmad/
│   ├── fmod-method/       # Official module record
│   ├── fmod-my-module/    # Your custom module's record
│   └── my-skill/
│       └── SKILL.md
├── _fmad/
│   ├── config.toml        # Team answers to every module's setup questions
│   ├── scripts/           # Shared runtime
│   ├── my-module/
│   │   └── scripts/       # The module's scripts, when its skills declare any
│   └── custom/            # Team and personal customizations
└── ...
```

The record's `update_source` tells `fmad` where to check for a newer
version: a `github:` source, an `https://` URL, or a `file:` path.

## Update modules

Custom modules follow the same update flow as the official ones:

- **Check** (`fmad status`): Compares each installed module's version with
  the version at its `update_source`. A source that cannot be reached is
  reported, and the module stays as it is.
- **Update** (`fmad setup`): Runs `npx skills update` for modules with a
  newer version, then asks any new config questions and offers to delete
  skills the module renamed or removed.

## Create your own module

A module needs no special tooling or build step. The files listed above
are the whole contract, and FMAD's own `fmod-method` and `fmod-core-tools`
folders are working examples to copy:

1. Create a `fmod-<code>` folder with `fmod.toml`, the stub `SKILL.md`, and `help/help.md`
2. Add your skills, each with a small `fmod.toml` whose `[skill]` table names the module folder and source
3. Publish to a Git repository or share the folder
4. Others install with `npx skills add <owner>/<repo>`, then run `fmad setup`

Raise `version` in `fmod.toml` with each release: `fmad` compares the
installed version with the one at `update_source` to offer updates. List
skills you rename or remove in a `retired.toml` beside the record, so setup
can clean up old copies.

:::tip[Test locally first]
During development, work from a local copy with a `file:` update source
before publishing to a Git repository.
:::
