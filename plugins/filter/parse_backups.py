import re

from ansible.errors import AnsibleFilterError


def parse_actions(backup, scope) -> dict:
    if not scope in ["after", "before"]:
        raise AnsibleFilterError("Actions scope need to be 'before' or 'after'.")

    actions = [
        "actions",
        "backup",
        "prune",
        "compact",
        "check",
        "extract",
    ]

    result = {}

    for action in actions:
        option_name = f"{scope}_{action}"
        if option_name in backup.keys():
            result[option_name] = backup[option_name]

    return result


def parse_databases_integrations(backup) -> list:
    databases = [
        "mariadb",
        "mongodb",
        "mysql",
        "postgresql",
        "sqlite",
    ]
    databases_integrations = []

    for database in databases:
        option_name = f"{database}_databases"
        if option_name in backup.keys():
            databases_integrations.append(
                {"key": option_name, "value": backup[option_name]}
            )

    return databases_integrations


def parse_retention_policy(backup) -> dict:
    retention_scopes = [
        "secondly",
        "minutely",
        "hourly",
        "daily",
        "weekly",
        "monthly",
        "yearly",
        "within",
    ]
    retention_defaults = {
        "keep_hourly": 24,
        "keep_daily": 14,
        "keep_weekly": 12,
        "keep_monthly": 24,
    }
    retention_policy = {}

    for scope in retention_scopes:
        option_name = f"keep_{scope}"
        if option_name in backup.keys():
            retention_policy[option_name] = backup[option_name]
        elif option_name in retention_defaults.keys():
            retention_policy[option_name] = retention_defaults[option_name]

    return retention_policy


def compose_repo_label(repo_location):
    repo_label = repo_location.replace("ssh://", "")

    return re.sub("[^a-zA-Z0-9_]", "_", repo_label)


def compose_location(repo):
    if "user" in repo.keys() and "hostname" in repo.keys():
        return f"ssh://{repo['user']}@{repo['hostname']}{repo['path']}"
    else:
        return f"{repo['path']}"


def parse_location(repo):
    if not isinstance(repo, dict):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type dict."
        )

    if "location" in repo.keys():
        return repo["location"]
    else:
        return compose_location(repo)


def parse_repo(repo, backup):
    result = {
        "after": parse_actions(backup, "after"),
        "before": parse_actions(backup, "before"),
        "databases_integrations": parse_databases_integrations(backup),
        "exclude_patterns": backup.get("exclude_patterns", None),
        "init": repo.get("init", False),
        "location": parse_location(repo),
        "match_archives": backup.get("match_archives", None),
        "on_error": backup.get("on_error", None),
        "passphrase": backup["passphrase"],
        "removable": repo.get("removable", False),
        "retention_policy": parse_retention_policy(backup),
        "skip_actions": backup.get("skip_actions", None),
        "source_directories": backup["source_directories"],
    }

    result["label"] = compose_repo_label(result["location"])

    return result


def parse_backup(backup):
    if not isinstance(backup, dict):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type dict."
        )

    result = {
        "after_everything": backup.get("after_everything", None),
        "before_everything": backup.get("before_everything", None),
        "name": backup["name"],
        "passphrase": backup["passphrase"],
        "repos": [],
        "systemd_service_options_override": backup.get(
            "systemd_service_options_override", {}
        ),
    }

    for repo in backup["repos"]:
        result["repos"].append(parse_repo(repo, backup))

    return result


def parse_backups(backups):
    if not isinstance(backups, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type list."
        )

    result = []

    for backup in backups:
        result.append(parse_backup(backup))

    return result


# Register the filters
class FilterModule(object):
    def filters(self):
        return {
            "parse_backup": parse_backup,
            "parse_backups": parse_backups,
            "parse_location": parse_location,
        }
