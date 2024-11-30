def get_factors(n: int) -> set[int]:
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors


def get_number_of_presents_for_house(house_number: int) -> int:
    return 10 * sum(get_factors(n=house_number))


def get_lowest_house_number_given_total_presents(total_presents: int) -> int:
    house_number = 1
    present_count = 0
    while present_count < total_presents:
        present_count = get_number_of_presents_for_house(house_number=house_number)
        house_number += 1
    return house_number - 1


def get_new_lowest_house_number_given_total_presents(total_presents: int) -> int:
    house_number = 1
    present_count = 0
    while present_count < total_presents:
        present_count = 11 * sum(
            [i for i in get_factors(n=house_number) if house_number <= i * 50]
        )
        house_number += 1
    return house_number - 1


if __name__ == "__main__":
    import sys
    import time
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_20/input.txt"
    result_path = "./src/aoc_2015/day_20/result.txt"

    input = int(helpers.read_file(file_path=input_path))

    part_1_start = time.time()

    lowest_house = get_lowest_house_number_given_total_presents(total_presents=input)
    part_1_end = time.time()

    new_lowest_house = get_new_lowest_house_number_given_total_presents(
        total_presents=input
    )

    part_2_end = time.time()
    result = f"""\
        Part 1: The lowest house number is {lowest_house}. It took {part_1_end - part_1_start:.3f}s.
        Part 2: The new lowest house number is {new_lowest_house}. It took {part_2_end - part_1_end:.3f}s.
        """

    helpers.write_file(file_path=result_path, contents=result)
