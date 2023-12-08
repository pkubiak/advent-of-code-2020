import re

def a(text: str):
    x, y = text.split("\n\n")
    mapa = dict()
    for line in y.split("\n"):
        line = re.sub(r"[^A-Z]", " ", line)
        line = re.sub(r"\s+", " ", line).strip()
        s, l, r = line.split(" ")
        mapa[s] = (l, r)

    i = 0
    pos = "AAA"
    while pos != "ZZZ":
        dir = x[i % len(x)]
        i += 1
        pos = mapa[pos][0 if dir == "L" else 1]
    
    return i


def b(text: str):
    x, y = text.split("\n\n")
    mapa = dict()
    for line in y.split("\n"):
        line = re.sub(r"[^0-9A-Z]", " ", line)
        line = re.sub(r"\s+", " ", line).strip()
        s, l, r = line.split(" ")
        mapa[s] = (l, r)

    nodes = []
    for k in mapa:
        if k.endswith('A'):
            nodes.append(k)
    i = 0
    visited_at = dict()
    for j, n in enumerate(nodes):
        visited_at[(j, n)] = 0
    loops_at = dict()
    loops = {i: False for i in range(len(nodes))}
    while True:
        if all(n.endswith('Z') for n in nodes):
            return i
        
        dir = x[i % len(x)]
        
        i += 1

        nodes = [mapa[n][0 if dir == "L" else 1] for n in nodes]

        for j, n in enumerate(nodes):
            if (j, n, i % len(x)) in visited_at and loops[j] is False:
                loops[j] = i - visited_at[j,n,i%len(x)]
            else:
                visited_at[j, n, i % len(x)] = i

        if all(loops.values()):
            rems = [
                [(k, visited_at[k]) for k in visited_at if k[0] == j and k[1].endswith('Z')]
                for j in range(len(nodes))
            ]
            
            # print(rems)
            # print(loops)
            o = math.lcm(*loops.values())
            return o

import math


if __name__ == "__main__":
    for fn, val in [(a, 6), (b, 6)]:
        name = fn.__name__
        # res = fn(open(f"test_{name}.txt").read())
        # assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))