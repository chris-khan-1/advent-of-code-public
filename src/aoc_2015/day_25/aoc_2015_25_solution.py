if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_25/input.txt"
    result_path = "./src/aoc_2015/day_25/result.txt"

    string_input = helpers.read_file(file_path=input_path)

    result = f"""\
        Part 1: {1}
        Part 2: {2}
        """

    helpers.write_file(file_path=result_path, contents=result)
