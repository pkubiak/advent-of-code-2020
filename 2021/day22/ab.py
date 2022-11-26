from itertools import product

# Load Data
items = []
with open("input.txt") as file:
    for line in file:
        op, rest = line.strip().split(" ")
        coords = [tuple(map(int, i.split("=")[1].split(".."))) for i in rest.split(",")]
        items.append(coords + [op])


def length_z(items, pool):
    events_z, length = [], 0
    for id in pool:
        events_z.append((items[id][2][0], 1, id))
        events_z.append((items[id][2][1]+1, -1, id))
    events_z.sort()
    pool = set()

    for i, (z, op, id) in enumerate(events_z):
        if i > 0 and pool:
            max_id = max(pool)
            length += (events_z[i][0] - events_z[i-1][0]) * (items[max_id][3] == "on")
        if op == 1:
            pool.add(id)
        else:
            pool.remove(id)
    return length


def area_yz(items, pool):
    events_y, area = [], 0
    for id in pool:
        events_y.append((items[id][1][0], 1, id))
        events_y.append((items[id][1][1]+1, -1, id))
    pool = set()
    events_y.sort()
    for i, (y, op, id) in enumerate(events_y):
        if i > 0:
            area += length_z(items, pool) * (events_y[i][0] - events_y[i-1][0])
        if op == 1:
            pool.add(id)
        else:
            pool.remove(id)
        
    return area


def volume_xyz(items):
    events_x, pool, volume = [], set(), 0
    for i, item in enumerate(items):
        events_x.append((item[0][0], 1, i))
        events_x.append((item[0][1]+1, -1, i))

    events_x.sort()
    for i, (x, op, id) in enumerate(events_x):
        if i > 0:
            volume += area_yz(items, pool) * (events_x[i][0] - events_x[i-1][0])
        if op == 1:
            pool.add(id)
        else:
            pool.remove(id)
    return volume

print(volume_xyz(items))