from collections import defaultdict
from functools import cache

def read_tree(text: str):
    lines = text.split("\n")
    i, path, children = 0, [], defaultdict(list)
    while i < len(lines):
        _, cmd, *args = lines[i].split(" ")
        i+= 1
        if cmd == 'cd':
            if args[0] == '..':
                path.pop()
            else:
                path.append(args[0])
        else:
            while i < len(lines) and not lines[i].startswith('$'):
                x, y = lines[i].split(" ")
                if x == 'dir':
                    x = None
                else:
                    x = int(x)
                children["/".join(path)].append((x, y))
                i += 1

    return children


with open("input.txt") as file:
    text = file.read()
    children = read_tree(text)

    @cache
    def get_size(path):
        total = 0
        for x, y in children[path]:
            total += get_size(path + "/" + y) if x is None else x

        return total

    sizes = [get_size(path) for path in children]
    print("a:", sum(size for size in sizes if size <= 100_000))

    sizes = [size for size in sizes if 70_000_000 - get_size("/") + size > 30_000_000]
    print("b:", min(sizes))