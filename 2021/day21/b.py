from itertools import product
from collections import Counter
from functools import cache

MAX=21
counts = Counter(sum(i) for i in product([1,2,3], repeat=3))

@cache
def count(pos_this, score_this, pos_other, score_other) -> int:
    win_this, win_other = 0, 0
    for k, v in counts.items():
        pos = (pos_this + k - 1)%10 + 1
        if score_this + pos >= MAX:
            win_this += v
        else:
            _win_other, _win_this = count(pos_other, score_other, pos, score_this+pos)
            win_this += v*_win_this
            win_other += v*_win_other
    return [win_this, win_other]

assert max(count(4, 0, 8, 0)) == 444356092776315

print(max(count(2, 0, 5, 0)))