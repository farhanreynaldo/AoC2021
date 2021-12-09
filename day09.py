from collections import deque
from math import prod

SAMPLES = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def neighbors(point):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, right, left, down
    x, y = point
    for xi, yi in dirs:
        yield x + xi, y + yi


def lowest_point(input):
    grids = {
        (x, y): int(col)
        for x, row in enumerate(input.strip().split("\n"))
        for y, col in enumerate(row)
    }
    points = [
        p
        for p in grids
        if all(grids[p] < grids[np] for np in neighbors(p) if np in grids)
    ]
    return grids, points


def total_risks(input):
    grids, points = lowest_point(input)
    return sum(grids[p] + 1 for p in points)


assert total_risks(SAMPLES) == 15
input = open("input/day09.txt").read()
print(total_risks(input))


def largest_basins(input):
    grids, points = lowest_point(input)
    basins = []
    for p in points:
        visited = deque()
        queue = deque([p])
        while queue:
            cur = queue.popleft()
            for np in neighbors(cur):
                if np not in grids or np in visited or grids[np] == 9:
                    continue
                visited.append(np)
                queue.append(np)
        basins.append(len(visited))

    return prod(sorted(basins)[-3:])


assert largest_basins(SAMPLES) == 1134
input = open("input/day09.txt").read()
print(largest_basins(input))
