import sys

forest = [
    line.strip()
    for line in sys.stdin
]

W, H = len(forest[0]), len(forest)

count = sum(
    forest[y][(3 * y) % W] == '#'
    for y in range(1, H)
)

print(count)