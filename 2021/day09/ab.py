with open("input.txt") as file:
    heightmap = {
        (x, y): int(h)
        for y, line in enumerate(file)
        for x, h in enumerate(line.strip())
    }

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
total = 0
for x, y in heightmap:
    for dx, dy in D:
        h = heightmap.get((x + dx, y + dy))
        if h is not None and h <= heightmap[(x, y)]:
            break
    else:
        total += 1 + heightmap[(x, y)]

print("a:", total)


def visit(x, y):
    return 1 + sum(
        visit(x + dx, y + dy)
        for dx, dy in D
        if heightmap.pop((x + dx, y + dy), None) is not None
    )


for key in list(heightmap):
    if heightmap[key] >= 9:
        del heightmap[key]

basins = []
while heightmap:
    loc, _ = heightmap.popitem()
    basins.append(visit(*loc))

basins.sort()
print("b:", basins[-1] * basins[-2] * basins[-3])
