from functools import reduce

solution = lambda a: reduce(lambda b, c: (b if b[-1] == c or b.append(c) else b), a, [-1])[1:]
