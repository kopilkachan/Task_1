class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_increases_count(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_add_ingredient_adds_correct_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger, mock_ingredients_list):
        burger.ingredients = mock_ingredients_list.copy()
        original_len = len(burger.ingredients)
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == original_len - 1

    def test_move_ingredient(self, burger, mock_ingredients_list):
        burger.ingredients = mock_ingredients_list.copy()
        moved_item = burger.ingredients[0]
        burger.move_ingredient(0, 2)

        assert burger.ingredients[2] == moved_item

    def test_get_price(self, burger, mock_bun, mock_ingredients_list):
        burger.set_buns(mock_bun)
        for ing in mock_ingredients_list:
            burger.add_ingredient(ing)
        expected_price = mock_bun.get_price.return_value * 2
        expected_price += sum(ing.get_price.return_value for ing in mock_ingredients_list)

        assert burger.get_price() == expected_price

    def test_get_receipt_returns_correct_full_string(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        expected_receipt = (
           "(==== Тестовая булка ====)\n"
            "= filling Тестовый ингредиент =\n"
            "(==== Тестовая булка ====)\n"
            "\n"
            "Price: 130.0"
        )
        
        assert burger.get_receipt() == expected_receipt