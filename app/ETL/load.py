import pandas as pd
   
def load_to_excel(consolidado: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    função que salva um excel em uma pasta de saída

    args: consolidado: pd.Dataframe, output_path: str

    return: "Arquivo salvo com sucesso
    """
    consolidado.to_excel(output_path + file_name, index=False)
    return "Arquivo salvo com sucesso"
