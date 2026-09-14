# Troubleshooting matrix

| Symptom | Likely cause | Safe response |
| --- | --- | --- |
| Security setting is unavailable | Plan, visibility, role, or license limitation | Use the repository-scoped path and label the limitation |
| Check is queued too long | Runner capacity or Actions minutes | Capture the queue time; do not weaken the ruleset |
| Alert is absent | Scan has not completed or path is unsupported | Confirm workflow status and scan scope before concluding “clean” |
| Dependency Review is green | No known advisory in the diff | Explain that green is not proof of safe runtime behavior |
| Secret push is blocked | Push protection matched a fixture | Use the fake fixture procedure; never bypass with a real secret |
| Action SHA is rejected | Typo or unverified release reference | Verify upstream release and review the changed SHA |
| Browser is slow | Low bandwidth or large screenshots | Use the text lab, pair learners, and defer optional scans |
| Learner cannot use a mouse | Accessibility need | Offer keyboard-only steps and a facilitator-operated demonstration |
| Reset leaves a check failing | Temporary ruleset/workflow remains | Follow the reset checklist and record the owner of any exception |
