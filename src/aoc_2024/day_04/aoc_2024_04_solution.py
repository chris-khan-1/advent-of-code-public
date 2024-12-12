def count_word_occurrences(target_word: str, grid: list[list[str]]):
    word_length = len(target_word)
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    total_occurrences = 0

    target_words = {target_word, target_word[::-1]}

    for row in range(grid_rows):
        for col in range(grid_cols):

            if col + word_length <= grid_cols:
                horizontal_word = "".join(grid[row][col : col + word_length])
                if horizontal_word in target_words:
                    total_occurrences += 1

            if row + word_length <= grid_rows:
                vertical_word = "".join(grid[row + i][col] for i in range(word_length))
                if vertical_word in target_words:
                    total_occurrences += 1

            if row + word_length <= grid_rows and col + word_length <= grid_cols:
                diagonal_word = "".join(
                    grid[row + i][col + i] for i in range(word_length)
                )
                if diagonal_word in target_words:
                    total_occurrences += 1

            if row + word_length <= grid_rows and col + word_length <= grid_cols:
                anti_diagonal_word = "".join(
                    grid[row + i][col + word_length - 1 - i] for i in range(word_length)
                )
                if anti_diagonal_word in target_words:
                    total_occurrences += 1

    return total_occurrences


def check_x_diagonal(grid: list[list[str]], row: int, col: int) -> bool:

    # clockwise rotation
    corners = [
        grid[row - 1][col - 1],  # up-left
        grid[row - 1][col + 1],  # up-right
        grid[row + 1][col + 1],  # down-right
        grid[row + 1][col - 1],  # down-left
    ]

    return "".join(corners) in ["SSMM", "SMMS", "MMSS", "MSSM"]


def count_mas_diagonals(grid: list[list[str]]):
    grid_rows = len(grid)
    grid_cols = len(grid[0])

    total = 0

    # skip edges as 'A' cannot be there
    for row in range(1, grid_rows - 1):
        for col in range(1, grid_cols - 1):
            if grid[row][col] != "A":
                continue
            if check_x_diagonal(grid=grid, row=row, col=col):
                total += 1

    return total


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers  # noqa: E402

    input_path = "./src/aoc_2024/day_04/input.txt"
    result_path = "./src/aoc_2024/day_04/result.txt"

    input = helpers.read_file_lines(file_path=input_path)

    total_xmas = count_word_occurrences(target_word="XMAS", grid=input)
    total_x_mas = count_mas_diagonals(grid=input)

    result = f"""\
        Part 1: The total 'XMAS' words is {total_xmas}.
        Part 2: The total 'X-MAS' words is {total_x_mas}.
        """

    helpers.write_file(file_path=result_path, contents=result)
