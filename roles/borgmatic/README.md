<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.borg.borgmatic

Install borgmatic on a client

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for borgmatic role

Longer descriptions.
Every list item is a new paragraph.

### Options for `main`

#### `borgmatic_compression`

Type: `str`, Default: `zstd`.

Compression to be used on the repositories.

#### `borgmatic_backups`

Type: list of dicts of `borgmatic_backups` [options](#options-for-main--borgmatic_backups), **required**.

#### `borgmatic_systemd_service_create`

Type: `bool`, Default: `True`.

Whether the borgmatic.service unit should be deployed or not. If set to `false` the borgmatic.service will be removed.

#### `borgmatic_systemd_service_options__override`

Type: `dict`, optional.

Options for the `[Service]` section in the borgmatic.service unit. Will be combined with the default options from `borgmatic_systemd_service_options__default` specified in vars/main.yaml.

#### `borgmatic_systemd_service_start`

Type: `bool`, Default: `False`.

Whether or not the borgmatic.service should be started or not. Setting this to `true` will create a backup. Can be useful to create ad-hoc backups with Ansible.

#### `borgmatic_systemd_timer_create`

Type: `bool`, Default: `True`.

Whether the borgmatic.timer unit should be deployed or not. Only has an effect if `borgmatic_systemd_service_create` is also `true`. If set to `false` the borgmatic.timer will be removed.

#### `borgmatic_systemd_timer_enable`

Type: `bool`, Default: `True`.

Whether the borgmatic.timer unit should be enabled or not.

#### `borgmatic_systemd_timer_options`

Type: `dict`, Default: `{"OnCalendar": "*-*-* 04:00:00"}`.

Options for the `[Timer]` section in the borgmatic.timer unit.

### Options for `main` > `borgmatic_backups`

- `after_actions` (Type: list of `str`, optional).

- `after_backup` (Type: list of `str`, optional).

- `after_check` (Type: list of `str`, optional).

- `after_compact` (Type: list of `str`, optional).

- `after_everything` (Type: list of `str`, optional).

  Actions to to after all backups.

- `after_extract` (Type: list of `str`, optional).

- `after_prune` (Type: list of `str`, optional).

- `before_actions` (Type: list of `str`, optional).

- `before_backup` (Type: list of `str`, optional).

- `before_check` (Type: list of `str`, optional).

- `before_compact` (Type: list of `str`, optional).

- `before_everything` (Type: list of `str`, optional).

  Actions to do before all backups.

- `before_extract` (Type: list of `str`, optional).

- `before_prune` (Type: list of `str`, optional).

- `exclude_patterns` (Type: list of `str`, optional).

  List of borg exclude patterns (see `borg help patterns`).

- `keep_daily` (Type: `int`, optional).

  Number of daily archives to keep.

- `keep_hourly` (Type: `int`, optional).

  Number of hourly archives to keep.

- `keep_minutely` (Type: `int`, optional).

  Number of minutely archives to keep.

- `keep_monthly` (Type: `int`, optional).

  Number of monthly archives to keep.

- `keep_secondly` (Type: `int`, optional).

  Number of secondly archives to keep.

- `keep_weekly` (Type: `int`, optional).

  Number of weekly archives to keep.

- `keep_within` (Type: `str`, optional).

  Keep all archives within this time interval.

- `keep_yearly` (Type: `int`, optional).

  Number of yearly archives to keep.

- `mariadb_databases` (Type: list of `dict`, optional).

  MariaDB databases to backup.

- `mongodb_databases` (Type: list of `dict`, optional).

  MongoDB databases to backup.

- `mysql_databases` (Type: list of `dict`, optional).

  MySQL databases to backup.

- `match_archives` (Type: `str`, optional).

- **`name`** (Type: `str`, **required**).

- `on_error` (Type: list of `str`, optional).

- `passphrase` (Type: `str`, optional).

- `skip_actions` (Type: list of `str`, optional).

  List of one or more actions to skip.

  _Choices:_ `init`, `compact`, `create`, `prune`, `check`

- `systemd_service_options_override` (Type: `dict`, optional).

  Override options for the systemd unit. Has higher precedence than `borgmatic_systemd_service_options__override`.

- `postgresql_databases` (Type: list of `dict`, optional).

  PostgreSQL databases to backup.

- **`source_directories`** (Type: list of `str`, **required**).

- `repos` (Type: list of dicts of `repos` [options](#options-for-main--borgmatic_backups--repos), optional).

- `sqlite_databases` (Type: list of `dict`, optional).

  SQLite databases to backup.

### Options for `main` > `borgmatic_backups` > `repos`

- `hostname` (Type: `str`, optional).

- `init` (Type: `bool`, Default: `False`).

- **`path`** (Type: `str`, **required**).

- `removable` (Type: `bool`, Default: `False`).

- `required_mount` (Type: `str`, optional).

  When `init` is `true` and the folder specified by this variable is a mount, then a local repository will be initialized in it. This variable has no effect if `init` is set to `false`.

- `user` (Type: `str`, optional).

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.borg][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://github.com/lingfra/ansible-collection-lingfra-borg
<!-- END_ANSIBLE_DOCS -->
