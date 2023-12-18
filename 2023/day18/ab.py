DIRS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

def a(text: str) -> int:
    lines = text.split("\n")
    x, y = 0, 0
    mapa = {(0, 0): True}
    for line in lines:
        a, b, c = line.split(" ")
        b = int(b)
        c = c.strip('()')
        for i in range(b):
            x += DIRS[a][0]
            y += DIRS[a][1]
            mapa[x,y] = True
        
    minx, miny = min(x for x, y in mapa), min(y for x, y in mapa)
    maxx, maxy = max(x for x, y in mapa), max(y for x, y in mapa)

    total = 0
    for y in range(miny, maxy+1):
        ile = 0 
        for x in range(minx, maxx+1):
            if (x,y) in mapa and (x,y-1) in mapa:
                ile += 1
            if (x, y) in mapa:
                total += 1
            else:
                total += (ile % 2) == 1
    return total
def get_area(coords):
    assert coords[0] == coords[-1]
    area, length = 0, 0

    maxy = max(y for x,y in coords)
    for i in range(len(coords)-1):
        # length = abs(coords[i+1][0] - coords[i][0]) + abs(coords[i+1][1] - coords[i][1]) 
        if coords[i][1] == coords[i+1][1]:
            assert coords[i+1][0] != coords[i][0]
            m = (coords[i+1][0] - coords[i][0])
            y = (maxy+10) - coords[i][1]# + (1 if coords[i+1][0] > coords[i][0] else 0)
            area += m * y
            # print(m, y)

        length += abs(coords[i+1][0] - coords[i][0]) + abs(coords[i+1][1] - coords[i][1])

    # print(area, length)
    return area + length // 2 + 1
        # else:
        #     x = maxy+1 - max(coords[i][1], coords[i+1][1])
        #     print(">>>>>", x)
        #     total -= x


# assert get_area([(-1, 0), (1,0), (1,1),(0,1), (0, 2), (1,2), (1,3), (-1, 3), (-1, 0)] ) == 12

# assert get_area([(0,0), (2, 0), (2, 2), (0, 2), (0, 0)]) == 9

# assert get_area([(0,0), (2,0), (2,1), (0, 1), (0, 0)]) == 6

##
###
###

assert get_area([(0, 0), (1, 0), (1, 1), (2, 1), (2,2), (0, 2), (0, 0)]) == 8

def b(text: str) -> int:
    dirs = 'RDLU'
    coords = [(0, 0)]
    lines = text.split("\n")
    for line in lines:
        a, b, c = line.split(" ")
        # b = int(b)
        c = c.strip('()#')
        a = int(c[:5], 16)
        b = dirs[int(c[5])]
        # print(c, a, b)
        x, y = coords[-1]
        new_x = x + a * DIRS[b][0]
        new_y = y + a * DIRS[b][1]
        coords.append((new_x, new_y))

    return get_area(coords)


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 62),
        ("input.txt", a, None),
        ("test_a.txt", b, 952408144115),
        ("input.txt", b, None),
    ])

