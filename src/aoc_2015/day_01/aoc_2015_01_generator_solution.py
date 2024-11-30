from collections.abc import Generator


def generate_next_floor(input: str) -> Generator[int]:
    """
    Generates the value of increasing or decreasing floor number.

    Args:
        input: string consisting of '(' or ')'.

    Yields:
        The next value for floor direction.
    """
    for i in input:
        if i == "(":
            yield 1
        elif i == ")":
            yield -1


def get_final_floor(input: str) -> int:
    """
    Retrieves the final floor.

    Args:
        input: string consisting of '(' and ')'.

    Returns:
        The final floor value.
    """
    return sum([i for i in generate_next_floor(input=input)])


def get_basement(input: str) -> int:
    """
    Gets the character position when you reach the basement.

    Args:
        input: string consisting of multiple '(' and/or ')'.

    Returns:
        Character position of basement
    """
    floor = 0
    character_position = 0
    floor_direction = generate_next_floor(input=input)
    while floor != -1:
        floor += next(floor_direction)
        character_position += 1

    return character_position


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_01/input.txt"
    result_path = "./src/aoc_2015/day_01/result.txt"

    string_input = helpers.read_file(file_path=input_path)

    final_floor = get_final_floor(input=string_input)
    basement_character_position = get_basement(input=string_input)

    result = f"""\
        Part 1: Santa ends up on floor {final_floor}
        Part 2: Character position for basement is {basement_character_position}
        """

    helpers.write_file(file_path=result_path, contents=result)
