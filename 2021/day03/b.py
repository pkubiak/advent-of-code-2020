with open('input.txt') as file:
    records = [
        line.strip()
        for line in file
    ]

def reduce(records, crit, index):
    if len(records) == 1:
        return records[0]
    
    c_0 = sum(r[index] == '0' for r in records)
    c_1 = sum(r[index] == '1' for r in records)

    if crit == 'most':
        if c_1 >= c_0:
            v = '1'
        else: v = '0'
    if crit == 'least':
        if c_0 <= c_1 and (c_0 > 0):
            v = '0'
        elif c_1 > 0:
            v = '1'
        else: v = '0'

    return reduce([
        r for r in records if r[index] == v
    ], crit, index+1)


a = reduce(records, 'most', 0)
b = reduce(records, 'least', 0)
print(a, b)
print(int(a,2)*int(b,2))