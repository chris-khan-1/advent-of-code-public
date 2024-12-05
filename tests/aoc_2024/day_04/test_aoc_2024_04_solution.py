import pytest

from src.aoc_2024.day_04.aoc_2024_04_solution import (
    check_x_diagonal,
    count_mas_diagonals,
    count_word_occurrences,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(
            [["X", "M", "A", "S", ".", "."]], 1, id="horizontal_left_to_right"
        ),
        pytest.param([["S", "A", "M", "X", "."]], 1, id="horizontal_right_to_left"),
        pytest.param(
            [
                ["X"],
                ["M"],
                ["A"],
                ["S"],
                ["."],
            ],
            1,
            id="vertical_top_to_bottom",
        ),
        pytest.param(
            [
                ["S"],
                ["A"],
                ["M"],
                ["X"],
                ["."],
            ],
            1,
            id="vertical_bottom_to_top",
        ),
        pytest.param(
            [
                ["X", ".", ".", ".", "."],
                [".", "M", ".", ".", "."],
                [".", ".", "A", ".", "."],
                [".", ".", ".", "S", "."],
                [".", ".", ".", ".", "."],
            ],
            1,
            id="diagonal_top_left_to_bottom_right",
        ),
        pytest.param(
            [
                [".", ".", ".", ".", "."],
                [".", "S", ".", ".", "."],
                [".", ".", "A", ".", "."],
                [".", ".", ".", "M", "."],
                [".", ".", ".", ".", "X"],
                [".", ".", ".", ".", "."],
            ],
            1,
            id="diagonal_bottom_right_to_top_left",
        ),
        pytest.param(
            [
                [".", ".", ".", "X", "."],
                [".", ".", "M", ".", "."],
                [".", "A", ".", ".", "."],
                ["S", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
            ],
            1,
            id="anti_diagonal_top_right_to_bottom_left",
        ),
        pytest.param(
            [
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "S"],
                [".", ".", ".", "A", "."],
                [".", ".", "M", ".", "."],
                [".", "X", ".", ".", "."],
            ],
            1,
            id="anti_diagonal_bottom_left_to_top_right",
        ),
        pytest.param(
            [
                [".", ".", "X", ".", ".", "."],
                [".", "S", "A", "M", "X", "."],
                [".", "A", ".", ".", "A", "."],
                ["X", "M", "A", "S", ".", "S"],
                [".", "X", ".", ".", ".", "."],
            ],
            4,
        ),
        pytest.param(
            [
                ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
                ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
                ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
                ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
                ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
                ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
                ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
                ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
                ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
                ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
            ],
            18,
        ),
    ],
)
def test_count_word_occurrences(input, expected):
    actual = count_word_occurrences(target_word="XMAS", grid=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param(
            [
                ["S", ".", "S"],
                [".", "A", "."],
                ["M", ".", "M"],
            ],
            True,
        ),
        pytest.param(
            [
                ["M", ".", "S"],
                [".", "A", "."],
                ["M", ".", "S"],
            ],
            True,
        ),
        pytest.param(
            [
                ["S", ".", "M"],
                [".", "A", "."],
                ["S", ".", "M"],
            ],
            True,
        ),
        pytest.param(
            [
                ["M", ".", "M"],
                [".", "A", "."],
                ["S", ".", "S"],
            ],
            True,
        ),
        pytest.param(
            [
                ["S", ".", "M"],
                [".", "A", "."],
                ["M", ".", "S"],
            ],
            False,
        ),
    ],
)
def test_check_x_diagonal(input, expected):
    actual = check_x_diagonal(grid=input, row=1, col=1)
    assert actual == expected


def test_count_mas_diagonals():
    input = [
        [".", "M", ".", "S", ".", ".", ".", ".", ".", "."],
        [".", ".", "A", ".", ".", "M", "S", "M", "S", "."],
        [".", "M", ".", "S", ".", "M", "A", "A", ".", "."],
        [".", ".", "A", ".", "A", "S", "M", "S", "M", "."],
        [".", "M", ".", "S", ".", "M", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["S", ".", "S", ".", "S", ".", "S", ".", "S", "."],
        [".", "A", ".", "A", ".", "A", ".", "A", ".", "."],
        ["M", ".", "M", ".", "M", ".", "M", ".", "M", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    actual = count_mas_diagonals(grid=input)
    assert actual == 9
