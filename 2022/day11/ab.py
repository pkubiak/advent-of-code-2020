
import re, math

def parse(text):
    for monkey in text.split("\n\n"):
        op = re.findall(r"= (.*)", monkey)[0]
        nums = list(map(int, re.findall(r"\d+", monkey.replace(op,''))))
        yield [nums[1:-3], op, *nums[-3:]]
    

def count(monkeys, rounds, fn) -> int:
    counts = [0] * len(monkeys)
    for _ in range(rounds):
        for i, (items, op, div, true, false) in enumerate(monkeys):
            counts[i] += len(items)
            for old in items:
                new = fn(eval(op))
                x = true if (new % div) == 0 else false
                monkeys[x][0].append(new)
            items.clear()

    counts.sort(reverse=True)
    return counts[0] * counts[1]


text = open("input.txt").read()

print("a:", count(list(parse(text)), 20, lambda x: x//3))

data = list(parse(text))
M = math.prod(x[2] for x in data)
print("b:", count(data, 10_000, lambda x: x%M))