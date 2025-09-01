import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """ Фильтрация списка по описанию """

    filtered_list = []
    pattern = ""
    if search.lower() == "открытие вклада":
        pattern = r"Открытие вклада"
    elif search.lower() == "перевод с карты на карту":
        pattern = r"Перевод с карты на карту"
    elif search.lower() == "перевод организации":
        pattern = r"Перевод организации"
    elif search.lower() == "перевод со счета на счет":
        pattern = r"Перевод со счета на счет"

    for i in data:
        text = i.get("description")
        if re.match(pattern, text):
            filtered_list.append(i)

    return filtered_list
