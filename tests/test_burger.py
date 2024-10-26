import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
class TestInitData:
    bun = None
    ingredients = []

class TestData:
    exempl_bun = Bun("exo", 11.22)

class TestBurger:
    @pytest.mark.parametrize('test_param', [
        'bun',
        'ingredients'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        burger = Burger()
        assert getattr(burger, test_param) == getattr(TestInitData, test_param)

    def test_setter_buns(self):
        burger = Burger()
        burger.set_buns(TestData.exempl_bun)
        assert getattr(burger, 'bun') == TestData.exempl_bun


