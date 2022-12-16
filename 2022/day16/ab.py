import re
from collections import defaultdict
from functools import cache
from itertools import product, permutations

text = open("input.txt").read()

RATES = {}
G = {}
revG = defaultdict(list)
IDS = {}
for item in re.findall(r"^Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)$", text, re.MULTILINE):
    node = item[0]
    
    RATES[node]  = int(item[1])
    if RATES[node] > 0:
        IDS[node] = len(IDS)
    G[node] =  list(item[2].split(", "))

for a in G:
    for b in G[a]:
        revG[b].append(a)

best = 0
non_zero = set([k for k,v in RATES.items() if v > 0])


@cache
def check(time, node, op):
    ### najlepszy wynik ktory po `time` sekundach znajduje sie w `a`` i ma zapalone `op`

    if time == 0:
        if node == 'AA' and op == 0:
            return 0
        return -123456789
    best = -123456789
    score = 0

    for k in non_zero:
        if op & (1<<IDS[k]):
            score += RATES[k]

    # move somewhere
    for k in revG[node]:
        best = max(best, check(time-1, k, op) + score)

    # try open
    if node in non_zero and (op & (1<<IDS[node])):
        best = max(best, check(time-1, node, op^(1<<IDS[node]))+score)


    return best

best_of_mask = {}
from tqdm import tqdm, trange
for mask in trange(2**len(non_zero)):
    best = 0
    for end_node in G:
        res =  check(25, end_node, mask)
        best = max(best, res)
    best_of_mask[mask] = best

@cache
def best_of_submask(mask):
    best = best_of_mask[mask]
    for i in range(len(non_zero)):
        if mask & (1<<i):
            best = max(best, best_of_submask(mask ^ (1<<i)))
    return best

# print(max(best_of_mask.values()))
x = 2**len(non_zero) - 1
best = 0
for mask in trange(2**len(non_zero)):
    best = max(best, best_of_submask(mask) + best_of_submask(x^mask))
print(best)
