from dataclasses import dataclass
from pathlib import Path

from structlog import get_logger, stdlib

from .programming_language_analysis import analyse_programming_languages
from .repository_languages import RepositoryLanguages

logger: stdlib.BoundLogger = get_logger()


@dataclass
class RepositoryAnalysis:
    """A repository analysis."""

    file_count: int
    languages: RepositoryLanguages


def analyse_repository(path_to_repo: str) -> RepositoryAnalysis:
    """Analyse a repository.

    Args:
        path_to_repo (str): The path to the repository.
    """
    file_count = 0
    languages = RepositoryLanguages()
    # Count the number of files
    iterator = Path(path_to_repo).walk()
    for root, _dirs, files in iterator:
        for file in files:
            file_count += 1
            file_path = f"{root.__str__()}/{file}"
            logger.debug("Analysing file", file_path=file_path)
            languages = analyse_programming_languages(file_path, languages)

    return RepositoryAnalysis(file_count, languages)
