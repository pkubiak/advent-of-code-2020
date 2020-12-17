import sys, itertools

def simulate(state):
    cells = set()
    for x,y,z,t in state:
        cells.update(
            (x+dx, y+dy, z+dz, t+dt)
            for dx, dy, dz, dt in itertools.product([-1,0,1], repeat=4)
        )

    new_state = set()
    for x, y, z, t in cells:
        total = sum(
            (x+dx, y+dy, z+dz, t+dt) in state
            for dx, dy, dz, dt in itertools.product([-1,0,1], repeat=4)
            if (dx!=0 or dy!=0 or dz!=0 or dt!=0)
        )
        if (x,y,z,t) in state:
            if 2 <= total <= 3:
                new_state.add((x,y,z,t))
        else:
            if total == 3:
                new_state.add((x,y,z,t))

    return new_state



space = set()
for y, line in enumerate(sys.stdin.read().split("\n")):
    for x, char in enumerate(line):
        if char == '#':
            space.add((x,y,0,0))


for i in range(6):

    space =simulate(space)
    print(len(space))
