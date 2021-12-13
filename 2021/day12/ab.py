from collections import defaultdict

with open("input.txt") as file:
    G = defaultdict(set)
    for line in file:
        a, b = line.strip().split("-")
        G[a].add(b)
        G[b].add(a)


def dfs(G, u="start", visited={"start"}, visited_twice=True):
    if u == "end":
        return 1
    total = 0
    for v in G[u]:
        if "a" <= v[0] <= "z" and v in visited:
            if not visited_twice and v != "start":
                total += dfs(G, v, visited | {v}, True)
            continue
        total += dfs(G, v, visited | {v}, visited_twice)

    return total

print("a:", dfs(G, visited_twice=True))
print("b:", dfs(G, visited_twice=False))
