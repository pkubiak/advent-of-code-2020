import sys, math

forest = [
    line.strip()
    for line in sys.stdin
]

def count_trees(board, dx, dy):
    w, h = len(board[0]), len(board)
    return [
        board[dy * i][(dx * i) % w]
        for i in range(1, h // dy, 1)
    ].count('#')

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total = math.prod(count_trees(forest, *s) for s in SLOPES)

print(total)