def load_cubes(path):
    """Load data"""
    cubes = []
    with open(path) as file:
        for line in file:
            op, rest = line.strip().split(" ")
            coords = [tuple(map(int, i.split("=")[1].split(".."))) for i in rest.split(",")]
            cubes.append(coords + [op])

    return cubes


def recursive_sweep(cubes, ids, dim, fn):
    """Recursive Sweeping over consecutive dimensions"""

    events, result = [], 0

    for id in ids:
        events.append((cubes[id][dim][0], 1, id)) # event start
        events.append((cubes[id][dim][1]+1, -1, id)) # event end
    ids = set()

    events.sort()
    for i, (pos, op, id) in enumerate(events):
        if i > 0 and ids:
            result += (recursive_sweep(cubes, ids, dim-1, fn) if dim else fn(cubes, ids)) * (pos - events[i-1][0])
        (ids.add if op==1 else ids.remove)(id)

    return result


def filter_cubes(cubes):
    """Cut cubes to -50..50 box"""
    for *coords, op in cubes:
        coords = [
            (max(dim[0], -50), min(dim[1], 50))
            for dim in coords
        ]
        if all(dim[0]<=dim[1] for dim in coords):
            yield coords + [op]


def part_a(cubes):
    filtered_cubes = list(filter_cubes(cubes))
    return part_b(filtered_cubes)

def part_b(cubes):    
    def fn(items, ids):
        return items[max(ids)][3] == 'on'
    return recursive_sweep(cubes, range(len(cubes)), 2, fn)


if __name__ == '__main__':
    cubes = load_cubes("input.txt")
    print("a:", part_a(cubes))
    print("b:", part_b(cubes))