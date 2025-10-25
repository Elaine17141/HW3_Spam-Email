## ADDED Requirements

### Requirement: Project scaffold and CI
The repository SHALL include a minimal, documented project scaffold and a CI workflow that runs linting and tests on pull requests.

#### Scenario: Developer can run lint and tests locally
- **GIVEN** a developer has cloned the repository and installed dependencies
- **WHEN** they run `npm run lint` and `npm test`
- **THEN** lint completes without critical errors and unit tests run (at least a sanity test) and exit 0

#### Scenario: CI validates lint and tests on PR
- **GIVEN** a pull request is opened against `develop` or `main`
- **WHEN** the CI workflow runs
- **THEN** the workflow runs lint and test steps and reports pass/fail status on the PR
