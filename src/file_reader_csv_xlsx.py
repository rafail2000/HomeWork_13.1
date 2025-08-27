import json
import pandas as pd


def read_csv_file(path):
    """ Чтение csv файла. """
    df = pd.read_csv(path)
    return df.to_dict(orient='records')


def read_excel_file(path):
    """ Чтение xlsx файла. """
    df = pd.read_excel(path)
    return df.to_dict(orient='records')


if __name__ == "__main__":
    csv_path = "../data/transactions.csv"
    excel_path = "../data/transactions_excel.xlsx"
    print(read_csv_file(csv_path))
    print(read_excel_file(excel_path))