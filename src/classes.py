from abc import ABC, abstractmethod


class MixinRepr:

    def __init__(self, *args, **kwargs):
        print(self.__repr__())

    def __repr__(self):
        return f'{self.__class__.__name__}, {self.__dict__}'


class AbstractCategoryOrder(ABC):
    """ Абстрактный класс для категории и заказа """

    product = str
    quantity = int

    @abstractmethod
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def get_total_cost(self):
        pass


class Order(AbstractCategoryOrder):
    """ Класс заказа """

    def __init__(self, product, quantity):
        super().__init__(product, quantity)

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def get_total_cost(self):
        return self.product * self.quantity


class Category(AbstractCategoryOrder):
    """Класс категории"""

    description: str
    goods: list

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods, product):
        """Инициализация имени, описания и товаров"""
        self.name = name
        self.description = description
        self.__goods = goods
        super().__init__(name, product)

        Category.total_numbers_of_category += 1
        Category.unique_goods += 1

    @property
    def goods(self):
        """Получение приватного атрибута __goods"""
        return self.__goods

    def add_goods(self, product):
        """Добавление данных с приватного атрибута __goods"""
        if isinstance(product, self.__class__)\
                and isinstance(self, product.__class__):
            if product.quantity < 1:
                raise ValueError("Товар с нулевым \
                количеством не может быть добавлен.")
            self.__goods.append(product)
        else:
            raise TypeError

    @property
    def get_product(self):
        """Получение имени, цены и остатка"""
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name},\
{product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'

    def __len__(self):
        """ Подсчёт кол-ва продуктов в категории. """
        product_counter = 0
        for product in self.__goods:
            product_counter += product.quantity
        return product_counter

    def __str__(self):
        """ Вывод кол-ва продуктов в следующем виде:
        Название категории, количество продуктов: 200 шт. """
        return (f'Название категории \
{self.name}, количество продуктов: {len(self)} шт.')

    def get_total_cost(self):
        """ Вывод общей стоимости. """
        return self.product * self.quantity

    def middle_price(self, sum_of_price=None):
        """ Вывод средней стоимости товаров. """
        for product in self.__goods:
            sum_of_price += product.price
        try:
            return sum_of_price / len(self.__goods)
        except ZeroDivisionError:
            return 0


class ProductExceptions:
    """ Класс исключений """

    def __init__(self, name, goods, product):
        """Инициализация имени, описания и товаров"""
        super().__init__(name, goods, product)


class AbstractProduct(ABC):

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def get_product_price(self):
        pass

    @classmethod
    @abstractmethod
    def add_new_product(cls, product_data, list_of_products=None):
        pass


class Product(MixinRepr, AbstractProduct):
    """Классы продукт"""
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        """Инициализация имени, описания цены и количества"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @property
    def price(self):
        """Получение приватных данных через гетер"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Условия изменения цены"""
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась.\
            Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена осталась прежней')
        else:
            self.__price = new_price

    def get_product_price(self):
        """Получение приватного атрибута price"""
        return self.price

    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        # забираем данные в переменные для удобства работы
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        color = product_data
        # если передан и словарь и список продуктов - попытаться найти в списке продуктов продукт схожий по имени
        if list_of_products:
            for product in list_of_products:
                if product.name == name:  # если перебираемый продукт по имени равен тому имени продукта,
                    # который предлагается создать
                    # здесь мы нашли продукт, вернем его, сначала установив количество и цену
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    # установив атрибуты у продукта - возвращаем его
                    return product

        # здесь мы окажемся в двух случаях: если не передан список продуктов, либо он был передан, но в цикле не
        # нашлось совпадения по имени - значит мы должны создать продукт и вернуть его
        new_product = cls(name, description, price, quantity, color)
        return new_product

    def __str__(self):
        """ Строковое отображение остатка продукта на складе """
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ Сложение сумм продуктов """
        if isinstance(other, self.__class__) and isinstance(self, other.__class__):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError


class Smartphone(Product):
    """Класс Смартфоны"""
    performance: float
    model: str
    ram: float

    def __init__(self, name, description, price, quantity, performance, model, ram, color):
        """Инициализация производительности, модели, ОЗУ и цвета"""
        self.performance = performance
        self.model = model
        self.ram = ram
        super().__init__(name, description, price, quantity, color)
        """Добавление атрибутов: название, описание, цены, и кол-ва из класса Product"""


class LawnGrass(Product):
    """Класс трава газонная"""
    country_origin: str
    germination_period: str

    def __init__(self, name, description, price, quantity, country_origin, germination_period, color):
        """Инициализация страны-производителя, срока произрастания и цвета"""
        self.country_origin = country_origin
        self.germination_period = germination_period
        super().__init__(name, description, price, quantity, color)
        """Добавление атрибутов: название, описание, цены, и кол-ва из класса Product"""
