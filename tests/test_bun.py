import pytest

from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize('test_param', [
        'name',
        'price'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        name = 'slim'
        price =  11.1
        bun = Bun(name, price)
        assert getattr(bun, test_param) == locals().get(test_param)