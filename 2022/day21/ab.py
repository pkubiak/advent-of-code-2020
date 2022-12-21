import re
text = open("input.txt").read()

text = re.sub(r"\b([a-z]{4})\b", r"\1()", text)
text = re.sub("([a-z]{4})\(\):", r"\1=lambda:", text)
exec(text)

print("a:", int(root()))

exec(re.sub('[-+*/]', '-', re.findall("root=.*", text)[0]))

a, b = 0, 10000000000000

while a+1 < b:
    s = (a+b)//2
    exec(f"humn = lambda: {s}")
    if root() >= 0:
        a = s
    else:
        b = s
print("b:", a)