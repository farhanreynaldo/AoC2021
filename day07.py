SAMPLES = """16,1,2,0,4,2,7,1,2,14"""


def minimum_fuel(input):
    positions = [int(num) for num in input.split(",")]
    fuels = [
        sum(abs(pos - crab) for crab in positions)
        for pos in range(max(positions))
    ]
    return min(fuels)


assert minimum_fuel(SAMPLES) == 37

input = open("input/day07.txt").read()
print(minimum_fuel(input))


def fuel_consumption(pos, crab):
    n = abs(pos - crab)
    return n * (n + 1) / 2


def minimum_fuel_costly(input):
    positions = [int(num) for num in input.split(",")]
    fuels = [
        sum(fuel_consumption(pos, crab) for crab in positions)
        for pos in range(max(positions))
    ]
    return min(fuels)


assert minimum_fuel_costly(SAMPLES) == 168
print(minimum_fuel_costly(input))
