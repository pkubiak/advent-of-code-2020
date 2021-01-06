import sys
# 0 0 0 
#  0 0 
# 0 0 0 

def split_dirs(desc):
    i = 0
    while i < len(desc):
        if desc[i] in ('w', 'e'):
            yield desc[i]
            i+=1
        else:
            yield desc[i:i+2]
            i += 2

def get_coords(desc: int) -> tuple:
    x, y = 0, 0
    for d in split_dirs(desc):
        offset = 1-(y%2)
        if 'e' in d:
            x += 1
        elif 'w' == d:
            x -= 1

        if 'n' in d:
            y -= 1
        elif 's' in d:
            y += 1

        if d not in ('e' ,'w'):
            x -= offset
    return x, y

from collections import Counter
c = Counter()
for line in sys.stdin.read().split("\n"):
    c[get_coords(line)] += 1

print(sum(v%2 for v in c.values()))