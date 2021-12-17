from string import ascii_lowercase


def react(polymer):
    stack = []
    for c in polymer:
        stack.append(c)
        while (
            len(stack) >= 2
            and stack[-1].lower() == stack[-2].lower()
            and stack[-1] != stack[-2]
        ):
            stack.pop()
            stack.pop()
    return len(stack)


with open("input.txt") as file:
    polymer = file.read().strip()
print("a:", react(polymer))

min_length = min(
    react(polymer.replace(c, "").replace(c.upper(), "")) for c in ascii_lowercase
)
print("b:", min_length)
