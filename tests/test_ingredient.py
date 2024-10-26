import pytest

from praktikum.ingredient import Ingredient
class TestData:
    type = "green"
    name = 'onion'
    price = 3.3

class TestBun:
    @pytest.mark.parametrize('test_param', [
        'type',
        'name',
        'price'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        ingredient = Ingredient(TestData.type, TestData.name, TestData.price)
        assert getattr(ingredient, test_param) == getattr(TestData, test_param)

    @pytest.mark.parametrize('test_param', [
        'type',
        'name',
        'price'
    ])
    def test_class_getters_return_value(self, test_param):
        ingredient = Ingredient(TestData.type, TestData.name, TestData.price)
        assert getattr(ingredient, f'get_{test_param}')() == getattr(TestData, test_param)