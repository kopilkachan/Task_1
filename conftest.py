import pytest
from unittest.mock import Mock 
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Тестовая булка"
    bun.get_price.return_value = 50.0
    return bun

@pytest.fixture
def mock_ingredient():
    ing = Mock()
    ing.get_type.return_value = "FILLING"
    ing.get_name.return_value = "Тестовый ингредиент"
    ing.get_price.return_value = 30.0
    return ing

@pytest.fixture
def mock_ingredients_list():
    ingredients = []
    for i in range(3):
        ing = Mock()
        ing.get_type.return_value = f"type_{i}"
        ing.get_name.return_value = f"Ингредиент {i}"
        ing.get_price.return_value = 10.0 * (i + 1)
        ingredients.append(ing)
    return ingredients
