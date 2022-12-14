text = open("input.txt").read()

mapa = {}

def sgn(x):
    if x>0:return 1
    if x<0:return -1
    return 0

# load map
for line in text.split("\n"):
    items = [tuple(map(int, item.split(","))) for item in line.split(" -> ")]
    print(items)

    x, y = items[0]

    for x2, y2 in items[1:]:
        dx, dy = sgn(x2-x), sgn(y2-y)
        while (x,y)!=(x2,y2):
            mapa[(x,y)] = True
            x +=dx
            y+=dy
        mapa[(x,y)] = True

# simulate
def simulate(mapa, maxy):
    miny = min(y for x,y in mapa)
    # maxy = max(y for x,y in mapa)

    x, y = 500, miny - 2
    while y < maxy + 5:
        if y == maxy:
            mapa[(x,y)] = True
            return True
        if (x,y+1) not in mapa:
            y += 1
        elif (x-1,y+1) not in mapa:
            x-=1
            y+=1
        elif (x+1, y+1) not in mapa:
            x+=1
            y+=1
        else:
            mapa[x,y] = True
            return True
    return False

ile = len(mapa)
maxy = max(y for x,y in mapa)
while simulate(mapa, maxy+1) and (500, 0) not in mapa:
    pass
ile2 = len(mapa)

print(ile2-ile)
    