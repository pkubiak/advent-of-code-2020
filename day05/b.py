import sys

def get_id(ticket):
    row, col = ticket[:7], ticket[7:]

    row = row.replace('F', '0').replace('B', '1')
    col = col.replace('L', '0').replace('R', '1')

    return 8 * int(row, 2) + int(col, 2)

assert get_id('BFFFBBFRRR') == 567

all_ids = set(map(get_id, sys.stdin.read().split()))

ticket = set(range(min(all_ids), max(all_ids)+1)) - all_ids
print(ticket.pop())