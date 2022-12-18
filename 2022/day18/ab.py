DIRS = [(-1,0,0),(1,0,0), (0,1,0),(0,-1,0), (0,0,1), (0,0,-1)]

def bfs(shape):
    minx = min(x for x,y,z in shape)-1
    maxx = max(x for x,y,z in shape)+1
    miny = min(y for x,y,z in shape)-1
    maxy = max(y for x,y,z in shape)+1
    minz = min(z for x,y,z in shape)-1
    maxz = max(z for x,y,z in shape)+1

    queue = [(minx, miny, minz)]
    visited = {queue[0]: True}

    while queue:
        q, *queue = queue
        x,y,z = q
        for dx, dy, dz in DIRS:
            p = x2,y2,z2 = x+dx, y+dy,z+dz
            
            if (minx<=x2<=maxx) and (miny<=y2<=maxy) and (minz <=z2<=maxz) and p not in shape and p not in visited:
                queue.append(p)
                visited[p] = True
    return visited

def count(shape, boundary=None):
    total = 0
    for x, y, z in shape:
        for dx,dy,dz in DIRS:
            p = x+dx, y+dy, z+dz
            total += p not in shape and (not boundary or p in boundary)
    return total


shape = set()
for line in open("input.txt").read().split("\n"):
    point = tuple(map(int, line.strip().split(",")))
    shape.add(point)

print("a:", count(shape))

boundary = bfs(shape)
print("b:", count(shape, boundary))