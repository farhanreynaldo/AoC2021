SAMPLES = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

report = SAMPLES.strip().split("\n")


def flip(report):
    return list(zip(*report))


def power_consumption(report):
    gamma = ""
    epsilon = ""
    matrix = [[num for num in row] for row in report]
    n_row, n_col = len(matrix), len(matrix[0])
    for col in range(n_col):
        bit = sum(int(matrix[row][col]) for row in range(n_row))
        gamma += "1" if bit > n_row / 2 else "0"
        epsilon += "1" if bit < n_row / 2 else "0"
    return int(gamma, 2) * int(epsilon, 2)


assert power_consumption(report) == 198

input = open("input/day03.txt").read().strip().split("\n")
print(power_consumption(input))


def oxygen_generator(report, n=0):
    if len(report) == 1:
        return int(report[0], 2)
    flipped = flip(report)
    if sum(int(num) for num in flipped[n]) >= len(flipped[n]) / 2:
        next_report = [line for line in report if line[n] == "1"]
        return oxygen_generator(next_report, n + 1)
    else:
        next_report = [line for line in report if line[n] == "0"]
        return oxygen_generator(next_report, n + 1)


def co2_scrubber(report, n=0):
    if len(report) == 1:
        return int(report[0], 2)
    flipped = flip(report)
    if sum(int(num) for num in flipped[n]) >= len(flipped[n]) / 2:
        next_report = [line for line in report if line[n] == "0"]
        return co2_scrubber(next_report, n + 1)
    else:
        next_report = [line for line in report if line[n] == "1"]
        return co2_scrubber(next_report, n + 1)


def life_support(report):
    oxygen = oxygen_generator(report)
    co2 = co2_scrubber(report)
    return oxygen * co2


assert life_support(report) == 230
print(life_support(input))
