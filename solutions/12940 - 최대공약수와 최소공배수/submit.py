def solution(n, m):
    k = n * m
    n, m = max(n, m), min(n, m)
    while (d := n % m):
        n, m = m, d
    return [m, k // m]
