solution = lambda s: " ".join([w[0].upper() + w[1:].lower() if w else "" for w in s.split(" ")])
