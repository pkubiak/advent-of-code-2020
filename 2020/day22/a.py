import sys

p1, p2 = sys.stdin.read().split("\n\n")
cards1 = list(int(x) for x in p1.split("\n")[1:])
cards2 = list(int(x) for x in p2.split("\n")[1:])

while len(cards1) and len(cards2):
    c1 = cards1[0]
    cards1 = cards1[1:]
    c2 = cards2[0]
    cards2 = cards2[1:]

    if c1 > c2:
        cards1.append(c1)
        cards1.append(c2)
    else:
        cards2.append(c2)
        cards2.append(c1)

print(cards1)
print(cards2)

print(sum(i*x for i, x in enumerate(cards1[::-1], start=1)))
print(sum(i*x for i, x in enumerate(cards2[::-1], start=1)))