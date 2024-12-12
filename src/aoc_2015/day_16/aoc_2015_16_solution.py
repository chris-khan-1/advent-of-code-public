from collections import defaultdict

default_attributes = [
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes",
]


def parse_sue_info(input: list[str]) -> dict:
    sue_info = defaultdict(dict)
    for info_str in input:
        sue_number_str, attribute_str = info_str.split(sep=": ", maxsplit=1)
        sue_number = sue_number_str.split(" ")[1]
        attribute_dict: dict[str, int | None] = {i: None for i in default_attributes}
        for attribute in attribute_str.split(", "):
            key, value = attribute.split(": ")
            attribute_dict[key] = int(value)
        sue_info[sue_number] = attribute_dict

    return sue_info


def check_sue(individual_sue_info: dict, test_results: dict):
    for attribute, value in individual_sue_info.items():
        if value is not None:
            if test_results[attribute] != value:
                return False
    return True


def get_correct_sue(input: list[str], test_results: dict):
    sue_info = parse_sue_info(input=input)
    for sue, attributes in sue_info.items():
        if check_sue(individual_sue_info=attributes, test_results=test_results):
            return sue


def check_sue_updated(individual_sue_info: dict, test_results: dict):
    for attribute, value in individual_sue_info.items():
        if value is not None:
            if attribute in ("cats", "trees"):
                if value <= test_results[attribute]:
                    return False
            elif attribute in ("pomeranians", "goldfish"):
                if test_results[attribute] <= value:
                    return False
            else:
                if test_results[attribute] != value:
                    return False
    return True


def get_correct_sue_updated(input: list[str], test_results: dict):
    sue_info = parse_sue_info(input=input)
    for sue, attributes in sue_info.items():
        if check_sue_updated(individual_sue_info=attributes, test_results=test_results):
            return sue


if __name__ == "__main__":
    with open("./2015/16/input.txt", "r") as input_file:
        input = [line.strip() for line in input_file.readlines()]
        test_results = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }
        correct_sue = get_correct_sue(input=input, test_results=test_results)
        updated_correct_sue = get_correct_sue_updated(
            input=input, test_results=test_results
        )

    with open("./2015/16/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: The correct sue is number {correct_sue}.\n")
        output_file.write(f"Part 2: The updated sue is number {updated_correct_sue}.")

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

    input_path = "./src/aoc_2015/day_16/input.txt"
    result_path = "./src/aoc_2015/day_16/result.txt"

    input = helpers.read_file_lines(file_path=input_path)

    test_results = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    correct_sue = get_correct_sue(input=input, test_results=test_results)
    updated_correct_sue = get_correct_sue_updated(
        input=input, test_results=test_results
    )

    result = f"""\
        Part 1: The correct sue is number {correct_sue}.
        Part 2: The updated sue is number {updated_correct_sue}.
        """

    helpers.write_file(file_path=result_path, contents=result)
