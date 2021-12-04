SAMPLES = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def parse_boards(input):
    seq, *boards = input.strip().split("\n\n")
    seq = seq.split(",")
    boards = [
        [line.strip().split() for line in board.split("\n")]
        for board in boards
    ]
    return seq, boards


def flip(board):
    return list(zip(*board))


seq, boards = parse_boards(SAMPLES)


def first_win(seq, boards):
    for i in range(1, len(seq) + 1):
        cur = seq[:i]
        for board in boards:
            rows = [set(row) for row in board]
            cols = [set(col) for col in flip(board)]
            for line in rows + cols:
                if line.issubset(set(cur)):
                    last_num = int(cur[-1])
                    cur = set(int(num) for num in cur)
                    unmarked = (
                        set(int(num) for line in board for num in line) - cur
                    )
                    return last_num * sum(unmarked)


assert first_win(seq, boards) == 4512

input = open("input/day04.txt").read()
print(first_win(*parse_boards(input)))


def last_win(seq, boards):
    for i in range(1, len(seq) + 1):
        cur = seq[:i]
        win_board = False
        for board in boards:
            rows = [set(row) for row in board]
            cols = [set(col) for col in flip(board)]
            for line in rows + cols:
                if line.issubset(set(cur)):
                    if len(boards) == 1:
                        last_num = int(cur[-1])
                        cur = set(int(num) for num in cur)
                        unmarked = (
                            set(int(num) for line in board for num in line)
                            - cur
                        )
                        return last_num * sum(unmarked)
                    else:
                        win_board = True
            if win_board:
                boards.remove(board)
                win_board = False


assert last_win(seq, boards) == 1924
print(last_win(*parse_boards(input)))
