import sys, functools

numbers = set(map(int, sys.stdin.read().split())) | {0}

T = max(numbers) + 3

@functools.cache
def count(n):
    if n == T:
        return 1
    if n not in numbers:
        return 0
    return sum(count(n+d) for d in [1,2,3])

print(count(0))