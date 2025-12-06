from functools import reduce

def solve_math_homework(question_input: str) -> int:
    lines = question_input.splitlines()

    numbers: list[list[int]] = [[int(i) for i in row.split()] for row in lines[:-1]]

    operators = [c for c in lines[-1] if c in '+*']

    total = 0
    for index, operator in enumerate(operators):
        column = [row[index] for row in numbers]
        if operator == "+":
            total += sum(column)
        elif operator == "*":
            total += reduce(lambda x, y: x * y, column)

    return total


with open("./input_6.txt") as file:
    print(solve_math_homework(file.read()))
