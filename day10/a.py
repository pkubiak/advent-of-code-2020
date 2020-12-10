import sys

numbers = sorted(map(int, sys.stdin.read().split()))
print(numbers)
c = {0:0, 1:0, 2:0, 3:1}
for a, b in zip(numbers, numbers[1:]):
    c[b-a] += 1
c[numbers[0]] += 1
print(c)
print(c[1] * c[3])