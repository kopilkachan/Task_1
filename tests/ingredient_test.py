import pytest
from praktikum.ingredient import Ingredient
from data import IngredientData


class TestIngredient:

    @pytest.mark.parametrize("ingredient_data", IngredientData.INGREDIENTS)
    def test_create_various_ingredient_returns_all_added(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])

        assert ingredient.get_name() == ingredient_data["name"]
        assert ingredient.get_price() == ingredient_data["price"]
        assert ingredient.get_type() == ingredient_data["type"]
