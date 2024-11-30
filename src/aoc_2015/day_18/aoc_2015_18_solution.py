from itertools import product


def get_neighbour_values(
    input: list[str], light_location: tuple[int, int]
) -> tuple[int, int]:
    """Returns the number of on and off neighbours (on, off)."""
    x, y = light_location
    neighbours_locations = [
        i
        for i in product(range(x - 1, x + 2), range(y - 1, y + 2))
        if (i != light_location)
        and (0 <= i[0] < len(input))
        and (0 <= i[1] < len(input))
    ]
    neighbour_light_values = []
    for loc in neighbours_locations:
        neighbour_light_values.append(input[loc[0]][loc[1]])
    return neighbour_light_values.count("#"), neighbour_light_values.count(".")


def get_next_light_state(input: list[str], light_location: tuple[int, int]):
    on_count, off_count = get_neighbour_values(
        input=input, light_location=light_location
    )
    current_state = input[light_location[0]][light_location[1]]
    if current_state == "#" and 2 <= on_count <= 3:
        return "#"
    elif current_state == "." and on_count == 3:
        return "#"
    else:
        return "."


def get_next_total_state(input: list[str]):
    output = [""] * len(input)
    for x in range(len(input)):
        for y in range(len(input)):
            output[x] += get_next_light_state(input=input, light_location=(x, y))
    return output


def get_next_total_state_exclude_corners(input: list[str]):
    output = [""] * len(input)
    for x in range(len(input)):
        for y in range(len(input)):
            if (x, y) in [
                (0, 0),
                (0, len(input) - 1),
                (len(input) - 1, 0),
                (len(input) - 1, len(input) - 1),
            ]:
                output[x] += "#"
            else:
                output[x] += get_next_light_state(input=input, light_location=(x, y))
    return output


def get_final_state(
    input: list[str], steps: int, updated_rules: bool = False
) -> list[str]:
    if updated_rules:
        next_state_func = get_next_total_state_exclude_corners
    else:
        next_state_func = get_next_total_state
    iteration = 0
    while iteration < steps:
        input = next_state_func(input=input)
        iteration += 1
    return input


def get_final_light_on_count(
    input: list[str], steps: int, updated_rules: bool = False
) -> int:
    final_state = get_final_state(input=input, steps=steps, updated_rules=updated_rules)
    return sum([row.count("#") for row in final_state])


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_18/input.txt"
    result_path = "./src/aoc_2015/day_18/result.txt"

    input = helpers.read_file_lines(file_path=input_path)
    final_light_on_count = get_final_light_on_count(input=input, steps=100)
    final_light_on_count_updated = get_final_light_on_count(
        input=input, steps=100, updated_rules=True
    )

    result = f"""\
        Part 1: The final count for lights on is {final_light_on_count}.
        Part 2: The final count for lights on is {final_light_on_count_updated}.
        """

    helpers.write_file(file_path=result_path, contents=result)
