from itertools import cycle

dice = cycle(range(1,101))

print([next(dice) for _ in range(110)])

positions = [2, 5]
scores = [0, 0]
player = rolls = 0

while True:
    positions[player] = (positions[player] + next(dice) + next(dice) + next(dice) - 1 )%10 + 1
    scores[player] += positions[player]
    rolls += 3

    if scores[player] >= 1000:
        break
    player = (player+1)%2

print("a:", rolls * min(scores))
