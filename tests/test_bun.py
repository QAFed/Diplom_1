import pytest
from praktikum.bun import Bun


class TestData:
    name = 'slim'
    price = 11.1


class TestBun:
    @pytest.mark.parametrize('test_param', [
        'name',
        'price'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        bun = Bun(TestData.name, TestData.price)
        assert getattr(bun, test_param) == getattr(TestData, test_param)

    @pytest.mark.parametrize('test_param', [
        'name',
        'price'
    ])
    def test_class_getters_return_value(self, test_param):
        bun = Bun(TestData.name, TestData.price)
        assert getattr(bun, f'get_{test_param}')() == getattr(TestData, test_param)
