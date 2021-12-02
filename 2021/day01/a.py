with open("input.txt") as file:
    numbers = [int(v.strip()) for v in file]

count = 0
for a, b in zip(numbers, numbers[1:]):
    count += a < b

print(count)
