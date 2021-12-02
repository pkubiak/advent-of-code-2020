import re, sys

PRODUCTS = []

for line in sys.stdin:
    ingredients, allergens = re.fullmatch(r'(.*) \((.*)\)', line.strip()).groups()
    ingredients = ingredients.split(' ')
    allergens = allergens.replace("contains ", "").split(", ")
    print(ingredients, allergens)
    PRODUCTS.append((set(ingredients), set(allergens)))

ALL_ALLERGENS = set.union(*[y for x, y in PRODUCTS])
print(ALL_ALLERGENS)
ALL_INGREDIENTS = set.union(*[x for x, y in PRODUCTS])

ALLERGENS = {ingredient: ALL_ALLERGENS for ingredient in ALL_INGREDIENTS}
print(ALLERGENS)
POSSIBLE_WITH_ALLERGENS = set()
for allergen in ALL_ALLERGENS:
    ss = set.intersection(*[i for i, a in PRODUCTS if allergen in a])
    POSSIBLE_WITH_ALLERGENS.update(ss)
    print(allergen, ss)

print(POSSIBLE_WITH_ALLERGENS)
NOT_POSSIBLE = ALL_INGREDIENTS - POSSIBLE_WITH_ALLERGENS
total = sum(
    len(s & NOT_POSSIBLE) for s, _ in PRODUCTS
)
print(total)

known = {}
while len(known) < len(ALL_ALLERGENS):
    for allergen in ALL_ALLERGENS:
        ss = set.intersection(*[i for i, a in PRODUCTS if allergen in a])
        ss -= set(known)
        if len(ss) == 1:
            known[ss.pop()] = allergen
print(known)

res = sorted(known.keys(), key=lambda x: known[x])
print(','.join(res))