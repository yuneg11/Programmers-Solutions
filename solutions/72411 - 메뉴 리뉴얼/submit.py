from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    d, m = defaultdict(int), defaultdict(lambda: 2)
    for order in orders:
        for n in [n for n in course if n <= len(order)]:
            for v in combinations(sorted(order), n):
                d[v], m[n] = d[v] + 1, d[v] + 1 if d[v] >= m[n] else m[n]
    return sorted(["".join(v) for v, c in d.items() if c == m[len(v)]])
