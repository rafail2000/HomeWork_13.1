import pytest

from src.classes import Category, Product


@pytest.fixture
def class_category():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      })

def test_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.goods == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }
    assert class_category.total_numbers_of_category == 1
    assert class_category.unique_goods == 1


def test_get_name(class_category):
    class_category.get_name()
    assert class_category.get_name() == 'Смартфоны'


def test_get_description(class_category):
    class_category.get_description()
    assert class_category.get_description() == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'


def test_get_goods(class_category):
    class_category.get_goods()
    assert class_category.get_goods() == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }


@pytest.fixture
def class_product():
    return Product('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      })


def test_init(class_product):
    assert class_product.name == 'Смартфоны'
    assert class_product.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_product.price == 180000.0
    assert class_product.quantity_in_stock == 5