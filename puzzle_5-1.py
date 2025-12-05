def count_fresh_ingredients(ranges: list[str], ingredients: list[int]) -> int:
    pairs: list[tuple[int, int]] = []
    for cur_range in ranges:
        start, end = map(int, cur_range.split("-"))
        pairs.append((start, end))

    count = 0
    for ingredient in ingredients:
        if any(start <= ingredient <= end for start, end in pairs):
            count += 1

    return count

with open("./input_5.txt", "r") as file:
    input_5 = file.read()

ranges = input_5.split("\n\n")[0].split("\n")
ingredients = [int(ingredient) for ingredient in input_5.split("\n\n")[1].split("\n")[:-1]]
print(count_fresh_ingredients(ranges, ingredients))
