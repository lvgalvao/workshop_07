from ETL.extract import extract_from_excel
from ETL.load import load_to_excel
from ETL.transformation import consolidate_dataframes

def pipeline(path_input: str, output_path: str, file_name: str):
    """
    o objetivo dessa função é executar o pipeline completo
    
    Args:
        path_input (str): caminho da pasta onde estão os arquivos de entrada
        output_path (str): caminho da pasta onde será salvo o arquivo de saída
        file_name (str): nome do arquivo de saída
        
    Returns:
        str: mensagem de sucesso
    """
    lista_de_data_frames = extract_from_excel(path_input=path_input)
    data_frame_consolidado = consolidate_dataframes(dataframes=lista_de_data_frames)
    load_to_excel(data_frame_consolidado, output_path, file_name)
    return "Arquivo salvo com sucesso"

if __name__ == "__main__":
    print(pipeline(path_input="./data/input", output_path="./data/output/", file_name="output.xlsx"))