import sys

numbers = [
    int(number)
    for number in sys.stdin.read().split()
]

for i in range(len(numbers)):
    used = set()
    for j in range(i+1, len(numbers))[::-1]:
        k = 2020 - numbers[i] - numbers[j]
        if k in used:
            print(numbers[i] * numbers[j] * k)
        used.add(numbers[j])
