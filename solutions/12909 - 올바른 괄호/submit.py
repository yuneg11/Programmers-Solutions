from functools import reduce

solution = lambda s: reduce(lambda c, v: c - 1 + 2 * (v == "(") if c + 1 else -1, s, 0) == 0
