from functools import reduce

solution = lambda l: max(reduce(lambda l, r: [0] + [max(l[:i+1] + l[i+2:]) + r[i] for i in range(len(r))] + [0], l[1:], [0] + l[0] + [0]))
