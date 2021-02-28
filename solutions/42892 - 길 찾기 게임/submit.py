import sys
sys.setrecursionlimit(1007)

def tree(n):
    v = max(n, key=lambda v: v[1])
    i = n.index(v)
    return [tree(l) if (l := n[:i]) else 0, v[2], tree(r) if (r := n[i + 1:]) else 0]

def trav(t, p):
    l = trav(t[0], p) if t[0] else []
    r = trav(t[2], p) if t[2] else []
    return [t[1], *l, *r] if p else [*l, *r, t[1]]

def solution(n):
    t = tree(sorted([(*v, i + 1) for i, v in enumerate(n)]))
    return [trav(t, 1), trav(t, 0)]
