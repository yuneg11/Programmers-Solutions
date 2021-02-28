def solution(a, m=1000000001, n=1000000001):
    l = [(m := min(m, v)) for v in a[:-1]]
    r = [(n := min(n, v)) for v in reversed(a[2:])]
    return sum((x > y or z > y for x, y, z in zip(l, a[1:-1], reversed(r)))) + 2
