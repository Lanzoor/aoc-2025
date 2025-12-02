with open("./input_1.txt", "r") as file:
    input_1 = file.read()

def rotate_dial_new(*instructions: str) -> int:
    dial_number = 50
    zeroes = 0

    for instruction in instructions:
        rotation = instruction[0]
        amount = int(instruction[1:])
        step = 1 if rotation == "R" else -1

        for _ in range(amount):
            dial_number = (dial_number + step) % 100
            if dial_number == 0:
                zeroes += 1

    return zeroes

print(rotate_dial_new(*input_1.splitlines()))
