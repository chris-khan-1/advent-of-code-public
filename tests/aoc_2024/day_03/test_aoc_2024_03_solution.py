from src.aoc_2024.day_03.aoc_2024_03_solution import (
    do_instruction,
    get_conditional_valid_instructions,
    get_total,
    get_valid_instructions,
)


def test_get_valid_instructions():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    actual = get_valid_instructions(input=input)
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    assert sorted(actual) == sorted(expected)


def test_get_conditional_valid_instructions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    actual = get_conditional_valid_instructions(input=input)
    expected = ["mul(2,4)", "mul(8,5)"]
    assert sorted(actual) == sorted(expected)


def test_do_instruction():
    input = "mul(44,46)"
    actual = do_instruction(input=input)
    assert actual == 44 * 46


def test_get_total_no_conditions():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    actual = get_total(input=input, conditional=False)
    assert actual == 161


def test_get_total_conditions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    actual = get_total(input=input, conditional=True)
    assert actual == 48
