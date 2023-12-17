from collections import defaultdict

DIRS = [(1,0), (0, 1), (-1, 0), (0, -1)]

def solve(text: str, min_i: int, max_i: int):
    lines = text.split("\n")
    mapa = {
        (x, y): int(c)
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
    }

    w, h = len(lines[0]), len(lines)

    Q = defaultdict(list)

    Q[0].append((0, 0, 0 ))
    Q[0].append((0, 0, 1))
    
    min_q = -1
    best = {(0,0,0): 0, (0,0,1): 0}

    while True:
        min_q += 1
        if min_q not in Q:
            continue
        
        for x, y, d in Q.pop(min_q):
            if (x, y) == (w-1, h-1):
                return min_q
        
            if min_q > best[x,y,d]:
                continue

            for dd in [(d+1)%4, (d+3)%4]:
                t2 = min_q

                for i in range(1, max_i + 1):
                    x2, y2 = x + i * DIRS[dd][0], y + i * DIRS[dd][1]
                    if (x2,y2) not in mapa:
                        break
                    t2 += mapa[x2, y2]

                    if i >= min_i:
                        if (x2,y2,dd) not in best or t2 < best[x2,y2,dd]:
                            best[x2,y2,dd] = t2
                            Q[t2].append((x2,y2,dd))

def a(text: str) -> int:
    return solve(text, 1, 3)


def b(text: str) -> int:
    return solve(text, 4, 10)


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 102),
        ("input.txt", a, None),
        ("test_a.txt", b, 94),
        ("input.txt", b, None),
    ])