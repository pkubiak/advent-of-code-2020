from tqdm import trange


def read_input(text: str):
    seeds, *maps = text.split("\n\n")

    mappings = []
    for m in maps:
        mapping = []
        lines = m.split("\n")
        for line in lines[1:]:
            a, b, r = map(int, line.strip().split(" "))
            mapping.append((a,b,r))
        mappings.append(mapping)

    seeds = list(map(int, seeds.replace("seeds: ", "").split(" ")))

    return seeds, mappings


def a(text: str):
    seeds, mappings = read_input(text)

    mins = 10e100
    def gv(seed):
        for m in mappings:
            for a, b, r in m:
                if b <= seed < b+r:
                    seed = a + (seed-b)
                    break
        return seed
    
    for seed in seeds:
        mins = min(mins, gv(seed))
    return mins


def b(text: str):
    seeds, mappings = read_input(text)

    mins = 10e100
    def gv(seed, l=0):
        for m in mappings[l:]:
            for a, b, r in m:
                if b <= seed < b+r:
                    seed = a + (seed-b)
                    break
        return seed
    
    def gvrev(seed, l=0):
        for i in list(range(l+1))[::-1]:
            m = mappings[i]
            for a, b, r in m:
                if a <= seed < a+r:
                    seed = b + (seed-a)
                    break
        return seed
        
    candidates = []
    for i, ms in enumerate(mappings):
        for a, b, r in ms:
            for x in [a, a+r-1]:
                revb = gvrev(x,i)
                forw = gv(x, i+1)
                assert gv(revb) == forw
                for j in range(0, len(seeds), 2):
                    if seeds[j] <= revb <= seeds[j] + seeds[j+1]:
                        candidates.append(revb)

    return (min(gv(i) for i in candidates))


if __name__ == "__main__":
    for fn, val in [(a, 35), (b, 46)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))
