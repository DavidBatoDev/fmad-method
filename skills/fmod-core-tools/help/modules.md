# FMAD modules

Open this when the user asks what an FMAD module is, what is in one, how to make or share one, or how to package agents and parties for others.

## What a module is

A module is a set of skills that belong together, plus one folder that tells `fmad` about them. There is no installer plugin, registry, or build step. A module is installed with `npx skills add <owner>/<repo>`, and `fmad` finds it on its next run. In return the module gets setup and config questions, help that `fmad` answers from, agents and parties in party mode, dependency prompts, and update checks.

## The module folder

One skill folder named `fmod-<code>`, for example `fmod-method`. Nobody runs it; `fmad` reads it. Its files:

| File | What it is |
|---|---|
| `fmod.toml` | The module record, under a `[fmod]` table: the module's code, version, where updates come from, the list of its skills, the skills it requires or recommends, and any questions `fmad setup` should ask. |
| `SKILL.md` | A stub that marks the folder as a skill so it installs with the others. It says never to invoke it. |
| `help/help.md` | What `fmad` reads to guide users: what each skill is for, when to recommend it, what comes next. Written for an agent, short. |
| `help/<topic>.md` | Optional deeper files on one subject each. `help.md` says what each covers, and `fmad` opens one only when a question needs it. |
| `roster.toml` | Optional. The personas the module offers and the parties they form, for `fmad-party-mode` and any skill that casts personas. |
| `retired.toml` | Optional. Skills the module no longer ships: `renamed` as `{ from, to }` pairs and `removed` as names. After an update, `fmad setup` offers to delete old copies still installed and moves a renamed skill's `_fmad/custom/` files to the new name. A retired name is never reused. |

## Each skill in the module

Every member skill carries its own small `fmod.toml` with a `[skill]` table naming its module folder and source. It can also list skills that this one skill requires or recommends. A skill belongs to one module. Depending on a skill from another module is fine.

## A module that is one skill

A standalone skill can be its own module: one `fmod.toml` holding both `[fmod]` and `[skill]`, with no separate `fmod-` folder. That is how a single skill brings its own config questions and help.

## A module that only adds personas and parties

A module with no skills is valid. A `fmod-<code>` folder holding `fmod.toml`, the stub `SKILL.md`, `help/help.md`, and a `roster.toml` is enough to distribute a cast.

- A roster member has a `code`, `name`, `icon`, `title`, and a `persona` paragraph. A member with a `skill` is an agent and appears only while that skill is installed. A member without one is a guest, available to parties.
- A roster group is a party: an `id`, a `name`, a `scene` describing how the room behaves, and its `members` by code.
- Once installed, the personas and parties appear in party mode with no setup. For a cast used in one repository or one team, a party saved through customization is simpler (`help/party-mode.md`).

## Setup and config questions

A module can declare questions in its `fmod.toml`. `fmad setup` asks them once: a team answer goes to the committed `_fmad/config.toml`, a personal answer to `_fmad/custom/config.user.toml`. A skill reads an answer without needing to know which file holds it.

## Building one

The file list above is the whole contract, and an existing `fmod-*` folder is a working example to copy.
