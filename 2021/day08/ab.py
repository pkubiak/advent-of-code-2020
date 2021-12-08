from itertools import permutations

MAPPING = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

def digit(x, p):
    x = set(x)
    y = set()
    for z, v in zip("abcdefg", p):
        if v in x:
            y.add(z)
    return MAPPING.get(''.join(sorted(y)))

def detect(a, b):
    good = []
    for p in permutations('abcdefg', 7):
        m = {}
        for x in a:
            d = digit(x, p)
            if d is None:
                break
            m[''.join(sorted(x))] = d
        if len(m) == 10:                
            good.append(m)
    assert len(good) == 1
    
    m = good[0]
    return [m[''.join(sorted(x))] for x in b]

with open('input.txt') as file:
    N = []
    suma = 0
    for line in file:
        a, b = line.strip().split(" | ")
        a = a.split(" ")
        b = b.split(" ")

        n = detect(a, b)
        suma += int(''.join(map(str, n)))
        N.extend(n)

total = N.count(1) + N.count(4) + N.count(7) + N.count(8)
print(total, suma)