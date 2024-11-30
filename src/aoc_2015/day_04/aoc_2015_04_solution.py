import hashlib


def get_md5_hash(secret_key: str, value: int) -> str:
    message = secret_key + str(value)
    return hashlib.md5(message.encode("utf-8")).hexdigest()


def check_starts_with_number_of_zeroes(input: str, digit_length: int) -> bool:
    if input[:digit_length] == "0" * digit_length:
        return True
    return False


def get_lowest_value_required(secret_key: str, digit_length: int) -> int:
    number = 1
    while (
        check_starts_with_number_of_zeroes(
            input=get_md5_hash(secret_key=secret_key, value=number),
            digit_length=digit_length,
        )
        is False
    ):
        number += 1
    return number


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_04/input.txt"
    result_path = "./src/aoc_2015/day_04/result.txt"

    secret_key = helpers.read_file(file_path=input_path)
    lowest_value_5_zeroes = get_lowest_value_required(
        secret_key=secret_key, digit_length=5
    )
    lowest_value_6_zeroes = get_lowest_value_required(
        secret_key=secret_key, digit_length=6
    )

    result = f"""\
        Part 1: Lowest value for 5 zeroes is {lowest_value_5_zeroes}
        Part 2: Lowest value for 6 zeroes is {lowest_value_6_zeroes}
        """

    helpers.write_file(file_path=result_path, contents=result)
