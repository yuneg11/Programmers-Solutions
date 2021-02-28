def solution(a, l=1):
    for v in a:
        n, m, k = max(l, v), min(l, v), l * v
        while (d := n % m):
            n, m = m, d
        l = k // m
    return l
