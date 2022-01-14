def solution(n, p=[], c=0):
    if c == n:
        return 1
    a = [True for _ in range(n)]
    for i, v in enumerate(p[:c]):
        a[v] = False
        if (k := v - abs(c - i)) >= 0:
            a[k] = False
        if (k := v + abs(c - i)) < n:
            a[k] = False

    return sum(solution(n, p[:c] + [i], c+1) for i, v in enumerate(a) if v)
