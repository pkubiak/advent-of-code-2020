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
    "abcdfg": 9,
}


def decode_digit(x, p):
    m = dict(zip(p, "abcdefg"))
    y = "".join(sorted([m[i] for i in x]))
    return MAPPING[y]


def get_mapping(a, b):
    good = []
    for p in permutations("abcdefg", 7):
        try:
            m = {"".join(sorted(x)): decode_digit(x, p) for x in a}
            good.append(m)
        except KeyError:
            continue

    assert len(good) == 1
    return good[0]


def decode(a, b):
    m = get_mapping(a, b)
    return "".join([str(m["".join(sorted(x))]) for x in b])


with open("input.txt") as file:
    N = ""
    suma = 0
    for line in file:
        a, b = line.strip().split(" | ")
        a = a.split(" ")
        b = b.split(" ")

        n = decode(a, b)
        suma += int(n)
        N += n

count = N.count("1") + N.count("4") + N.count("7") + N.count("8")
print(count, suma)
