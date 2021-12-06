from collections import Counter, defaultdict

c = defaultdict(Counter)

with open('input.txt') as file:
    for line in file:
        for i, b in enumerate(line.strip()):
            c[i].update(b)

gamma = [c[d].most_common()[0][0] for d in sorted(c.keys())]
gamma = int(''.join(gamma), 2)

epsilon = [c[d].most_common()[1][0] for d in sorted(c.keys())]
epsilon = int(''.join(epsilon), 2)

print(gamma * epsilon)