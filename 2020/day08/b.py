import sys

code = sys.stdin.read().split("\n")

OPS = {
    False: lambda a,b: a+1,
    True: lambda a,b: a+int(b)
}

def visit(acc, ip, fixed, visited):
    if ip in visited:
        return False
    if ip == len(code):
        return acc
    if ip > len(code):
        return False

    op, arg = code[ip].split()
    visited = visited | {ip}

    if op == 'acc':
        return visit(acc + int(arg), ip+1, fixed, visited)

    val = visit(acc, OPS[op=='jmp'](ip, arg), fixed, visited)

    if not val and not fixed:
        val = visit(acc, OPS[op!='jmp'](ip, arg), True, visited)
    
    return val


print(visit(0, 0, False, set()))