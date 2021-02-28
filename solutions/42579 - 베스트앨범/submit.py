from operator import itemgetter as get

def solution(gs, ps):
    c = {g: [] for g in set(gs)}
    for i, [g, p] in enumerate(zip(gs, ps)):
        c[g].append((-p, i))        
    return [i for l in sorted(c.values(), key=lambda l: sum(map(get(0), l)))
              for i in map(get(1), sorted(l)[:2])]
