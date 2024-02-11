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

def test_classes_category(class_category):
    assert class_category.get_name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.goods == {
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
    assert class_producte.price == 180000.0
    assert gclass_product.quantity_in_stock == 5