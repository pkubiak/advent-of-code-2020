import sys, itertools


def check(seatch, x, y):
    total = 0
    for dx, dy in itertools.product((-1,0,1), repeat=2):
        if dx != 0 or dy != 0:
            i = 1
            while seats.get((x + i*dx, y + i*dy)) == '.':
                i += 1
            total += seats.get((x + i*dx, y + i*dy)) == '#'
    return total


def simulate(seats):
    new = {}
    for (x, y), state in seats.items():
        occupied = check(seats, x, y)
        
        if state == '#' and occupied >= 5:
            new[(x, y)] = 'L'
        elif state == 'L' and occupied == 0:
            new[(x, y)] = '#'
        else:
            new[(x, y)] = state

    return new


seats = {
    (x, y): char
    for y, line in enumerate(sys.stdin)
    for x, char in enumerate(line.strip())
}

while seats != (seats := simulate(seats)):
    pass

print(list(seats.values()).count('#'))