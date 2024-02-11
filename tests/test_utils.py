from src.utils import load_data


def test_load_data():
    assert load_data() is not None
