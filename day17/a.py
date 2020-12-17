import sys, itertools
from collections import Counter


def simulate(state):
    counts = Counter()
    diffs = set(itertools.product([-1,0,1], repeat=3)) - {(0,0,0)}

    for x,y,z in state:
        counts.update(
            (x+dx, y+dy, z+dz)
            for dx, dy, dz in diffs
        )

    return {
        cell 
        for cell in counts
        if counts[cell] == 3 or (counts[cell] == 2 and cell in state)
    }


space = set()
for y, line in enumerate(sys.stdin.read().split("\n")):
    for x, char in enumerate(line):
        if char == '#':
            space.add((x,y,0))


for i in range(6):
    space = simulate(space)

print(len(space))
