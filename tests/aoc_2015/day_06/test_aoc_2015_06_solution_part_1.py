import pytest

from src.aoc_2015.day_06.aoc_2015_06_solution_part_1 import (
    do_instruction,
    do_multiple_instructions,
    extract_instruction,
    get_starting_grid,
)


@pytest.mark.parametrize(
    argnames=["size", "expected"],
    argvalues=[
        pytest.param(1, [[0]]),
        pytest.param(2, [[0, 0], [0, 0]]),
        pytest.param(3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
    ],
)
def test_get_starting_grid(size, expected):
    actual = get_starting_grid(size=size)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["instruction", "expected_command", "expected_start", "expected_end"],
    argvalues=[
        pytest.param(
            "toggle 461,550 through 564,900",
            "toggle",
            [461, 550],
            [564, 900],
            id="toggle",
        ),
        pytest.param("turn off 1,1 through 3,3", "turn off", [1, 1], [3, 3], id="off"),
        pytest.param("turn on 4,4 through 5,5", "turn on", [4, 4], [5, 5], id="on"),
    ],
)
def test_extract_instruction(
    instruction, expected_command, expected_start, expected_end
):
    command, start, end = extract_instruction(instruction=instruction)
    assert command == expected_command
    assert start == expected_start
    assert end == expected_end


@pytest.mark.parametrize(
    argnames=["grid", "instruction", "expected"],
    argvalues=[
        pytest.param(
            [[0, 0], [0, 0]],
            "turn on 0,0 through 1,1",
            [[1, 1], [1, 1]],
            id="turn all on, prev off",
        ),
        pytest.param(
            [[0, 0], [1, 0]],
            "turn on 0,0 through 1,1",
            [[1, 1], [1, 1]],
            id="turn all on, some already on",
        ),
        pytest.param(
            [[0, 0], [0, 0]],
            "turn on 0,0 through 1,0",
            [[1, 0], [1, 0]],
            id="turn some on",
        ),
        pytest.param(
            [[1, 1], [1, 1]],
            "turn off 0,0 through 1,1",
            [[0, 0], [0, 0]],
            id="turn all off",
        ),
        pytest.param(
            [[1, 0], [0, 0]],
            "turn off 0,0 through 1,1",
            [[0, 0], [0, 0]],
            id="turn all off, some already off",
        ),
        pytest.param(
            [[1, 0], [1, 0]],
            "toggle 0,0 through 1,1",
            [[0, 1], [0, 1]],
            id="toggle",
        ),
    ],
)
def test_do_instruction(grid, instruction, expected):
    actual = do_instruction(grid=grid, instruction=instruction)
    assert actual == expected


def test_do_multiple_instructions():
    actual = do_multiple_instructions(
        grid=[[0, 0], [0, 0]],
        instructions=["turn on 0,0 through 1,1", "turn off 0,0 through 0,1"],
    )
    assert actual == [[0, 0], [1, 1]]
