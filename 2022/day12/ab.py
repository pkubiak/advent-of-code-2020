mapa = [list(line.strip()) for line in open("input.txt")]
W, H = len(mapa[0]), len(mapa)

for y in range(H):
    for x in range(W):
        if mapa[y][x] == 'S':
            start = (x,y)
            mapa[y][x] = 'a'
        if mapa[y][x] == 'E':
            end = (x,y)
            mapa[y][x] = 'z'

def bfs(mapa, starts, end):
    queue = list(starts)
    visited = {s:0 for s in starts}
    
    while queue:
        pos, *queue = queue
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            x = pos[0]+dx
            y = pos[1]+dy
            if 0<=x<W and 0<=y<H and (x,y) not in visited and (ord(mapa[y][x]) <= ord(mapa[pos[1]][pos[0]])+1):
                visited[(x,y)] = visited[pos] + 1
                queue.append((x,y))

    return visited.get(end)


print("a:", bfs(mapa, [start], end))
print("b:", bfs(mapa, [(x,y) for x in range(W) for y in range(H) if mapa[y][x]=='a'], end))
            