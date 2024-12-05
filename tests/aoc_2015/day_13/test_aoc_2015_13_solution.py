import pytest

from src.aoc_2015.day_13.aoc_2015_13_solution import (
    add_myself_to_happiness_info,
    get_largest_happiness_change,
    get_pair_happiness,
    get_possible_seating_arrangement,
    parse_happiness_info,
)


@pytest.fixture(scope="function")
def mock_happiness_info():
    return {
        "Alice": {"Bob": 54, "Carol": -79, "David": -2},
        "Bob": {"Alice": 83, "Carol": -7, "David": -63},
        "Carol": {"Alice": -62, "Bob": 60, "David": 55},
        "David": {"Alice": 46, "Bob": -7, "Carol": 41},
    }


def test_parse_happiness_info():
    input = [
        "Alice would gain 54 happiness units by sitting next to Bob.",
        "Alice would lose 79 happiness units by sitting next to Carol.",
        "Bob would gain 83 happiness units by sitting next to Alice",
    ]
    expected = {"Alice": {"Bob": 54, "Carol": -79}, "Bob": {"Alice": 83}}
    actual = parse_happiness_info(input=input)
    assert actual == expected


def test_add_myself_to_happiness_info(mock_happiness_info):
    actual = add_myself_to_happiness_info(happiness_info=mock_happiness_info)
    expected = {
        "Alice": {"Bob": 54, "Carol": -79, "David": -2, "Me": 0},
        "Bob": {"Alice": 83, "Carol": -7, "David": -63, "Me": 0},
        "Carol": {"Alice": -62, "Bob": 60, "David": 55, "Me": 0},
        "David": {"Alice": 46, "Bob": -7, "Carol": 41, "Me": 0},
        "Me": {"Alice": 0, "Bob": 0, "Carol": 0, "David": 0},
    }
    assert actual == expected


def test_get_pair_happiness(mock_happiness_info):
    actual = get_pair_happiness(
        happiness_info=mock_happiness_info, person_1="Alice", person_2="Bob"
    )
    assert actual == 54 + 83


def test_get_possible_seating_arrangement(mock_happiness_info):
    actual = get_possible_seating_arrangement(happiness_info=mock_happiness_info)
    expected = [
        ["Alice", "Bob", "Carol", "David"],
        ["Alice", "Bob", "David", "Carol"],
        ["Alice", "Carol", "Bob", "David"],
        ["Alice", "Carol", "David", "Bob"],
        ["Alice", "David", "Bob", "Carol"],
        ["Alice", "David", "Carol", "Bob"],
        ["Bob", "Alice", "Carol", "David"],
        ["Bob", "Alice", "David", "Carol"],
        ["Bob", "Carol", "Alice", "David"],
        ["Bob", "Carol", "David", "Alice"],
        ["Bob", "David", "Alice", "Carol"],
        ["Bob", "David", "Carol", "Alice"],
        ["Carol", "Alice", "Bob", "David"],
        ["Carol", "Alice", "David", "Bob"],
        ["Carol", "Bob", "Alice", "David"],
        ["Carol", "Bob", "David", "Alice"],
        ["Carol", "David", "Alice", "Bob"],
        ["Carol", "David", "Bob", "Alice"],
        ["David", "Alice", "Bob", "Carol"],
        ["David", "Alice", "Carol", "Bob"],
        ["David", "Bob", "Alice", "Carol"],
        ["David", "Bob", "Carol", "Alice"],
        ["David", "Carol", "Alice", "Bob"],
        ["David", "Carol", "Bob", "Alice"],
    ]
    assert sorted(actual) == sorted(expected)


def test_get_largest_happiness_change():
    input = [
        "Alice would gain 54 happiness units by sitting next to Bob.",
        "Alice would lose 79 happiness units by sitting next to Carol.",
        "Alice would lose 2 happiness units by sitting next to David.",
        "Bob would gain 83 happiness units by sitting next to Alice.",
        "Bob would lose 7 happiness units by sitting next to Carol.",
        "Bob would lose 63 happiness units by sitting next to David.",
        "Carol would lose 62 happiness units by sitting next to Alice.",
        "Carol would gain 60 happiness units by sitting next to Bob.",
        "Carol would gain 55 happiness units by sitting next to David.",
        "David would gain 46 happiness units by sitting next to Alice.",
        "David would lose 7 happiness units by sitting next to Bob.",
        "David would gain 41 happiness units by sitting next to Carol.",
    ]
    actual = get_largest_happiness_change(input=input)
    assert actual == 330
