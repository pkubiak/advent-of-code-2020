matching = {
    "(": ")", "<": ">", "[": "]", "{": "}"
}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
closing = {"(": 1, "[": 2, "{": 3, "<": 4}

total = 0
all_scores = []
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        stack = []
        for c in line:
            if c in matching:
                stack.append(c)
            elif len(stack) and matching[stack[-1]] == c:
                stack.pop()
            else:
                total += scores[c]
                break
        else:
            score = 0
            for c in reversed(stack):
                score = 5*score + closing[c]
            all_scores.append(score)

    print("a:", total)
    all_scores.sort()
    print("b:", all_scores[len(all_scores)//2])