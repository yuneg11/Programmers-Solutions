from functools import reduce

solution = lambda m, l=lambda a, v: (*a[1:], max(a[:2]) + v): max(max(reduce(l, m[2:-1], (0, *m[:2]))), max(reduce(l, m[3:], (0, m[1], m[2]))))
