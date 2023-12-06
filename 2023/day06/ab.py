import re

def a(text: str):
    time, distance = text.split("\n")

    time = list(map(int, re.findall(r"\d+", time)))
    distance = list(map(int, re.findall(r"\d+", distance)))

    res = 1
    for t, d in zip(time, distance):
        res *= sum((t-i)*i > d for i in range(t+1))
    return res 


def b(text: str):
    return a(text.replace(" ", ""))


if __name__ == "__main__":
    for fn, val in [(a, 288), (b, 71503)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))