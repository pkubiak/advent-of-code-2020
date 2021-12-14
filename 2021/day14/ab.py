from collections import Counter

with open("input.txt") as file:
    template, rules = file.read().split("\n\n")
    rules = dict(line.split(" -> ") for line in rules.split("\n"))

count = Counter()
for a, b in zip(template, template[1:]):
    count[a + b] += 1

res = {}
for i in range(1, 41):
    count2 = Counter()
    for k, c in count.items():
        if k in rules:
            v = rules[k]
            count2[k[0] + v] += c
            count2[v + k[1]] += c
        else:
            count2[k] += c
    count = count2

    c = Counter()
    for k, v in count.items():
        c[k[0]] += v
        c[k[1]] += v
    c[template[0]] += 1
    c[template[-1]] += 1

    res[i] = (c.most_common()[0][1] - c.most_common()[-1][1]) // 2

print("a:", res[10])
print("b:", res[40])
