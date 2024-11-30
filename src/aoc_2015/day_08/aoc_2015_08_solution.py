from typing import Callable


def count_memory_characters(string: str) -> int:
    return len(string)


def count_decoded_characters(string: str) -> int:
    return len(bytes(string[1:-1], "utf-8").decode("unicode-escape"))


def encode_string(string: str) -> str:
    encoded_string = string.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + encoded_string + '"'


def count_encoded_characters(string: str) -> int:
    return len(encode_string(string))


def get_diff(string: str) -> int:
    return count_memory_characters(string) - count_decoded_characters(string)


def get_diff_2(string: str) -> int:
    return count_encoded_characters(string) - count_memory_characters(string)


def get_diff_list_input(diff_func: Callable, input_string_list: list[str]) -> int:
    return sum([diff_func(string) for string in input_string_list])


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_08/input.txt"
    result_path = "./src/aoc_2015/day_08/result.txt"

    input_string_list = helpers.read_file_lines(file_path=input_path)

    part_1_diff = get_diff_list_input(
        diff_func=get_diff, input_string_list=input_string_list
    )
    part_2_diff = get_diff_list_input(
        diff_func=get_diff_2, input_string_list=input_string_list
    )
    result = f"""\
        Part 1: The difference is {part_1_diff}.
        Part 2: The difference is {part_2_diff}.
        """

    helpers.write_file(file_path=result_path, contents=result)
