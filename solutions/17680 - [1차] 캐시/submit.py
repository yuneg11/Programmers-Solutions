from functools import reduce

def solution(s, c, t=0, l=dict()):
    for i, v in enumerate(map(lambda x: x.lower(), c)):
        if v in l:
            t += 1
            l[v] = i
        else:
            if s:
                if len(l) == s:
                    del l[reduce(lambda m, n: min(m, n, key=lambda x: x[1]), l.items())[0]]
                l[v] = i
            t += 5    

    return t
