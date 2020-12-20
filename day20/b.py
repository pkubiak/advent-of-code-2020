import sys, itertools, math
from collections import Counter, defaultdict
from copy import copy as copy2
tiles = sys.stdin.read().split("\n\n")


def get_borders(tile):
    borders = [
        tile[0],
        tile[-1],
        ''.join([tile[i][0] for i in range(len(tile))]),
        ''.join([tile[i][-1] for i in range(len(tile))])
    ]

    borders_rev = [b[::-1] for b in borders]
    return set(borders) | set(borders_rev)

def copy(board, tile, x, y):
    for xi in range(10):
        for yi in range(10):
            board[y+yi][x+xi] = tile[yi][xi]

def rot90(tile):
    return [
        ''.join(tile[9-j][i] for j in range(10))
        for i in range(10)
    ]


def flip(tile):
    return [
        line[::-1]
        for line in tile
    ]


def copy_match(board, tile, x, y):
    tile = copy2(tile)
    for i in range(8):
        tile = rot90(tile)
        if i == 4:
            tile = flip(tile)
        print("\n".join(tile) + "\n\n")

        for i in range(10):
            if y > 0 and board[y-1][x+i] and tile[0][i] != board[y-1][x+i]:
                break
            if x > 0 and board[y+i][x-1] and board[y+i][x-1] != tile[i][0]:
                break
            if board[y+i][x+10] and board[y+i][x+10] != tile[i][-1]:
                break
            if board[y+10][x+i] and board[y+10][x+i] != tile[-1][i]:
                break
        else:
            copy(board, tile, x, y)
            return True
    assert False
    # return False

BORDERS = {}
TILES = {}
for tile in tiles:
    title, *lines = tile.split("\n")
    title = title.replace("Tile ", "").strip(":")

    BORDERS[title] = get_borders(lines)
    TILES[title] = lines
    # lines#[list(line) for line in lines]

print(BORDERS)

NEIGHBORS = defaultdict(set)

for a, b in itertools.combinations(BORDERS.keys(), 2):
    if BORDERS[a] & BORDERS[b]:
        print(a, b)
        NEIGHBORS[a].add(b)
        NEIGHBORS[b].add(a)

CORNERS = [int(x) for x in NEIGHBORS if len(NEIGHBORS[x]) == 2]
assert len(CORNERS) == 4

print(CORNERS)
# print(math.prod(CORNERS))
# print(NEIGHBORS)

def build_frame(node="1453"):
    print(">>>>>>>>>>")
    print(NEIGHBORS[node])
    used = set()
    frame = []
    while True:
        if len(NEIGHBORS[node]) == 2:
            frame.append([])
        frame[-1].append(node)
        print(node)
        used.add(node)
        nodes = [x for x in NEIGHBORS[node] if len(NEIGHBORS[x]) in (2,3) and x not in used]
        if len(nodes) == 0:
            break
        node = nodes[0]
    board = [[None] * 12 for _ in range(12)]

    print([len(x) for x in frame])
    for i in range(11):
        board[0][i] = frame[0][i]
        board[i][-1] = frame[1][i]
        board[-1][11-i] = frame[2][i]
        board[11-i][0] = frame[3][i]
    
    for y in range(12):
        for x in range(12):
            if board[y][x] is None:
                z = (NEIGHBORS[board[y-1][x]] & NEIGHBORS[board[y][x-1]]) - used
                assert len(z) == 1
                z = z.pop()
                board[y][x] = z
                used.add(z)

    for x in board:
        print(x)
    # print(board)
    return board

ids = build_frame()
print(ids)

board = [[None]*(12*10+1) for i in range(12*10+1)]

for y in range(12):
    for x in range(12):
        if x == 0 and y == 0:
            copy(board, rot90(rot90(TILES[ids[0][0]])), 0, 0)
        else:
            copy_match(board, TILES[ids[y][x]], 10*x, 10*y)

# print(board)
extracted = [[None]*(12*8) for _ in range(12*8)]
for ty in range(12):
    for tx in range(12):
        for y in range(8):
            for x in range(8):
                extracted[8*ty+y][8*tx+x] = board[10*ty+y+1][10*tx+x+1]

print(extracted)

DRAGON = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

def match(board, pattern, x, y):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == '#' and board[y+i][x+j] == '.':
                return False
    return True

def mark(board, pattern, x, y):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == '#':
                board[y+i][x+j] = 'x'

for i in range(8):
    extraced = rot90(extracted)
    if i == 4:
        extracted = flip(extracted)

    for y in range(len(extracted)-len(DRAGON)+1):
        for x in range(len(extracted[0]) - len(DRAGON[0])+1):
            if match(extracted, DRAGON, x, y):
                mark(extracted, DRAGON, x, y)
                # total += 1
    

total = sum(line.count('#') for line in extracted)
print(total)

# # copy_match(board, TILES["1291"], 10, 0)
# # used = {"1453", "1291"}



# # print(NEIGHBORS["1453"])
# # print(NEIGHBORS["1291"])