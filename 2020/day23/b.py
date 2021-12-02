import sys
from itertools import chain
from dataclasses import dataclass


@dataclass
class Chain:
    value: int
    next: 'Chain'


MOVES = 10_000_000

labeling = list(map(int, sys.stdin.read().strip()))
sCUPS = chain(labeling, range(max(labeling)+1, 1_000_001))

# Build chain
MAPPING = dict()
prev = None
for x in CUPS:
    MAPPING[x] = Chain(x, None)
    if prev:
        prev.next = MAPPING[x]
    prev = MAPPING[x]

prev.next = MAPPING[labeling[0]]

current = labeling[0]

# Perform moves
for i in range(MOVES):
    # Remove selected nodes from chain
    selected = MAPPING[current].next
    MAPPING[current].next = selected.next.next.next

    selected_values = {selected.value, selected.next.value, selected.next.next.value}
    # Compute destination position
    destination = current
    while True:
        destination = (((destination - 1) - 1) % len(MAPPING)) + 1
        if destination not in selected_values:
            break
    # print(current, destination)

    # Insert selected nodes in 
    selected.next.next.next = MAPPING[destination].next
    MAPPING[destination].next = selected

    current = MAPPING[current].next.value

a, b = MAPPING[1].next.value, MAPPING[1].next.next.value
print(a, b)
print(a * b)

