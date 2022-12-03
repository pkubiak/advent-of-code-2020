def priority(c):
    return ord(c) - ord('a') + 1 if 'a'<=c<='z' else ord(c) - ord('A') + 27


with open("input.txt") as file:
    score_a = score_b = 0
    lines = [line.strip() for line in file]

    for line in lines:
        pivot = len(line) // 2
        score_a += priority((set(line[:pivot]) & set(line[pivot:])).pop())

    for i in range(0, len(lines), 3):
        a, b, c = lines[i:i+3]
        
        score_b += priority((set(a) & set(b) & set(c)).pop())

    print("a:", score_a)
    print("b:", score_b)