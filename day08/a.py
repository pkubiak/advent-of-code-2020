import sys

code = sys.stdin.read().split("\n")

acc = ip = 0

while True:
    if code[ip] is None:
        break

    op, arg = code[ip].split()
    code[ip] = None

    if op == 'jmp':
        ip += int(arg)
    if op == 'acc':
        acc += int(arg)
        ip += 1
    if op == 'nop':
        ip += 1
        
print(acc)