from copy import deepcopy

def a(text: str):
    workflows_str, parts = text.split("\n\n")
    workflows = {}
    for line in workflows_str.split("\n"):
        name, rules = line.split("{", 1)
        rules_str = rules.strip("}").split(",")
        rules = []
        for rule in rules_str:
            rules.append(rule.split(":"))
        workflows[name] = rules

    def test_workflow(part, workflow) -> str:
        x, m, a, s = part["x"], part["m"], part["a"], part["s"]
        for rule in workflow:
            if len(rule) == 2:
                if eval(rule[0]) is True:
                    if rule[1] in ["A", "R"]:
                        return rule[1]
                    return test_workflow(part, workflows[rule[1]])
            else:
                if rule[0] in ["A", "R"]:
                    return rule[0]
                return test_workflow(part, workflows[rule[0]])


    first_workflow = "in" #list(workflows.keys())[0]
    total = 0
    for line in parts.split("\n"):
        line = "dict" + line.replace("{", "(").replace("}", ")")
        part = eval(line)
        result = test_workflow(part, workflows[first_workflow])
        if result == "A": 
            total += part["x"] + part["m"] + part["a"] + part["s"]

    return total


def b(text: str):
    workflows_str, parts = text.split("\n\n")
    workflows = {}
    for line in workflows_str.split("\n"):
        name, rules = line.split("{", 1)
        rules_str = rules.strip("}").split(",")
        rules = []
        for rule in rules_str:
            rules.append(rule.split(":"))
        workflows[name] = rules

    def split_by_test(ranges, rule):
        copy1, copy2 = deepcopy(ranges), deepcopy(ranges)

        name = rule[0]
        cond = rule[1]
        value = int(rule[2:])

        if cond == '<':
            if ranges[name][1] < value:
                return ranges, None
            if value <= ranges[name][0]:
                return None, ranges
            assert ranges[name][0] < value <= ranges[name][1]
            copy1[name][1] = value-1
            assert copy1[name][0] <= copy1[name][1]
            copy2[name][0] = value
            assert copy2[name][0] <= copy2[name][1], f"{name}:{value} {copy2} {ranges}"
            return copy1, copy2
        
        if cond == '>':
            if ranges[name][1] <= value:
                return None, ranges
            if value < ranges[name][0]:
                return ranges, None
            assert ranges[name][0] <= value < ranges[name][1]
            copy1[name][0] = value+1
            assert copy1[name][0] <= copy1[name][1]
            copy2[name][1] = value
            assert copy2[name][0] <= copy2[name][1]
            return copy1, copy2
        
        assert False

    def count_workflows(ranges, rule_name) -> int:
        if ranges is None:
            return 0
        if rule_name == "R":
            return 0
        
        if rule_name == "A":
            x = [(ranges[i][1] - ranges[i][0]+1) for i in 'xmas']
            return x[0]*x[1]*x[2]*x[3]
        
        total = 0
        for rule in workflows[rule_name]:
            if ranges is None:
                break
            if len(rule) == 2:
                match_range, ranges = split_by_test(ranges, rule[0])
                total += count_workflows(match_range, rule[1])
            if len(rule) == 1:
                total += count_workflows(ranges, rule[0])
        return total

    ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}

    return count_workflows(ranges, "in")

if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 19114),
        ("input.txt", a, None),
        ("test_a.txt", b, 167409079868000),
        ("input.txt", b, None),
    ])
