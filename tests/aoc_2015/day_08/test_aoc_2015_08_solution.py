import pytest

from src.aoc_2015.day_08.aoc_2015_08_solution import (
    count_decoded_characters,
    count_encoded_characters,
    count_memory_characters,
    encode_string,
    get_diff,
    get_diff_2,
    get_diff_list_input,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(r'""', 2),
        pytest.param(r'"abc"', 5),
        pytest.param(r'"aaa\"aaa"', 10),
        pytest.param(r'"\x27"', 6),
    ],
)
def test_count_memory_characters(input, expected):
    actual = count_memory_characters(string=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(r'""', 0),
        pytest.param(r'"abc"', 3),
        pytest.param(r'"aaa\"aaa"', 7),
        pytest.param(r'"\x27"', 1),
    ],
)
def test_count_characters(input, expected):
    actual = count_decoded_characters(string=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(r'""', r'"\"\""'),
        pytest.param(r'"abc"', r'"\"abc\""'),
        pytest.param(r'"aaa\"aaa"', r'"\"aaa\\\"aaa\""'),
        pytest.param(r'"\x27"', r'"\"\\x27\""'),
    ],
)
def test_encode_string(input, expected):
    actual = encode_string(string=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(r'""', 6),
        pytest.param(r'"abc"', 9),
        pytest.param(r'"aaa\"aaa"', 16),
        pytest.param(r'"\x27"', 11),
    ],
)
def test_count_encoded_characters(input, expected):
    actual = count_encoded_characters(string=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(r'""', 2),
        pytest.param(r'"abc"', 2),
        pytest.param(r'"aaa\"aaa"', 3),
        pytest.param(r'"\x27"', 5),
    ],
)
def test_get_diff(input, expected):
    actual = get_diff(string=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["diff_func", "expected"],
    argvalues=[pytest.param(get_diff, 12), pytest.param(get_diff_2, 19)],
)
def test_get_diff_list_input(diff_func, expected):
    input = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
    actual = get_diff_list_input(diff_func=diff_func, input_string_list=input)
    assert actual == expected
