from functools import reduce

solution = lambda d, b: list(reduce(lambda a, v: (a[0] + 1, a[1] + v) if a[1] + v <= b else a, sorted(d), [0, 0]))[0]
