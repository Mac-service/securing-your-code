# Supply-chain depth

This extension is discussion-first and uses no credentials.

## Concepts to demonstrate

- **SBOM:** generate a CycloneDX or SPDX inventory for the workshop artifact;
  compare direct and transitive components and record the generation time.
- **Provenance and attestations:** explain which workflow built an artifact,
  from which commit, with which inputs. An attestation is evidence, not a
  guarantee that the source or dependency is safe.
- **Dependency pinning:** review lockfiles and immutable versions. Pin
  reusable Actions to a full commit SHA and retain a human-readable version
  comment for review.
- **Dependency Review limits:** it focuses on the proposed dependency diff and
  known advisories. It does not replace CodeQL, malware analysis, SBOM review,
  runtime testing, provenance verification, or future advisory monitoring.

## Safe minimal-permission example

The following is a teaching snippet. Replace the example SHA only after
verifying the intended release in the upstream repository; do not paste a
token or cloud credential.

```yaml
name: supply-chain-evidence
on:
  pull_request:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  evidence:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          persist-credentials: false
      - name: Generate a local SBOM
        run: npm run sbom:json
```

The workflow intentionally has no write permission, deployment step, secret,
or cloud login. A production attestation workflow needs a separately reviewed
trust model and should grant only the narrowly required attestations
permission.
