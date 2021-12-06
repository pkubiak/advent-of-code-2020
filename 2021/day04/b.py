import re

numbers, *boards = open("input.txt").read().split("\n\n")

numbers = {x: i for i, x in enumerate(numbers.split(","))}

boards = [
    [re.split("\s+", line.strip()) for line in board.split("\n")] for board in boards
]

# Find wining board
best = (0, None)
for i, board in enumerate(boards):
    times = []
    for y in range(5):
        v = max(numbers[board[y][x]] for x in range(5))
        times.append(v)
        v = max(numbers[board[x][y]] for x in range(5))
        times.append(v)
    best = max(best, (min(times), board))

# Find unmarked numbers
n, board = best
unmarked = sum(sum(int(x) for x in row if numbers[x] > n) for row in board)
called = [int(x) for x in numbers if numbers[x] == n][0]
print(unmarked * called)
