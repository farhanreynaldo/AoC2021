SAMPLES = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def start_fold(paper, axis, value):
    folded = set()
    idx = 0 if axis == "x" else 1
    for dot in paper:
        x = 2 * value - dot[0] if axis == "x" and dot[idx] > value else dot[0]
        y = 2 * value - dot[1] if axis == "y" and dot[idx] > value else dot[1]
        folded.add((x, y))
    return folded


def parse_paper(paper_raw: str):
    paper = set()
    for dot in paper_raw.split("\n"):
        x, y = (int(pos) for pos in dot.split(","))
        paper.add((x, y))
    return paper


def fold_paper(input, n_fold=None):
    paper_raw, folds_raw = input.strip().split("\n\n")
    paper = parse_paper(paper_raw)
    folds = folds_raw.split("\n")
    n_fold = n_fold or len(folds)
    paper = get_paper(paper, folds[:n_fold])
    return len(paper)


def get_paper(paper, folds):
    for fold in folds:
        fold = fold.split()[-1]
        axis, value = fold.split("=")
        new_paper = start_fold(paper, axis, int(value))
        paper = new_paper
    return paper


assert fold_paper(SAMPLES, 1) == 17
assert fold_paper(SAMPLES, 2) == 16
input = open("input/day13.txt").read()
print(fold_paper(input, n_fold=1))


def display_paper(input, n_fold=None):
    paper_raw, folds_raw = input.strip().split("\n\n")
    paper = parse_paper(paper_raw)
    folds = folds_raw.split("\n")
    n_fold = n_fold or len(folds)
    paper = get_paper(paper, folds[:n_fold])

    xmax = max(dot[0] for dot in paper)
    ymax = max(dot[1] for dot in paper)
    return "".join(
        "".join("#" if (x, y) in paper else "." for x in range(xmax + 1))
        + "\n"
        for y in range(ymax + 1)
    )


print(display_paper(input))
