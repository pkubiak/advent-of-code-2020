import sys
from copy import copy 
def win(stack1, stack2):
    c1 = stack1[0]
    stack1 = stack1[1:]
    c2 = stack2[0]
    stack2 = stack2[1:]

    # print(stack1, stack2)

    if c1 <= len(stack1) and c2 <= len(stack2):
        return win_play(stack1[:c1], stack2[:c2])

    return c1 > c2

def win_play(cards1, cards2):
    cards1 = copy(cards1)
    cards2 = copy(cards2)
    # print('>>', cards1, cards2)
    cards1, cards2 = play(cards1,cards2)
    # print('--', cards1, cards2)
    return len(cards1) > len(cards2)
NEST = 0
def play(cards1, cards2):
    global NEST
    NEST += 1
    used = set()
    while len(cards1) and len(cards2):
        key = (tuple(cards1), tuple(cards2))
        if key in used:
            # print('Ending')
            return ['xxx'], []
        used.add(key)
        # print("\t"*NEST, cards1, cards2)
        if win(cards1, cards2):
            c1 = cards1[0]
            cards1 = cards1[1:]
            c2 = cards2[0]
            cards2 = cards2[1:]
            cards1.append(c1)
            cards1.append(c2)
        else:
            c1 = cards1[0]
            cards1 = cards1[1:]
            c2 = cards2[0]
            cards2 = cards2[1:]
            cards2.append(c2)
            cards2.append(c1)
    # print('DONE')
    NEST -= 1
    return cards1, cards2

p1, p2 = sys.stdin.read().split("\n\n")
cards1 = list(int(x) for x in p1.split("\n")[1:])
cards2 = list(int(x) for x in p2.split("\n")[1:])

cards1, cards2 = play(cards1, cards2)


print(cards1)
print(cards2)

print(sum(i*x for i, x in enumerate(cards1[::-1], start=1)))
print(sum(i*x for i, x in enumerate(cards2[::-1], start=1)))
