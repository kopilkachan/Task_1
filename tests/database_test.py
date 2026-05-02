from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestDatabase:

    def test_available_buns_returns_same_list_object(self):
        db = Database()
        buns = db.available_buns()
        assert buns is db.buns

    def test_available_buns_length_is_3(self):
        db = Database()
        assert len(db.available_buns()) == 3

    @pytest.mark.parametrize("index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_element_name(self, index, expected_name, expected_price):
        db = Database()
        bun = db.available_buns()[index]
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("index,expected_name,expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_element_price(self, index, expected_name, expected_price):
        db = Database()
        bun = db.available_buns()[index]
        assert bun.get_price() == expected_price

    def test_available_ingredients_returns_same_list_object(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients is db.ingredients

    def test_available_ingredients_length_is_6(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients_element_type(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ing = db.available_ingredients()[index]
        assert ing.get_type() == expected_type

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients_element_name(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ing = db.available_ingredients()[index]
        assert ing.get_name() == expected_name

    @pytest.mark.parametrize("index,expected_type,expected_name,expected_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients_element_price(self, index, expected_type, expected_name, expected_price):
        db = Database()
        ing = db.available_ingredients()[index]
        assert ing.get_price() == expected_price