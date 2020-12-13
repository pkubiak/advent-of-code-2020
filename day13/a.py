import sys

lines = sys.stdin.read().split("\n")

t = int(lines[0])
buses = [
    int(x)
    for x in lines[1].split(',')
    if x != 'x'
]

bus_id = min(
    buses,
    key=lambda x: x * ((t+x-1)//x)
)


t2 = bus_id * ((t+bus_id-1)//bus_id)

print(bus_id * (t2-t))