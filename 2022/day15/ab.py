import re

text = open("input.txt").read()

points = []
beacons = []
for line in text.split("\n"):
    x, y, bx, by = map(int, re.findall(r"[-]?\d+", line))

    d = abs(x-bx) + abs(y-by)
    points.append((x,y,d))
    beacons.append((bx,by))

vals = set()
LIMIT = 4_000_000
for Y in range(LIMIT+1):
    ranges = []
    for x,y,d in points:
        v = abs(Y-y)
        if v > d: continue
        z = d-v
        ranges.append((-z+x, -1))
        ranges.append((z+1+x, 1))
        # vals.update(i+x for i in range(-z, z+1))
    ranges.sort()
    ile = 0
    for x, t in ranges:
        ile += t
        if ile == 0 and x <= LIMIT:
            print(x, Y)
            print(x *LIMIT+ Y)
    # for x,y in beacons:
    #     if y == Y:
    #         vals.discard(x)
    
print(len(vals))

