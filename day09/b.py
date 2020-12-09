import sys
from itertools import combinations, accumulate

x = 22477624

numbers = [int(line.strip()) for line in sys.stdin]

prefsum = list(accumulate([0] + numbers))

for i, j in combinations(range(len(prefsum)), 2):
    if prefsum[j] - prefsum[i] == x and j - i > 1:
        minv = min(numbers[i:j])
        maxv = max(numbers[i:j])
        
        print(minv + maxv)
