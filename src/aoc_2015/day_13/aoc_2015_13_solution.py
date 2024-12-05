from collections import defaultdict
from itertools import permutations


def parse_happiness_info(input: list[str]) -> dict:
    info_dict = defaultdict(dict)

    for info in input:
        info_list = info.split(" ")
        first_person = info_list[0]
        second_person = info_list[-1].replace(".", "")
        gain_or_lose = info_list[2]
        happiness_change = int(info_list[3])
        if gain_or_lose == "lose":
            happiness_change = -happiness_change
        info_dict[first_person][second_person] = happiness_change
    return info_dict


def add_myself_to_happiness_info(happiness_info: dict) -> dict:
    for person in happiness_info.keys():
        happiness_info[person]["Me"] = 0
    happiness_info["Me"] = {person: 0 for person in happiness_info.keys()}
    return happiness_info


def get_pair_happiness(happiness_info: dict, person_1: str, person_2: str) -> int:
    return happiness_info[person_1][person_2] + happiness_info[person_2][person_1]


def get_possible_seating_arrangement(happiness_info: dict) -> list:
    people = set(happiness_info.keys())
    return [list(pair) for pair in permutations(people)]


def get_largest_happiness_change(
    input: list[str], include_me: bool = False
) -> int | float:
    happiness_info = parse_happiness_info(input=input)

    if include_me:
        happiness_info = add_myself_to_happiness_info(happiness_info=happiness_info)
    print
    best_happiness_change = -float("inf")

    seating_arrangements = get_possible_seating_arrangement(
        happiness_info=happiness_info
    )

    for arrangement in seating_arrangements:
        # add first person to end for circle
        arrangement = arrangement + [arrangement[0]]
        happiness_change = 0
        for i in range(len(arrangement) - 1):
            happiness_change += get_pair_happiness(
                happiness_info=happiness_info,
                person_1=arrangement[i],
                person_2=arrangement[i + 1],
            )
        if happiness_change > best_happiness_change:
            best_happiness_change = happiness_change
    return best_happiness_change


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_13/input.txt"
    result_path = "./src/aoc_2015/day_13/result.txt"

    input = helpers.read_file_lines(file_path=input_path)

    largest_happiness_change = get_largest_happiness_change(input=input)
    largest_happiness_change_with_me = get_largest_happiness_change(
        input=input, include_me=True
    )

    result = f"""\
        Part 1: The largerst happiness change is {largest_happiness_change}.
        Part 2: The largerst happiness change including myself is {largest_happiness_change_with_me}.
        """

    helpers.write_file(file_path=result_path, contents=result)
