from ETL.extract import extract_from_excel
# from ETL.load import
# from ETL.transformation import

def pipeline():
    data = extract_from_excel()
    # data = transform(data)
    # load(data)
    return data

if __name__ == "__main__":
    print(pipeline())