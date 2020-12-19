import sys, re


def evaluate(s) -> str:
    assert '(' not in s
    terms = re.split('([+*])', re.sub('\s', '', s))

    value = int(terms[0])
    for i in range(1, len(terms), 2):
        x = int(terms[i+1])
        if terms[i] == '+':
            value += x
        else:
            value *= x

    return str(value)


def reduce(expr):
    while '(' in expr:
        expr = re.sub(r'\(([^()]+)\)', lambda m: evaluate(m.group(1)), expr)

    return evaluate(expr)


total = sum(
    int(reduce(line))
    for line in sys.stdin.read().split("\n")
)
print(total)