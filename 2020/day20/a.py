import sys, itertools, math
from collections import Counter

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


BORDERS = {}
for tile in tiles:
    title, *lines = tile.split("\n")
    title = title.replace("Tile ", "").strip(":")

    BORDERS[title] = get_borders(lines)
    
    # lines#[list(line) for line in lines]

print(BORDERS)

NEIGHBORS = Counter()

for a, b in itertools.combinations(BORDERS.keys(), 2):
    if BORDERS[a] & BORDERS[b]:
        print(a, b)
        NEIGHBORS[a] += 1
        NEIGHBORS[b] += 1

CORNERS = [int(x) for x in NEIGHBORS if NEIGHBORS[x] == 2]
assert len(CORNERS) == 4

print(math.prod(CORNERS))
# print(NEIGHBORS)