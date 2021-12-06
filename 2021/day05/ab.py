from collections import Counter

counts = Counter()

with open('input.txt') as file:
    for line in file:
        p0, p1 = line.strip().split(' -> ')
        x0, y0 = map(int, p0.split(','))
        x1, y1 = map(int, p1.split(','))
        
        dx = 0 if x0 == x1 else (x1 - x0) // abs(x1-x0)
        dy = 0 if y0 == y1 else (y1 - y0) // abs(y1-y0)

        # if dx != 0 and dy != 0:
            # continue
        while True:
            counts[(x0, y0)] += 1
            if (x0, y0) == (x1, y1):
                break
            x0 += dx
            y0 += dy

print(sum(v > 1 for v in counts.values()))