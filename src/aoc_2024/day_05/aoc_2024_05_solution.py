import functools


def parse_rules_and_updates(input: str) -> tuple[list, list]:
    top, bottom = [s.split("\n") for s in input.split("\n\n")]

    rules = []
    for line in top:
        rules.append(list(map(int, line.split("|"))))

    updates = []
    for line in bottom:
        updates.append(list(map(int, line.split(","))))
    return rules, updates


def get_rule_cache(rules: list) -> dict:
    """
    Getting comparisons between two values.
    Setting to 1 if order is correct, -1 if not.
    """
    cache = {}
    for x, y in rules:
        cache[(x, y)] = -1  # correct order
        cache[(y, x)] = 1  # incorrect order
    return cache


def check_update(update: list, rule_cache: dict) -> bool:
    # check each index with every index to right
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key_compare = (update[i], update[j])
            if key_compare in rule_cache and rule_cache[key_compare] == 1:
                # check if in rule_cache incase rules are not comprehensive
                # == 1 means incorrect order
                return False
    return True


def get_correct_and_incorrect_updates(input: str) -> tuple[list, list, dict]:
    rules, updates = parse_rules_and_updates(input=input)
    rule_cache = get_rule_cache(rules=rules)

    correct_updates = []
    incorrect_updates = []
    for update in updates:
        if check_update(update=update, rule_cache=rule_cache):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    return correct_updates, incorrect_updates, rule_cache


def get_correct_updates_total(correct_updates: list, rule_cache: dict) -> int:
    total = 0
    for update in correct_updates:
        if check_update(update=update, rule_cache=rule_cache):
            total += update[(len(update) // 2)]
    return total


def get_corrected_update(update: list, rule_cache: dict) -> list:
    def cmp(x: int, y: int) -> int:
        """
        Comparison function based on the given rules.
        Defaults to 0 if comparison not in rules.

        Information:
        Default comparitor for ascending sort is x-y:
            x < y => correct order => x-y = -1 (negative)
            x > y => incorrect order => x-y = 1 (positive)
            x = y => same value => x-y = 0
        """
        return rule_cache.get((x, y), 0)

    return sorted(update, key=functools.cmp_to_key(mycmp=cmp))


def get_corrected_updates_total(incorrect_updates: list, rule_cache: dict) -> int:
    total = 0
    for update in incorrect_updates:
        corrected_update = get_corrected_update(update=update, rule_cache=rule_cache)
        total += corrected_update[(len(corrected_update) // 2)]
    return total


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2024/day_05/input.txt"
    result_path = "./src/aoc_2024/day_05/result.txt"

    input = helpers.read_file(file_path=input_path)
    correct_updates, incorrect_updates, rule_cache = get_correct_and_incorrect_updates(
        input=input
    )
    part_1_total = get_correct_updates_total(
        correct_updates=correct_updates, rule_cache=rule_cache
    )
    part_2_total = get_corrected_updates_total(
        incorrect_updates=incorrect_updates, rule_cache=rule_cache
    )

    result = f"""\
        Part 1: The total for correct updates is {part_1_total}.
        Part 2: The total for the corected updates is {part_2_total}.
        """

    helpers.write_file(file_path=result_path, contents=result)
