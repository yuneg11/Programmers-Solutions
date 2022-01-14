from itertools import combinations

solution = lambda n: list(sorted({sum(v) for v in combinations(n, 2)}))
