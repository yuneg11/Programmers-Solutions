from collections import deque

def solution(n, e):
    g = [[] for _ in range(n + 1)]

    for a, b in e:
        g[a].append(b)
        g[b].append(a)

    d = [100000] * (n + 1)
    q = deque([(1, 0)])
    m, c = (0, 1)

    while q:
        v, f = q.popleft()
        if f < d[v]:
            d[v] = f
            m, c = (f, 1) if m < f else (f, c + 1) if m == f else (m, c)
            q.extend((x, f + 1) for x in g[v])

    return c
