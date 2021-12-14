with open("input.txt") as file:
    points, folds = file.read().split("\n\n")

    points = {
        tuple(map(int, line.split(","))) for line in points.split("\n")
    }

    folds = [line.split("=") for line in folds.split("\n")]


for i, (axis, value) in enumerate(folds):
    value = int(value)
    if 'x' in axis:
        points = {
            (2*value - x, y) if x >= value else (x, y)
            for x, y in points
        }
    else:
        points = {
            (x, 2*value - y) if y >= value else (x, y)
            for x, y in points
        }
    if i == 0: print("a:", len(points))

print("b:")
maxx = max(x for x, y in points)
maxy = max(y for x, y in points)
for y in range(0, maxy+1):
    for x in range(0, maxx+1):
        print("#" if (x,y) in points else " ", sep="", end="")
    print()
#AHPRPAUZ