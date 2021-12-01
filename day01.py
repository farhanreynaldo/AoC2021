SAMPLE = """
199
200
208
210
200
207
240
269
260
263
"""

depths = [int(num) for num in SAMPLE.strip().split("\n")]


def total_increase(depths):
    return sum(nxt > cur for cur, nxt in zip(depths, depths[1:]))


assert total_increase(depths) == 7

with open("input/day01.txt", "r") as fn:
    day01 = [int(line) for line in fn]

print(total_increase(day01))


def sum_threeway(depths):
    return [
        sum((first, second, third))
        for first, second, third in zip(depths, depths[1:], depths[2:])
    ]


assert total_increase(sum_threeway(depths)) == 5

print(total_increase(sum_threeway(day01)))
