from functools import reduce

solution = lambda s, t: sum([s.startswith("".join([v for v in b if v in s])) for b in t])
