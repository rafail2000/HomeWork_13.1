from src.file_reader_csv_xlsx import (read_csv_file, read_excel_file,
                                      read_json_file)
from src.utils import process_bank_search
from collections import Counter


def main():
    """ Основная функция для взаимодействия с пользователем """

    type_file = ""  # Выбор типа файла JSON, CSV или, XLSX.
    type_operation = ""  # Выбор типа операции EXECUTED, CANCELED или PENDING.
    sort_on_time = False  # Сортировать по времени или нет.
    sort_up_or_down = False  # Сортировать по возрастанию ил по убыванию.
    only_rub = False  # Выводить только рублёвые транзакции, да или нет.
    sort_on_word = False  # сортировать по слову, да или нет.

    while True:
        type_files = ("JSON", "CSV", "XLSX")

        print("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")
        user_input = input("Введите номер необходимого вам пункта: ")
        if user_input not in "123":
            print("Выберите пункты из представленных!")
            continue
        type_file = type_files[int(user_input) - 1]
        print(f"Для обработки выбран {type_file}-файл.")
        break

    while True:
        type_operations = ("executed", "canceled", "pending")

        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_input = input("Введите статус: ").lower()
        if user_input not in type_operations:
            print(f"Статус операции {user_input} недоступен")
            continue
        type_operation = user_input.upper()
        print(f"Операции отфильтрованы по статусу {type_operation}")
        break

    json_path = "../data/operations.json"
    csv_path = "../data/transactions.csv"
    excel_path = "../data/transactions_excel.xlsx"

    if type_file == "JSON":
        data = read_json_file(json_path)
    elif type_file == "CSV":
        data = read_csv_file(csv_path)
    else:
        data = read_excel_file(excel_path)

    filtered_data = [i for i in data if i.get('state', False) == type_operation]

    while True:
        yes_or_not = ("да", "нет")
        up_or_down = ("по возрастанию", "по убыванию")
        print("Отсортировать операции по дате Да/Нет?")
        user_input = input("Введите да или нет: ").lower()
        if user_input not in yes_or_not:
            print("Необходимо выбрать, да или нет!")
            continue
        sort_on_time = True if user_input == "да" else False
        if sort_on_time:
            print("Отсортировать по возрастанию или по убыванию?")
            user_input = input("Введите по возрастанию или по убыванию: ").lower()
            if user_input not in up_or_down:
                print("Необходимо выбрать, по возрастанию или убыванию!")
                continue
            sort_up_or_down = True if user_input == "по возрастанию" else False

        print("Выводить только рублевые транзакции Да/Нет?")
        user_input = input("Введите да или нет: ").lower()
        if user_input not in yes_or_not:
            print("Необходимо выбрать, да или нет!")
            continue
        only_rub = True if user_input == "да" else False

        print("Отфильтровать список транзакций по определенному слову в описании да или нет?")
        user_input = input("Введите да или нет: ").lower()
        if user_input not in yes_or_not:
            print("Необходимо выбрать, да или нет!")
            continue
        sort_on_word = True if user_input == "да" else False
        break

    if sort_on_time:
        if sort_up_or_down:
            filtered_data.sort(key=lambda x: x["date"], reverse=False)
        else:
            filtered_data.sort(key=lambda x: x["date"], reverse=True)

    if only_rub:
        if type_file == "JSON":
            filtered_data = [i for i in filtered_data
                             if i.get("operationAmount").get('currency').get('code').lower() == "rub"]
        else:
            filtered_data = [i for i in filtered_data
                             if i.get("currency_code").lower() == "rub"]

    if sort_on_word:
        user_search = input("Введите текст для поиска: ")
        filtered_data = process_bank_search(filtered_data, user_search)

    if not (len(filtered_data) > 0):
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        sum_operations = Counter([i.get("description") for i in filtered_data])
        print(f"Всего банковских операций в выборке: {sum_operations}\n")
        if type_file == "JSON":
            for i in filtered_data:
                if i.get("description") == "Открытие вклада":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get("to", False)[:5] + "**" + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("operationAmount").get("amount")} "
                          f"{i.get("operationAmount").get('currency').get('name')}")
                    print("*******************")
                elif i.get("description") == "Перевод с карты на карту":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get('from', False)[:19] + "**" + " " + "****" + " " + i.get("from", False)[-4:]} "
                          f"-> {i.get('to', False)[:19] + "**" + " " + "****" + " " + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("operationAmount").get("amount")} "
                          f"{i.get("operationAmount").get('currency').get('name')}")
                    print("*******************")
                elif i.get("description") == "Перевод организации":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get('from', False)[:19] + "**" + " " + "****" + " " + i.get("from", False)[-4:]} "
                          f"-> {i.get("to", False)[:5] + "**" + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("operationAmount").get("amount")} "
                          f"{i.get("operationAmount").get('currency').get('name')}")
                    print("*******************")
                elif i.get("description") == "Перевод со счета на счет":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get("from", False)[:5] + "**" + i.get("from", False)[-4:]} "
                          f"-> {i.get("to", False)[:5] + "**" + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("operationAmount").get("amount")} "
                          f"{i.get("operationAmount").get('currency').get('name')}")
                    print("*******************")
        else:
            for i in filtered_data:
                if i.get("description") == "Открытие вклада":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get("to", False)[:5] + "**" + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("amount")} {i.get("currency_name")}")
                    print("*******************")
                elif i.get("description") == "Перевод с карты на карту":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get('from', False)[:19] + "**" + " " + "****" + " " + i.get("from", False)[-4:]} "
                          f"-> {i.get('to', False)[:19] + "**" + " " + "****" + " " + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("amount")} {i.get("currency_name")}")
                    print("*******************")
                elif i.get("description") == "Перевод организации":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get('from', False)[:19] + "**" + " " + "****" + " " + i.get("from", False)[-4:]} "
                          f"-> {i.get("to", False)[:5] + "**" + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("amount")} {i.get("currency_name")}")
                    print("*******************")
                elif i.get("description") == "Перевод со счета на счет":
                    print(f"{i.get('date', False)} {i.get('description', False)}\n"
                          f"{i.get("from", False)[:5] + "**" + i.get("from", False)[-4:]} "
                          f"-> {i.get("to", False)[:5] + "**" + i.get("to", False)[-4:]}\n"
                          f"Сумма: {i.get("amount")} {i.get("currency_name")}")
                    print("*******************")


if __name__ == '__main__':
    main()
