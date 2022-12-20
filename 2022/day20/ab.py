from tqdm import tqdm

def compute(numbers, multiplier, iterations):
    numbers = [(i, multiplier * x) for i, x in enumerate(numbers)]
    numbers_orig = list(numbers)
    L = len(numbers)

    for _ in range(iterations):
        for num in tqdm(numbers_orig):
            if num == 0: continue

            pos = numbers.index(num)
            num = num[1] % (L-1)
            dir = -1 if num < 0 else 1

            for i in range(abs(num)):
                numbers[pos], numbers[(pos+dir)%L] = numbers[(pos+dir)%L], numbers[pos]
                pos = (pos + dir) % L

    zeros = [i for i in range(L) if numbers[i][1] == 0]
    assert len(zeros) == 1
    z = zeros[0]
    
    return sum(numbers[(z+i)%L][1] for i in [1000, 2000, 3000])


text = open("input.txt").read()
numbers = list(map(int, text.split("\n")))

print("a:", compute(numbers, 1, 1))
print("b:", compute(numbers, 811589153, 10))