import sys, math


def egcd(a, b):
    """Extended Euclidean algorithm"""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y



def crt(eqs):
    """Chinese remainder theorem"""
    M = math.prod([n for n, _ in eqs])

    total = 0
    for n, y in eqs:
        Mi = M // n
        _, _, g = egcd(n, Mi)
        total += y * g * Mi

    return total % M


_, line = sys.stdin.read().split("\n")

print(crt([
    (int(x), (-i)% int(x))
    for i, x in enumerate(line.split(','))
    if x != 'x'
]))