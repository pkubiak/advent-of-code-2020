from copy import deepcopy

def a(text: str):
    lines = text.split("\n")
    bricks = []
    brick_ids = {}
    heights = {}
    
    for line in lines:
        start, end = line.split("~")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))
        bricks.append((start, end))

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))

    supporting_bricks = set()
    for bid, (start, end) in enumerate(bricks):
        if start[2] == end[2]:
            positions = []
            if start[0] == end[0]:
                a, b = sorted([start[1], end[1]])
                for i in range(a, b+1):
                    positions.append((start[0], i))
            elif start[1] == end[1]:
                a, b = sorted([start[0], end[0]])
                for i in range(a, b+1):
                    positions.append((i, start[1]))
            else:
                assert False

            elevations = [heights.get(p, 0) for p in positions]
            max_elevation = max(elevations)
            under_ids = set()
            for p in positions:
                brick_id = brick_ids.get(p, None)
                if brick_id is not None and heights[p] == max_elevation:
                    under_ids.add(brick_id)
                heights[p] = max_elevation +1
                brick_ids[p] = bid
            if len(under_ids) == 1:
                supporting_bricks.update(under_ids)
        else:
            elevation = heights.get((start[0], start[1]), 0)
            brick_id = brick_ids.get((start[0], start[1]), None)
            height = abs(start[2] - end[2])+1
            brick_ids[(start[0], start[1])] = bid

            if brick_id is not None:
                supporting_bricks.add(brick_id)
            heights[(start[0], start[1])] = elevation + height
        
    return len(bricks) - len(supporting_bricks)

def count_above(hierarchy, bid):
    fallen = {bid}
    while True:
        start = len(fallen)
        new_fallen = set()
        for i in hierarchy:
            if i not in fallen and len(hierarchy[i] - fallen) == 0:
                new_fallen.add(i)
        
        fallen.update(new_fallen)
        end = len(fallen)
        if start == end:
            break

    return len(fallen) - 1


def b(text: str):
    lines = text.split("\n")
    bricks = []
    brick_ids = {}
    heights = {}
    
    for line in lines:
        start, end = line.split("~")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))
        bricks.append((start, end))

    bricks.sort(key=lambda x: min(x[0][2], x[1][2]))
    supporting_bricks = set()

    from collections import defaultdict
    is_supporting = defaultdict(set)
    is_ling_on = defaultdict(set)

    for bid, (start, end) in enumerate(bricks):
        if start[2] == end[2]:
            positions = []
            if start[0] == end[0]:
                a, b = sorted([start[1], end[1]])
                for i in range(a, b+1):
                    positions.append((start[0], i))
            elif start[1] == end[1]:
                a, b = sorted([start[0], end[0]])
                for i in range(a, b+1):
                    positions.append((i, start[1]))
            else:
                assert False

            elevations = [heights.get(p, 0) for p in positions]
            max_elevation = max(elevations)
            under_ids = set()
            for p in positions:
                brick_id = brick_ids.get(p, None)
                if heights.get(p, 0) == max_elevation:
                    under_ids.add(brick_id)
                heights[p] = max_elevation +1
                brick_ids[p] = bid
            if len(under_ids) == 1:
                is_supporting[list(under_ids)[0]].add(bid)
                supporting_bricks.update(under_ids)
            is_ling_on[bid] = under_ids
        else:
            elevation = heights.get((start[0], start[1]), 0)
            brick_id = brick_ids.get((start[0], start[1]), None)
            height = abs(start[2] - end[2])+1
            brick_ids[(start[0], start[1])] = bid

            if brick_id is not None:
                supporting_bricks.add(brick_id)
                is_supporting[brick_id].add(bid)
            is_ling_on[bid] = {brick_id}
            heights[(start[0], start[1])] = elevation + height

    total = 0
    for i in is_ling_on:
        total += count_above(is_ling_on, i)
    return total


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", fn(open(test_fn).read()))

    test([
        ("test_a.txt", a, 5),
        ("input.txt", a, None),
        ("test_a.txt", b, 7),
        ("input.txt", b, None),
    ])
# 109518
    109531