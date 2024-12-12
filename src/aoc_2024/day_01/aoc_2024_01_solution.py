def parse_input(input: list[str]) -> tuple[list, list]:
    left = []
    right = []
    for value in input:
        left_value, right_value = map(int, value.split())
        left.append(left_value)
        right.append(right_value)
    return sorted(left), sorted(right)


def get_total_difference(left: list, right: list) -> int:
    return sum(abs(x - y) for x, y in zip(left, right))


def get_total_similarity(left: list, right: list) -> int:
    return sum(x * right.count(x) for x in left)


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

    input_path = "./src/aoc_2024/day_01/input.txt"
    result_path = "./src/aoc_2024/day_01/result.txt"

    input = helpers.read_file_lines(file_path=input_path)
    left_input, right_input = parse_input(input=input)

    total_distance = get_total_difference(left=left_input, right=right_input)
    total_similarity = get_total_similarity(left=left_input, right=right_input)

    result = f"""\
        Part 1: The total distance is {total_distance}.
        Part 2: The total similarity is {total_similarity}.
        """

    helpers.write_file(file_path=result_path, contents=result)
