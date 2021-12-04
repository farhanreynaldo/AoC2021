COMMAND_SAMPLES = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def get_position(input):
    depth = 0
    horizontal = 0
    for command in input.strip().split("\n"):
        direction, value = command.split()
        if direction == "up":
            depth -= int(value)
        elif direction == "down":
            depth += int(value)
        else:
            horizontal += int(value)
    return depth * horizontal


assert get_position(COMMAND_SAMPLES) == 150

with open("input/day02.txt", "r") as fn:
    print(get_position(fn.read()))


def get_position_with_aim(input):
    depth = 0
    horizontal = 0
    aim = 0
    for command in input.strip().split("\n"):
        direction, value = command.split()
        if direction == "up":
            aim -= int(value)
        elif direction == "down":
            aim += int(value)
        else:
            depth += aim * int(value)
            horizontal += int(value)
    return depth * horizontal


assert get_position_with_aim(COMMAND_SAMPLES) == 900

with open("input/day02.txt", "r") as fn:
    print(get_position_with_aim(fn.read()))
