import pytest

from src.aoc_2015.day_05.aoc_2015_05_solution import (
    contains_pair_of_letters_at_least_twice,
    contains_repeat_with_one_letter_gap,
    double_letter_exists,
    is_clear_of_bad_strings,
    is_definitely_nice_string,
    is_nice_string,
    three_vowels_exist,
)


# --- Part One ---
@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("aaa", True),
        pytest.param("eee", True),
        pytest.param("iii", True),
        pytest.param("ooo", True),
        pytest.param("uuu", True),
        pytest.param("xyz", False),
    ],
)
def test_three_vowels_exist(input, expected):
    actual = three_vowels_exist(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[pytest.param("aa", True), pytest.param("xy", False)],
)
def test_double_letter_exists(input, expected):
    actual = double_letter_exists(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("ab", False),
        pytest.param("cd", False),
        pytest.param("pq", False),
        pytest.param("xy", False),
        pytest.param("aa", True),
    ],
)
def test_is_clear_of_bad_strings(input, expected):
    actual = is_clear_of_bad_strings(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("ugknbfddgicrmopn", True),
        pytest.param("aaa", True),
        pytest.param("jchzalrnumimnmhp", False),
        pytest.param("haegwjzuvuyypxyu", False),
        pytest.param("dvszwmarrgswjxmb", False),
    ],
)
def test_is_nice_string(input, expected):
    actual = is_nice_string(input=input)
    assert actual == expected


# --- Part Two ---
@pytest.mark.parametrize(
    argnames=["string", "expected"],
    argvalues=[
        pytest.param("xyxy", True, id="xy"),
        pytest.param("aabcdefgaa", True, id="aa"),
        pytest.param("aaa", False, id="overlaps"),
        pytest.param("aaaaa", True, id="overlaps 5"),
        pytest.param("abcd", False, id="no matches"),
    ],
)
def test_contains_pair_of_letters_at_least_twice(string, expected):
    actual = contains_pair_of_letters_at_least_twice(string=string)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["string", "expected"],
    argvalues=[
        pytest.param("xyx", True, id="xyx"),
        pytest.param("abcdefeghi", True, id="efe"),
        pytest.param("aaa", True, id="aaa"),
        pytest.param("abc", False, id="no gap"),
        pytest.param("abca", False, id="2 gap"),
        pytest.param("abaca", True, id="multiple trues"),
    ],
)
def test_contains_repeat_with_one_letter_gap(string, expected):
    actual = contains_repeat_with_one_letter_gap(string=string)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("qjhvhtzxzqqjkmpb", True),
        pytest.param("xxyxx", True),
        pytest.param("uurcxstgmygtbstg", False, id="no repeat single letter"),
        pytest.param("ieodomkazucvgmuy", False, id="no pair twice"),
    ],
)
def test_is_definitely_nice_string(input, expected):
    actual = is_definitely_nice_string(input=input)
    assert actual == expected
