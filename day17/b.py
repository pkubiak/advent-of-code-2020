import sys, itertools
from collections import Counter


def simulate(active_cubes, NEIGHBORS):
    counts = Counter()

    for coord in active_cubes:
        counts.update(
            tuple(map(sum, zip(coord, diff)))
            for diff in NEIGHBORS
        )

    return {
        cell 
        for cell in counts
        if counts[cell] == 3 or (counts[cell] == 2 and cell in active_cubes)
    }


N = 4

active_cubes = set()
for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == '#':
            active_cubes.add((x, y) + (0,) * (N-2))


NEIGHBORS = set(itertools.product([-1,0,1], repeat=N)) - {(0,)*N}
for i in range(6):
    active_cubes = simulate(active_cubes, NEIGHBORS)

print(len(active_cubes))
