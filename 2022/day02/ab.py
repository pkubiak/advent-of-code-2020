POINTS = {
    "Rock": 1, "Paper": 2, "Scissors": 3,
    "Win": 6, "Draw": 3, "Lose": 0
}

WINS = {("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock")}

def part_a(a, b) -> int:
    a = {"A": "Rock", "B": "Paper", "C": "Scissors"}[a]
    b = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}[b]

    return POINTS[b] + POINTS["Draw" if a == b else (a, b) in WINS and "Win" or "Lose"]


def part_b(a, b) -> int:
    a = {"A": "Rock", "B": "Paper", "C": "Scissors"}[a]
    b = {"X": "Lose", "Y": "Draw", "Z": "Win"}[b]

    win = [y for x, y in WINS if a == x][0]
    lose = [x for x, y in WINS if a == y][0]
    b2 = a if b == "Draw" else win if b == "Win" else lose
    return POINTS[b2] + POINTS[b]


if __name__ == "__main__":
    total_a = total_b = 0
    
    with open("input.txt") as file:
        for line in file:
            a, b = line.strip().split(" ")

            total_a += part_a(a, b)
            total_b += part_b(a, b)

    print("a:", total_a)
    print("b:", total_b)
