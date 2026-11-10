<!-- BEGIN_ANSIBLE_DOCS -->
# Ansible Role: lingfra.borg.borg_install

Installs borg backup packages.

## Supported Platforms

Not specified.

## Entrypoint `main` - Main entry point for borg_install role

Installs borg backup packages on a host.
Depending on whether the target host is a borg server or a borg client (borgmatic), it is possible to customize the installed packages by adjusting [`borg_install_add_client_pkgs`](#borg_install_add_client_pkgs).

### Options for `main`

#### `borg_install_add_client_pkgs`

Type: `bool`, Default: `False`.

Whether or not to install packages that are only needed on a borg client.

## Dependencies

None.

## Project Information

This role is part of the Ansible collection [lingfra.borg][collection_url].
For more information, see the collections [README](../../README.md) file.

[collection_url]: https://github.com/lingfra/ansible-collection-lingfra-borg
<!-- END_ANSIBLE_DOCS -->
