from functools import reduce

solution = lambda n: reduce(lambda a, _: (a[1] % 1000000007, sum(a) % 1000000007), range(1, n), [1, 1])[1]
