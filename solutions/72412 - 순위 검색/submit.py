from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left

def solution(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]
