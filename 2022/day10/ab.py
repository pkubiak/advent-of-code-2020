lines = open("input.txt").read().splitlines()
x = 1
out = []

for line in lines:
    match line.split():
        case ["noop"]:
            out.append(x)
        case ["addx", v]:
            out.extend([x,x])
            x += int(v)

total = 0
for i in range(20, len(out)+1, 40):
    total += out[i-1]*i
print("a:", total)    

print("b:")
for i in range(len(out)):
    if i%40 == 0:
        print()
    print('#' if abs(out[i] - i%40) <= 1 else ' ', end='')
