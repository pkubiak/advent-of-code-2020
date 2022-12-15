import re

text = open("input.txt").read()

points = []
beacons = []
for line in text.split("\n"):
    x, y, bx, by = map(int, re.findall(r"[-]?\d+", line))

    d = abs(x-bx) + abs(y-by)
    points += [(x,y,d)]
    beacons += [(bx,by)]

def get_ranges(Y):
    ranges = []
    for x, y, d in points:
        z = d - abs(Y - y)
        if z < 0: continue
        ranges.append((-z+x, -1))
        ranges.append((z+1+x, 1))
    return ranges


def p1(Y):
    vals = set()
    r = get_ranges(Y)
    for i in range(0,len(r),2):
        vals.update(range(r[i][0], r[i+1][0]))

    for x, y in beacons:
        if y == Y:
            vals.discard(x)

    print("a:", len(vals))


def p2(limit):
    for y in range(limit + 1):
        ranges = get_ranges(y)
        ile = 0
        for x, t in sorted(ranges):
            ile += t
            if ile == 0 and 0 <= x <= limit:
                print("b:", x * limit + y)


p1(2_000_000) or p2(4_000_000)
