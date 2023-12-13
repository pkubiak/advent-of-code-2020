def count_diffs(a, b):
    ile = 0
    for i, j in zip(a, b):
        if i!=j:
            ile += 1
    return ile


def testt(lines, x) -> int:
    total = 0
    for i in range(x+1):
        if x+i+1 < len(lines):
            total += count_diffs(lines[x-i], lines[x+i+1])
    return total


def find_reflection(part, c):
    lines = part.split("\n")

    w, h = len(lines[0]), len(lines)

    xx, yy = [], []
    for y in range(h-1):
        if testt(lines, y) == c:
            yy.append(y)
    
    rev_lines = [''.join(lines[j][i] for j in range(h)) for i in range(w)]
    for x in range(w-1):
        if testt(rev_lines, x) == c:
            xx.append(x)

    assert len(xx) <= 1
    assert len(yy) <= 1
    return (xx[0] if xx else None, yy[0] if yy else None)


def solve(text: str, c):
    parts = text.split("\n\n")

    total = 0 
    for part in parts:
        x, y = find_reflection(part, c)
        if x is not None:
            total += x + 1
        if y is not None:
            total += (y+1)*100
        assert (x is None) or (y is None)

    return total


def a(text: str):
    return solve(text, 0)


def b(text: str):
    return solve(text, 1)


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 405),
        ("input.txt", a, None),
        ("test_a.txt", b, 400),
        ("input.txt", b, None),
    ])
