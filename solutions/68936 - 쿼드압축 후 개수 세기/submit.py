def solution(a):
    k = len(a) // 2
    b = [[r[:k] for r in a[:k]], [r[k:] for r in a[:k]],
         [r[:k] for r in a[k:]], [r[k:] for r in a[k:]]]
    s = [sum([sum(r) for r in c]) for c in b]
    e = [(1, 0) if d == 0 else (0, 1) if d == k * k else solution(c) for c, d in zip(b, s)]
    z, o = [sum(k) for k in zip(*e)]
    return [int(z > 0), int(o > 0)] if o == 0 or z == 0 else [z, o]
