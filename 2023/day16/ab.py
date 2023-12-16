DIRS = [(1,0), (0, 1), (-1, 0), (0, -1)]

def simulate(x, y, d, board, visited):
    while True:
        new_x, new_y = x+DIRS[d][0], y+DIRS[d][1]
        pos =  board.get((new_x, new_y), None)

        if pos is None or (new_x, new_y, d) in visited:
            break

        visited[new_x, new_y, d] = True
        if pos == '.':
            pass
        elif pos == "/":
            d = 3-d
        elif pos == "\\":
            d = {0:1, 1:0, 2:3, 3:2}[d]
        elif pos == "|":
            if d in (0,2):
                d = 1
                simulate(new_x, new_y, 3, board, visited)
        elif pos == "-":
            if d in (1,3):
                d = 0
                simulate(new_x, new_y, 2, board, visited)
        else:
            assert False

        x, y = new_x, new_y

def solve(text: str, positions):
    lines = text.split("\n")
    board = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            board[x,y] = c

    def count(x,y,d):
        visited = dict()
        simulate(x,y,d, board, visited)
        poss = dict()
        for x,y, _ in visited:
            poss[x,y] = True
        return len(poss)

    return max(count(x,y,d) for x, y, d in positions)


def a(text: str):
    return solve(text, [(-1,0,0)])


def b(text: str):
    lines = text.split("\n")
    w, h = len(lines[0]), len(lines)

    positions = []
    for x in range(0, w):
        positions += [(x, -1, 1), (x, h, 3)]
    for y in range(0, h):
        positions += [(-1, y, 0), (w, y, 2)]

    return solve(text, positions)


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 46),
        ("input.txt", a, None),
        ("test_b.txt", b, 51),
        ("input.txt", b, None),
    ])