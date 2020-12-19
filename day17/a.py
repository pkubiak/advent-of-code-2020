import sys, itertools
from collections import Counter


NEIGHBORES = set(itertools.product([-1,0,1], repeat=3)) - {(0,0,0)} 

def simulate(active_cubes):
    counts = Counter()

    for x, y, z in active_cubes:
        counts.update(
            (x + dx, y + dy, z + dz)
            for dx, dy, dz in NEIGHBORES
        )

    return {
        cell 
        for cell in counts
        if counts[cell] == 3 or (counts[cell] == 2 and cell in active_cubes)
    }


active_cubes = set()
for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == '#':
            active_cubes.add((x,y,0))


for i in range(6):
    active_cubes = simulate(active_cubes)

print(len(active_cubes))
