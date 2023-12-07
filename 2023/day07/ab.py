from collections import Counter


def lower(a, b, symbols: str = "23456789TJQKA"):
    aa = Counter(a)
    bb = Counter(b)

    ak = list([i[1] for i in aa.most_common()])
    bk = list([i[1] for i in bb.most_common()])

    if ak != bk:
        return ak < bk
    
    for ai, bi in zip(a, b):
        if ai != bi:
            return symbols.index(ai) < symbols.index(bi)
    return False


def lower2(a, b, symbols: str = "J23456789TQKA"):
    aa = Counter(a.replace("J","") or "JJJJJ")
    aa = Counter(a.replace("J", aa.most_common()[0][0]))
    
    bb = Counter(b.replace("J","") or "JJJJJ")
    bb = Counter(b.replace("J", bb.most_common()[0][0]))

    ak = list([i[1] for i in aa.most_common()])
    bk = list([i[1] for i in bb.most_common()])

    if ak != bk:
        return ak < bk
    
    for ai, bi in zip(a, b):
        if ai != bi:
            return symbols.index(ai) < symbols.index(bi)
    return False


def solve(text: str, cmp_fn) -> int:
    lines = text.split("\n")
    cards = []
    for line in lines:
        a, b = line.split(" ")
        b = int(b)
        cards.append((a, b))

    # bubble sort
    for i in range(len(cards)):
        for j in range(len(cards)):
            if cmp_fn(cards[i][0], cards[j][0]):
                cards[i], cards[j] = cards[j], cards[i]

    return sum(card[1] * i for i, card in enumerate(cards, 1))


def a(text: str) -> int:
    return solve(text, lower)


def b(text: str) -> int:
    return solve(text, lower2)


if __name__ == "__main__":
    for fn, val in [(a, 6440), (b, 5905)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))