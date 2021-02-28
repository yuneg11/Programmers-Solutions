from functools import reduce

solution = lambda n: reduce(lambda d, _: (d[1], ((d[1][2] + d[0][0]) % 1000000007, d[1][2], (d[1][1] + d[1][0] * 2) % 1000000007)), range(2, n + 1), ((1, 0, 0), (0, 0, 2)))[1][0]
