from functools import reduce

solution = lambda s: reduce(lambda a, c: (a[0] + list(c - a[1]), c), sorted([set(v) for v in eval(s.replace("{", "[").replace("}", "]"))], key=lambda x: len(x)), ([], set()))[0]
