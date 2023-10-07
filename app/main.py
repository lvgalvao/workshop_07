from ETL.extract import extract_from_excel
# from ETL.load import
# from ETL.transformation import

def pipeline(path_input: str):
    data = extract_from_excel(path_input=path_input)
    # data = transform(data)
    # load(data)
    return data

if __name__ == "__main__":
    print(pipeline(path_input="./data/input"))