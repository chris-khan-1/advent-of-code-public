import random
import re


def parse_replacement_map(input: list[str]) -> list[tuple]:
    replacements = []
    for replacement_string in input:
        old, new = replacement_string.split(" => ")
        replacements.append((old, new))
    return replacements


def get_possible_molecules(
    calibration_molecule: str, replacements: list[tuple]
) -> list[str]:
    output = []
    for substring, replacement_string in replacements:
        substring_index_span = [
            match.span()
            for match in re.finditer(pattern=substring, string=calibration_molecule)
        ]
        for start, end in substring_index_span:
            output.append(
                calibration_molecule[:start]
                + replacement_string
                + calibration_molecule[end:]
            )
    return output


def count_distinct_possible_molecules(
    input: list[str], calibration_molecule: str
) -> int:
    replacements = parse_replacement_map(input=input)
    possible_molecules = get_possible_molecules(
        calibration_molecule=calibration_molecule, replacements=replacements
    )
    return len(set(possible_molecules))


def get_fewest_replacements(input: list[str], molecule: str) -> int:
    replacements = sorted(parse_replacement_map(input=input))
    target = molecule
    steps = 0

    while target != "e":
        tmp = target
        for left, right in replacements:
            if right not in target:
                continue

            target = target.replace(right, left, 1)
            steps += 1

        if tmp == target:
            target = molecule
            steps = 0
            random.shuffle(replacements)
    return steps


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_19/input.txt"
    result_path = "./src/aoc_2015/day_19/result.txt"

    raw_input = helpers.read_file_lines(file_path=input_path)
    input = raw_input[:-2]
    calibration_molecule = raw_input[-1]

    distinct_count = count_distinct_possible_molecules(
        input=input, calibration_molecule=calibration_molecule
    )
    fewest_replacements = get_fewest_replacements(
        input=input, molecule=calibration_molecule
    )
    result = f"""\
        Part 1: The number of distinct molecules created is {distinct_count}.
        Part 2: The fewest steps is {fewest_replacements}.
        """

    helpers.write_file(file_path=result_path, contents=result)
