import re


def simulate(stars, epoch):
    stars = {
        (x0+dx*epoch, y0+dy*epoch)
        for x0, y0, dx, dy in stars
    }

    minx = min(x for x, y in stars)
    maxx = max(x for x, y in stars)
    miny = min(y for x, y in stars)
    maxy = max(y for x, y in stars)

    # print(maxx - minx, maxy - miny)
    if maxx-minx > 100 or maxy-miny > 100:
        return False
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print('#' if (x,y) in stars else ' ', sep="", end="")
        print()
    return True

with open("input.txt") as file:
    stars = [
        tuple(map(int, re.findall("[-0-9]+", line)))
        for line in file
    ]

epoch = 0
while not simulate(stars, epoch):
    epoch += 1

for i in range(10):
    print(f"\n{epoch}")
    simulate(stars, epoch)
    epoch += 1