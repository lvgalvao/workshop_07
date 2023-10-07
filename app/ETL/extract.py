import os # biblioteca para manipular arquivos e pastas
import glob # biblioteca para listar arquivos de uma pasta

import pandas as pd


def extract_from_excel(path_input: str) -> list[pd.DataFrame]:
    """o objetivo dessa função é extrar os dados de diversos arquivos em excel, terá como saída uma lista de dataframes"""
    
    files = glob.glob(os.path.join(path_input, "*.xlsx")) # lista todos os arquivos com a extensão .xlsx
    if not files:
        raise FileNotFoundError("Nenhum arquivo encontrado")
    
    all_data = []
    for file in files:
        data = pd.read_excel(file)
        all_data.append(data)

    return all_data

if __name__ == "__main__":
    data = extract_from_excel(path_input="./data/input")
    print(data)