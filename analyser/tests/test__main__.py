from unittest.mock import MagicMock, patch

import pytest

from analyser.application.__main__ import main

FILE_PATH = "analyser.application.__main__"


@patch(f"{FILE_PATH}.create_statistics")
def test_main(mock_create_statistics: MagicMock) -> None:
    # Act
    main()
    # Assert
    mock_create_statistics.assert_called_once_with()


@patch(f"{FILE_PATH}.create_statistics")
def test_main__error(mock_create_statistics: MagicMock) -> None:
    # Arrange
    mock_create_statistics.side_effect = Exception("Test")
    # Act
    with pytest.raises(Exception, match="Test"):
        main()
    # Assert
    mock_create_statistics.assert_called_once_with()
