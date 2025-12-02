with open("./input_1.txt", "r") as file:
    input_1 = file.read()

def rotate_dial(*instructions: str) -> int:
    dial_number = 50
    zeroes = 0

    for instruction in instructions:
        rotation = instruction[0]
        amount = int(instruction[1:])
        dial_number = (dial_number - amount if rotation == "L" else dial_number + amount) % 100

        if dial_number == 0:
            zeroes += 1

    return zeroes

print(rotate_dial(*input_1.splitlines()))
