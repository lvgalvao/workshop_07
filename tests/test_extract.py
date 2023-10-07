import os

import pandas as pd
import pytest

from app.ETL.extract import extract_from_excel

# Sample data for testing
df1 = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
df2 = pd.DataFrame({"A": [4, 5, 6], "B": ["d", "e", "f"]})

@pytest.fixture
def mock_input_folder(tmpdir):
    """
    Criação de um fixture para criar uma pasta de entrada de teste.
    """
    # Criando arquivos Excel de exemplo para testes
    input_folder = tmpdir.mkdir("input_folder")
    df1.to_excel(
        input_folder.join("file1.xlsx"), index=False
    )  # Retirado engine='openpyxl'
    df2.to_excel(
        input_folder.join("file2.xlsx"), index=False
    )  # Retirado engine='openpyxl'
    return str(input_folder)


@pytest.fixture
def mock_output_folder(tmpdir):
    """Criação de um fixture para criar uma pasta de saída de teste."""""
    return str(tmpdir.mkdir("output_folder"))


def test_extract(mock_input_folder):
    """Test the extraction of data from the input folder."""
    extracted_data = extract_from_excel(mock_input_folder)
    assert len(extracted_data) == 2  # Expecting two DataFrames
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)


def test_extract_no_files(tmpdir):
    """Test extraction functionality with an empty input folder."""
    # Criando uma pasta vazia
    empty_folder = tmpdir.mkdir("empty_folder")
    with pytest.raises(FileNotFoundError, match="Nenhum arquivo encontrado"):
        extract_from_excel(str(empty_folder))