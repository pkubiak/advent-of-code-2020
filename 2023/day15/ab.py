def hash2(text):
    r = 0
    for i in text:
        r = 17 * (r + ord(i))
        r %= 256
        # print(r, ord(i))
    return r
assert hash2('HASH') == 52


def a(text: str):
    steps = text.split(",")
    total = 0
    for step in steps:
        total += hash2(step)
    return total


def b(text: str):
    steps = text.split(",")
    boxes = [[]] * 256
    for step in steps:
        if step.endswith("-"):
            step = step.strip("-")
            box_id = hash2(step)
            box = [i for i in boxes[box_id] if i[0]!=step]
        else:
            label, b = step.split("=")
            focal = int(b)
            box_id = hash2(label)
            if any(i[0] == label for i in boxes[box_id]):
                box = [(i[0], focal) if i[0] == label else i for i in boxes[box_id]]
            else:
                box =  boxes[box_id] + [(label, focal)]
        boxes[box_id] = box
    
    total = 0
    for i, box in enumerate(boxes, start=1):
        for j, slot in enumerate(box, start=1):
            total += i*j*slot[1]
            # print(slot[0], i,j,slot[1], i*j*slot[1])
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
        ("test_a.txt", a, 1320),
        ("input.txt", a, None),
        ("test_a.txt", b, 145),
        ("input.txt", b, None),
    ])
