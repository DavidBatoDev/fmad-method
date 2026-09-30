# Release Runbook — FMAD-METHOD

FMAD uses a single branch. `main` is the default branch and every release is a tagged commit on it. There are no release branches, release PRs, or back-merges.

This is a hand-run process. Use Git, `uv`, and the Node version in `docs-site/.nvmrc`. Do the release in one sitting and stop on any failed command or unexpected diff.

The version lives in one place per module: the `version` line in the `[fmod]` table of `skills/fmod-method/fmod.toml` and `skills/fmod-core-tools/fmod.toml`. The skills of a module carry no version. Every module record in this repository carries the same version, and the stamper writes them together.

## 1. Prepare

Start in a clean checkout of `main` with no unpublished commits:

```bash
git status --porcelain
git fetch origin
git switch main
git pull --ff-only origin main
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"

fmad_release_version=1.1.0
git show origin/main:skills/fmod-core-tools/fmod.toml
git tag --list "v$fmad_release_version"
```

Choose the version explicitly. It must differ from what `main` serves and must not reuse a tag. Use SemVer, optionally with a prerelease; no `-dev` or build metadata (`+...`). The stamper enforces the version syntax, not release history.

## 2. Stamp, check, and push

```bash
uv run --python 3.11 tools/stamp_release.py "$fmad_release_version"
git diff
git add skills/*/fmod.toml
git commit -m "chore(release): v$fmad_release_version"
uv sync --frozen && (cd docs-site && npm ci) && uv run --frozen tools/quality.py
git push origin main
```

Before it writes, the stamper runs the repository checks in `tools/validate_manifests.py`, the same ones the commit hook runs, and writes nothing if any of them fails. Review before committing: only the `[fmod]` version line in the two module records should change. Wait for the GitHub status checks on the pushed commit to pass before tagging.

If a module raises the minimum version it needs from another module (`required_skills` in `skills/fmod-method/fmod.toml`), update that minimum in the same commit.

## 3. Tag

```bash
git fetch origin
git tag -a "v$fmad_release_version" origin/main -m "Release v$fmad_release_version"
git push origin "refs/tags/v$fmad_release_version"
```

Never force a push or move a release tag.

## 4. Verify

Verify the release through `npx skills add DavidBatoDev/fmad-method` in a scratch project, then ask the `fmad` skill for `fmad status`.

An installed module checks `main` through `raw.githubusercontent.com`, which caches files for around five minutes. Verify the release through Git first, or wait before trusting an update check that still reports the previous version.

## Web Bundles

Web bundles are released separately under their own tag (the `releaseTag` in `web-bundles/bundles.json`). Run `uv run tools/bundle_web_bundles.py` and follow the `gh release` command it prints.
