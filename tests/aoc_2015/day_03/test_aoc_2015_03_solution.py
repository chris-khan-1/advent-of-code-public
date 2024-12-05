import pytest

from src.aoc_2015.day_03.aoc_2015_03_solution import (
    get_all_house_visit_coordinates,
    get_new_total_unique_house_visits,
    get_next_house_cordinate,
    get_total_unique_house_visits,
    split_directions,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("^", (0, 1)),
        pytest.param(">", (1, 0)),
        pytest.param("v", (0, -1)),
        pytest.param("<", (-1, 0)),
    ],
)
def test_get_next_house_cordinate(input, expected):
    actual = get_next_house_cordinate(start_coordinates=[0, 0], direction=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(">", [(0, 0), (1, 0)]),
        pytest.param("^>v<", [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
        pytest.param(
            "^v^v^v^v^v",
            [
                (0, 0),
                (0, 1),
                (0, 0),
                (0, 1),
                (0, 0),
                (0, 1),
                (0, 0),
                (0, 1),
                (0, 0),
                (0, 1),
                (0, 0),
            ],
        ),
    ],
)
def test_get_all_house_visit_coordinates(input, expected):
    actual = get_all_house_visit_coordinates(directions=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(">", (">", "")),
        pytest.param("^>v<", ("^v", "><")),
        pytest.param("^v^v^v^v^v", ("^^^^^", "vvvvv")),
    ],
)
def test_split_directions(input, expected):
    actual = split_directions(directions=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(">", 2),
        pytest.param("^>v<", 4),
        pytest.param("^v^v^v^v^v", 2),
    ],
)
def test_get_total_unique_house_visits(input, expected):
    actual = get_total_unique_house_visits(directions=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("^>", 3),
        pytest.param("^>v<", 3),
        pytest.param("^v^v^v^v^v", 11),
    ],
)
def test_get_new_total_unique_house_visits(input, expected):
    actual = get_new_total_unique_house_visits(directions=input)
    assert actual == expected
