import sys, re, functools

G = dict()

for line in sys.stdin.read().split("\n"):
    m = re.fullmatch("(.*) bags contain (.*)\.", line, re.DOTALL)
    name, contains = m.groups()
    G[name] = re.findall('\d+ (.*?) bag[s]?', contains)


@functools.cache
def visit(v: str) -> bool:
    if v == 'shiny gold':
        return True
    for bag in G.get(v, []):
        if visit(bag):
            return True
    return False

total = sum(
    visit(v)
    for v in G
    if v != 'shiny gold'
)
print(total)