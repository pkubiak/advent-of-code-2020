import sys, re
import functools


rules, messages = sys.stdin.read().split("\n\n")

RULES = {}
for rule in rules.split("\n"):
    name, def_list = rule.split(": ")
    defs = [l.split(" ") for l in def_list.split(" | ")]
    RULES[name] = defs


RULES["8"] = [["42"] * i for i in range(1, 10)]
RULES["11"] = [["42"] * i + ["31"] * i for i in range(1, 10)]

@functools.cache
def build_regex(name):
    rules = []
    for clause in RULES[name]:
        regex = ""
        for term in clause:
            if term.startswith('"'):
                regex += term.strip('"')
            else:
                regex += build_regex(term)
        rules.append(regex)

    if len(rules) == 1 and len(rules[0]) == 1:
        return rules[0]

    return "(?:" + "|".join(rules) + ")"

regex = re.compile(build_regex('0'))
print(regex.pattern)

total = 0
for message in messages.split("\n"):
    total += bool(regex.fullmatch(message))
print(total)