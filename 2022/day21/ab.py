text = open("input.txt").read()

values, operations = {}, {}

for line in text.split("\n"):
    a, b = line.split(": ")
    if b.isnumeric():
        values[a] = int(b)
    else:
        operations[a] = b.split(" ")

def calculate(values, operations):
    values = dict(values)
    operations = dict(operations)
        
    while operations:
        for k in list(operations):
            b, op, c = operations[k]
            if b in values and c in values:
                values[k] = eval(f"{values[b]} {op} {values[c]}")
                del operations[k]
                if k == 'root':
                    return values[k]

def check(value):
    values['humn'] = value
    return calculate(values, operations)

# part1
print("a:", int(calculate(values, operations)))

# part2
operations['root'][1] = '-'
a, b = 0, 10000000000000
assert (check(a) > 0) and (check(b) < 0)

while a+1 < b:
    s = (a+b)//2
    if check(s) >= 0:
        a = s
    else:
        b = s
print("b:", a)