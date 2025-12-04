def safe_get(lines: list[str], r: int, c: int) -> str | None:
    if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
        return lines[r][c]
    return None

def count_accessable_rolls(grid: str) -> int:
    lines = grid.splitlines()
    rolls = 0

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            surrounding_rolls = 0

            conditions = [
                safe_get(lines, line_index - 1, char_index) == "@",      # T-M
                safe_get(lines, line_index - 1, char_index + 1) == "@",  # T-DR
                safe_get(lines, line_index - 1, char_index - 1) == "@",  # T-DL
                safe_get(lines, line_index, char_index + 1) == "@",      # R
                safe_get(lines, line_index, char_index - 1) == "@",      # L
                safe_get(lines, line_index + 1, char_index) == "@",      # B-M
                safe_get(lines, line_index + 1, char_index + 1) == "@",  # B-DR
                safe_get(lines, line_index + 1, char_index - 1) == "@",  # B-DL
            ]

            surrounding_rolls += conditions.count(True)

            if char == "@" and surrounding_rolls < 4:
                rolls += 1

    return rolls

with open("./input_4.txt", "r") as file:
    input_4 = file.read()

print(count_accessable_rolls(input_4))
