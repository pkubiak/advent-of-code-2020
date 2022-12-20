def compute(numbers, multiplier, iterations):
    numbers = [(i, multiplier * x) for i, x in enumerate(numbers)]
    numbers_orig = list(numbers)
    L = len(numbers)

    for _ in range(iterations):
        for num in numbers_orig:
            pos = numbers.index(num)

            numbers = numbers[:pos] + numbers[pos+1:]
            assert num not in numbers
            new_pos = pos + num[1]%(L-1)
            if new_pos >= L: new_pos = (new_pos%L) + 1

            numbers = numbers[:new_pos] + [num] + numbers[new_pos:]

    zeros = [i for i in range(L) if numbers[i][1] == 0]
    assert len(zeros) == 1
    z = zeros[0]

    return sum(numbers[(z+i)%L][1] for i in [1000, 2000, 3000])


text = open("input.txt").read()
numbers = list(map(int, text.split("\n")))

print("a:", compute(numbers, 1, 1))
print("b:", compute(numbers, 811589153, 10))