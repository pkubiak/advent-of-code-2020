import math

text = open("input.txt").read()

blizards = set()
lines = text.split("\n")
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in '><^v':
            blizards.add((x,y,c))
W, H = len(lines[0]), len(lines)
PERIOD = math.lcm(W-2, H-2)

DIRS = {'<': (-1, 0), '>': (1,0), '^': (0, -1), 'v': (0, 1), 'x': (0,0)}

def simulate(blizards):
    new = set()
    for x, y, dir in blizards:
        dx, dy = DIRS[dir]
        x2, y2 = x+dx, y+dy
        if x2 == 0:
            x2 = W-2
        if x2 == W-1:
            x2 = 1
        if y2 == 0:
            y2 = H-2
        if y2 == H-1:
            y2 = 1
        new.add((x2,y2,dir))
    return new

def BFS(blizards, target):
    queue = [(1, 0, 0, 0)]
    bests = {}
    bests[queue[-1]] = 0
    last_time = -1

    while queue:
        item, *queue = queue
        x, y, time, count = item
        # print(len(queue), count)

        if time != last_time:
            last_time = time
            blizards = simulate(blizards)
            cells = {(x,y) for x,y,_ in blizards}

        if (x,y,count) == target:
            return bests[item]

        new_count = count
        if (count%2 == 0) and (x, y)== (W-2, H-1):
            new_count += 1
        elif (count % 2 == 1) and (x,y) == (1,0):
            new_count += 1

        for dx, dy in DIRS.values():
            x2, y2 = x+dx, y+dy
            
            if (x2,y2)==(1,0) or (x2,y2) == (W-2, H-1) or ((1 <= x2 < W-1) and (1 <= y2 < H-1)):
                item2 = (x2, y2, (time+1), new_count)

                if ((x2, y2) not in cells) and (item2 not in bests):
                    queue.append(item2)
                    bests[item2] = bests[item]+1

print("a:", BFS(blizards, (W-2,H-1,0)))
print("b:", BFS(blizards, (W-2,H-1,2)))