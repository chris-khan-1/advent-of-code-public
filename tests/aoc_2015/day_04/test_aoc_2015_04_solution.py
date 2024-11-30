import pytest

from src.aoc_2015.day_04.aoc_2015_04_solution import (  # noqa: F401
    check_starts_with_number_of_zeroes,
    get_lowest_value_required,
    get_md5_hash,
)


@pytest.mark.parametrize(
    argnames=["secret_key", "input", "expected"],
    argvalues=[
        pytest.param("abcdef", 609043, "000001dbbfa3a5c83a2d506429c7b00e"),
        pytest.param("pqrstuv", 1048970, "000006136ef2ff3b291c85725f17325c"),
    ],
)
def test_get_md5_hash(secret_key, input, expected):
    actual = get_md5_hash(secret_key=secret_key, value=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "digit_length", "expected"],
    argvalues=[
        pytest.param("00000xy", 5, True),
        pytest.param("abcdefg", 5, False),
    ],
)
def test_check_starts_with_number_of_zeroes(input, digit_length, expected):
    actual = check_starts_with_number_of_zeroes(input=input, digit_length=digit_length)
    assert actual == expected


# Commented out for perfomance
# @pytest.mark.parametrize(
#     argnames=["secret_key", "digit_length", "expected"],
#     argvalues=[
#         pytest.param("abcdef", 5, 609043),
#         pytest.param("pqrstuv", 5, 1048970),
#     ],
# )
# def test_get_lowest_value_required(secret_key, digit_length, expected):
#     actual = get_lowest_value_required(secret_key=secret_key, digit_length=digit_length)
#     assert actual == expected
