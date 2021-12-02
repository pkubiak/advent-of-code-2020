import sys, re

policy = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')

total = 0
for line in sys.stdin:
    a, b, char, text = policy.fullmatch(line.strip()).groups()

    total += (text[int(a)-1] == char) ^ (text[int(b)-1] == char)

print(total)