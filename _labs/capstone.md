# Capstone: detect -> triage -> remediate -> enforce -> measure

## Scenario

You are the security engineer for a disposable Juice Shop-derived repository.
An application change introduces a CodeQL finding, a dependency update has a
known advisory, and a fake secret fixture is committed on a test branch. No
cloud account or real credential is needed.

## Procedure

1. **Detect:** open the CodeQL, Dependabot/Dependency Review, and secret
   scanning signals. Record alert URL, rule or advisory, affected path, and
   first-seen time.
2. **Triage:** assign an owner, severity, exploitability/reachability note, and
   target SLA. Mark which signal is authoritative and which evidence is
   missing.
3. **Remediate:** fix the code or dependency in a pull request and remove the
   fake fixture. Do not test a real secret. Link the fix to the alert.
4. **Enforce:** require the relevant security check in a temporary branch
   ruleset. Demonstrate one blocked pull request and one passing pull request.
5. **Measure:** record MTTD, MTTR, alert age at closure, check coverage,
   bypass count, and SLA status for the exercise. State the source and time
   window for every value.

## Acceptance evidence

The capstone passes when the learner has five linked artifacts (one per stage),
the vulnerable change cannot merge while the check fails, and the metrics sheet
contains no invented values. An unavailable organization feature may be
replaced with a repository-scoped equivalent and must be labeled as a
limitation.

## Debrief

- Which alert was actionable first, and why?
- Where could a bypass occur?
- What did Dependency Review not establish?
- Which metric would persuade a manager to fund the control?
- What would you automate next?
