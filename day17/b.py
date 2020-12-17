import sys, itertools
from collections import Counter


def simulate(state, N):
    counts = Counter()
    diffs = set(itertools.product([-1,0,1], repeat=N)) - {(0,)*N}

    for coord in state:
        counts.update(
            tuple(map(sum, zip(coord, diff)))
            for diff in diffs
        )

    return {
        cell 
        for cell in counts
        if counts[cell] == 3 or (counts[cell] == 2 and cell in state)
    }

N = 4

state = set()
for y, line in enumerate(sys.stdin.read().split("\n")):
    for x, char in enumerate(line):
        if char == '#':
            state.add((x, y) + (0,)*(N-2))


for i in range(6):
    state = simulate(state, N)

print(len(state))
