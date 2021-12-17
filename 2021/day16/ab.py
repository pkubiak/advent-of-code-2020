from math import prod
from operator import gt, lt, eq


def parse(data):
    data = [bin(int(c, 16))[2:].zfill(4) for c in data]
    return "".join(data)


def read(n):
    global data
    bits, data = data[:n], data[n:]
    return bits


def read_package(init=None):
    global data
    if init:
        data = parse(init)

    version, type = int(read(3), 2), int(read(3), 2)

    if type == 4:
        output = []
        while True:
            p = read(5)
            output.append(p[1:])
            if p[0] == "0":
                break
        output = "".join(output)
        return (version, type, int(output, 2))

    length_type = read(1)
    if length_type == "0":
        length = int(read(15), 2)
        start_length = len(data)
        subpackages = []
        while start_length - len(data) < length:
            subpackages.append(read_package())
    else:
        count = int(read(11), 2)
        subpackages = [read_package() for _ in range(count)]
    return (version, type, subpackages)


def sum_version(p):
    version, type, content = p
    return version + (type != 4 and sum(map(sum_version, content)))


OPS = {0: sum, 1: prod, 2: min, 3: max, 5: gt, 6: lt, 7: eq}


def calculate(p):
    _, type, content = p
    if type == 4:
        return content

    content = [calculate(s) for s in content]
    if type in (0, 1, 2, 3):
        return OPS[type](content)
    return OPS[type](*content)


ASSERTIONS = {
    "C200B40A82": 3,
    "04005AC33890": 54,
    "880086C3E88112": 7,
    "CE00C43D881120": 9,
    "D8005AC2A8F0": 1,
    "F600BC2D8F": 0,
    "9C005AC2F8F0": 0,
    "9C0141080250320F1802104A08": 1,
}
for k, v in ASSERTIONS.items():
    assert calculate(read_package(k)) == v


with open("input.txt") as file:
    transmission = read_package(file.read().strip())
    print("a:", sum_version(transmission))
    print("b:", calculate(transmission))
