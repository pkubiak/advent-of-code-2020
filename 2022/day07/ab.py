from collections import defaultdict
from functools import cache

def read_tree(text: str):
    path, tree = [], defaultdict(list)
    for line in text.splitlines():
        match line.split():
            case ["$", "ls"]:
                pass
            case ["$", "cd", ".."]:
                path.pop()
            case ["$", "cd", name]:
                path.append(name)
            case [size, name]:
                tree["/".join(path)].append((size, name))
    return tree

with open("input.txt") as file:
    text = file.read()
    tree = read_tree(text)

    @cache
    def get_size(path):
        total = 0
        for x, y in tree[path]:
            total += get_size(path + "/" + y) if x == "dir" else int(x)

        return total

    sizes = [get_size(path) for path in tree]
    print("a:", sum(size for size in sizes if size <= 100_000))

    sizes = [size for size in sizes if 70_000_000 - get_size("/") + size > 30_000_000]
    print("b:", min(sizes))