class Category:
    """Класс категории"""
    name: str
    description: str
    goods: str

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_goods(self):
        return self.goods



class Product:
    """Классы продукт"""
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_price(self):
        return self.price

    def get_product_quantity_in_stock(self):
        return self.quantity_in_stock

