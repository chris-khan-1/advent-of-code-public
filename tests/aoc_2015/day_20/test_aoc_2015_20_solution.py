import pytest

from src.aoc_2015.day_20.aoc_2015_20_solution import (
    get_factors,
    get_lowest_house_number_given_total_presents,
    get_number_of_presents_for_house,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(1, {1}),
        pytest.param(2, {1, 2}),
        pytest.param(3, {1, 3}),
        pytest.param(4, {1, 2, 4}),
        pytest.param(5, {1, 5}),
        pytest.param(6, {1, 2, 3, 6}),
        pytest.param(7, {1, 7}),
        pytest.param(8, {1, 2, 4, 8}),
        pytest.param(9, {1, 3, 9}),
    ],
)
def test_get_factors(input, expected):
    actual = get_factors(n=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(1, 10),
        pytest.param(2, 30),
        pytest.param(3, 40),
        pytest.param(4, 70),
        pytest.param(5, 60),
        pytest.param(6, 120),
        pytest.param(7, 80),
        pytest.param(8, 150),
        pytest.param(9, 130),
    ],
)
def test_get_number_of_presents_for_house(input, expected):
    actual = get_number_of_presents_for_house(house_number=input)
    assert actual == expected


def test_get_lowest_house_number_given_total_presents():
    actual = get_lowest_house_number_given_total_presents(total_presents=80)
    assert actual == 6
