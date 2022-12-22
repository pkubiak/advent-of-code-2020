import re

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SIDES = {
    (1,0): 'A', (2,0): 'B',
    (1,1): 'C',
    (0,2): 'D', (1,2): 'E',
    (0,3): 'F'
}

text = open("input.txt").read()

mapa, moves = text.split("\n\n")
mapa = mapa.split("\n")
L = len(mapa) // 4
mapa = {(x, y): c for y, line in enumerate(mapa) for x, c in enumerate(line) if c in '#.'}

moves = re.findall("(\d+|[LR])", moves)


def generate(side, dir):
    s = [k for k,v in SIDES.items() if v==side][0]
    x0, y0 = s[0]*L, s[1]*L
    if dir == 'top':
        return [(x0+i, y0) for i in range(L)]
    if dir == 'right':
        return [(x0+L-1, y0+i) for i in range(L)]
    if dir == 'bottom':
        return [(x0 +L-1-i, y0+L-1) for i in range(L)]
    if dir == 'left':
        return [(x0, y0+L-1-i) for i in range(L)]

TELEPORTS = {}

def match(d0, pos1, d1, pos2):
    for a, b in zip(pos1, pos2):
        assert (a[0], a[1], d0) not in TELEPORTS
        TELEPORTS[(a[0], a[1], d0)] = (b[0], b[1], d1)
        TELEPORTS[(b[0], b[1], (d1+2)%4)] = (a[0], a[1], (d0+2)%4)


match(3, generate('A', 'top'), 0, reversed(generate('F','left')))
match(2, generate('A', 'left'), 0, reversed(generate('D', 'left')))
match(2, generate('C', 'left'), 1, reversed(generate('D', 'top')))
match(0, generate('C', 'right'), 3, reversed(generate('B','bottom')))
match(0, generate('B','right'), 2, reversed(generate('E', 'right')))
match(3, generate('B', 'top'), 3, reversed(generate('F','bottom')))
match(1, generate('E', 'bottom'), 2, reversed(generate('F', 'right')))


def crawl(mapa, moves, overflow_method):
    x = y = d = 0 
    while (x, y) not in mapa:
        x+=1
    for move in moves:
        if move in 'LR':
            d = (d + (1 if move == 'R' else -1)) % 4
            continue
        length = int(move)

        for i in range(length):
            x2, y2, d2 = (x+DIRS[d][0]), (y + DIRS[d][1]), d

            if (x2, y2) not in mapa:
                if overflow_method == 'cube':
                    assert (x, y, d) in TELEPORTS, f"{x}, {y}, {d}"
                    x2, y2, d2 = TELEPORTS[x,y,d]
                elif overflow_method == 'normal':
                    while True:
                        x2 += DIRS[(d+2)%4][0]
                        y2 += DIRS[(d+2)%4][1]
                        if (x2, y2) not in mapa:
                            break
                    x2 += DIRS[d%4][0]
                    y2 += DIRS[d%4][1]

            if mapa[x2,y2] == '#':
                break
            x, y, d = x2, y2, d2
        
    return 1000 * (y+1) + 4 * (x+1) + d

print("a:", crawl(mapa, moves, 'normal'))
print("b:", crawl(mapa, moves, 'cube'))