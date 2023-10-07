import pandas as pd
import pytest


@pytest.fixture
def df_fixture():
    return pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})


@pytest.fixture
def output_fixture():
    return ('data/output/', 'output.xlsx')


from app.ETL.load import load_to_excel


def test_load_to_excel(df_fixture, output_fixture):
    """Test using Arrange, Act, Assert pattern."""
    output_folder, output_file = output_fixture

    # Arrange
    expected = 'Arquivo salvo com sucesso'

    # Act salve o result em um temp file

    result = load_to_excel(df_fixture, output_folder, output_file)

    # Assert
    assert result == expected
