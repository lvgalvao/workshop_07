import pandas as pd

from app.ETL.transformation import consolidate_dataframes


def test_consolidate_dataframe():
    """função de teste da função consolidate_dataframe"""

    # Arrange
    dataframes = [
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}),
        pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]}),
    ]

    # Act
    result = consolidate_dataframes(dataframes)

    # Assert
    expected = pd.DataFrame({'col1': [1, 2, 5, 6], 'col2': [3, 4, 7, 8]})

    assert result.equals(expected)
