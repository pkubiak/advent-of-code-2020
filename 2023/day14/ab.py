def a(text: str) -> int:
    lines = text.split("\n")
    mapa = [
        list(line)
        for line in lines
    ]

    total = 0
    for x in range(len(mapa[0])):
        ile = 0
        base = len(mapa)
        for y in range(len(mapa)):
            if mapa[y][x] == '#':
                ile = 0
                base = len(mapa) - y - 1
            if mapa[y][x] == 'O':
                total += base - ile
                ile += 1

    return total


def b(text: str) -> int:
    lines = text.split("\n")

    mapa = [
        list(line)
        for line in lines
    ]

    def move_north():
        nonlocal mapa
        for x in range(len(mapa[0])):
            start = 0
            for y in range(len(mapa)):
                if mapa[y][x] == '#':
                    start = y+1
                elif mapa[y][x] == 'O':
                    mapa[start][x], mapa[y][x] = mapa[y][x], mapa[start][x]
                    start += 1
    
    def rotate_right():
        nonlocal mapa
        w = len(mapa[0])
        mapa2 = [
            # [mapa[i][w - 1 - j] for i in range(len(mapa))]
            [mapa[len(mapa)-1-i][j] for i in range(len(mapa))]
            for j in range(w)
        ]
        mapa = mapa2


    def turn():
        nonlocal mapa
        for i in range(4):
            move_north()
            rotate_right()

        state = "\n".join("".join(line) for line in mapa)
        total = 0
        for x in range(len(mapa[0])):
            for y in range(len(mapa)):
                if mapa[y][x] == 'O':
                    total += len(mapa) - y
        return hash(state), total
    
    values = {}
    i = 0
    target = None
    while True:
        if i == target:
            return v
        h, v = turn()
        
        # print(i, h, v)
        if h in values and target is None:
            offset = i - values[h]
            target = i - (i % offset) + offset + (1000000000 % offset)
            # print(">>", offset, i, target, 1000000000 % offset)
        values[h] = i
        i += 1
    return v


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 136),
        ("input.txt", a, None),
        ("test_a.txt", b, 64),
        ("input.txt", b, None),
    ])
