# Security metrics and ROI

Use a fixed time window and name the source (alert export, pull request
timeline, ruleset log, or manual worksheet). Never infer precision the source
does not provide.

| Metric | Definition | Workshop measurement |
| --- | --- | --- |
| MTTD | Mean time from introduction to detection | First-seen timestamp to alert timestamp |
| MTTR | Mean time from detection to verified remediation | Alert timestamp to merged/fixed evidence |
| Alert aging | Open time by severity and owner | Age at triage and at closure |
| Coverage | Repositories, branches, or workflows with the control | Covered / in-scope, with denominator |
| Bypasses | Allowed or observed control bypasses | Count, reason, approver, and follow-up |
| SLA | Findings remediated within target | Within-SLA / eligible findings |
| Export | Reproducible evidence | CSV/API export or dated screenshot with query scope |

For ROI, pair a leading measure (coverage or policy adoption) with an outcome
measure (MTTR, escaped findings, or bypass rate). State assumptions such as
engineer hours saved; do not convert a workshop result into a financial claim
without a cost baseline.
