def parse_input(input: list) -> list:
    return [list(map(int, line.split())) for line in input]


def check_safety(data: list) -> bool:
    # sorted not checking strictly increasing, but handled by diff > 1 condition
    if data == sorted(data) or data == sorted(data, reverse=True):
        for i in range(len(data) - 1):
            diff = abs(data[i] - data[i + 1])
            if diff < 1 or diff > 3:
                return False
        return True
    return False


def check_safety_with_damper(data: list) -> bool:
    if check_safety(data=data):
        return True
    else:
        for i in range(len(data)):
            new_data = data.copy()
            del new_data[i]

            if check_safety(data=new_data):
                return True
    return False


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2024/day_02/input.txt"
    result_path = "./src/aoc_2024/day_02/result.txt"

    string_input = helpers.read_file_lines(file_path=input_path)

    input = parse_input(string_input)
    total_safe = sum([check_safety(report) for report in input])
    total_safe_with_damper = sum([check_safety_with_damper(report) for report in input])

    result = f"""\
        Part 1: The total safe reports is {total_safe}
        Part 2: The total safe reports with the damper is {total_safe_with_damper}
        """

    helpers.write_file(file_path=result_path, contents=result)
