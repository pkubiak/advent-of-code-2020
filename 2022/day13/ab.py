import functools

def cmp(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return a-b
        return cmp([a], b)

    if isinstance(b, int):
        return cmp(a, [b])
    
    for x, y in zip(a, b):
        if v := cmp(x, y):
            return v
    return len(a) - len(b)
    

text = open("input.txt").read().replace("\n\n", "\n")
items = [eval(line) for line in text.split("\n")]

total = sum(i+1 for i in range(len(items)//2) if cmp(*items[2*i:2*i+2]) < 0)
print("a:", total)

items += [[[2]], [[6]]]
items.sort(key=functools.cmp_to_key(cmp))

v = (items.index([[2]]) + 1) * (items.index([[6]]) + 1)
print("b:", v)