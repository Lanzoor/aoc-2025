def sum_joltages(*banks: int) -> int:
    joltages_sum = 0

    for bank in banks:
        bank_str = str(bank)

        for maximum in range(9, -1, -1):
            index = bank_str.find(str(maximum))
            if index == -1:
                continue

            rest = bank_str[index + 1:]
            if rest:
                maximum_rest = max(rest)
                joltage = maximum * 10 + int(maximum_rest)
                joltages_sum += joltage
                break

    return joltages_sum



with open("./input_3.txt", "r") as file:
    input_3 = [int(n) for n in file.read().splitlines()]

print(sum_joltages(*input_3))
