# Lab requirements

## Accounts and permissions

- A GitHub account that can create repositories and pull requests.
- A **public** repository for personal accounts. Organization repositories can
  be private or internal when the organization plan includes the required
  GitHub Advanced Security features.
- Repository administrator access to enable security features, create
  rulesets, and configure Actions.
- Organization owner or security-manager access is required for Lab 6. Lab 6
  is not available for a repository owned only by a personal account.
- GitHub Advanced Security features are subject to plan and repository
  visibility limits. Check the current [GitHub feature
  availability](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)
  before the workshop.

## Local setup

- Git and a current web browser.
- Docker Desktop, or Node.js 20 and npm, if you want to run the included
  Juice Shop locally. The labs can otherwise be completed in the GitHub UI.
- Permission to create a temporary fork or branch. Do not use a production
  repository or production credentials.

## Safety and cleanup

- Never create, paste, or commit a real personal access token, API key,
  password, or other credential for this workshop. `secrets.txt` contains
  deliberately fake fixtures only.
- Use temporary repositories, branches, rulesets, and organization settings.
  Delete the temporary repository after the workshop, or reset its visibility
  and security settings according to your organization's policy.
- Close or merge workshop pull requests, delete test branches, remove
  temporary rulesets, and disable optional workflows when finished.
- If a real credential is accidentally exposed, stop using it immediately,
  revoke it at the issuing provider, rotate any dependent credentials, and
  notify the repository owner/security team. Removing the file or closing a
  pull request does not make the credential safe.

For the sequence of exercises, return to the [labs index](README.md).
