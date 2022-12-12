DIRS = {
    "U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)
}

def update(p0, p1):
    Hx, Hy = p0
    Tx, Ty = p1

    dx, dy = abs(Hx-Tx), abs(Hy-Ty)
    if dx > 1:
        Tx += 1 if Hx > Tx else -1
        if dy != 0:
            Ty += 1 if Hy > Ty else -1
    elif dy > 1:
        Ty += 1 if Hy > Ty else -1
        if dx != 0:
            Tx += 1 if Hx > Tx else -1

    return Tx, Ty


N = 10

positions = {i: (0,0) for i in range(N)}
visited = {i: {} for i in range(N)}

for line in open("input.txt").readlines():
    d, n = line.split(" ")
    n = int(n)

    for _ in range(n):
        positions[0] = positions[0][0] + DIRS[d][0], positions[0][1] + DIRS[d][1]
        for i in range(1, N):
            positions[i] = update(positions[i-1], positions[i])
            visited[i][positions[i]] = True

print("a:", len(visited[1]))
print("b:", len(visited[9]))