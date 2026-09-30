---
title: 'Test Completed Work'
description: Decide whether finished work needs more automated coverage, then generate API and end-to-end tests with fmad-qa-generate-e2e-tests.
sidebar:
  order: 4
---

After a change is implemented, decide whether it needs more automated
coverage. `fmad-qa-generate-e2e-tests` generates API and end-to-end tests
from code that already exists, and it stays simple on purpose. See
[how the skill runs](#run-fmad-qa-generate-e2e-tests).

This is generated coverage of finished work. It is not code review, and it
is not the manual observations in [Walk Through a Change](walk-through-a-change.md).

## Run `fmad-qa-generate-e2e-tests`

Open a **fresh chat** and name the skill. You can say what to test before,
with, or after the command — a feature, a directory, or "discover what is
untested."

```text
/fmad-qa-generate-e2e-tests
```

```text
/fmad-qa-generate-e2e-tests Create API and E2E tests for the login flow.
```

It uses whatever test framework the project already has. If there is none,
it looks at the stack and suggests one.

### What a run does

1. **Detect the test framework** — scans dependencies and existing tests
   (Playwright, Jest, Vitest, Cypress, and similar).
2. **Identify features** — asks what to test, or auto-discovers features in
   the codebase.
3. **Generate API tests** when there are endpoints — status codes, response
   shape, happy path, and one or two error cases.
4. **Generate E2E tests** when there is a UI — user workflows with semantic
   locators (roles, labels, text) and visible-outcome assertions.
5. **Run the tests** and fix failures immediately.
6. **Write a summary** of what was generated and what is still uncovered.

Generated tests stay simple on purpose: standard framework APIs, independent
cases, no hardcoded waits, descriptions that read as feature documentation.

## What You Get

- Test files under the project's `tests/` directory
- A test summary at `test-summary-<slug>/test-summary-<slug>.md` in the
  active initiative's folder, or in the output folder when no initiative is
  active
- Tests that were run once in this session and made to pass

## Limits

`fmad-qa-generate-e2e-tests` generates tests only. It does not review the
implementation — that is `fmad-build` during the run, or
[`fmad-code-review`](review-a-change.md) if you want another pass.

Happy path plus a few critical errors is the ceiling, and it does not
compose complex fixtures. More edge cases are follow-up work in your
project's own test suite.

## Where It Fits

[`fmad-build`](build-a-change.md) implements a change and, if a suite
already exists, aims to leave those tests passing. This page is the next
testing decision: generate additional coverage for that finished work.

You can run built-in QA after one change. You do not have to wait for an
epic to finish. A typical sequence is implement with `fmad-build`,
optionally [walk through the result](walk-through-a-change.md), then generate
coverage here. After a whole epic, `fmad-retrospective` is a different
check — it judges the epic against its spec, not the test suite.
