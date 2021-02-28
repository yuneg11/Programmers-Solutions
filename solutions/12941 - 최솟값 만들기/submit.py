solution = lambda a, b: sum([c * d for c, d in zip(sorted(a), sorted(b, reverse=True))])
