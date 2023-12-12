from functools import lru_cache

@lru_cache(100000)
def rec_count(mapa, counts) -> int:
    # print(mapa, counts)
    if len(counts) == 0:
        return 1 if mapa.count('#') == 0 else 0
    
    if len(mapa) == 0:
        return 1 if len(counts) == 0 else 0

    if mapa[0] == '.':
        return rec_count(mapa[1:], counts)
    
    if mapa[0] == '#':
        if len(mapa) < counts[0]:
            return 0
        
        for i in range(counts[0]):
            if mapa[i] == '.':
                return 0

        if len(mapa) == counts[0]:
            return 1 if len(counts) == 1 else 0
        if mapa[counts[0]] == '#':
            return 0
        return rec_count(mapa[counts[0]+1:], counts[1:])
    
    return rec_count('.'+mapa[1:], counts) + rec_count('#'+mapa[1:], counts)


def solve(text: str, length: int = 1):
    lines = text.split("\n")
    total = 0
    for line in lines:
        x, y = line.split(" ")
        x = "?".join([x]*length)
        y = list(int(i) for i in y.split(","))
        y *= length
        ile = rec_count(x, tuple(y))
        total += ile

    return total

def a(text: str):
    return solve(text, 1)

def b(text: str):
    return solve(text, 5)


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 21),
        ("input.txt", a, None),
        ("test_a.txt", b, 525152),
        ("input.txt", b, None),
    ])
