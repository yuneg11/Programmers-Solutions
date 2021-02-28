def solution(l, w, ts):
    s = 0
    q = [(0, 0)]

    while len(ts) > 0 and (s := s + 1):
        if q[0][1] + l == s:
            w += q.pop(0)[0]
        if w >= ts[0]:
            q.append((ts[0], s))
            w -= ts.pop(0)
        else:
            s = l + q[0][1] - 1

    return s + l
