text = open("input.txt").read()
elves = set()

for y, line in enumerate(text.split("\n")):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x,y))

DIRS = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
ORDER = [1, 5, 7, 3]

from collections import Counter
def simulate(elves, n):
    props = {}
    for (x,y) in elves:
        count = 0
        for dx,dy in DIRS:
            x2, y2 = x+dx, y+dy
            if (x2,y2) in elves:
                count += 1
        if count == 0:
            continue

        for i in range(4):
            center = ORDER[(n+i)%4]
            count = 0
            for d in [-1, 1, 0]:
                dx, dy = DIRS[(center+d)%8]
                x2, y2 = x+dx, y+dy
                if (x2,y2) in elves:
                    count += 1
            if count == 0:
                props[x,y] = (x2,y2)
                break
    c = Counter(props.values())
    ile = 0
    for k, v in list(props.items()):
        if c[v] == 1:
            elves.discard(k)
            elves.add(v)
            ile += 1
    return ile


for i in range(1000000):
    if i == 10:
        minx, *_, maxx = sorted(x for x,y in elves)
        miny, *_, maxy = sorted(y for x,y in elves)
        total = (maxx-minx+1)*(maxy-miny+1) - len(elves)
        print("a:", total)

    if simulate(elves, i) == 0:
        print("b:", i+1)
        break

