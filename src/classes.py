class Category:
    """Класс категории"""
    name: str
    description: str
    goods: list

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods):
        """Инициализация имени, описания и товаров"""
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    @property
    def goods(self):
        """Получение приватного атрибута __goods"""
        return self.__goods

    def add_goods(self, product):
        """Добавление данных с приватного атрибута __goods"""
        self.__goods.append(product)

    # @property
    # def get_product(self):
    #     """Получение имени, цены и остатка"""
    #     current_list = []
    #     for product in self.__goods:
    #         current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
    #     return current_list

    def __str__(self):
        """Получение имени, цены и остатка"""
        return f'{self.name}, {self.price} руб. Остаток: {len(self.__goods)} шт.'

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def __len__(self):
        """ Вывод кол-ва продуктов в следующем виде: 'Название категории, количество продуктов: 200 шт.' """
        count_of_products = 0
        for product in self.__goods:
            count_of_products += product.quantity
        return f'{self.name}, количество продуктов: {int(count_of_products)} шт.'


class Product:
    """Классы продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация имени, описания цены и колличества"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Получение приватных данных через гетер"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Условия изменения цены"""
        if new_price <= 0:
            print('Цена введена некоректно')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась. Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена осталась прежней')
        else:
            self.__price = new_price

    def get_product_price(self):
        """Получение приватного атрибута price"""
        return self.price

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'

    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        # забираем данные в переменные для удобства работы
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        # если передан и словарь и список продуктов - попытаться найти в списке продуктов продукт схожий по имени
        if list_of_products:
            for product in list_of_products:
                if product.name == name:  # если перебираемый продукт по имени равен тому имени продукта, который предлагается создать
                    # здесь мы нашли продукт, вернем его, сначала установив количество и цену
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    # установив атрибуты у продукта - возвращаем его
                    return product

        # здесь мы окажемся в двух случаях: если не передан список продуктов, либо он был передан но в цикле не нашлось совпадения по имени - значит мы должны создать продукт и вернуть его
        new_product = cls(name, description, price, quantity)
        return new_product

    def __str__(self):
        """ Строковое отображение остатка продукта на складе """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ Сложение сумм продуктов """
        return self.quantity * self.__price + other.quantity * other.__price
