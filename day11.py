from itertools import product


SAMPLES = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def gridify(input):
    return {
        (x, y): int(col)
        for x, row in enumerate(input.strip().split("\n"))
        for y, col in enumerate(row)
    }


def pretty_output(grids):
    rows, cols = max(grids)
    return "\n".join(
        "".join(str(grids[(row, col)]) for col in range(cols + 1))
        for row in range(rows + 1)
    )


def neighbors(p):
    x, y = p
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        if (dx, dy) != (0, 0):
            yield x + dx, y + dy


def count_flashes(input, steps=100):
    grids = gridify(input)
    count = 0
    for _ in range(steps):
        for p in grids:
            grids[p] += 1
        flashing = set(p for p in grids if grids[p] > 9)
        while flashing:
            p = flashing.pop()
            grids[p] = 0
            count += 1
            nps = [np for np in neighbors(p) if np in grids and grids[np] != 0]
            for np in nps:
                grids[np] += 1
                if grids[np] > 9:
                    flashing.add(np)
    return count


assert count_flashes(SAMPLES, 100) == 1656
input = open("input/day11.txt").read()
print(count_flashes(input, steps=100))


def find_synchronize(input):
    grids = gridify(input)
    synchronize = False
    steps = 0
    while not synchronize:
        for p in grids:
            grids[p] += 1
        flashing = set(p for p in grids if grids[p] > 9)
        while flashing:
            p = flashing.pop()
            grids[p] = 0
            nps = [np for np in neighbors(p) if np in grids and grids[np] != 0]
            for np in nps:
                grids[np] += 1
                if grids[np] > 9:
                    flashing.add(np)
        if all(grids[p] == 0 for p in grids):
            return steps + 1
        steps += 1


assert find_synchronize(SAMPLES) == 195
print(find_synchronize(input))
