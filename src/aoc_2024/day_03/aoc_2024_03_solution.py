import re


def get_valid_instructions(input: str) -> list:
    return re.findall(pattern=r"mul\(\d{1,3},\d{1,3}\)", string=input)


def do_instruction(input: str) -> int:
    a, b = input[4:-1].split(",")
    return int(a) * int(b)


def get_conditional_valid_instructions(input: str) -> list:
    instructions_to_do = []
    do = True
    for match in re.findall(
        pattern=r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", string=input
    ):
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do:
            instructions_to_do.append(match)
    return instructions_to_do


def get_total(input: str, conditional: bool = False) -> int:
    if conditional:
        func = get_conditional_valid_instructions
    else:
        func = get_valid_instructions

    instructions = func(input=input)
    return sum([do_instruction(input=i) for i in instructions])


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2024/day_03/input.txt"
    result_path = "./src/aoc_2024/day_03/result.txt"

    input = helpers.read_file(file_path=input_path)

    total_no_conditionals = get_total(input=input, conditional=False)
    total_w_conditionals = get_total(input=input, conditional=True)

    result = f"""\
        Part 1: The total without conditionals is {total_no_conditionals}.
        Part 2: The total with conditionals is {total_w_conditionals}.
        """

    helpers.write_file(file_path=result_path, contents=result)
