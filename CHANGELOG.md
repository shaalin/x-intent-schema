# Changelog

All notable changes to the x-intent schema will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-19

### Added

- Initial release of x-intent schema v1
- Effect kinds: `read`, `mutate`, `delete`, `notify`, `external_call`, `financial_transfer`, `provision`, `compute`
- Risk levels: `low`, `medium`, `high`
- Data classification: `public`, `internal`, `confidential`, `restricted`
- PII indicator for effects
- Documentation: overview, semantics, publishing guide
- Example intents: minimal, read-only, draft-mutate, external-financial-high-risk
- GitHub Actions workflow for schema validation
