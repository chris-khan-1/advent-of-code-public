import itertools


def get_starting_grid(size: int) -> list[list]:
    """
    Returns a size x size grid of list of lists.
    Initialised with value 0 signalling off
    """
    return [[0] * size for _ in range(size)]


def extract_instruction(instruction: str) -> tuple[str, list, list]:
    """
    Extract the command to action and the start and end coordinates of the instruction.
    """
    actions = ["toggle", "turn on", "turn off"]
    for action in actions:
        if action in instruction:
            command = action
            remaining_instruction = (
                instruction.replace(action, "").strip().split(" through ")
            )
            start_coordinate = [int(i) for i in remaining_instruction[0].split(",")]
            end_coordinate = [int(i) for i in remaining_instruction[1].split(",")]
        continue

    return command, start_coordinate, end_coordinate


def turn_on(value):
    return value + 1


def turn_off(value):
    return max(value - 1, 0)


def toggle_light(value):
    return value + 2


def do_instruction(grid: list[list], instruction: str) -> list[list]:
    command, start_coordinate, end_coordinate = extract_instruction(
        instruction=instruction
    )
    x_to_change = [x for x in range(start_coordinate[0], end_coordinate[0] + 1)]
    y_to_change = [y for y in range(start_coordinate[1], end_coordinate[1] + 1)]

    coordinates_to_change = list(itertools.product(x_to_change, y_to_change))

    func_dict = {"turn on": turn_on, "turn off": turn_off, "toggle": toggle_light}

    for coordinate in coordinates_to_change:
        x, y = coordinate
        grid[x][y] = func_dict[command](value=grid[x][y])

    return grid


def do_multiple_instructions(grid: list[list], instructions: list[str]) -> list[list]:
    for instruction in instructions:
        grid = do_instruction(grid=grid, instruction=instruction)
    return grid


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_06/input.txt"
    result_path = "./src/aoc_2015/day_06/result.txt"

    instructions = helpers.read_file_lines(file_path=input_path)
    initial_grid = get_starting_grid(1000)
    final_grid = do_multiple_instructions(grid=initial_grid, instructions=instructions)
    brightness = sum([sum(sublist) for sublist in final_grid])

    result = f"Part 2: The total brightness is now {brightness}!"

    helpers.append_to_file(file_path=result_path, contents=result)
