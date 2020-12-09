import sys
from itertools import combinations

data = []

def check(x):
    return x in map(sum, combinations(data, 2))


for line in sys.stdin:
    x = int(line.strip())

    if len(data) == 25 and not check(x):
        print(x)
        break
    
    data = (data + [x])[-25:]
