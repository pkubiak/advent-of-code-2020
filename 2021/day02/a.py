x, y = 0, 0

with open("input.txt") as file:
    for line in file:
        match line.split():
            case ["forward", n]:
                x += int(n)
            case ["down", n]:
                y += int(n)
            case ["up", n]:
                y -= int(n)
print(x * y)
