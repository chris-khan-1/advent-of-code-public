import pytest

from src.aoc_2015.day_01.aoc_2015_01_solution import (
    get_basement,
    get_direction,
    get_final_floor,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("(", 1, id="up"),
        pytest.param(")", -1, id="down"),
    ],
)
def test_get_direction(input, expected):
    actual = get_direction(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("(())", 0, id="0"),
        pytest.param("()()", 0, id="0*"),
        pytest.param("(((", 3, id="3"),
        pytest.param("(()(()(", 3, id="3*"),
        pytest.param("))(((((", 3, id="3**"),
        pytest.param("())", -1, id="-1"),
        pytest.param("))(", -1, id="-1*"),
        pytest.param(")))", -3, id="-3"),
        pytest.param(")())())", -3, id="-3*"),
    ],
)
def test_get_final_floor(input, expected):
    actual = get_final_floor(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(")", 1, id="basement on first position"),
        pytest.param("()())", 5, id="basement on fifth position"),
    ],
)
def test_get_basement(input, expected):
    actual = get_basement(input=input)
    assert actual == expected


def test_get_basement_not_reached():
    with pytest.raises(ValueError):
        get_basement(input="")
