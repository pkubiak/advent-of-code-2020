import sys

data = []
def check(x):
    for a in range(25):
        for b in range(a+1, 25):
            if data[a] + data[b] == x:
                return True
    return False

x = 22477624

numbers = [int(line.strip()) for line in sys.stdin]

prefix = [0]
for n in numbers:
    prefix.append(prefix[-1] + n)


for a in range(len(prefix)):
    for b in range(a+1, len(prefix)):
        if prefix[b] - prefix[a] == x:
            print(a, b)
            c = min(numbers[a:b])
            d = max(numbers[a:b])
            print(sum(numbers[a:b]))
            print(c+d)
