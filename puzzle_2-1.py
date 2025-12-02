def count_invalid_ids(ranges: str) -> int:
    total = 0
    ranges_list = ranges.split(",")
    for current_range in ranges_list:
        start, end = map(int, current_range.split("-"))

        for number in range(start, end + 1):
            length = len(str(number))
            if length % 2 == 0:
                mid = length // 2
                if str(number)[:mid] == str(number)[mid:]:
                    total += number

    return total

with open("./input_2.txt", "r") as file:
    input_2 = file.read()

print(count_invalid_ids(input_2))
