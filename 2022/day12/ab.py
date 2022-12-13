def bfs(mapa, starts, end):
    queue = list(starts)
    visited = {s:0 for s in starts}
    
    while queue:
        pos, *queue = queue
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            new = pos[0]+dx, pos[1]+dy
            if (new in mapa) and (new not in visited) and (ord(mapa[new]) <= ord(mapa[pos]) + 1):
                visited[new] = visited[pos] + 1
                queue.append(new)

    return visited.get(end)


with open("input.txt") as file:
    mapa = {
        (x,y): k 
        for y, line in enumerate(file) 
        for x, k in enumerate(line.strip())
    }

find = lambda c: [k for k, v in mapa.items() if v == c]

mapa[start := find('S')[0]] = 'a'
mapa[end := find('E')[0]] = 'z'

print("a:", bfs(mapa, [start], end))
print("b:", bfs(mapa, find('a'), end))