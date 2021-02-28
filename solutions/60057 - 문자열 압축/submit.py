def solution(s):
    m = n = len(s)

    for w, t, l, a in ((w, s[:w], 0, 1) for w in range(1, n // 2 + 1)):
        for c in (s[i: i + w] for i in range(w, n + w, w)):
            t, l, a = (c, l, a + 1) if c == t else (c, l + len(t) + len(str(a)) * (a > 1), 1)
        m = min(m, l)

    return m
