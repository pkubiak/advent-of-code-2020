monkeys = open("input.txt").read().split("\n\n")

print(monkeys)

# parse
data = []
for monkey in monkeys:
    lines = monkey.split("\n")
    items = list(map(int, lines[1].split(": ")[1].split(", ")))
    op = lines[2].split(": ")[1]
    divs = int(lines[3].split("by ")[1])
    case_true = int(lines[4].split("monkey ")[1])
    case_false = int(lines[5].split("monkey ")[1])
    data.append([items, op, divs, case_true, case_false])

from collections import Counter
M = [x[2] for x in data]
res = 1
for m in M:
    res*=m
print(M, res)
counts = Counter()
from tqdm import trange
for round in trange(10000):
    for i in range(len(data)):
        items = data[i][0]
        data[i][0] = []
        for item in items:
            counts[i] += 1
            old = item
            exec(data[i][1])
            new %= res         
            x = data[i][3] if (new % data[i][2]) == 0 else data[i][4]
            data[x][0].append(new)

a, b = counts.most_common(2)
print(a[1]*b[1])