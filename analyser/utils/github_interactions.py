from __future__ import annotations

from os import getenv
from pathlib import Path

from git import Repo
from github import Github, PaginatedList, Repository
from structlog import get_logger, stdlib

logger: stdlib.BoundLogger = get_logger()


def clone_repo(owner_name: str, repository_name: str) -> str:
    """Clone the repository and return the path to the repository.

    Uses existing clone if available in analyser/cloned_repositories.

    Args:
        owner_name (str): The owner name of the repository.
        repository_name (str): The repository name.

    Returns:
        str: The path to the repository.
    """
    file_path = f"cloned_repositories/{repository_name}"
    if not Path.exists(Path(file_path)):
        repo_url = f"https://github.com/{owner_name}/{repository_name}.git"
        Repo.clone_from(repo_url, Path(file_path))
        logger.info("Cloned repository", owner_name=owner_name, repository_name=repository_name)
    return file_path


def retrieve_repositories() -> PaginatedList[Repository]:
    """Retrieve the list of repositories to analyse.

    Returns:
        PaginatedList[Repository]: The list of repositories.
    """
    repository_owner = getenv("INPUT_REPOSITORY_OWNER", "")
    if repository_owner == "":
        msg = "repository_owner environment variable is not set."
        raise ValueError(msg)
    token = getenv("github_token", "")
    if token == "":
        github = Github()
        logger.debug("Using unauthenticated GitHub API")
    else:
        github = Github(token)
        logger.debug("Using authenticated GitHub API")
    repositories = github.search_repositories(query=f"user:{repository_owner} archived:false")
    logger.info(
        "Found repositories",
        repositories_count=repositories.totalCount,
        repositories=[repository.full_name for repository in repositories],
    )
    return repositories
