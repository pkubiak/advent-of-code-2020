import sys
groups = sys.stdin.read().split("\n\n")

total = 0
for g in groups:
    sg = g.split("\n")
    base = set(list(sg[0]))
    for ss in sg[1:]:
        base = base & set(list(ss))
    
    total += len(base)

print(total)