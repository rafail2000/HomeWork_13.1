import json
import os


def load_data():
    """Загружает даннные из json файла"""
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, "data", "products.json")
    with open(PATH, encoding='UTF-8') as read_data:
        data = json.load(read_data)
        return data
