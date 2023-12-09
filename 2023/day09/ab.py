def extr(nums):
    diffs = [v2 - v1 for v1, v2 in zip(nums, nums[1:])]
    if all(i == 0 for i in diffs):
        return nums[-1]
    return nums[-1] + extr(diffs)

def extr2(nums):
    diffs = [v2 - v1 for v1, v2 in zip(nums, nums[1:])]
    if all(i == 0 for i in diffs):
        return nums[0]
    return nums[0] - extr2(diffs)


def solve(text: str, fn)  -> int:
    total = 0
    for line in text.split("\n"):
        nums = [int(i) for i in line.split(" ")]
        n = fn(nums)
        total += n
    return total


def a(text: str) -> int:
    return solve(text, extr)    


def b(text: str) -> int:
    return solve(text, extr2)    


if __name__ == "__main__":
    for fn, val in [(a, 114), (b, 2)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))