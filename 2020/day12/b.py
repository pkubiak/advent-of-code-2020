import sys

X, Y = 10, -1
Xs, Ys = 0, 0

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for line in sys.stdin.read().split():
    T, n = line[0], int(line[1:])

    if T in 'LR':
        d = ((-n if T == 'L' else n)%360)//90
        for _ in range(d):
            X, Y = -Y, X # rot90
    elif T == 'F':
        Xs += n * X
        Ys += n * Y
    else:
        d = DIRS['ESWN'.index(T)]
        X += n * d[0]
        Y += n * d[1]

print(abs(Xs) + abs(Ys))