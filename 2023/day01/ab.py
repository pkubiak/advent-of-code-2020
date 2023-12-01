import re

def a(text: str) -> int:
    total = 0
    for line in text.split("\n"):
        nums = re.findall(r"\d", line)
        total += int(nums[0] + nums[-1])
    return total


def b(text: str) -> int:
    total = 0
    nums = "one, two, three, four, five, six, seven, eight, nine".split(", ")
    nums = {k: i for i, k in enumerate(nums, start=1)} | {k: i for i, k in enumerate("123456789", start=1)}

    for line in text.split("\n"):
        poss = []
        for k, v in nums.items():
            if k not in line:
                continue
            poss.append((line.find(k), v))
            poss.append((line.rfind(k), v))
        
        poss.sort()
        total += 10 * poss[0][1] + poss[-1][1]

    return total


if __name__ == "__main__":
    for fn, val in [(a, 142), (b, 281)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))
