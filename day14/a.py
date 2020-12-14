import sys, re

mask = None
mem = {}

for line in sys.stdin.read().split("\n"):
    if m := re.fullmatch("mask = ([X01]{36})", line):
        mask = m.group(1)
    else:
        m = re.fullmatch(r"mem\[(\d+)\] = (\d+)", line)
        addr, value = m.groups()
        value = bin(int(value))[2:].zfill(36)

        res = ''.join([
            v if m == 'X' else m
            for m, v in zip(mask, value)
        ])
        mem[int(addr)] = int(res, 2)

print(sum(mem.values()))