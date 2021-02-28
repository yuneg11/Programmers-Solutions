from collections import defaultdict

def solution(a):
    d, p = defaultdict(int), [-1, -1, -1]

    for x, y, z in zip([a[0]] + a[:-1], a, a[1:] + [a[-1]]):
        if x != y and p[0] != y:
            d[y] += 1
            p[2] = -1
        elif y != z:
            d[y] += 1
            p[2] = y
        p[:2] = p[1:]

    return max(d.values()) * 2 if d.values() else 0
