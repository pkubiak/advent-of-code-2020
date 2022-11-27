with open("input.txt") as file:
    grid = {
        (x, y): c
        for y, line in enumerate(file)
        for x, c in enumerate(line.strip())
    }
    w = max(grid,key=lambda x: x[0])[0] + 1
    h = max(grid,key=lambda x: x[1])[1] + 1

from collections import Counter

i = 0;
while True:
    i += 1
    # for y in range(h):
    #     print(''.join([grid[x,y] for x in range(w)]))

    grid2 = {}
    ile = 0
    ## Move Right
    for y in range(h):
        for x in range(w):
            if grid[x,y] == '>' and grid[(x+1)%w,y] == '.':
                grid2[x,y] = '.'
                ile += 1
            elif grid[x,y] == '.' and grid[(x-1)%w,y] == '>':
                grid2[x,y] = '>'
            else:
                grid2[x,y] = grid[x,y]
    grid = grid2.copy()
        
    ## Move Down
    for y in range(h):
        for x in range(w):
            if grid[x,y] == 'v' and grid[x,(y+1)%h] == '.':
                grid2[x,y] = '.'
                ile += 1
            elif grid[x,y] == '.' and grid[(x,(y-1)%h)] == 'v':
                grid2[x,y] = 'v'
            else:
                grid2[x,y] = grid[x,y]
    grid = grid2
    if ile == 0:
        print(i)
        break