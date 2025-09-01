import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """ Фильтрация списка по описанию """

    filtered_list = []
    pattern = search

    for i in data:
        text = i.get("description")
        if re.findall(pattern, text, flags=re.IGNORECASE):
            filtered_list.append(i)

    return filtered_list
