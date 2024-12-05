import pytest

from src.aoc_2015.day_12.aoc_2015_12_solution import (
    get_digits_from_string,
    get_reduced_sum_of_digits_from_json,
    get_sum_of_digits_from_string,
    read_json_no_red,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("[1,2,3]", ["1", "2", "3"]),
        pytest.param('{"a":2,"b":4}', ["2", "4"]),
        pytest.param("[[[3]]]", ["3"]),
        pytest.param('{"a":{"b":4},"c":-1}', ["4", "-1"]),
        pytest.param(' {"a":[-1,1]}', ["-1", "1"]),
        pytest.param('[-1,{"a":1}]', ["-1", "1"]),
        pytest.param("[]", []),
        pytest.param("{}", []),
    ],
)
def test_get_digits_from_string(input, expected):
    actual = get_digits_from_string(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("[1,2,3]", 6),
        pytest.param('{"a":2,"b":4}', 6),
        pytest.param("[[[3]]]", 3),
        pytest.param('{"a":{"b":4},"c":-1}', 3),
        pytest.param(' {"a":[-1,1]}', 0),
        pytest.param('[-1,{"a":1}]', 0),
        pytest.param("[]", 0),
        pytest.param("{}", 0),
    ],
)
def test_get_sum_of_digits_from_string(input, expected):
    actual = get_sum_of_digits_from_string(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("[1, 2, 3]", [1, 2, 3]),
        pytest.param('[1, {"c": "red", "b": 2}, 3]', [1, {}, 3]),
        pytest.param('{"d": "red", "e": [1, 2, 3, 4], "f": 5}', {}),
    ],
)
def test_read_json_no_red(input, expected):
    actual = read_json_no_red(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("[1, 2, 3]", 6),
        pytest.param('[1, {"c": "red", "b": 2}, 3]', 4),
        pytest.param('{"d": "red", "e": [1, 2, 3, 4], "f": 5}', 0),
    ],
)
def test_get_reduced_sum_of_digits_from_json(input, expected):
    actual = get_reduced_sum_of_digits_from_json(input=input)
    assert actual == expected
