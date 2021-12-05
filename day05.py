from collections import Counter
from typing import List, Tuple

SAMPLES = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def point_in_lines(a, b):
    """Only consider horizontal or vertical line."""
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        low, high = sorted((y1, y2))
        return [(x1, y) for y in range(low, high + 1)]
    elif y1 == y2:
        low, high = sorted((x1, x2))
        return [(x, y1) for x in range(low, high + 1)]
    else:
        return []


def parse(input: str) -> List[List[Tuple[int]]]:
    coords = []
    for coord in input.strip().split("\n"):
        a, b = coord.split(" -> ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        coords.append([(int(x1), int(y1)), (int(x2), int(y2))])
    return coords


def total_intersection(input):
    coords = parse(input)
    points = []
    for coord in coords:
        points += point_in_lines(*coord)
    return sum(1 for _, v in Counter(points).items() if v > 1)


assert total_intersection(SAMPLES) == 5
input = open("input/day05.txt").read()
print(total_intersection(input))


def point_in_lines_vertical(a, b):
    """consider horizontal, vertical, and diagonal line."""
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        low, high = sorted((y1, y2))
        return [(x1, y) for y in range(low, high + 1)]
    elif y1 == y2:
        low, high = sorted((x1, x2))
        return [(x, y1) for x in range(low, high + 1)]
    else:
        x_dir = 1 if x1 < x2 else -1
        y_dir = 1 if y1 < y2 else -1
        xs = [x for x in range(x1, x2 + x_dir, x_dir)]
        ys = [y for y in range(y1, y2 + y_dir, y_dir)]
        return list(zip(xs, ys))


def total_intersection_vertical(input):
    coords = parse(input)
    points = []
    for coord in coords:
        points += point_in_lines_vertical(*coord)
    return sum(1 for _, v in Counter(points).items() if v > 1)


assert total_intersection_vertical(SAMPLES) == 12
print(total_intersection_vertical(input))
