def find(text, n):
    for i in range(len(text)):
        if len(set(text[i:i+n])) == n:
            return i+n

with open("input.txt") as file:
    text = file.read()
    print("a:", find(text, 4))
    print("b:", find(text, 14))
    