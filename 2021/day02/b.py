x, y, aim = 0, 0, 0

with open("input.txt") as file:
    for line in file:
        match line.split():
            case ["forward", n]:
                x += int(n)
                y += int(n) * aim
            case ["down", n]:
                aim += int(n)
            case ["up", n]:
                aim -= int(n)

print(x * y)
