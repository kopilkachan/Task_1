import pytest
from praktikum.ingredient import Ingredient
from data import IngredientData


class TestIngredient:

    @pytest.mark.parametrize("ingredient_data", IngredientData.INGREDIENTS)
    def test_get_name_returns_correct_name(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        
        assert ingredient.get_name() == ingredient_data["name"]

    @pytest.mark.parametrize("ingredient_data", IngredientData.INGREDIENTS)
    def test_get_price_returns_correct_price(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])

        assert ingredient.get_price() == ingredient_data["price"]

    @pytest.mark.parametrize("ingredient_data", IngredientData.INGREDIENTS)
    def test_get_type_returns_correct_type(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])

        assert ingredient.get_type() == ingredient_data["type"]