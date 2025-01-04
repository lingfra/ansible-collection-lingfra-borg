from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.action import ActionBase


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
            }
        )

        result = {"changed": False, **new_module_args}

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
