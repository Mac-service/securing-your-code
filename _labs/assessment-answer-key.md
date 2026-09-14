# Assessment answer key

1. Code scanning with CodeQL.
2. Dependency Review; it evaluates the proposed dependency diff and known
   advisories, but does not prove that every transitive risk, runtime behavior,
   build output, or newly published advisory is absent.
3. Stop using it, revoke it at the provider, rotate dependent credentials, and
   notify the owner/security team. Removing the file is not sufficient.
4. Detect -> triage -> remediate -> enforce -> measure.
5. It makes the referenced action content immutable and reviewable, reducing
   tag-retargeting and unexpected upstream changes. It does not make an action
   trustworthy by itself.
6. SPDX or CycloneDX; an SBOM alone does not prove exploitability, provenance,
   runtime reachability, or that the listed artifact was not altered.
7. A pull request shows the required check as a blocking rule, and a failing
   check prevents merge until the finding is fixed or an approved exception is
   recorded.
8. Mean time to detect and mean time to remediate.
9. Keyboard-only instructions, text alternatives to screenshots, paired work,
   downloadable labs, or a text-only worksheet.
10. Temporary changes are removed, no credentials remain exposed, local copies
    are cleaned up, and the documentation validator passes.

Accept equivalent answers that preserve the safety boundary and distinguish a
signal, a control, and evidence of outcome.
