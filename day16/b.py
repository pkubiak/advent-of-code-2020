import sys, re, math
from copy import copy
fields, your_ticket, nearby_tickets = sys.stdin.read().split("\n\n")

your_ticket = list(int(x) for x in your_ticket.split("\n")[1].split(','))

def match(order, candidates):
    matching = {}
    results = []
    def rec(i):
        if i == len(candidates):
            results.append(copy(matching))
            return 

        for key in candidates[order[i]]:
            if key not in matching:
                matching[key] = order[i]
                rec(i+1)
                del matching[key]

    rec(0)
    return results

ranges = {}
for line in fields.split("\n"):
    m = re.fullmatch(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
    name, a0, a1, b0, b1 = m.groups()
    s = set()
    s.update(range(int(a0), int(a1)+1))
    s.update(range(int(b0), int(b1)+1))
    ranges[name] = s


valid_tickets = []


for ticket in nearby_tickets.split("\n")[1:]:
    ticket = list(int(x) for x in ticket.split(","))

    candidates = [
        {
            key
            for key in ranges
            if x in ranges[key]
        }
        for x in ticket
    ]

    is_valid = all(bool(field) for field in candidates)
    if is_valid:
        valid_tickets.append(candidates)
        # print(candidates)
        # break

field_candidates = [
    set.intersection(*[
        ticket[i]
        for ticket in valid_tickets
    ])

    for i in range(len(valid_tickets[0]))
]

order = sorted(range(len(field_candidates)), key=lambda x: len(field_candidates[x]))

matching = match(order, field_candidates)
assert len(matching) == 1
matching = matching[0]

total = math.prod(
    your_ticket[v]
    for k, v in matching.items()
    if k.startswith('departure')
)
print(total)