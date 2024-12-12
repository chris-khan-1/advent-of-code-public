def get_direction(input: str):
    """
    Gets direction or up (+1) or down (-1) a floor

    Args:
        input: string consisting of '(' or ')'.

    Returns:
        Value for direction
    """
    if input == "(":
        return 1
    elif input == ")":
        return -1


def get_final_floor(input: str) -> int:
    """
    Retrieves the final floor.

    Args:
        input: string consisting of '(' and ')'.

    Returns:
        The final floor value.
    """
    floor = 0
    for i in input:
        floor += get_direction(input=i)
    return floor


def get_basement(input: str) -> int:
    """
    Gets the character position when you reach the basement.

    Args:
        input: string consisting of multiple '(' and/or ')'.

    Returns:
        Character position of basement
    """
    floor = 0
    for character_position, character in enumerate(input):
        floor += get_direction(input=character)

        if floor == -1:
            return character_position + 1

    raise ValueError("Basement was not reached")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

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
