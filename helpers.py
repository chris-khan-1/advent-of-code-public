from textwrap import dedent


def read_file(file_path: str) -> str:
    with open(file_path, "r") as input_file:
        return input_file.read()


def read_file_lines(file_path: str) -> list:
    with open(file_path, "r") as input_file:
        return [line.rstrip() for line in input_file]


def write_file(file_path: str, contents: str) -> None:
    with open(file_path, "w") as output_file:
        output_file.write(dedent(contents))


def append_to_file(file_path: str, contents: str) -> None:
    with open(file_path, "a") as output_file:
        output_file.write("\n" + dedent(contents))
