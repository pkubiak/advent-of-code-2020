import sys, re

fields, your_ticket, nearby_tickets = sys.stdin.read().split("\n\n")


ranges = set()
for line in fields.split("\n"):
    m = re.fullmatch(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
    _name, a0, a1, b0, b1 = m.groups()
    ranges.update(range(int(a0), int(a1)+1))
    ranges.update(range(int(b0), int(b1)+1))


total = 0
for ticket in nearby_tickets.split("\n")[1:]:
    numbers = map(int, ticket.split(","))
    total += sum(
        x
        for x in numbers
        if x not in ranges
    )

print(total)