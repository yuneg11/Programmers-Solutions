from itertools import combinations

def solution(n, d=[False, False]+[True for _ in range(2, 49726)]):
    for i, v in ((i, v) for i, v in enumerate(d) if v):
        for j in range(i * 2, 49726, i):
            d[j] = False

    return sum([d[sum(v)] for v in combinations(n, 3)])
