from functools import reduce

solution = lambda b, y: reduce(lambda a, i: [j + 1, i + 1] if (i - 1) * ((j := b // 2 - i) - 1) == y else a, range(1, b // 4 + 1))
