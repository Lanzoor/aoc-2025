def count_fresh_ingredients(ranges: list[str], ingredients: list[int]) -> int:
    pairs: list[tuple[int, int]] = []
    for cur_range in ranges:
        start, end = map(int, cur_range.split("-"))
        pairs.append((start, end))

    pairs.sort()
    count = 0
    merged = [pairs[0]]

    for current in pairs[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    count = sum(end - start + 1 for start, end in merged)
    return count

with open("./input_5.txt", "r") as file:
    input_5 = file.read()

ranges = input_5.split("\n\n")[0].split("\n")
ingredients = [int(ingredient) for ingredient in input_5.split("\n\n")[1].split("\n")[:-1]]
print(count_fresh_ingredients(ranges, ingredients))
