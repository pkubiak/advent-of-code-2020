import sys

groups = sys.stdin.read().split("\n\n")

total = sum(
    len(set(group) - {"\n"})
    for group in groups
)

print(total)