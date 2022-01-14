def solution(n, w):
    s = set([w[0]])
    for i, v in enumerate(w[1:], start=2):
        if w[i - 2][-1] != v[0] or v in s:
            return [i % n or n, i // n + (i % n > 0)]
        else:
            s.add(v)
    return [0, 0]
