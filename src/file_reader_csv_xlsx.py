import json
import pandas as pd


def read_json_file(path):
    """ Чтение JSON файла """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def read_csv_file(path):
    """ Чтение csv файла. """
    df = pd.read_csv(path, delimiter=';')
    return df.to_dict(orient='records')


def read_excel_file(path):
    """ Чтение xlsx файла. """
    df = pd.read_excel(path)
    return df.to_dict(orient='records')


if __name__ == "__main__":
    json_path = "../data/operations.json"
    csv_path = "../data/transactions.csv"
    excel_path = "../data/transactions_excel.xlsx"
