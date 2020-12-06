import sys

groups = sys.stdin.read().split("\n\n")

total = 0
for group in groups:
    s = set(g)
    s.discard('\n')
    total += len(s)

print(total)