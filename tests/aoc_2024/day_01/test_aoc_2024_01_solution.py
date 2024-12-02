from src.aoc_2024.day_01.aoc_2024_01_solution import (
    get_total_difference,
    get_total_similarity,
    parse_input,
)


def test_parse_input():
    input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    actual_one, actual_two = parse_input(input=input)

    assert actual_one == [1, 2, 3, 3, 3, 4]
    assert actual_two == [3, 3, 3, 4, 5, 9]


def test_get_total_difference():
    left_input = [1, 2, 3, 3, 3, 4]
    right_input = [3, 3, 3, 4, 5, 9]

    actual = get_total_difference(left=left_input, right=right_input)

    assert actual == 11


def test_get_total_similarity():
    left_input = [1, 2, 3, 3, 3, 4]
    right_input = [3, 3, 3, 4, 5, 9]

    actual = get_total_similarity(left=left_input, right=right_input)

    assert actual == 31
