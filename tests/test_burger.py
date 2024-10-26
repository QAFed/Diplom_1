import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
class TestInitData:
    bun = None
    ingredients = []

class TestData:
    exempl_bun = Bun("exo", 11.22)
    exempl_ingred = Ingredient('red','paper',9.7)

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

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        assert getattr(burger, 'ingredients') == [TestData.exempl_ingred]

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(TestData.exempl_ingred)
        burger.remove_ingredient(0)
        assert getattr(burger, 'ingredients') == []


