import pytest

from src.aoc_2015.day_18.aoc_2015_18_solution import (
    get_final_light_on_count,
    get_final_state,
    get_neighbour_values,
    get_next_light_state,
    get_next_total_state,
    get_next_total_state_exclude_corners,
)


@pytest.fixture
def mock_input():
    return [
        ".#.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####..",
    ]


@pytest.fixture
def mock_updated_input():
    return [
        "##.#.#",
        "...##.",
        "#....#",
        "..#...",
        "#.#..#",
        "####.#",
    ]


@pytest.mark.parametrize(
    argnames=["light_location", "expected"],
    argvalues=[
        pytest.param((0, 0), (1, 2)),
        pytest.param((2, 2), (2, 6)),
    ],
)
def test_get_neighbour_values(mock_input, light_location, expected):
    actual = get_neighbour_values(input=mock_input, light_location=light_location)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["light_location", "expected"],
    argvalues=[
        pytest.param((0, 0), "."),
        pytest.param((2, 2), "."),
        pytest.param((0, 2), "#"),
    ],
)
def test_get_next_light_state(mock_input, light_location, expected):
    actual = get_next_light_state(input=mock_input, light_location=light_location)
    assert actual == expected


def test_get_next_total_state(mock_input):
    actual = get_next_total_state(input=mock_input)
    assert actual == [
        "..##..",
        "..##.#",
        "...##.",
        "......",
        "#.....",
        "#.##..",
    ]


def test_get_next_total_state_exclude_corners(mock_updated_input):
    actual = get_next_total_state_exclude_corners(input=mock_updated_input)
    assert actual == [
        "#.##.#",
        "####.#",
        "...##.",
        "......",
        "#...#.",
        "#.####",
    ]


def test_get_final_state_after_4_steps(mock_input):
    actual = get_final_state(input=mock_input, steps=4)
    assert actual == [
        "......",
        "......",
        "..##..",
        "..##..",
        "......",
        "......",
    ]


@pytest.mark.parametrize(
    argnames=["steps", "expected"],
    argvalues=[
        pytest.param(1, 11),
        pytest.param(2, 8),
        pytest.param(3, 4),
        pytest.param(4, 4),
    ],
)
def test_get_final_light_on_count(mock_input, steps, expected):
    actual = get_final_light_on_count(input=mock_input, steps=steps)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["steps", "expected"],
    argvalues=[
        pytest.param(1, 18),
        pytest.param(2, 18),
        pytest.param(3, 18),
        pytest.param(4, 14),
        pytest.param(5, 17),
    ],
)
def test_get_final_light_on_count_updated_rules(mock_updated_input, steps, expected):
    actual = get_final_light_on_count(
        input=mock_updated_input, steps=steps, updated_rules=True
    )
    assert actual == expected
