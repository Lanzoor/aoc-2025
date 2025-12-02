
def repeat_count(number: int) -> int:
    string = str(number)
    length = len(string)

    for size in range(1, length):
        if length % size != 0:
            continue
        pattern = string[:size]
        times = length // size
        if times < 2:
            continue
        if pattern * times == string:
            return times

    return 0


def count_invalid_ids_new(ranges: str) -> int:
    total = 0
    ranges_list = ranges.split(",")
    for current_range in ranges_list:
        start, end = map(int, current_range.split("-"))

        for number in range(start, end + 1):
            if repeat_count(number) >= 2:
                total += number

    return total

with open("./input_2.txt", "r") as file:
    input_2 = file.read()

print(count_invalid_ids_new(input_2))
