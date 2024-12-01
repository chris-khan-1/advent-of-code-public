def parse_input(input: list[str]) -> tuple[list, list]:
    left = []
    right = []
    for i, value in enumerate(input):
        left_value, right_value = value.split()
        left.append(int(left_value))
        right.append(int(right_value))
    return sorted(left), sorted(right)


def get_difference(a: int, b: int) -> int:
    return abs(a - b)


def get_total_difference(left: list, right: list) -> int:
    total = 0
    for i in range(len(left)):
        total += get_difference(a=left[i], b=right[i])
    return total


def get_total_similarity(left: list, right: list) -> int:
    total = 0
    for i in set(left):
        total += i * left.count(i) * right.count(i)
    return total


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

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
