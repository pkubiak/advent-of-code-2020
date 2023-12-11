def a(text: str, d: int = 2):
    lines = text.split("\n")
    w, h = len(lines[0]), len(lines)
    mapa = dict()
    rows = set()
    cols = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                mapa[x,y]=True
                rows.add(y)
                cols.add(x)

    galaxies = list(mapa.keys())
    total = 0
    ile = 0 
    for a in range(len(galaxies)):
        for b in range(a+1, len(galaxies)):
            ile += 1
            minx, maxx = sorted([galaxies[a][0], galaxies[b][0]])
            miny, maxy = sorted([galaxies[a][1], galaxies[b][1]])

            for i in range(minx, maxx):
                total += d if i not in cols else 1
            for i in range(miny, maxy):
                total += d if i not in rows else 1
    
    return total
    
def b1(text):
    return a(text, 10)

def b2(text):
    return a(text, 100)

def b(text: str):
    return a(text, 1_000_000)


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 374),
        ("input.txt", a, None),
        ("test_a.txt", b1, 1030),
        ("test_a.txt", b2, 8410),
        ("input.txt", b, None),
    ])
