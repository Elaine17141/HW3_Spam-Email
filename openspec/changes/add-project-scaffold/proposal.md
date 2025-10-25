## Why
The repository currently contains OpenSpec files but lacks a documented, runnable project scaffold and CI pipeline. Adding an initial project scaffold (README, basic src layout, lint/test/ci config) will make it easier for contributors to start development, follow conventions, and validate changes.

## What Changes
- ADDED: A project scaffold that includes recommended tech stack, linting, formatting, and CI workflows.
- ADDED: Basic README and developer quickstart.
- ADDED: GitHub Actions workflow to run lint and tests on PRs.

## Impact
- Affected specs: none (this is an infrastructure and developer-experience change)
- Affected code: repository root (README, .github/workflows/, package.json or similar), `openspec/project.md` updated to define conventions.

## Migration
No data migration required. Developers will need to run initial install steps documented in the README.

## Non-Goals
- This proposal does not implement application business features (APIs, frontend pages).
- It does not integrate production infra (cloud deployment) beyond CI actions.
