def simulate(text ,order):
    init, moves = text.split("\n\n")

    init = init.split("\n")[:-1]
    n = init[-1].count("[")
    cranes = [[] for _ in range(n)]

    for line in reversed(init):
        for i, crane in enumerate(cranes):
            if (z := line[4*i+1]) != ' ':
                crane.append(z)
    
    for line in moves.split("\n"):
        _, count, _, b, _, c = line.split(" ")
        count, b, c = int(count), int(b) - 1, int(c) - 1
        load  = cranes[b][-count:]
        cranes[b] = cranes[b][:-count]
        cranes[c] += load[::order]

    return ''.join(crane[-1] for crane in cranes)


with open("input.txt") as file:
    text = file.read()
    print("a:", simulate(text, -1))
    print("b:", simulate(text, 1))