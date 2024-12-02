import pytest

from src.aoc_2024.day_02.aoc_2024_02_solution import (
    check_safety,
    check_safety_with_damper,
    parse_input,
)


def test_parse_input():
    input = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    acutal = parse_input(input=input)

    expected = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert acutal == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param([7, 6, 4, 2, 1], True),
        pytest.param([1, 2, 7, 8, 9], False),
        pytest.param([9, 7, 6, 2, 1], False),
        pytest.param([1, 3, 2, 4, 5], False),
        pytest.param([8, 6, 4, 4, 1], False),
        pytest.param([1, 3, 6, 7, 9], True),
    ],
)
def test_check_safety(input, expected):
    actual = check_safety(data=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param([7, 6, 4, 2, 1], True),
        pytest.param([1, 2, 7, 8, 9], False),
        pytest.param([9, 7, 6, 2, 1], False),
        pytest.param([1, 3, 2, 4, 5], True),
        pytest.param([8, 6, 4, 4, 1], True),
        pytest.param([1, 3, 6, 7, 9], True),
    ],
)
def test_check_safety_with_damper(input, expected):
    actual = check_safety_with_damper(data=input)
    assert actual == expected
