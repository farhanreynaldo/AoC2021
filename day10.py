SAMPLES = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def find_corrupted(line):
    PAIRS = {"(": ")", "{": "}", "<": ">", "[": "]"}
    chars = []
    for char in line:
        if char in PAIRS:
            chars.append(char)
        elif PAIRS[chars.pop()] != char:
            return char
    return ""


def total_illegal(input):
    SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
    lines = input.strip().split("\n")
    corrupted = [find_corrupted(line) for line in lines]
    return sum(SCORES[char] for char in corrupted if char)


assert total_illegal(SAMPLES) == 26397
input = open("input/day10.txt").read()
print(total_illegal(input))


def incomplete_points(line):
    PAIRS = {"(": ")", "{": "}", "<": ">", "[": "]"}
    chars = []
    for char in line:
        if char in PAIRS:
            chars.append(char)
        elif PAIRS[chars.pop()] != char:
            return 0

    total = 0
    SCORES = {")": 1, "]": 2, "}": 3, ">": 4}
    for char in chars[::-1]:
        total = total * 5 + SCORES[PAIRS[char]]
    return total


def find_incomplete(input):
    lines = input.strip().split("\n")
    scores = sorted([incomplete_points(line) for line in lines])
    scores = [score for score in scores if score != 0]
    return scores[len(scores) // 2]


assert find_incomplete(SAMPLES) == 288957
print(find_incomplete(input))
