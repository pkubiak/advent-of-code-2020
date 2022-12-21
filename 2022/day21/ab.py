def calculate(values, key):
    match values[key]:
        case [a, op, b]:
            a = calculate(values, a)
            b = calculate(values, b)
            return eval(f"a {op} b")
        case x:
            return x


def check(value):
    values['humn'] = value
    return calculate(values, 'root')


values = {}
for line in open("input.txt"):
    a, b = line.strip().split(": ")
    if b.isnumeric():
        values[a] = int(b)
    else:
        values[a] = b.split(" ")

# part1
print("a:", int(calculate(values, 'root')))

# part2
values['root'][1] = '-'
a, b = 0, 10000000000000
assert (check(a) > 0) and (check(b) < 0)

while a+1 < b:
    s = (a+b)//2
    if check(s) >= 0:
        a = s
    else:
        b = s
print("b:", a)