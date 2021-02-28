from functools import reduce

solution = lambda n, s: [v for _, v in sorted(reduce(lambda a, v: ((a[0] + [(-v[1]/a[1] if a[1] else 0, v[0])]), a[1] - v[1]), [(i, len(list(filter(lambda x: x == i, s)))) for i in range(1, n + 1)], ([], len(s)))[0])]
