def solution(clothes):
    ts = {}
    for _, t in clothes:
        if t not in ts:
            ts[t] = 1
        ts[t] += 1
    vs = 1
    for v in ts.values():
        vs *= v
    return vs - 1
