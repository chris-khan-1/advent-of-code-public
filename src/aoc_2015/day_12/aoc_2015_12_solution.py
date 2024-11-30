import json
import re
from typing import Any


def get_digits_from_string(input: str) -> list[str]:
    """Gets all positive and negative digits from a string"""
    return re.findall(r"[-]?\d+", input)


def get_sum_of_digits_from_string(input: str) -> int:
    digits = get_digits_from_string(input=input)
    return sum([int(i) for i in digits])


def hook(obj: dict[Any, Any]) -> dict[Any, Any]:
    if "red" in obj.values():
        return {}
    return obj


def read_json_no_red(input: str):
    """Read json input with custom hook to remove objects with 'red' in them."""
    return json.loads(s=input, object_hook=hook)


def get_reduced_sum_of_digits_from_json(input: str):
    reduced_input = str(read_json_no_red(input=input))
    return get_sum_of_digits_from_string(input=reduced_input)


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_12/input.json"
    result_path = "./src/aoc_2015/day_12/result.txt"

    input = helpers.read_file(file_path=input_path)

    sum_of_all_digits = get_sum_of_digits_from_string(input=input)
    sum_of_reduced_input_digits = get_reduced_sum_of_digits_from_json(input=input)

    result = f"""\
        Part 1: The sum of all digits is {sum_of_all_digits}.
        Part 2: The sum of all digits for the reduced input is {sum_of_reduced_input_digits}.
        """

    helpers.write_file(file_path=result_path, contents=result)
