with open("input.txt") as file:
    board = {
        (x, y): int(v)
        for y, line in enumerate(file)
        for x, v in enumerate(line.strip())
    }

flashes = 0
for step in range(1, 1000):
    for k in board:
        board[k] += 1

    visited, ok = {}, True
    while ok:
        ok = False
        for k in board:
            if board[k] > 9 and k not in visited:
                visited[k] = True
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if (dx+k[0], dy+k[1]) in board:
                            board[dx+k[0], dy+k[1]] += 1
                ok = True

    for k in visited:
        board[k] = 0
    flashes += len(visited)

    if step == 100:
        print("a:", flashes)

    if len(visited) == len(board):
        print("b:", step)
        break    