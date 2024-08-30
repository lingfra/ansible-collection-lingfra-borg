# Ansible Role: borginstall

Installs [BorgBackup](https://www.borgbackup.org/).

## Features

## Limitations

## Requirements

None.

## Role Variables

### External Variables

### Public Role Variables

### Internal Role Variables

## Tags

To simplify the testing of this role, all tasks are tagged. See the Ansible
documentation on
[Tags](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html)
for reference. The following tags are available:

- `checks`: Added to all tasks that perform checks or gather information for
subsequent checks. This tag contains a superset of tasks whose tag begins with
`checks-`.
- `checks-syntax`: Added only to tasks that perform simple syntax checks on
variables, such as whether they are defined and have the correct data type.
- `checks-host-config`: Added to tasks that verify that the host configuration
meets the requirements of this role for further configuration.
- `configure`: Added to tasks that actually make or prepare changes on the
target host.

## Dependencies

None.

## Example Playbook

**Playbook (`playbook.yaml`)**:

```yaml
- name: Configure
  hosts: somehost.mydomain.tld
  tasks:
    - name: Include role borginstall
      ansible.builtin.include_role:
        name: lingling9000.borg.borginstall
      vars:
        borginstall_add_client_pkgs: true
```
