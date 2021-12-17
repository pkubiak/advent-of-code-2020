with open("input.txt") as file:
    cavern = [
        list(map(int, line.strip()))
        for line in file.read().split("\n")
    ]
    w, h = len(cavern[0]), len(cavern)
    cavern = {
        (x, y): int(v)
        for y, line in enumerate(cavern)
        for x, v in enumerate(line)
    }
    print(cavern)

def bfs(cavern):
    stack = [(0,0,0)]
    visited = {(0,0): True}
    
    w = max(x for x, y in cavern)
    h = max(y for x, y in cavern)
    while stack:
        stack.sort(key=lambda v: v[2])
        x, y, d = stack[0]
        stack = stack[1:]
        if x == w and y == h:
            return d
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x2, y2 = x+dx, y+dy
            if 0 <= x2 <= w and 0 <= y2 <= h and (x2,y2) not in visited:
                stack.append((x2,y2,d+cavern[(x2,y2)]))
                visited[(x2,y2)] = True
        

            
print(bfs(cavern))
cavern2 = {}
for x, y in cavern:
    for sx in range(5):
        for sy in range(5):
            v = cavern[(x,y)] + sx + sy
            if v >= 10: v-=9
            cavern2[(sx*w+x, sy*h+y)] = v
print(bfs(cavern2))