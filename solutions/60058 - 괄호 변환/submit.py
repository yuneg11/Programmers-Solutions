from operator import lt, eq

def s(p, op, c=0, x="("):
    for i, c in ((i, (c := c - 1 + 2 * (v == x))) for i, v in enumerate(p)):
        if op(c, 0):
            break
    return p[:i+1], p[i+1:]

def solution(p, f="", b="", x="(", z=")"):
    while p:
        u, p = s(p, eq)
        if s(u, lt)[1]:
            b, u = z + "".join([z if v == x else x for v in u[1:-1]]) + b, x
        f += u
    return f + b
