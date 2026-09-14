# Workshop map

This map turns the labs into a role-based workshop. Use a temporary repository
and the deliberately fake fixtures in [`secrets.txt`](../secrets.txt); never use
production code, credentials, or personal data.

## Learning objectives

By the end of the workshop, learners can:

1. Enable GHAS features and explain which signal each feature produces.
2. Triage a code, dependency, and secret alert using severity, reachability,
   ownership, and due date.
3. Fix a finding, verify the fix, and enforce the control with a ruleset.
4. Describe SBOM, provenance/attestation, dependency pinning, and the limits of
   Dependency Review.
5. Choose measurable security outcomes: MTTD, MTTR, coverage, alert aging,
   bypasses, and SLA adherence.

## Personas and prerequisites

| Persona | Prior knowledge | Best contribution |
| --- | --- | --- |
| Developer | Git and pull requests | Fix the vulnerable change and add tests |
| Security engineer | Alert triage and threat modeling | Classify risk and set acceptance criteria |
| Platform/DevOps engineer | Actions and deployment basics | Pin actions and enforce workflow policy |
| Instructor/manager | Workshop facilitation | Keep time, capture metrics, and run the reset |

All participants need a browser, Git, and access to a disposable repository. An
organization owner or security-manager is needed for the organization-level
views in Lab 6; otherwise use the repository-scoped path.

## Recommended paths

### 90 minutes: signal to control

| Minutes | Activity | Evidence of completion |
| ---: | --- | --- |
| 0-10 | Safety briefing, baseline assessment | Baseline score recorded |
| 10-25 | Lab 1: enable features | Code scanning, Dependabot, and secret protection visible |
| 25-45 | Lab 2: review and triage alerts | One triage note per alert type |
| 45-65 | Lab 3: CodeQL plus ruleset | Vulnerable PR blocked, fixed PR passes |
| 65-80 | Lab 4 or 5: dependency or secret protection | One blocked change and documented safe reset |
| 80-90 | Post-assessment and retrospective | Acceptance criteria met or follow-up assigned |

### 180 minutes: full detect-to-measure journey

Use the 90-minute path, then add:

| Minutes | Activity | Evidence of completion |
| ---: | --- | --- |
| 90-115 | Lab 4: Dependency Review | Dependency change assessed and limitation recorded |
| 115-135 | Lab 5: Secret scanning | Fake fixture blocked; no real secret created |
| 135-150 | Lab 6: Security Overview and metrics | Export or screenshot of agreed measures |
| 150-170 | [Capstone](capstone.md) | Finding moves through all five control stages |
| 170-180 | Post-assessment, reset, and feedback | Score, metrics, and clean repository |

Optional container, IaC, and API exercises are in
[`optional-coverage.md`](optional-coverage.md). Advanced CodeQL and custom
patterns remain useful extensions when the group has more time.

## Lab index

The canonical sequence is:

1. [Feature introduction](lab1.md)
2. [Alert review](lab2.md)
3. [Code scanning and enforcement](lab3.md)
4. [Dependency Review](lab4.md)
5. [Secret scanning](lab5.md)
6. [Security Overview](lab6.md)
7. [Advanced CodeQL](lab7-ec.md)
8. [Custom secret patterns](lab8-ec.md)
9. [Capstone](capstone.md)

The instructor should use the [runbook](instructor-runbook.md) and complete the
[reset checklist](instructor-runbook.md#reset-checklist) before handing the
repository to the next cohort.
