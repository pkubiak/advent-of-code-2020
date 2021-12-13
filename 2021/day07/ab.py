with open('input.txt') as file:
    numbers = list(map(int, file.read().strip().split(',')))

numbers.sort()

print(numbers, len(numbers))

opt = numbers[len(numbers) // 2]

cost = sum(abs(x - opt) for x in numbers)
print(cost)

costs = []
for opt in range(min(numbers), max(numbers)+1):
    cost = sum(abs(x-opt)*(abs(x-opt)+1)//2 for x in numbers)
    costs.append(cost)

print(min(costs))