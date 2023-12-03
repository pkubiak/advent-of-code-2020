# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
from collections import defaultdict

def a(text: str):
    total = 0
    t = text.strip().split("\n")

    d = defaultdict(lambda: ".")
    
    for y in range(len(t)):
        for x in range(len(t[y])):
            d[(x,y)] = t[y][x]
    def test(x, y):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                c = d[(x+dx, y+dy)]            
                if not ("0" <= c <= "9" or c == "."):
                    return True        
        return False
    parts = set()
    for y in range(len(t)):
        n = 0
        is_ok = False
        for x in range(len(t[y])):
            if '0' <= t[y][x] <= '9':
                is_ok = is_ok or test(x, y)
                n = 10*n + ord(t[y][x]) - ord('0')
            else:
                if is_ok:
                    total += n
                n = 0
                is_ok = False
                
        if is_ok:
            total += n

    return total

def b(text: str):
    total = 0
    t = text.strip().split("\n")

    d = defaultdict(lambda: ".")
    gears = defaultdict(list)

    for y in range(len(t)):
        for x in range(len(t[y])):
            d[(x,y)] = t[y][x]
    def test(x, y):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx!=0 or dy!=0:
                    yield (x+dx, y+dy)

    parts = set()
    for y in range(len(t)):
        n = 0
        is_ok = False
        positions = set()
        for x in range(len(t[y])):
            if '0' <= t[y][x] <= '9':
                positions.update(test(x,y))
                n = 10*n + ord(t[y][x]) - ord('0')
            else:
                for xx, yy in positions:
                    if d[(xx, yy)] == '*':
                        gears[(xx, yy)].append(n)

                n = 0
                positions = set()
                
        if positions:
            for xx, yy in positions:
                if d[(xx, yy)] == '*':
                    gears[(xx, yy)].append(n)

    total = 0
    for k, v in gears.items():
        if len(v) == 2:
            total += v[0] * v[1]
    return total

if __name__ == "__main__":
    for fn, val in [(a, 4361), (b, 467835)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))

# if __name__ == "__main__":
#     # assert a(open("testa.txt").read()) == 4361
#     # print("a:", a(open("input.txt").read()))

#     assert b(open("testb.txt").read()) == 467835
#     print("b:", b(open("input.txt").read()))  