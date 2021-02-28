def solution(p, l):
    p.sort()
    c, i, j = 0, 0, len(p) - 1

    while i <= j:
        c, i, j = c + 1, i + (p[i] + p[j] <= l), j - 1

    return c
