import pytest
from praktikum.bun import Bun
from data import BunData


class TestBun:

    @pytest.mark.parametrize("bun_data", BunData.BUNS)
    def test_create_various_bun_return_all_added(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])

        assert bun.get_name() == bun_data["name"]
        assert bun.get_price() == bun_data["price"]
