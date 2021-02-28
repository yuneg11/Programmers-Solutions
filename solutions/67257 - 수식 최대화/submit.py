from itertools import permutations
from operator import add, mul, sub

op = {"*": mul, "+": add, "-": sub}

def solution(e, m=0):
    ex, tmp = [], ""
    for v in e:
        if v in "*+-":
            ex.extend([int(tmp), v])
            tmp = ""
        else:
            tmp += v
    ex.append(int(tmp))

    for ops in permutations("*+-"):
        e, s = ex, []
        for o in ops:
            i = 0
            while i < len(e):
                if e[i] == o:
                    s.append(op[e[i]](s.pop(), e[i+1]))
                    i += 1
                else:
                    s.append(e[i])
                i += 1
            e, s = s, []
        m = max(abs(e[0]), m)

    return m
