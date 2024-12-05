import pytest

from src.aoc_2015.day_10.aoc_2015_10_solution import (
    get_final_look_and_say_number,
    get_next_look_and_say_number,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("1", "11"),
        pytest.param("11", "21"),
        pytest.param("21", "1211"),
        pytest.param("1211", "111221"),
        pytest.param("111221", "312211"),
    ],
)
def test_get_next_look_and_say_number(input, expected):
    actual = get_next_look_and_say_number(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "iterations", "expected"],
    argvalues=[
        pytest.param("1", 1, "11"),
        pytest.param("1", 2, "21"),
        pytest.param("1", 5, "312211"),
    ],
)
def test_get_final_look_and_say_number(input, iterations, expected):
    actual = get_final_look_and_say_number(input=input, iterations=iterations)
    assert actual == expected
