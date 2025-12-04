from typing import Tuple

def safe_get(lines: list[str], r: int, c: int) -> str | None:
    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
        return lines[r][c]
    return None

def replace_accessable_rolls(grid: str) -> Tuple[int, str]:
    lines = grid.splitlines()
    new_lines = lines.copy()
    rolls = 0

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char != "@":
                continue

            conditions = [
                safe_get(lines, line_index - 1, char_index) == "@",
                safe_get(lines, line_index - 1, char_index + 1) == "@",
                safe_get(lines, line_index - 1, char_index - 1) == "@",
                safe_get(lines, line_index, char_index + 1) == "@",
                safe_get(lines, line_index, char_index - 1) == "@",
                safe_get(lines, line_index + 1, char_index) == "@",
                safe_get(lines, line_index + 1, char_index + 1) == "@",
                safe_get(lines, line_index + 1, char_index - 1) == "@",
            ]

            surrounding = conditions.count(True)

            if surrounding < 4:
                row = new_lines[line_index]
                new_lines[line_index] = (
                    row[:char_index] + "." + row[char_index+1:]
                )
                rolls += 1

    return rolls, "\n".join(new_lines)

def get_replaced_rolls(grid: str):
    total_replaced = 0
    while True:
        replaced, grid = replace_accessable_rolls(grid)
        total_replaced += replaced

        if replaced == 0:
            return total_replaced

with open("./input_4.txt", "r") as file:
    input_4 = file.read()

print(get_replaced_rolls(input_4))
