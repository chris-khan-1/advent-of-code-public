from itertools import combinations


def get_combinations(containers: list[int], total_size: int) -> list[tuple]:
    container_combinations = []
    for number_of_containers in range(1, len(containers) + 1):
        for combo in combinations(containers, number_of_containers):
            if sum(combo) == total_size:
                container_combinations.append(combo)
    return container_combinations


def get_total_combinations(containers: list[int], total_size: int) -> int:
    return len(get_combinations(containers=containers, total_size=total_size))


def get_min_container_combinations(
    containers: list[int], total_size: int
) -> list[tuple] | None:
    container_combinations = []
    for number_of_containers in range(1, len(containers) + 1):
        for combo in combinations(containers, number_of_containers):
            if sum(combo) == total_size:
                container_combinations.append(combo)
        if len(container_combinations) == 0:
            container_combinations = []
        else:
            return container_combinations
    return None


def get_total_min_container_combinations(containers: list[int], total_size: int) -> int:
    return len(
        get_min_container_combinations(containers=containers, total_size=total_size)
        or ""
    )


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

    input_path = "./src/aoc_2015/day_17/input.txt"
    result_path = "./src/aoc_2015/day_17/result.txt"

    containers = [int(i) for i in helpers.read_file_lines(file_path=input_path)]
    total_combos = get_total_combinations(containers=containers, total_size=150)
    total_min_size_combos = get_total_min_container_combinations(
        containers=containers, total_size=150
    )

    result = f"""\
        Part 1:
        The total number of combos to fit 150 litres of eggnog is {total_combos}.

        Part 2:
        The total number of combos, with minimal size, to fit 150 litres of eggnog is {total_min_size_combos}.
        """

    helpers.write_file(file_path=result_path, contents=result)
