import os
import shutil
from pathlib import Path
from textwrap import dedent


def ignore_files(dir, files):
    return [
        file for file in files if file.startswith(("input", "result", "instruction"))
    ]


directories = ["src", "tests"]

base_path = Path.cwd().parent  # Set base path to the parent directory using pathlib

for directory in directories:
    source_dir = os.path.join(base_path, "advent-of-code", directory)
    destination_dir = os.path.join(base_path, "advent-of-code-public", directory)

    shutil.copytree(
        source_dir, destination_dir, ignore=ignore_files, dirs_exist_ok=True
    )

    print(
        dedent(
            f"""\
        Successfully copied contents from
        '{source_dir}' -->
        '{destination_dir}'
        """
        )
    )
