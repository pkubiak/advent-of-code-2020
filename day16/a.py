import sys, re

fields, your_ticket, nearby_tickets = sys.stdin.read().split("\n\n")

ranges = set()
ranges.update(*[
    range(int(start), int(end) + 1)
    for start, end in re.findall(r'(\d+)-(\d+)', fields)
])

total = sum(
    int(number)
    for number in re.findall(r'\d+', nearby_tickets)
    if int(number) not in ranges
)

print(total)