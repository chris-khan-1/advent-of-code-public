import pytest

from src.aoc_2015.day_02.aoc_2015_02_solution import (
    get_ribbon_length,
    get_wrapping_paper_square_footage,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[pytest.param("2x3x4", 58), pytest.param("1x1x10", 43)],
)
def test_get_wrapping_paper_square_footage(input, expected):
    actual = get_wrapping_paper_square_footage(dimensions=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[pytest.param("2x3x4", 34), pytest.param("1x1x10", 14)],
)
def test_get_ribbon_length(input, expected):
    actual = get_ribbon_length(dimensions=input)
    assert actual == expected
