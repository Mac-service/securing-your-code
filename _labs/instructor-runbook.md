# Instructor runbook

## Before the session

- Create a disposable repository from this template and record its URL and
  default branch.
- Confirm the plan supports the features in the selected path; feature
  availability varies by account, organization, repository visibility, and
  license.
- Prepare one facilitator-only copy of the [assessment](assessment.md) and
  [answer key](assessment-answer-key.md).
- Test the browser, GitHub Actions minutes, and any optional local container.
- Assign one learner to each persona in the
  [workshop map](workshop-map.md), or let individuals rotate roles.
- Do not pre-create tokens, cloud resources, or credentials. Use fake fixtures
  only.

## Facilitation flow

1. State the safety boundary: temporary repository, no real secrets, and no
   production changes.
2. Collect the baseline assessment without coaching. Record score and time.
3. Demonstrate where to find the signal, then let learners perform the change.
4. Ask learners to explain *why* an alert is actionable before they fix it.
5. Require evidence at each gate: alert URL, pull request check, ruleset state,
   or exported metric. Screenshots are acceptable when an API export is not.
6. Pause for plan or permission differences instead of asking learners to
   bypass a control.
7. Run the capstone only after the group can distinguish detection from
   enforcement.
8. Collect the post-assessment and compare results to the acceptance criteria.

## Instructor prompts

- “What asset is affected, and what is the exploit path?”
- “Which signal proves the fix, and which control prevents recurrence?”
- “What does this check *not* see?”
- “Who owns the alert, what is the SLA, and how will we measure aging?”
- “What is the safe rollback if the rule blocks unrelated work?”

## Reset checklist

Run this checklist for every cohort. Record `done`, `not applicable`, or an
explicit owner and due date; do not silently skip a step.

- [ ] Close, merge, or delete workshop pull requests.
- [ ] Delete learner branches and temporary forks.
- [ ] Remove temporary branch rulesets and required checks.
- [ ] Disable optional workflows and scheduled scans created during the session.
- [ ] Remove test issues, discussions, webhooks, environments, and deploy keys.
- [ ] Confirm no real credentials were created or pasted. If one was exposed,
      stop, revoke, rotate dependents, and notify the owner/security team.
- [ ] Remove local clones, downloaded artifacts, and browser downloads that
      contain workshop data.
- [ ] Export only aggregate assessment/metric results; do not retain personal
      data without a documented purpose.
- [ ] Re-run `python3 scripts/validate_docs.py` and verify the repository is
      clean before reuse.

## Accessibility and low-bandwidth delivery

Offer a keyboard-only path, read all image content aloud, and provide the
Markdown steps as the source of truth rather than requiring screenshots. Avoid
color-only alert descriptions; name severity and status text. Share a
downloadable copy of the labs and a text-only metric worksheet before class.
For slow connections, pair learners, use the UI only for the required state
change, and defer optional scans until the group has a result to discuss.

For localization, keep product names and alert titles in English when they must
match the GitHub UI, but explain them in the learner's language. Prefer short
sentences, ISO dates, and explicit time zones. Do not translate code, action
identifiers, SHAs, or URLs.
