def execute(code, input):
    variables = {}
    for line in code:
        op, *args = line.split(" ")
        if op == 'inp':
            variables[args[0]] = input[0]
            input = input[1:]
            continue
        val_a = variables.get(args[0], 0)
        value = variables.get(args[1], 0) if args[1].isalpha() else int(args[1])

        if op == 'add':
            variables[args[0]] = val_a + value
        if op == 'mul':
            variables[args[0]] = val_a * value
        if op == 'div':
            variables[args[0]] = int(val_a / value)
        if op == 'mod':
            variables[args[0]] = val_a % value
        if op == 'eql':
            variables[args[0]] = 1 if val_a == value else 0
    return variables



def solve(digits, limit=50000):
    results = {0: ()}
    for part in parts:
        # print(len(results), min(results), max(results))
        results = {k: results[k] for k in sorted(results)[:limit]}
        new_results = {}
        for digit in digits:
            for z_value in results:
                vars = execute(['inp z'] + part, [z_value, digit])
                # print(vars)/
                new_results[vars['z']] = results[z_value] + (digit,)
        results = new_results
    return "".join(map(str,results[0]))

if __name__ == '__main__':
    with open("input.txt") as file:
        parts = []
        for line in file:
            line = line.strip()
            if line == 'inp w':
                parts.append([])
            parts[-1].append(line)


    print("a:", solve([1,2,3,4,5,6,7,8,9]))
    print("b:", solve([9,8,7,6,5,4,3,2,1]))