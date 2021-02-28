from functools import reduce

solution = lambda n: reduce(lambda a, _: (a[1], (a[0] + a[1]) % 1234567), range(n), (0, 1))[0]
