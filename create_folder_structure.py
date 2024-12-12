import os
from textwrap import dedent

for year in [2024]:
    for day in range(1, 26):
        day_directory = f"./src/aoc_{year}/day_{day:02d}"
        test_day_directory = f"./tests/aoc_{year}/day_{day:02d}"

        input_path = f"{day_directory}/input.txt"
        instruction_path = f"{day_directory}/instructions.txt"
        solution_path = f"{day_directory}/aoc_{year}_{day:02d}_solution.py"
        result_path = f"{day_directory}/result.txt"

        test_path = f"{test_day_directory}/test_aoc_{year}_{day:02d}_solution.py"

        if os.path.exists(path=day_directory):
            pass
        else:
            print(f"Created {day_directory}")
            os.makedirs(name=day_directory)

            with open(input_path, "w") as output_file:
                output_file.write("")

            with open(instruction_path, "w") as output_file:
                output_file.write("")

            with open(solution_path, "w") as output_file:
                output_file.write(
                    dedent(
                        f'''\
            if __name__ == "__main__":
                import sys
                from pathlib import Path

                sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

                import helpers  # noqa: E402

                input_path = "./src/aoc_{year}/day_{day:02d}/input.txt"
                result_path = "./src/aoc_{year}/day_{day:02d}/result.txt"

                string_input = helpers.read_file(file_path=input_path)

                result = f"""\\
                    Part 1: {{1}}
                    Part 2: {{2}}
                    """

                helpers.write_file(file_path=result_path, contents=result)
            '''
                    )
                )

        if os.path.exists(path=test_day_directory):
            pass
        else:
            print(f"Created {test_day_directory}")
            os.makedirs(name=test_day_directory)

            with open(test_path, "w") as output_file:
                output_file.write(
                    dedent(
                        f"""\
            # import pytest
            # from src.aoc_{year}.day_{day:02d}.aoc_{year}_{day:02d}_solution import *
            """
                    )
                )
