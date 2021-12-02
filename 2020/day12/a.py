import sys

X, Y, DIR = 0, 0, 0

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def move(d, a):
    global X, Y
    a = DIRS[(a%360)//90]
    X += d * a[0]
    Y += d * a[1]


for line in sys.stdin.read().split():
    T, n = line[0], int(line[1:])
    if T == 'L':
        DIR -= n
    elif T == 'R':
        DIR += n
    elif T == 'F':
        move(n, DIR)
    else:
        move(n, 90 * 'ESWN'.index(T))


print(abs(X) + abs(Y))