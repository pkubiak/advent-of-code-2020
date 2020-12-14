import sys, re, itertools

mask = None
mem = {}



for line in sys.stdin.read().split("\n"):
    if m := re.fullmatch("mask = ([X01]{36})", line):
        mask = m.group(1)
    else:
        m = re.fullmatch(r"mem\[(\d+)\] = (\d+)", line)
        addr, value = m.groups()
        addr = bin(int(addr))[2:].zfill(36)
        value = int(value)

        for bits in itertools.product('01', repeat=mask.count('X')):
            bits = list(bits)
            addr2 = ''.join([
                bits.pop() if m == 'X' else ('1' if m == '1' else a)
                for m, a in zip(mask, addr)
            ])
            addr2 = int(addr2, 2)
            mem[addr2] = value

        # res = ''.join([
        #     v if m == 'X' else m
        #     for m, v in zip(mask, value)
        # ])
        # mem[int(addr)] = int(res, 2)

print(sum(mem.values()))