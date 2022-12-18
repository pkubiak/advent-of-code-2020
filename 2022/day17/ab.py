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

moves = open("input.txt").read().strip()
print(len(moves))
# moves = cycle(text)
# blocks = cycle(blocks)

move_i = block_i = 0

board = set()
used= {}
height = {}
target = 1000000000000
cycle_length = None
cycle_height = 0
i = 0
while True:
    height[i] = min([y for x,y in board] + [0])
    if cycle_length and (target - i) % cycle_length == 0:
        print(">>", cycle_length, cycle_height)
        print(">>", height[i] + cycle_height * (target -i)//cycle_length)
        break
    
    depths = [min([y for x,y in board if x==i]+[0]) for i in range(7)]
    min_depth = min(depths)
    depths = [i - min_depth for i in depths]
    # print(depths)
    key = (block_i, move_i, tuple(depths))
    if key in used:
        diff = i - used[key]
        cycle_length = i - used[key]
        cycle_height = height[i] - height[used[key]]
        # break
    used[key] = i

    block = blocks[block_i]
    block_i = (block_i+1) % len(blocks)

    dy = min(y for x, y in board) if board else 0
    dx = 2
    block = move(block, dx, dy-4)

    while True:
        dx = {">":1, "<":-1}[moves[move_i]]
        move_i = (move_i+1)% len(moves)
        if can_move(board, block, dx, 0):
            block = move(block, dx, 0)
        if can_move(board, block, 0, 1):
            block = move(block, 0, 1)
        else:
            board.update(block)
            break
    i += 1
    # print(board)
    # print_board(board)

print(min(y for x, y in board))