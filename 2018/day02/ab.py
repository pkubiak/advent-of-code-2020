from collections import Counter

with open("input.txt") as file:
    count2 = count3 = 0
    ids = []
    for line in file:
        ids.append(line.strip())
        c = Counter(line)
        if 2 in c.values():
            count2 += 1
        if 3 in c.values():
            count3 += 1
    print("a:", count2*count3)

    for i in range(len(ids)):
        for j in range(i, len(ids)):
            a, b = ids[i], ids[j]
            diff = [k for k in range(len(a)) if a[k]!=b[k]]
            if len(diff) == 1:
                x = diff[0]
                print("b:",a[:x] + a[x+1:])