import sys

groups = sys.stdin.read().split("\n\n")

total = 0
for group in groups:
    answers = group.split("\n")
    common = set.intersection(*map(set, answers))
    total += len(common)

print(total)