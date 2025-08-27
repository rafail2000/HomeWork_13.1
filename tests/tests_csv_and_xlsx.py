import unittest

import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.main import read_csv_file, read_excel_file


def test_read_csv_file():
    data = read_csv_file()
    assert isinstance(data, list), "Ожидается список"
    assert len(data) > 0, "Данные не должны быть пустыми"
    assert isinstance(data[0], dict), "Каждый элемент должен быть словарём"


def test_read_excel_file():
    data = read_excel_file()
    assert isinstance(data, list), "Ожидается список"
    assert len(data) > 0, "Данные не должны быть пустыми"
    assert isinstance(data[0], dict), "Каждый элемент должен быть словарём"


class TestReadFiles(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_csv_file(self, mock_read_csv):
        # Создаём фиктивный dataframe
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{'id': 1, 'value': 100}]
        mock_read_csv.return_value = mock_df

        result = read_csv_file('fake_path.csv')
        # Проверяем, что pd.read_csv вызвался с нужным аргументом
        mock_read_csv.assert_called_once_with('fake_path.csv')
        # Проверяем, что возвращается корректный результат
        self.assertEqual(result, [{'id': 1, 'value': 100}])

    @patch('pandas.read_excel')
    def test_read_excel_file(self, mock_read_excel):
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{'id': 2, 'value': 200}]
        mock_read_excel.return_value = mock_df

        result = read_excel_file('fake_path.xlsx')
        mock_read_excel.assert_called_once_with('fake_path.xlsx')
        self.assertEqual(result, [{'id': 2, 'value': 200}])

if __name__ == '__main__':
    unittest.main()