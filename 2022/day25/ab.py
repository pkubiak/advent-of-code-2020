text = open("input.txt").read()

VALUE = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
MODULS = {0: '0', 1:'1', 2:'2', 3: '=', 4: '-'}

def from_snauf(text):
    value = 0
    for i in text:
        value = 5*value + VALUE[i]
    return value

def to_snauf(number):
    if number == 0:
        return ''
    v = MODULS[number % 5]
    number -= VALUE[v]
    return to_snauf(number//5) + v

assert from_snauf('1121-1110-1=0') == 314159265  
assert to_snauf(314159265) == '1121-1110-1=0'

total = 0
for line in text.split("\n"):
    total += from_snauf(line)

print("a:", to_snauf(total))