from ansible.errors import AnsibleFilterError


def parse_servers(backups):
    return parse_servers_from_backups(backups)


def parse_servers_from_backups(backups, servers: dict = {}) -> dict:
    if not isinstance(backups, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type list."
        )

    for backup in backups:
        servers = parse_servers_from_backup(backup, servers)

    return servers


def parse_servers_from_backup(backup, servers: dict = {}) -> dict:
    if not isinstance(backup, dict):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type dict."
        )

    servers = parse_servers_from_repos(backup["repos"], servers)

    return servers


def parse_servers_from_repos(repos, servers: dict = {}) -> dict:
    if not isinstance(repos, list):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type list."
        )

    for repo in repos:
        servers = parse_servers_from_repo(repo, servers)

    return servers


def parse_servers_from_repo(repo, servers: dict = {}) -> dict:
    if not isinstance(repo, dict):
        raise AnsibleFilterError(
            "Input variable for this filter need to be of type dict."
        )

    if "hostname" in repo.keys():
        if repo["hostname"] in servers.keys():
            if repo["user"] in servers[repo["hostname"]].keys():
                servers[repo["hostname"]][repo["user"]].append(repo["path"])
            else:
                servers[repo["hostname"]][repo["user"]] = [repo["path"]]
        else:
            servers[repo["hostname"]] = {repo["user"]: [repo["path"]]}

    return servers


# Register the filters
class FilterModule(object):
    def filters(self):
        return {
            "parse_servers": parse_servers,
            "parse_servers_from_backup": parse_servers_from_backup,
            "parse_servers_from_backups": parse_servers_from_backups,
            "parse_servers_from_repo": parse_servers_from_repo,
            "parse_servers_from_repos": parse_servers_from_repos,
        }
