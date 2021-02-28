from functools import reduce

solution = lambda p, s: reduce(lambda a, v: (a[0][:-1] + [a[0][-1] + 1], a[1]) if a[1] >= v else (a[0] + [1], v), [(100 - q) // r + ((100 - q) % r > 0) for q, r in zip(p, s)], ([0], 0))[0][1:]
