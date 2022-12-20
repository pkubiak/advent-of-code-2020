import re

def can_build(minerals, costs):
    return all(minerals[j] >= costs[j] for j in range(4))

def get_candidates(item, blueprint):
    robots, minerals = item[:4], item[4:]
    count = 0
    for i in [3,2,1,0]:
        schemat = blueprint[i]
        if can_build(minerals, schemat):
            count += 1
            yield tuple(robots[j] + (i == j) for j in range(4)), tuple(minerals[j] + robots[j] - schemat[j] for j in range(4))
            if i == 3: return
    
    if count < 3:
        yield robots, tuple(minerals[j] + robots[j] for j in range(4))

def simulate(candidates, blueprint):
    new_candidates = set()

    for c in candidates:
        for cc in get_candidates(c, blueprint):
            can = cc[0] + cc[1]
            new_candidates.add(can)

    for col in range(8):
        bests = {}
        for c in new_candidates:
            c2 = list(c)
            c2[col] = None
            c2 = tuple(c2)
            if c2 not in bests or bests[c2] < c:
                bests[c2] = c
        new_candidates = set(bests.values())

    return new_candidates

def main_simulation(time, blueprint):
    candidates = {(1,0,0,0,0,0,0,0)}
    for t in range(time):
        candidates = simulate(candidates, blueprint)

        best_min = max(c[7] + c[3] * (time-t-1) for c in candidates)

        for c in list(candidates):
            v = time-t-1
            best_max = c[7] + c[3]*v + v*(v-1)//2 # najlepszy możliwy wynik przy założeniu że budujemy w każdej iteracji
            if best_max < best_min:
                candidates.discard(c)

    return max(c[7] for c in candidates)


text = open("input.txt").read()

BLUEPRINTS = []
for item in text.split("\n"):
    costs = []
    ns = list(map(int, re.findall(r"\d+", item)))
    costs = [[ns[1], 0, 0, 0], [ns[2], 0, 0, 0], [ns[3], ns[4], 0, 0], [ns[5], 0, ns[6], 0]]
    BLUEPRINTS.append(costs)


score = 0
for i, bp in enumerate(BLUEPRINTS, start=1):
    score += i * main_simulation(24, bp)
print("a:", score)

score = 1
for i, bp in enumerate(BLUEPRINTS[:3], start=1):
    score *= main_simulation(32, bp)
print("b:", score)