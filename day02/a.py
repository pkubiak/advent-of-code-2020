import sys, re

policy = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')

total = 0
for line in sys.stdin:
    a, b, char, text = policy.fullmatch(line.strip()).groups()

    total += int(a) <= text.count(char) <= int(b)

print(total)