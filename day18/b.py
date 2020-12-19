import sys, re, math


def evaluate(s) -> str:
    assert '(' not in s
    x = re.split('([+*])', re.sub('\s', '', s))
    y = [int(x[0])]
    for i in range(1,len(x),2):
        if x[i] == '+':
            y.append(y.pop() + int(x[i+1]))
        else:
            y.append(int(x[i+1]))
    return str(math.prod(y))


def reduce(s):
    while '(' in s:
        s = re.sub(r'\(([^()]+)\)', lambda m: evaluate(m.group(1)), s)
    return evaluate(s)


total = sum(
    int(reduce(line))
    for line in sys.stdin.read().split("\n")
)
print(total)