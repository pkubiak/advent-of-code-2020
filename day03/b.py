import sys, functools, operator

forest = [
    line.strip()
    for line in sys.stdin
]

W, H = len(forest[0]), len(forest)

def count_trees(dx, dy):
    return sum(
        forest[dy*i][(dx * i) % W] == '#'
        for i in range(1, H // dy, 1)
    )    

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total = functools.reduce(
    operator.mul, 
    (count_trees(*s) for s in SLOPES)
)

print(total)