import sys
from itertools import groupby

sys.set_int_max_str_digits(1_000_000)


def get_next_look_and_say_number(input: str) -> str:
    groups = ["".join(group) for _, group in groupby(str(input))]
    output = ""
    for group in groups:
        output += str(len(group))  # num of values
        output += group[0]  # value
    return output


def get_final_look_and_say_number(input: str, iterations: int) -> str:
    i = 0
    value = input
    while i < iterations:
        value = get_next_look_and_say_number(input=value)
        i += 1
    return value


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_10/input.txt"
    result_path = "./src/aoc_2015/day_10/result.txt"

    input = str(helpers.read_file(file_path=input_path))
    part_one_value = get_final_look_and_say_number(input=input, iterations=40)
    part_one_value_length = len(part_one_value)

    part_two_value = get_final_look_and_say_number(input=input, iterations=50)
    part_two_value_length = len(part_two_value)

    result = f"""\
        Part 1: The length of the value after the 40th iteration is {part_one_value_length}.
        Part 2: The length of the value after the 50th iteration is {part_two_value_length}.
        """

    helpers.write_file(file_path=result_path, contents=result)
