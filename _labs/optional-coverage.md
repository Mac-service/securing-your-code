# Optional container, IaC, and API coverage

These exercises are additive and can be completed without credentials or
changing Juice Shop application code.

| Surface | Safe exercise | Evidence |
| --- | --- | --- |
| Container | Review the existing Dockerfile for a pinned base image, non-root user, and a scan step. | Checklist plus scan result |
| IaC | Inspect a disposable workflow or manifest for excessive permissions and unpinned actions. | Before/after diff |
| API | Use the existing API test suite or an OpenAPI view to identify one input-validation boundary. | Test result and triage note |

When adding an Actions step, use a verified full SHA and least privilege:

```yaml
permissions:
  contents: read
  security-events: write

steps:
  - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
    with:
      persist-credentials: false
```

Grant `security-events: write` only to the job that uploads a security result;
keep build and test jobs read-only. Do not add registry logins, cloud
credentials, self-hosted runners, or production endpoints to the workshop.
