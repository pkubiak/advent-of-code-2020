import sys


a, b = 1, 0 # partial solution: a*t + b

_, line = sys.stdin.read().split("\n")

for i, m in enumerate(line.split(',')):
    if m == 'x':
        continue

    m = int(m)
    r = (-i) % m

    candidates = {
        b + i * a
        for i in range(m+1)
    } - {0}

    a *= m
    b = min(
        x for x in candidates
        if (x - r) % m == 0
    )
    
print(b)