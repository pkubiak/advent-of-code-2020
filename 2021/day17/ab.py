# with open("input.txt") as file:
# target area: x=257..286, y=-101..-57


def test(sx, sy):
    x, y = 0, 0
    maxy = 0

    while y > -102:
        x += sx
        y += sy
        maxy = max(maxy, y)
        sy -= 1
        if sx > 0:
            sx -= 1
        elif sx < 0:
            sx += 1

        if (257 <= x <= 286) and (-101 <= y <= -57):
            return maxy
        # if (20 <= x <= 30) and (-10 <= y <= -5):
        
best = 0
count = 0
for sx in range(1, 300):
    for sy in range(-110, 400):
        res = test(sx, sy)
        if res is not None:
            count += 1
            if res > best:
                best = res
    
print("a:", best)
print("b:", count)