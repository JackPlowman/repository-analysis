from __future__ import annotations

from dataclasses import dataclass, field

# Consider typed dicts instead of this class


@dataclass
class RepositoryLanguages:
    """The file language types generated from a repository."""

    languages: dict[str, dict[str, int | str | list[str]]] = field(default_factory=dict)
    # example: {"Python": {"file_count": 1, "file_paths": ["file.py"]}}  # noqa: ERA001

    def add_file(self, language_name: str, file_path: str) -> None:
        """Add a file to the repository languages.

        Args:
            language_name (str): The language name.
            file_path (str): The file path.
        """
        if language_name not in self.languages:
            self.languages[language_name] = {"file_count": 1, "file_paths": [file_path]}
            return
        language_file_count = self.languages[language_name]["file_count"]
        self.languages[language_name]["file_count"] = language_file_count + 1
        self.languages[language_name]["file_paths"].append(file_path)

    def __repr__(self) -> str:
        """Return a string representation of the repository languages."""
        languages_strings = [f"{language}: {self.languages[language]['file_count']}" for language in self.languages]
        language_string = ", ".join(languages_strings)
        return f"RepositoryLanguages(languages={language_string})"

    def get_data(self) -> dict[str, int]:
        """Return the data for the repository languages."""
        return {language: self.languages[language]["file_count"] for language in self.languages}
