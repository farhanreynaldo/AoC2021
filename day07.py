from statistics import mean, median

SAMPLES = """16,1,2,0,4,2,7,1,2,14"""


def minimum_fuel(input):
    positions = [int(num) for num in input.split(",")]
    fuels = [
        sum(abs(pos - crab) for crab in positions)
        for pos in range(max(positions))
    ]
    return min(fuels)


# Alternative approach using median
def median_fuel(input):
    positions = [int(num) for num in input.split(",")]
    mid = median(positions)
    return sum(abs(mid - crab) for crab in positions)


assert minimum_fuel(SAMPLES) == 37
assert median_fuel(SAMPLES) == 37

input = open("input/day07.txt").read()
print(median_fuel(input))


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


# Alternative approach using numbers around mean
def mean_fuel(input):
    positions = [int(num) for num in input.split(",")]
    mid = round(mean(positions))
    fuels = [
        sum(fuel_consumption(pos, crab) for crab in positions)
        for pos in range(mid - 1, mid + 2)
    ]
    return min(fuels)


assert minimum_fuel_costly(SAMPLES) == 168
assert mean_fuel(SAMPLES) == 168
print(mean_fuel(input))
