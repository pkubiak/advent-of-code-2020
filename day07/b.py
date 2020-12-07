import sys, re, functools

G = dict()

for line in sys.stdin.read().split("\n"):
    m = re.fullmatch("(.*) bags contain (.*)\.", line, re.DOTALL)
    name, contains = m.groups()
    G[name] = re.findall('(\d+) (.*?) bag[s]?', contains)


@functools.cache
def count(v: str) -> int:
    return 1 + sum(
        int(t) * count(bag)
        for t, bag in G.get(v, [])
    )

total = count('shiny gold') - 1
print(total)