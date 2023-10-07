import pandas as pd
import os
   
def load_to_excel(consolidado: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    função que salva um excel em uma pasta de saída

    caso não existe a pasta de saída, a função irá criar

    args: consolidado: pd.Dataframe, output_path: str

    return: "Arquivo salvo com sucesso
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    consolidado.to_excel(output_path + file_name, index=False)
    return "Arquivo salvo com sucesso"
