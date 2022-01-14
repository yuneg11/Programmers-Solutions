solution = lambda a, b: [
    [sum(e * f for e, f in zip(c, d)) for d in zip(*b)] for c in a
]
