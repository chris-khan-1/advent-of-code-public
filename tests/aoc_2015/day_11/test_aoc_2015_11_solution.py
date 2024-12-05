import pytest

from src.aoc_2015.day_11.aoc_2015_11_solution import (  # noqa: F401
    get_next_valid_password,
)
from src.aoc_2015.day_11.aoc_2015_11_solution import (
    get_next_possible_password,
    is_password_valid,
    next_letter,
    update_password_with_next_letter,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("x", "y"),
        pytest.param("z", "a"),
    ],
)
def test_next_letter(input, expected):
    actual = next_letter(old_letter=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["old_password", "letter", "letter_index", "expected"],
    argvalues=[
        pytest.param("bx", "x", 1, "by"),
        pytest.param("xz", "z", 1, "xa"),
        pytest.param("xyz", "z", 2, "xya"),
        pytest.param("xza", "z", 1, "xaa"),
    ],
)
def test_update_password_with_next_letter(old_password, letter, letter_index, expected):
    actual = update_password_with_next_letter(old_password, letter, letter_index)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("bx", "by"),
        pytest.param("xz", "ya"),
        pytest.param("xyz", "xza"),
        pytest.param("xzz", "yaa"),
    ],
)
def test_get_next_possible_password(input, expected):
    actual = get_next_possible_password(old_password=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("hijklmmn", False),
        pytest.param("abbceffg", False),
        pytest.param("abbcegjk", False),
        pytest.param("abcxzyza", False),
        pytest.param("abcxxzza", True),
        pytest.param("", False),
    ],
)
def test_is_password_valid(input, expected):
    actual = is_password_valid(password=input)
    assert actual == expected


# commented out due to long runtime

# @pytest.mark.parametrize(
#     argnames=["input", "expected"],
#     argvalues=[
#         pytest.param("abcdefgh", "abcdffaa"),
#         pytest.param("ghijklmn", "ghjaabcc"),
#     ],
# )
# def test_get_next_valid_password(input, expected):
#     actual = get_next_valid_password(old_password=input)
#     assert actual == expected
