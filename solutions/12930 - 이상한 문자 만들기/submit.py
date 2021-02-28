solution = lambda s:  " ".join(["".join([v.upper() if not i % 2 else v.lower() for i, v in enumerate(w)]) for w in s.split(" ")])
