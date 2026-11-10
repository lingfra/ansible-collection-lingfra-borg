<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.borg.borg_server

Configures a central repository server for BorgBackup

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for borg_server role

This is the main entry point of the borg_server role.
If the role is started from this entry point the full configuration of a central borg repository server is executed. This includes checking the host configuration and doing the actual configuration on the host.

### Options for `main`

#### `borg_server_repo_pool_create`

Type: `bool`, Default: `True`.

Whether or not the repo pool directories should be created it is is absent.

#### `borg_server_repo_pool_restrict`

Type: `bool`, Default: `True`.

Whether or not the repo pool directories should be restricted. If `true`, it restricts the repo pool directory to `0701`, so that all users can cd into it, but can't see its contents. If `false`, the role sets the permissions to `0755`.

#### `borg_server_repo_pools`

Type: `list of dicts of 'borg_server_repo_pools' options`, **required**.

List of repo pool directories

**Options:**

- `create` (Type: `bool`, optional).

  Overrides [`borg_server_repo_pool_create`](#borg_server_repo_pool_create) for this repo pool.

- **`path`** (Type: `str`, **required**).

  Directory under which the borg repositories are created.

- **`repos`** (Type: `list of dicts of 'repos' options`, **required**).

  List with the repositories to be created / managed in this repo pool.

  **Options:**

  - **`name`** (Type: `str`, **required**).

    The name of the borg repository. Must be unique.

  - `group` (Type: `str`, optional).

    The group of the borg repository. Default to owner.

  - **`owner`** (Type: `str`, **required**).

    The owner (user) of the borg repository. Need to exist, have a valid login shell and a home directory, which is not a borg repo directory.

- `required_mount` (Type: `str`, optional).

  Path to a folder, which need to be a mount. Without it no actions for this repo root are taken. Useful for removable backups.

- `restrict` (Type: `bool`, optional).

  Overrides [`borg_server_repo_pool_restrict`](#borg_server_repo_pool_restrict) for this repo pool.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.borg][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://github.com/lingfra/ansible-collection-lingfra-borg
<!-- END_ANSIBLE_DOCS -->
