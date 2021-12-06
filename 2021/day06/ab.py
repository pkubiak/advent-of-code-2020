with open('input.txt') as file:
    numbers = [int(x) for x in file.read().split(',')]

counts = [numbers.count(i) for i in range(9)]

for i in range(257):
    if i in (80, 256):
        print(i, sum(counts))

    count0 = counts[0]
    counts = counts[1:]
    counts.append(count0)
    counts[6] += count0
