import pytest

from src.classes import Smartphone, LawnGrass


def test_sum_product_error():
    with pytest.raises(TypeError):
        Smartphone("Iphone",
                   "Unique design",
                   100_000,
                   15,
                   "3.8",
                   "15",
                   2048,
                   "black") + LawnGrass("Green grass",
                                        "Usual green grass",
                                        100,
                                        1000,
                                        "China",
                                        "two weeks",
                                        "green")


def test_sum_product():
    assert Smartphone("Iphone",
                      "Unique design",
                      100_000,
                      15,
                      "3.8",
                      "15",
                      2048,
                      "black") + Smartphone("Iphone",
                                            "Unique design",
                                            100_000,
                                            20,
                                            "3.8",
                                            "14",
                                            2048,
                                            "black") == 3500000
