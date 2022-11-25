def minmax(iter):
    minv = maxv = next(iter)
    for i in iter:
        if i < minv:
            minv = i
        elif i > maxv:
            maxv = i
    return minv, maxv 


def calculate(image, algorithm, fill):
    minx, maxx = minmax(x for (x, y) in image)
    miny, maxy = minmax(y for (x, y) in image)
    output = {}
    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            bits = [
                (image.get((x+dx,y+dy), fill))
                for dy in [-1,0,1]
                for dx in [-1,0,1]
            ]
            i = int(''.join(bits), 2)
            
            output[(x,y)] = algorithm[i]
    return output

with open("input.txt") as file:
    lines = file.readlines()
    algorithm = lines[0].strip().replace('#','1').replace('.','0')
    assert len(algorithm) == 512

    image = {}
    for y, line in enumerate(lines[2:]):
        line = line.strip()
        for x, v in enumerate(line):
            image[(x, y)] = '1' if v == '#' else '0'

fill = '0'
for i in range(50):
    image = calculate(image, algorithm, fill)
    fill = algorithm[int(9*fill,2)]
    if i == 2:
        print("a:", list(image.values()).count('1'))
    
print("b:", list(image.values()).count('1'))