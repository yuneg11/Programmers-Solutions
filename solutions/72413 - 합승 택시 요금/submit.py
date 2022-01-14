from itertools import product

def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1
    d = [[100000000] * n for _ in range(n)]
    for t, f, v in fares:
        d[t - 1][f - 1] = d[f - 1][t - 1] = v
    for t in range(n):
        d[t][t] = 0
    for k, i, j in product(range(n), repeat=3):
        if d[i][j] > (l := d[i][k] + d[k][j]):
            d[i][j] = l
    return min(d[s][k] + d[k][a] + d[k][b] for k in range(n))
