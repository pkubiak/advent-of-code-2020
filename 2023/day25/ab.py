from copy import deepcopy
import fractions
import sympy as sym
from collections import defaultdict
import networkx as nx
import itertools

def a(text: str):
    lines = text.split("\n")
    G = defaultdict(set)
    for line in lines:
        x, y = line.split(": ")
        ys = y.split(" ")
        for y in ys:
            G[x].add(y)
            G[y].add(x)

    Gg = nx.Graph()
    for i in G:
        for j in G[i]:
            if i < j:
                Gg.add_edge(i, j, capacity=1.0)

    nodes = list(G)
    for i, j in itertools.combinations(nodes, 2):
        cut_value, partition = nx.minimum_cut(Gg, i, j)
        L = list(len(x) for x in partition)

        if cut_value == 3.0:
            return L[0] * L[1]

if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", res)

    test([
        ("test_a.txt", a, 54),
        ("input.txt", a, None),
    ])
