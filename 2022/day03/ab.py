from string import ascii_letters

def priority(c):
    return ascii_letters.index(c) + 1

with open("input.txt") as file:
    score_a = score_b = 0
    lines = file.read().splitlines()

    for line in lines:
        pivot = len(line) // 2
        score_a += priority((set(line[:pivot]) & set(line[pivot:])).pop())

    for i in range(0, len(lines), 3):
        a, b, c = lines[i:i+3]
        
        score_b += priority((set(a) & set(b) & set(c)).pop())

    print("a:", score_a)
    print("b:", score_b)