from __future__ import absolute_import, division, print_function

__metaclass__ = type
from pathlib import Path

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError


def is_subpath(base_path: str, compare_path: str):
    """
    This function checks if one path is a subpath of another.
    """
    base = Path(base_path).resolve()
    compare = Path(compare_path).resolve()

    if compare == base or compare.is_relative_to(base):
        return True
    else:
        return False


def check_required_mount_availability(
    required_mount_path: str, available_mounts: list[str]
):
    """
    This function checks if the required_mount is available.

    :arg required_mount_path: Path of the mount, which need to be available.
    :arg available_mounts: List of mount paths, which are available on the host.
    :returns: Boolean value.
    """
    for compare_path in available_mounts:
        if is_subpath(required_mount_path, compare_path):
            return True
    else:
        return False


class ActionModule(ActionBase):
    """
    This action plugin is used in pre-checks for the borg_server role.

    It takes a required 'path' as parameter and optionally a bool 'create',
    which defaults to 'true'. It checks if the directory exists or if it is
    allowed to be created. If both are false, this module will fail.
    """

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        _, new_module_args = self.validate_argument_spec(
            argument_spec={
                "path": {"type": "str", "required": True},
                "create": {"type": "bool", "default": True},
                "required_mount": {"type": "str", "required": False},
            }
        )

        result = {"changed": False, **new_module_args}

        required_mount = new_module_args.get("required_mount", False)
        if required_mount:
            try:
                ansible_mounts = task_vars["ansible_mounts"]
            except KeyError:
                raise AnsibleError(
                    "The Ansible fact 'ansible_mounts' is not available."
                )

            mounted_folders = [m["mount"] for m in ansible_mounts]

            if not check_required_mount_availability(required_mount, mounted_folders):
                result["msg"] = (
                    f"The required mount '{required_mount}' for repo pool "
                    f"'{new_module_args['path']}' is not available. Therefore, "
                    f"this repo pool will be skipped."
                )
                return result

        module_stat_result = self._execute_module(
            module_name="ansible.builtin.stat",
            module_args={"path": new_module_args["path"]},
            task_vars=task_vars,
        )

        stat = module_stat_result.get("stat", {})
        result["stat"] = stat

        if not stat.get("exists"):
            if not new_module_args["create"]:
                result["failed"] = True
                result["msg"] = (
                    f"The repo pool directory '{new_module_args['path']}' "
                    "does not exist and should not be created. Refer to "
                    "the documentation for more information."
                )
            else:
                result["msg"] = (
                    f"The repo pool directory '{new_module_args['path']}' "
                    "does not exist but is allowed to be created."
                )

        else:
            result["msg"] = (
                f"The repo pool directory '{new_module_args['path']}' exists."
            )

        return result
