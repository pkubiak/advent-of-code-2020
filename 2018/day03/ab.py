from itertools import product
from collections import Counter

with open("input.txt") as file:
    claims = []
    for line in file:
        id, line = line.strip().split(" @ ")
        coords = map(int, line.replace(": ", ",").replace("x", ",").split(","))
        claims.append([id, tuple(coords)])

overlaps = Counter()
for _, (x0, y0, w, h) in claims:
    overlaps.update(product(range(x0, x0 + w), range(y0, y0 + h)))

print("a:", sum(v >= 2 for v in overlaps.values()))

for id, (x0, y0, w, h) in claims:
    if max(overlaps[pos] for pos in product(range(x0, x0 + w), range(y0, y0 + h))) == 1:
        print("b:", id)
