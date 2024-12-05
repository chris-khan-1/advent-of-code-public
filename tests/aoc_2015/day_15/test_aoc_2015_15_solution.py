import pytest

from src.aoc_2015.day_15.aoc_2015_15_solution import (
    Ingredient,
    get_best_score,
    get_combination_calories,
    get_combination_score,
    get_possible_combinations,
    parse_ingredients,
)


@pytest.fixture(scope="module")
def mock_ingredient_data():
    return [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]


@pytest.fixture(scope="module")
def mock_ingredients():
    return [
        Ingredient(
            name="Butterscotch",
            capacity=-1,
            durability=-2,
            flavour=6,
            texture=3,
            calories=8,
        ),
        Ingredient(
            name="Cinnamon",
            capacity=2,
            durability=3,
            flavour=-2,
            texture=-1,
            calories=3,
        ),
    ]


def test_parse_ingredients(mock_ingredient_data, mock_ingredients):
    actual = parse_ingredients(input=mock_ingredient_data)
    assert actual == mock_ingredients


def test_get_possible_combinations(mock_ingredients):
    actual = get_possible_combinations(total_teaspoons=3, ingredients=mock_ingredients)
    assert set(actual) == set([(3, 0), (2, 1), (1, 2), (0, 3)])


def test_get_combination_score(mock_ingredients):
    actual = get_combination_score(
        ingredients=mock_ingredients, ingredient_combination=(44, 56)
    )
    assert actual == 62842880


def test_get_combination_calories(mock_ingredients):
    actual = get_combination_calories(
        ingredients=mock_ingredients, ingredient_combination=(40, 60)
    )
    assert actual == 500


def test_get_best_score(mock_ingredient_data):
    actual = get_best_score(input=mock_ingredient_data, total_teaspoons=100)
    assert actual == 62842880


def test_get_best_score_with_calorie_total(mock_ingredient_data):
    actual = get_best_score(
        input=mock_ingredient_data, total_teaspoons=100, calorie_total=500
    )
    assert actual == 57600000
