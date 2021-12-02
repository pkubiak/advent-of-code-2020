import sys

numbers = [int(x) for x in sys.stdin.read().split(',')]

state = {
    x: i
    for i, x in enumerate(numbers[:-1], start=1)
}

last = numbers[-1]

for turn in range(len(numbers), 30_000_000):
    age = turn - state.get(last, turn)

    state[last] = turn

    last = age

print(age)

