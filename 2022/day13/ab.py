with open("input.txt") as file:
    text = file.read()

def cmp(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            if a == b:
                return None
            return a < b
        return cmp([a], b)
    if isinstance(b, int):
        return cmp(a, [b])
    
    for x, y in zip(a, b):
        v = cmp(x, y)
        if v is not None:
            return v
    if len(a) == len(b):
        return None
    return len(a) < len(b)
    

# total = 0
# for i, pairs in enumerate(text.split("\n\n"), start=1):
#     l1, l2 = pairs.split("\n")
#     l1 = eval(l1)
#     l2 = eval(l2)

#     if cmp(l1, l2):
#         total += i
# print(total)
items = [eval(line) for line in text.replace("\n\n", "\n").split("\n")]
items.extend([ [[2]], [[6]]])
# print(items)

for _ in range(len(items)):
    for j in range(1, len(items)):
        if cmp(items[j-1], items[j]) is True:
            items[j-1], items[j] = items[j], items[j-1]

items = items[::-1]

v = (items.index([[2]])+1) * (items.index([[6]])+1)
print(v)
