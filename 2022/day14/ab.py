sgn = lambda x: x//abs(x) if x else 0

def parse_input(text):
    for line in text.split("\n"):
        items = [tuple(map(int, item.split(","))) for item in line.split(" -> ")]

        x, y = items[0]
        for x2, y2 in items[1:]:
            dx, dy = sgn(x2 - x), sgn(y2 - y)
            while (x, y) != (x2, y2):
                yield x,y
                x += dx
                y += dy
        yield x,y


def simulate(mapa, limit, floor_on_limit):
    x, y = 500, 0

    while True:
        if y == limit:
            if not floor_on_limit: return False
            break

        for dx in [0, -1, 1]:
            if (x + dx, y + 1) not in mapa:
                x, y = (x + dx, y + 1)
                break
        else:
            break
    
    mapa.add((x,y))
    return True


text = open("input.txt").read()
cave = set(parse_input(text))
cave_copy = cave.copy()
original_size = len(cave)
limit = max(y for _, y in cave) + 1

while simulate(cave, limit, False): pass
print("a:", len(cave) - original_size)

while (500, 0) not in cave_copy:
    simulate(cave_copy, limit, True)
print("b:", len(cave_copy) - original_size)
    