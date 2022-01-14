from itertools import combinations

def solution(c, k=0, a=0):
    s = {k := k + v for v in [0] + c}
    for u, v in combinations(s, 2):
        if max(u, v) + (d := abs(v - u)) in s:
            a = max(a, d)
    return a
