def sum_joltages_new(*banks: int) -> int:
    joltages_sum = 0

    for bank in banks:
        result: list[str] = []
        start_point = 0

        for remaining in range(12, 0, -1):
            end_point = len(str(bank)) - remaining

            segment = str(bank)[start_point:end_point+1]
            max_digit = int(max(segment))

            index = segment.index(str(max_digit))

            result.append(str(max_digit))
            start_point += index + 1

        joltage = int("".join(result))
        joltages_sum += joltage

    return joltages_sum


with open("./input_3.txt", "r") as file:
    input_3 = [int(n) for n in file.read().splitlines()]

print(sum_joltages_new(*input_3))
