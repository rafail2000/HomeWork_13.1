from pprint import pprint

from src.classes import Category, Product
from src.utils import load_data


def main():
    data = load_data()
    list_category = []
    for unit in data:
        list_product = [un for un in unit["products"]]
        category = Category(unit["name"], unit["description"], unit["products"])
        list_category.append(f'{category.get_name()}\n'
                             f'{category.get_description()}\n'
                             f'{category.add_goods()}\n\n'
                             )
        result = []
        for element in list_product:
            product = Product(element["name"], element["description"],
                              element["price"], element["quantity"])
            result.append(f'{product.get_product_name()}\n'
                          f'{product.get_product_description()}\n'
                          f'{product.get_product_price()}\n'
                          f'{product.get_product_quantity_in_stock()}\n\n'
                          )
    pprint(list_category)


if __name__ == '__main__':
    main()
