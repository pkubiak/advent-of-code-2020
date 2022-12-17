from itertools import cycle
blocks = [
    [(0,0), (1,0),(2,0),(3,0)],
    [(0,-1), (1,-2),(1,-1),(1,0),(2,-1)],
    [(0,0), (1,0), (2,0), (2,-1), (2,-2)],
    [(0,0), (0,-1), (0,-2), (0,-3)],
    [(0,0), (1,0), (0,-1), (1,-1)],
]

def move(item, dx, dy):
    return [(x+dx, y+dy) for x,y in item]

def can_move(board, item, dx, dy):
    for x, y in item:
        x2, y2 = x+dx, y+dy
        if not (0 <= x2 < 7):
            return False
        if (x2, y2) in board:
            return False
        if 0 <= y2:
            return False
    return True

def print_board(board):
    miny = min(y for x,y in board)
    for y in range(miny, 0):
        print(str(y).rjust(5), ''.join(['#' if (i, y) in board else ' ' for i in range(7)]))
    print("-"*15)
    print()

moves = cycle(open("input.txt").read().strip())
blocks = cycle(blocks)

board = set()

for i in range(2022):
    block = next(blocks)
    dy = min(y for x, y in board) if board else 0
    dx = 2
    block = move(block, dx, dy-4)

    while True:
        dx = {">":1, "<":-1}[next(moves)]
        if can_move(board, block, dx, 0):
            block = move(block, dx, 0)
        if can_move(board, block, 0, 1):
            block = move(block, 0, 1)
        else:
            board.update(block)
            break
    # print(board)
    # print_board(board)

print(min(y for x, y in board))