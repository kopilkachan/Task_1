from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_database_initialization_creates_buns_list(self):
        db = Database()
        assert len(db.buns) == 3
        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]
        for i, (name, price) in enumerate(expected_buns):
            assert db.buns[i].get_name() == name
            assert db.buns[i].get_price() == price

    def test_database_initialization_creates_ingredients_list(self):
        db = Database()
        assert len(db.ingredients) == 6
        expected_ingredients = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
        for i, (ing_type, name, price) in enumerate(expected_ingredients):
            assert db.ingredients[i].get_type() == ing_type
            assert db.ingredients[i].get_name() == name
            assert db.ingredients[i].get_price() == price

    def test_available_buns_returns_buns_list(self):
        db = Database()
        buns = db.available_buns()
        assert buns is db.buns 
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients_returns_ingredients_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients is db.ingredients
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"