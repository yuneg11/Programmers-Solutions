def solution(p, l, c=1):
    p = [[v, i] for i, v in enumerate(p)]

    while True:
        if max(p)[0] == (v := p.pop(0))[0]:
            if v[1] == l:
                return c
            c += 1
        else:
            p.append(v)
