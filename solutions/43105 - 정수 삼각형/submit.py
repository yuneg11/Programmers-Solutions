from functools import reduce

solution = lambda t: max(reduce(lambda m, r: [0] + [max(m[i], m[i + 1]) + v for i, v in enumerate(r)] + [0], t, [0, 0]))
