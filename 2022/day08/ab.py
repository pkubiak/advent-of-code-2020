with open("input.txt") as file:
    text = file.read().split("\n")
    forest = [[int(i) for i in line] for line in text]

    H, W = len(forest), len(forest[0])
    visible = {}

def check_visibility():
    visible = {}
    xs, ys = list(range(W)), list(range(H))

    for y in ys:
        for xx in [xs, reversed(xs)]:
            best = -1
            for x in xx:
                if forest[y][x] > best:
                    visible[x,y] = True
                best = max(best, forest[y][x])

    for x in xs:
        for yy in [ys, reversed(ys)]:
            best = -1
            for y in yy:
                if forest[y][x] > best:
                    visible[x,y] = True
                best = max(best, forest[y][x])
    return len(visible.keys())

def count(x, y):
    res = 1
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        ile = 0
        for i in range(1,10000):
            xx = x + i * dx
            yy = y + i * dy
            if not (0 <= xx < W and 0 <= yy < H):
                break
            ile += 1
            if forest[yy][xx] >= forest[y][x]:
                break
        res *= ile

    return res

print("a:", check_visibility())
results = []
for y in range(H):
    for x in range(W):
        results.append(count(x, y))
print("b:", max(results))