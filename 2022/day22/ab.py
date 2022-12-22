import re

TELEPORTS = {}
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SIDES = {"A": (1, 0), "B": (2, 0), "C": (1, 1), "D": (0, 2), "E": (1, 2), "F": (0, 3)}

# read input
text = open("input.txt").read()

mapa, moves = text.split("\n\n")
mapa = {
    (x, y): c for y, line in enumerate(mapa.split("\n")) for x, c in enumerate(line) if c in "#."
}
L = round((len(mapa)//6)**0.5)

moves = re.findall("(\d+|[LR])", moves)


def generate(side, edge):
    """Generate cells on side's edge."""
    s = SIDES[side]
    x0, y0 = s[0] * L, s[1] * L
    dir = DIRS[["top", "right", "bottom", "left"].index(edge)]
    if edge in ("right", "bottom"):
        x0 += L - 1
    if edge in ("bottom", "left"):
        y0 += L - 1
    return [(x0 + i * dir[0], y0 + i * dir[1]) for i in range(L)]


def connect(side0, edge0, side1, edge1):
    EDGES = ["right", "bottom", "left", "top"]
    d0 = EDGES.index(edge0)
    d1 = (EDGES.index(edge1) + 2) % 4
    for a, b in zip(generate(side0, edge0), reversed(generate(side1, edge1))):
        assert (a[0], a[1], d0) not in TELEPORTS
        TELEPORTS[(a[0], a[1], d0)] = (b[0], b[1], d1)
        TELEPORTS[(b[0], b[1], (d1 + 2) % 4)] = (a[0], a[1], (d0 + 2) % 4)


def crawl(mapa, moves, overflow_method):
    x = y = d = 0
    while (x, y) not in mapa:
        x += 1
    for move in moves:
        if move in "LR":
            d = (d + (1 if move == "R" else -1)) % 4
            continue
        length = int(move)

        for i in range(length):
            x2, y2, d2 = (x + DIRS[d][0]), (y + DIRS[d][1]), d

            if (x2, y2) not in mapa:
                if overflow_method == "cube":
                    assert (x, y, d) in TELEPORTS, f"{x}, {y}, {d}"
                    x2, y2, d2 = TELEPORTS[x, y, d]
                elif overflow_method == "normal":
                    while True:
                        x2 += DIRS[(d + 2) % 4][0]
                        y2 += DIRS[(d + 2) % 4][1]
                        if (x2, y2) not in mapa:
                            break
                    x2 += DIRS[d % 4][0]
                    y2 += DIRS[d % 4][1]

            if mapa[x2, y2] == "#":
                break
            x, y, d = x2, y2, d2
    return 1000 * (y + 1) + 4 * (x + 1) + d

connect("A", "top", "F", "left")
connect("A", "left", "D", "left")
connect("B", "bottom", "C", "right")
connect("B", "right", "E", "right")
connect("B", "top", "F", "bottom")
connect("C", "left", "D", "top")
connect("E", "bottom", "F", "right")

print("a:", crawl(mapa, moves, "normal"))
print("b:", crawl(mapa, moves, "cube"))