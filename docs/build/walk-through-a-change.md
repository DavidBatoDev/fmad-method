---
title: 'Walk Through a Change'
description: Use fmad-walkthrough to review a commit, PR, file, or directory one block at a time.
sidebar:
  order: 3
---

`fmad-walkthrough` is a guided human review. It writes a review narrative,
then walks you through it one block at a time. You can stop to inspect,
edit, or test. A block is done only when you say it is.

:::note[Human review]
This skill is for human review. Agentic review is done during a
[`fmad-build`](build-a-change.md) run, or by
[`fmad-code-review`](review-a-change.md).
:::

## When to Use It

Invoke it by name: `/fmad-walkthrough`. Point it at a commit, PR, file, or
directory.

Typical moments:

- **After [`fmad-build`](build-a-change.md)** — take the wheel back
- **Reviewing a PR** — especially one with more than a handful of files
- **Onboarding to a change** — a branch you didn't write

## How it runs

1. **Orientation.** What the target is and what it is for, from a plan or
   spec, PR description, and commit messages when they exist.
2. **Create review narrative.** A file organized in blocks: intent, broad
   strokes, slices by concern (not by file), then periphery. An append-only
   review log sits beside it in a `walkthrough-<slug>/` folder in the
   active initiative's folder, or in the output folder when no initiative
   is active.
3. **Walkthrough.** Each block is presented in the session with a clickable
   link into the narrative and one to three moves that fit. Stay on the
   block until you say it is done.

Moves you can pick: Thoughts, Second opinion, Formal review, Test, Drive,
Wrap-up. Formal review prefers `fmad-code-review` when it is installed. You
can also ask for something that was not suggested.

## What It Is Not

Not a replacement for [`fmad-code-review`](review-a-change.md) or for the
review `fmad-build` already ran. It does not assign severity scores or
produce a pass/fail verdict.
