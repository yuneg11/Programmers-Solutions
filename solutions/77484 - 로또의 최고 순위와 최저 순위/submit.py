solution = lambda l, w: (min((d := 7 - len(set(l) & set(w))) - l.count(0), 6), min(d, 6))
