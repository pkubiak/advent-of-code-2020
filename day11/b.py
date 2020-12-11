import sys
from copy import deepcopy




def check(A, x, y):
    W , H = len(A[0]), len(A)
    total = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy ==0:
                continue
            i = 1
            while 0 <= x+dx*i < W and 0<=y+dy*i <H:
                if A[i*dy+y][i*dx+x] == '#':
                    total += 1
                    break
                if A[i*dy+y][i*dx+x] == 'L':
                    break
                i += 1
    return total
                
def simulate(A):
    B = deepcopy(A)
    W , H = len(A[0]), len(A)
    for y in range(H):
        for x in range(W):
            if A[y][x] != '.':
                total = check(A, x, y)
                if A[y][x] == 'L' and total == 0:
                    B[y][x] = '#'
                elif A[y][x] == '#' and total >= 5:
                    B[y][x] = 'L'
                else:
                    B[y][x] = A[y][x]
    return B


seats = [list(line) for line in sys.stdin.read().split('\n')]

while True:
    n = simulate(seats)
    if n == seats:
        break
    seats = n
    # print('\n'.join([''.join(line) for line in seats]))
    # print()

print(''.join([''.join(line) for line in seats]).count('#'))