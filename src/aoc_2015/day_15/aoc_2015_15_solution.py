import math
from dataclasses import dataclass
from itertools import permutations


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavour: int
    texture: int
    calories: int


def parse_ingredients(input: list[str]) -> list:
    ingredients = []
    for info in input:
        info_list = info.replace(":", "").replace(",", "").split(" ")
        ingredients.append(
            Ingredient(
                name=info_list[0],
                capacity=int(info_list[2]),
                durability=int(info_list[4]),
                flavour=int(info_list[6]),
                texture=int(info_list[8]),
                calories=int(info_list[10]),
            )
        )
    return ingredients


def get_possible_combinations(
    total_teaspoons: int, ingredients: list[Ingredient]
) -> list:
    ammounts = range(total_teaspoons + 1)
    return [
        j for j in permutations(ammounts, len(ingredients)) if sum(j) == total_teaspoons
    ]


def get_combination_score(
    ingredients: list[Ingredient], ingredient_combination: list
) -> int:
    scores = []
    for property in ["capacity", "durability", "flavour", "texture"]:
        tmp_score = 0
        for i in range(len(ingredients)):
            tmp_score += ingredient_combination[i] * getattr(ingredients[i], property)
        scores.append(max(0, tmp_score))
    return math.prod(scores)


def get_combination_calories(
    ingredients: list[Ingredient], ingredient_combination: list
) -> int:
    calories = 0
    for i in range(len(ingredients)):
        calories += ingredient_combination[i] * ingredients[i].calories
    return calories


def get_best_score(
    input: list[str], total_teaspoons: int, calorie_total: int = None
) -> int:
    ingredients = parse_ingredients(input=input)
    best_score = 0
    possible_combinations = get_possible_combinations(
        total_teaspoons=total_teaspoons, ingredients=ingredients
    )
    for combination in possible_combinations:
        score = get_combination_score(
            ingredients=ingredients, ingredient_combination=combination
        )
        calories = get_combination_calories(
            ingredients=ingredients, ingredient_combination=combination
        )
        if calorie_total and calories != calorie_total:
            continue
        if score > best_score:
            best_score = score
    return best_score


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_15/input.txt"
    result_path = "./src/aoc_2015/day_15/result.txt"

    input = helpers.read_file_lines(file_path=input_path)

    best_score = get_best_score(input=input, total_teaspoons=100)
    best_score_w_calorie_total = get_best_score(
        input=input, total_teaspoons=100, calorie_total=500
    )

    result = f"""\
        Part 1: The best score is {best_score}.
        Part 2: The best score with a calorie total of 500 is {best_score_w_calorie_total}.
        """

    helpers.write_file(file_path=result_path, contents=result)
