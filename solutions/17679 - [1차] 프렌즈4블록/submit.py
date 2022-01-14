from pprint import pprint

def solution(m, n, b, c1=0, c2=0):
    b = [[[v, True] for v in reversed(r)] for r in zip(*b)]

    while (c1 := c2) != (c2 := sum(len(r) for r in b)):
        for r1, r2 in zip(b[:-1], b[1:]):
            for e1, e2, e3, e4 in zip(r1[:-1], r1[1:], r2[:-1], r2[1:]):
                if e1[0] == e2[0] == e3[0] == e4[0]:
                    e1[1] = e2[1] = e3[1] = e4[1] = False

        b = [list(filter(lambda x: x[1], r)) for r in b]

    return m * n - c2
