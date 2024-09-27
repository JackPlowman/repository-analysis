from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pygments import lexers
from pygments.util import ClassNotFound
from structlog import get_logger, stdlib

if TYPE_CHECKING:
    from .repository_languages import RepositoryLanguages
logger: stdlib.BoundLogger = get_logger()


def analyse_programming_languages(file_path: str, repository_languages: RepositoryLanguages) -> RepositoryLanguages:
    """Analyse the programming languages in a file.

    Args:
        file_path (str): The path to the file.
        repository_languages (RepositoryLanguages): The repository languages.

    Returns:
        RepositoryAnalysis: The repository analysis.
    """
    guess = guess_language_from_file(file_path)
    if guess:
        logger.debug("Guessed language", guess=guess, file_path=file_path)
        repository_languages.add_file(language_name=guess, file_path=file_path)
    return repository_languages


def guess_language_from_file(file_path: str) -> str | None:
    """Guess the programming language from the file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str | None: The programming language, or None if no language is found.
    """
    try:
        with Path.open(file_path) as file:
            lexer = lexers.guess_lexer_for_filename(file_path, file.read())
            return lexer.name
    except (ClassNotFound, UnicodeDecodeError):
        logger.debug("Could not guess language from file", file_path=file_path)
        return None
