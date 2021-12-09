from itertools import product
from collections import deque
from math import prod

SAMPLES = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def find_adjacents(point):
    adjacents = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, right, left, down
    x, y = point
    for xi, yi in adjacents:
        yield x + xi, y + yi


def is_lowest(input):
    matrix = [[int(col) for col in row] for row in input.strip().split("\n")]
    n_row, n_col = len(matrix), len(matrix[0])
    total = 0
    for x, y in product(range(n_row), range(n_col)):
        if all(
            matrix[x][y] < matrix[xi][yi]
            for xi, yi in find_adjacents((x, y))
            if xi >= 0 and xi < n_row and yi >= 0 and yi < n_col
        ):
            total += matrix[x][y] + 1
    return total


assert is_lowest(SAMPLES) == 15
input = open("input/day09.txt").read()
print(is_lowest(input))


def lowest_point(input):
    matrix = [[int(col) for col in row] for row in input.strip().split("\n")]
    n_row, n_col = len(matrix), len(matrix[0])
    for x, y in product(range(n_row), range(n_col)):
        if all(
            matrix[x][y] < matrix[xi][yi]
            for xi, yi in find_adjacents((x, y))
            if xi >= 0 and xi < n_row and yi >= 0 and yi < n_col
        ):
            yield x, y


def largest_basins(input):
    grids = {
        (x, y): int(col)
        for x, row in enumerate(input.strip().split("\n"))
        for y, col in enumerate(row)
    }

    basins = []
    matrix = [[int(col) for col in row] for row in input.strip().split("\n")]
    n_row, n_col = len(matrix), len(matrix[0])
    for point in lowest_point(input):
        visited = deque()
        queue = deque([point])
        while queue:
            cur = queue.popleft()
            for np in find_adjacents(cur):
                if (
                    np in visited
                    or np[0] < 0
                    or np[0] >= n_row
                    or np[1] < 0
                    or np[1] >= n_col
                    or grids[np] == 9
                ):
                    continue
                visited.append(np)
                queue.append(np)
        basins.append(len(visited))

    return prod(sorted(basins)[-3:])


assert largest_basins(SAMPLES) == 1134
input = open("input/day09.txt").read()
print(largest_basins(input))
