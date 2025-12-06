from functools import reduce

def solve_math_homework(question_input: str) -> int:
    lines = question_input.splitlines()
    numbers_rows = lines[:-1]
    operator_row = lines[-1]

    width = len(numbers_rows[0]) if numbers_rows else 0

    total = 0
    col = width - 1

    while col >= 0:
        if all(row[col].isspace() for row in numbers_rows + [operator_row]):
            col -= 1
            continue

        current_numbers = []
        operator = None

        while col >= 0 and not all(row[col].isspace() for row in numbers_rows + [operator_row]):
            digits = []
            for row in numbers_rows:
                if row[col].isdigit():
                    digits.append(row[col])
            if digits:
                number = int(''.join(digits))
                current_numbers.append(number)

            if operator_row[col] in '+*':
                operator = operator_row[col]

            col -= 1

        if current_numbers and operator:
            if operator == '+':
                result = sum(current_numbers)
            elif operator == '*':
                result = reduce(lambda a, b: a * b, current_numbers)
            total += result

    return total


with open("./input_6.txt", "r") as f:
    input_6 = f.read()

print(solve_math_homework(input_6))
