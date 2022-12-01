from itertools import product, permutations
from collections import Counter

def load_scanners(path):
    with open(path) as file:
        scanners = file.read().split("\n\n")
        scanners = [scanner.split("\n") for scanner in scanners]
        scanners = [[tuple(map(int, coords.split(","))) for coords in scanner[1:]] for scanner in scanners]
    return scanners


def sub(i, j):
    return (i[0]-j[0], i[1]-j[1], i[2]-j[2])


def diffset(points):
    results = {}
    for i, ei in enumerate(points):
        for j, ej in enumerate(points):
            if i != j:
                d = sub(ei, ej)
                results[d] = (i, j)
    
    return results


def calculate(scannrs):
    used = {0}

    points = list(set(scanners[0]))

    orientations = list(product([-1, 1], repeat=3))
    axis_rotations = list(permutations([0,1,2]))

    centers = []

    while len(used) < len(scanners):
        base = diffset(points)
        not_used = set(range(len(scanners))) - used

        for s in not_used:
            for orientation, axis in product(orientations, axis_rotations):
                transform = [
                    tuple(coords[axis[i]]*orientation[i] for i in range(3))
                    for coords in scanners[s]
                ]
                diff = diffset(transform)
                common = diff.keys() & base.keys()

                if len(common) > 100:
                    most = Counter()
                    for key in common:
                        for a, b in product([0,1], repeat=2):
                            most[sub(points[base[key][a]], transform[diff[key][b]])] += 1

                    if most.most_common()[0][1] > 100:
                        offset = most.most_common()[0][0]
                        centers.append(offset)
                        new_points = [(i[0]+offset[0], i[1]+offset[1], i[2]+offset[2]) for i in transform]
                        print(f"Mergin with {s}")#, len(set(points) & set(new_points)))
                        points = list(set(points) | set(new_points))
                        used.add(s)
                        break
            else:
                continue
            break
    return points, centers

if __name__ == '__main__':
    scanners = load_scanners("input.txt")
    points, centers = calculate(scanners)
    print("a:",len(points))


    best = 0
    for a, b in product(centers, repeat=2):
        diff = sub(a, b)
        dist = abs(diff[0]) + abs(diff[1]) + abs(diff[2])
        best = max(best, dist)
    print("b:", best)