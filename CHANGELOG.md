# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-01-29

This release initially adds the borg_server role to configure a central
repository server for borg backup. The role supports the following features:

- Multiple pools (`1` pool can contain `n` borg repositories)
- Optional automatic repository pool creation and / or restriction
  - Can be specified per repository
- Optionally require a specific mount for configuration of a repository pool
- Set user and group per repository

See [0.3.0] for the full list of changes.

## [0.2.0] - 2025-01-29

This release is mostly about refactoring the collection and preparing for future
releases. Notable changes:

- Rename role borginstall to borg_install (breaking)
- Update namespace from lingling9000 to lingfra (breaking)
- Update documentations of collection and borg_install

See [0.2.0] for the full list of changes.

## [0.1.0] - 2024-09-01

### Added

- Basic borginstall role.
- `install_borg.yaml` playbook.
- Molecule test for borginstall role and playbook.

[0.3.0]: https://github.com/lingfra/ansible-collection-lingfra-borg/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/lingfra/ansible-collection-lingfra-borg/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/lingfra/ansible-collection-lingfra-borg/compare/ce7319bf20...v0.1.0
