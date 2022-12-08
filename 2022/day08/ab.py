import numpy as np

def get_views(x, y):
    return [
        forest[y,x-1::-1], # left
        forest[y,x+1:], # right
        forest[y-1::-1,x], # up
        forest[y+1:,x] # down
    ]


def score(v, L):
    if np.all(L < v):
        return L.size
    return np.argmax(L >= v) + 1


def scenic_score(x, y):
    center = forest[y,x]
    return np.prod([
        score(center, view) 
        for view in get_views(x,y)
    ])


def is_visible(x, y):
    center = forest[y, x]
    for view in get_views(x, y):
        if np.all(center > view):
            return True
    return False


if __name__ == "__main__":
    text = open("input.txt").read().split("\n")
    forest = np.array([[int(i) for i in line] for line in text])
    H, W = forest.shape

    count = sum(is_visible(x, y) for x in range(W) for y in range(H))
    print("a:", count)

    best = max(scenic_score(x, y) for x in range(1,W-1) for y in range(1,H-1))
    print("b:", best)