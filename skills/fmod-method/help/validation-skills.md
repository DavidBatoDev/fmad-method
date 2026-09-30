# Validation skills in detail

Read this when the question is about `fmad-code-review`, `fmad-walkthrough`, `fmad-qa-generate-e2e-tests`, or `fmad-retrospective`. For choosing review depth, getting another pass, and slow reviews, see `help/review-choices.md`.

| | Reviewer | Looks at | Fixes |
|---|---|---|---|
| Review inside `fmad-build` | Agents | The change just built | Clear findings, itself |
| `fmad-code-review` | Agents | Any diff, PR, branch, or commit | What the human chooses |
| `fmad-walkthrough` | The human, guided | A commit, PR, file, or directory | Nothing unless asked |
| `fmad-retrospective` | Agents, across tickets | A whole epic folder | Nothing; proposes action items |

**`fmad-code-review`** — agent review of any diff, with verified and triaged findings. With no argument it offers the tickets in review and diffs from the chosen plan's `baseline_revision`.
- Pick when: the code did not come from `fmad-build`; a PR or branch needs review; a build ran with review skipped or on the quick setting; after material fixes. Handing `fmad-build` its `built` plan also runs another review; a plan the user marked `done` is only context for new work. After an unattended run that sets `followup_review_recommended`, dispatch `fmad-build-auto` on the same ticket again; it goes straight to a fresh review pass.
- Not when: `fmad-build` just ran its full review on the same change. It is the same four lenses again. A run can take half an hour or more, and more than two rounds on one change usually points to a problem outside the change, such as weak planning or a messy codebase.
- Writes: a dated block in the plan's `## Code Review` section when it reviews a plan; otherwise findings stay in the chat. It never changes the ticket's `status`.

**`fmad-walkthrough`** — the human reviews a change block by block, at their own pace, with the agent as guide.
- Pick when: a person needs to understand and accept a change, after a build or for someone else's PR. It orders attention: intent first, then the broad strokes, then details.
- Not when: the user wants an automated bug hunt → `fmad-code-review`.
- Writes: `{output_folder}/{active_initiative}/walkthrough-<slug>/` holding `walkthrough-<slug>.md` and `walkthrough-<slug>-log.md`.

**`fmad-qa-generate-e2e-tests`** — generates API and end-to-end tests for features that already exist.
- Pick when: the project has a UI or API with little end-to-end coverage. It covers the happy path plus one or two error cases and runs the tests until they pass.
- Not when: the user wants unit tests for work in flight (`fmad-build` writes and runs tests for the edge cases its plan lists; ask for more in the build request), a review, or a test strategy.
- Writes: tests under `{project-root}/tests`, summary at `{output_folder}/{active_initiative}/test-summary-<slug>/test-summary-<slug>.md`. With no initiative active, this and the walkthrough folder go in `{output_folder}/`.

**`fmad-retrospective`** — judges a finished epic folder in the ticket tree as a whole against the epic's Done when and the initiative's requirements.
- Gives: sourced findings no single session could see (architecture drift, duplication, spec versus built), owned action items, and a verdict: accepted, accepted with open items, or rejected.
- Pick when: every ticket of the epic is `built`, `done`, or `dropped`, and especially after unattended runs. It reads `tickets.toml`, the epic file, and each ticket's plan. An unfinished ticket forces a rejected verdict; tickets still at `built` are listed for the user to mark done.
- Not when: one ticket or one diff is in question → `fmad-code-review` or `fmad-walkthrough`.
- Writes: `epic-<slug>-retrospective.md` in the epic folder, with the verdict in its frontmatter, and nothing else. It marks nothing done.
