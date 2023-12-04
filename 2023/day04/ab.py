import re

def a(text: str):
    res = 0
    for line in text.split("\n"):
        a, b = line.split(": ")
        b, c = b.split(" | ")
        b = [int(i) for i in re.findall(r"\d+", b)]
        c = [int(i) for i in re.findall(r"\d+", c)]
        ile = 0
        for i in c:
            if i in b:
                b.remove(i)
                ile += 1
        res += 2**(ile-1) if ile else 0
    return res


def b(text: str):
    lines = text.split("\n")
    counts = [1] * len(lines)

    for k, line in enumerate(lines):
        a, b = line.split(": ")
        b, c = b.split(" | ")
        b = [int(i) for i in re.findall(r"\d+", b)]
        c = [int(i) for i in re.findall(r"\d+", c)]
        ile = 0
        for i in c:
            if i in b:
                b.remove(i)
                ile += 1

        for m in range(ile):
            if k+m+1 < len(counts):
                counts[k+m+1] += counts[k]

    return sum(counts)

if __name__ == "__main__":
    assert a(open("test_a.txt").read()) == 13
    print("a:", a(open("input.txt").read()))

    assert b(open("test_b.txt").read()) == 30
    print("b:", b(open("input.txt").read()))  
