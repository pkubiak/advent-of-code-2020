import sys

numbers = sorted(map(int, sys.stdin.read().split()))

c = [0, 0, 0, 1]
c[numbers[0]] += 1

for a, b in zip(numbers, numbers[1:]):
    c[b-a] += 1

print(c[1] * c[3])