
class Category:
    """Класс категории"""
    name: str
    description: str
    goods: list

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1


    @property
    def goods(self):
        return self.__goods

    def add_goods(self, product):
        self.__goods.append(product)

    @property
    def get_product(self):
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'


class Product:
    """Классы продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некоректно')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась. Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена осталась прежней')



    def get_product_price(self):
        return self.price

    @classmethod
    def add_new_product(cls, name, description, price, quantity, list_of_products):
        new_product = cls(name, description, price, quantity)
        for product in list_of_products:
            if new_product.name == product.name:
                if new_product.price > product.price:
                    product.price = new_product.price
                product.quantity += new_product.quantity





    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'
