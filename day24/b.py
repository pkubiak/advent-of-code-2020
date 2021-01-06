import sys

def split_dirs(desc):
    i = 0
    while i < len(desc):
        if desc[i] in ('w', 'e'):
            yield desc[i]
            i+=1
        else:
            yield desc[i:i+2]
            i += 2

def move(pos, dir):
    x, y = pos
    offset = 1-(y%2)
    if 'e' in dir:
        x += 1
    elif 'w' == dir:
        x -= 1
    if 'n' in dir:
        y -= 1
    elif 's' in dir:
        y += 1
    if dir not in ('e' ,'w'):
        x -= offset
    return x, y

def get_coords(desc: int) -> tuple:
    pos = 0, 0
    for d in split_dirs(desc):
        pos = move(pos, d)
    return pos

from collections import Counter
c = Counter()
for line in sys.stdin.read().split("\n"):
    c[get_coords(line)] += 1

tiles = {k for k, v in c.items() if v%2 == 1}

for day in range(100):
    neighbores = Counter()
    for t in tiles:
        for dir in ('w', 'e', 'se', 'ne', 'sw', 'nw'):
            neighbores[move(t, dir)] += 1
    
    new_tiles = {t for t in tiles if neighbores[t] in (1,2)}
    for t in neighbores:
        if neighbores[t] == 2 and t not in tiles:
            new_tiles.add(t)
    tiles = new_tiles
    print(day+1, len(tiles))
    
# print(x)