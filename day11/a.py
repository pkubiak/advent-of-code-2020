import sys, itertools


def simulate(seats):
    new = {}
    for (x, y), state in seats.items():
        occupied = sum(
            seats.get((x+dx, y+dy)) == '#' 
            for dx, dy in itertools.product((-1,0,1), repeat=2)
            if dx != 0 or dy != 0
        )
        
        if state == '#' and occupied >= 4:
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