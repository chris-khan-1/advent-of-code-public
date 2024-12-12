# --- Part One ---


def three_vowels_exist(input: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for letter in input:
        if letter in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return True
    return False


def double_letter_exists(input: str) -> bool:
    for position in range(len(input) - 1):
        if input[position] == input[position + 1]:
            return True
    return False


def is_clear_of_bad_strings(input: str) -> bool:
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_string in bad_strings:
        if bad_string in input:
            return False
    return True


def is_nice_string(input: str) -> bool:
    if not is_clear_of_bad_strings(input=input):  # to exit early
        return False
    elif three_vowels_exist(input=input) and double_letter_exists(input=input):
        return True
    return False


# --- Part Two ---


def contains_pair_of_letters_at_least_twice(string: str) -> bool:
    for i in range(len(string) - 3):
        letter_pair = string[i : i + 2]
        if letter_pair in string[i + 2 :]:
            return True
    return False


def contains_repeat_with_one_letter_gap(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


def is_definitely_nice_string(input: str) -> bool:
    return contains_repeat_with_one_letter_gap(
        string=input
    ) and contains_pair_of_letters_at_least_twice(string=input)


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

    input_path = "./src/aoc_2015/day_05/input.txt"
    result_path = "./src/aoc_2015/day_05/result.txt"

    strings = helpers.read_file_lines(file_path=input_path)
    total_nice_strings = sum([is_nice_string(input=string) for string in strings])
    total_new_nice_strings = sum(
        [is_definitely_nice_string(input=string) for string in strings]
    )
    result = f"""\
        Part 1: There are a total of {total_nice_strings} nice strings!
        Part 2: There are a total of {total_new_nice_strings} nice strings with the new rules!
        """

    helpers.write_file(file_path=result_path, contents=result)
