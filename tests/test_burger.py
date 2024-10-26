import pytest

from praktikum.burger import Burger
class TestInitData:
    bun = None
    ingredients = []

class TestBurger:
    @pytest.mark.parametrize('test_param', [
        'bun',
        'ingredients'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        burger = Burger()
        assert getattr(burger, test_param) == getattr(TestInitData, test_param)
