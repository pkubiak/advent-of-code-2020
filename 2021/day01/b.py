with open("input.txt") as file:
    numbers = [int(v.strip()) for v in file]

triples = []
for a, b, c in zip(numbers, numbers[1:], numbers[2:]):
    triples.append(a + b + c)


count = 0
for a, b in zip(triples, triples[1:]):
    count += a < b

print(count)
