import sys

numbers = set()
for line in sys.stdin.read().split():
    number = int(line)
    if 2020 - number in numbers:
        print(number * (2020 - number))
    numbers.add(number)
